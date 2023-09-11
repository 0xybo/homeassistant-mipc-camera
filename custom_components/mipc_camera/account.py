from time import time
from typing import Any
from json import loads as json_loads
from re import IGNORECASE, MULTILINE, sub

from requests import get, Response, Timeout, HTTPError
from asyncio import timeout, TimeoutError as AsyncioTimeoutError, sleep, create_task

from homeassistant.core import HomeAssistant, HomeAssistantError

from .deps.mdh import mdh
from .deps.md5 import crypto
from .deps.mcodec import mcodec
from .deps.crypto import encrypt
from .const import (
    LOGGER,
    BASE_HOST,
    TIMEOUT,
    PATHS,
    PRIME,
    ROOT_NUM,
    DEBUG,
    CAM_TIMEOUT,
    MAX_REQUEST_TRY,
)


class RequestError(HomeAssistantError):
    pass


def _make_get_request(url: str, verify: bool = False):
    response = get(url, timeout=TIMEOUT, verify=verify)

    response.raise_for_status()
    response.close()

    return response


class MIPCAccount:
    def __init__(self, username: str, password: str) -> None:
        self.mdh = mdh.mdh
        self.md5 = crypto
        self.mcodec = mcodec.mcodec

        self._username: str = username
        self._password: str = password

        self._last_authentication: float | None = None

        self._host: str | None = None

        self._qid: str | None = None
        self._seq: int = 0
        self._private: str = self.mdh.gen_private()
        self._public: str = self.mdh.gen_public(self._private)
        self._sharedKey: str | None = None
        self._key: str | None = None
        self._lid: str | None = None
        self._shared_key: str | None = None
        self._encrypted_password: str | None = None
        self._sid: str | None = None
        self._nid: str | None = None
        self._host: str | None = None

    async def host(self, hass: HomeAssistant) -> str | None:
        if not self._host:
            await self.get_mipc_host(hass=hass)
        return self._host

    def log(self, msg: Any) -> None:
        if DEBUG:
            LOGGER.info(msg)

    def parse_response(self, response: str) -> dict:
        responseJSON = sub(
            r"(?P<before_key>[\{\[,])(?P<space_before>\s?)(?P<key>[a-z0-9_\.]+)(?P<after_key>:)(?P<space_after>\s?)",
            '\\g<before_key>"\\g<key>"\\g<after_key>',
            response[8:-2],
            0,
            IGNORECASE | MULTILINE,
        )

        return json_loads(responseJSON)

    def url(
        self,
        path_name: str,
        params: dict[str, str] | None = None,
        host: str | None = None,
    ) -> str:
        if not host:
            host = self._host if self._host else BASE_HOST
        if not params:
            params = {}

        self._seq += 1

        paramsList = [f"hfrom_handle={self._seq}"]
        for param in params.keys():
            paramsList.append(f"{param}={params[param]}")

        return f"{host}{PATHS[path_name]}?{'&'.join(paramsList)}"

    async def get(
        self,
        path_name: str,
        hass: HomeAssistant,
        params: dict[str, str] | None = None,
        https: bool = False,
        host: str | None = None,
    ) -> dict | None:
        if not params:
            params = {}

        url = self.url(path_name, params, host=host)
        error: str | None = None
        responseJSON: dict[str, Any] | None = None

        try:
            async with timeout(TIMEOUT):
                response: Response = await hass.async_add_executor_job(
                    _make_get_request, url, https
                )
                responseData = response.text

                responseJSON = self.parse_response(responseData)
                if (
                    "data" in responseJSON
                    and "result" in responseJSON["data"]
                    and type(responseJSON["data"]["result"]) == str
                    and responseJSON["data"]["result"] != ""
                ):
                    error = f"Error getting {url} : {responseJSON['data']['result']}"
                elif (
                    "data" in responseJSON
                    and "ret" in responseJSON["data"]
                    and "reason" in responseJSON["data"]["ret"]
                    and type(responseJSON["data"]["ret"]["reason"]) == str
                    and responseJSON["data"]["ret"]["reason"] != ""
                ):
                    error = (
                        f"Error getting {url} : {responseJSON['data']['ret']['reason']}"
                    )
                elif (
                    "data" in responseJSON
                    and "Result" in responseJSON["data"]
                    and "Reason" in responseJSON["data"]["Result"]
                    and type(responseJSON["data"]["Result"]["Reason"]) == str
                    and responseJSON["data"]["Result"]["Reason"] != ""
                ):
                    error = f"Error getting {url} : {responseJSON['data']['Result']['Reason']}"
        except AsyncioTimeoutError:
            error = f"Timeout getting '{url}'"
        except Timeout:
            error = f"Timeout getting '{url}'"
        except HTTPError as err:
            error = f"Error getting '{url}' : {err}"

        if error:
            raise RequestError(error)

        return responseJSON

    async def retry_if_error(
        self, fn: str, hass: HomeAssistant, params: dict | None = None
    ) -> Any | None:
        if not params:
            params = {}

        try_count = 0

        while try_count < MAX_REQUEST_TRY:
            try:
                try_count += 1
                return await getattr(self, fn)(hass=hass, in_retry_loop=True, **params)
            except HomeAssistantError as err:
                LOGGER.error(f"(try: {str(try_count)}) {err}")
                await self.clear_values()

        return None

    async def get_mipc_host(self, hass: HomeAssistant) -> str | None:
        """Return MIPC host"""

        self.log("Getting host")

        response = await self.get(
            path_name="HOSTS", https=True, host=BASE_HOST, hass=hass
        )
        if response:
            self._host = response["data"]["server"]["signal"][0]
            return self._host

        return None

    async def get_qid(
        self, hass: HomeAssistant, in_retry_loop: bool = False
    ) -> str | None:
        if not in_retry_loop:
            return await self.retry_if_error(fn="get_qid", hass=hass)

        await self.check_timeout()
        if not self._host:
            await self.get_mipc_host(hass=hass)

        self.log("Getting QID")

        response = await self.get(path_name="CREATE_SESSION", hass=hass)

        if response:
            self._qid = response["data"]["qid"]
            return response["data"]["qid"]

        return None

    async def generate_dh(
        self, hass: HomeAssistant, in_retry_loop: bool = False
    ) -> str | None:
        if not in_retry_loop:
            return await self.retry_if_error(fn="generate_dh", hass=hass)

        await self.check_timeout()
        if not self._qid:
            await self.get_qid(hass=hass)

        self.log("Generating DH")

        response = await self.get(
            path_name="KEY",
            params={
                "dbnum_prime": PRIME,
                "dkey_a2b": self._public,
                "droot_num": ROOT_NUM,
            },
            hass=hass,
        )

        if response:
            self._key = response["data"]["key_b2a"]
            self._lid = response["data"]["lid"]
            await self.generate_shared_key(hass=hass)
            return response["data"]["key_b2a"]

        return None

    async def auth(
        self, hass: HomeAssistant, in_retry_loop: bool = False
    ) -> str | None:
        if not in_retry_loop:
            return await self.retry_if_error(fn="auth", hass=hass)

        await self.check_timeout()
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        await self.crypt_password(hass=hass)

        self._nid = await self.generate_nid(self._lid, 2, hass=hass)

        self.log("Authentication")

        response = await self.get(
            path_name="LOGIN",
            params={
                "hqid": self._qid,
                "dlid": self._lid,
                "dnid": self._nid,
                "duser": self._username,
                "dpass": self._encrypted_password,
                "dsession_req": 1,
            },
            hass=hass,
        )

        if response:
            self._sid = response["data"]["sid"]

            return response["data"]["sid"]

        return None

    async def get_devices(
        self, hass: HomeAssistant, in_retry_loop: bool = False
    ) -> dict | None:
        if not in_retry_loop:
            return await self.retry_if_error(fn="get_devices", hass=hass)

        await self.check_timeout()
        if not self._nid:
            await self.auth(hass=hass)

        self.log("Getting devices")

        response = await self.get(
            path_name="DEVICES",
            params={
                "hqid": self._qid,
                "dsess": 1,
                "dsess_nid": self._nid,
                "dstart": 0,
                "dcounts": 1024,
            },
            hass=hass,
        )

        if response:
            return response["data"]["devs"]

        return None

    async def get_stream_source(
        self, device_name: str, hass: HomeAssistant, in_retry_loop: bool = False
    ) -> str | None:
        if not in_retry_loop:
            return await self.retry_if_error(
                fn="get_stream_source", params={"device_name": device_name}, hass=hass
            )

        if not device_name:
            return None

        await self.check_timeout()

        if not self._sid:
            await self.auth(hass=hass)

        nid = await self.generate_nid(self._sid, 0, hass=hass)

        self.log("Getting stream source")

        response = await self.get(
            path_name="PLAY",
            params={
                "hqid": self._qid,
                "dsess": 1,
                "dsess_nid": nid,
                "dsess_sn": device_name,
                "dsetup": 1,
                "dsetup_stream": "RTSP",
                "dsetup_trans": 1,
                "dsetup_trans_proto": "rtsp",
                "dtoken": "p0",
            },
            hass=hass,
        )

        if response:
            return response["data"]["MediaUri"]["Uri"]

    async def get_still_image(
        self, hass: HomeAssistant, device_name: str, in_retry_loop: bool = False
    ) -> bytes | None:
        if not in_retry_loop:
            return await self.retry_if_error(
                fn="get_still_image", hass=hass, params={"device_name": device_name}
            )

        if not self._sid:
            await self.auth(hass=hass)

        nid = await self.generate_nid(self._sid, 0, hass=hass)

        self.log("Getting still image")

        url = self.url(
            "STILL_IMAGE",
            {
                "dsess": 1,
                "dsess_nid": nid,
                "dsess_sn": device_name,
                "dtoken": "p1_xxxxxxxxxx",
                "dencode_type": 0,
                "dpic_types_support": 2,
                "dflag": 2,
            },
        )
        try:
            async with timeout(TIMEOUT):
                response: Response = await hass.async_add_executor_job(
                    _make_get_request, url
                )
                responseData = response.content

                return responseData
        except AsyncioTimeoutError:
            LOGGER.error("Timeout getting '%s'", url)
        except Timeout:
            LOGGER.error("Timeout getting '%s'", url)
        except HTTPError as err:
            LOGGER.error("Error getting '%s' : %s", url, err)

    async def generate_shared_key(self, hass: HomeAssistant) -> str:
        if not self._key:
            await self.generate_dh(hass=hass)

        self.log("Generating shared key")

        self._shared_key = self.mdh["gen_shared_secret"](self._private, self._key)

        return self._shared_key

    async def crypt_password(self, hass: HomeAssistant) -> str:
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        self.log("Encrypting password")

        self._encrypted_password = encrypt(self._password, self._shared_key)

        return self._encrypted_password

    async def generate_nid(self, id_: str, num: int, hass: HomeAssistant) -> str:
        await self.check_timeout()
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        self.log("Generating NID")

        return self.mcodec.nid(
            self._seq, id_, self._shared_key, num, None, None, self.md5, "hex"
        )

    async def clear_values(self) -> None:
        self.log("Clearing values")
        self._qid = None
        self._sharedKey = None
        self._key = None
        self._lid = None
        self._shared_key = None
        self._encrypted_password = None
        self._sid = None
        self._nid = None

        self._private = self.mdh.gen_private()
        self._public = self.mdh.gen_public(self._private)

    async def check_timeout(self) -> None:
        if not self._last_authentication:
            self._last_authentication = time()

        if time() - self._last_authentication >= CAM_TIMEOUT / 1000:
            await self.clear_values()
            self._last_authentication = time()

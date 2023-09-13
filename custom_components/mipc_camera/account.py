"""
Implement the MIPCAccount that represents an account on MIPC 
with some methods to fetch data from mipcm.com.
"""

from time import time
from typing import Any
from json import loads as json_loads
from re import IGNORECASE, MULTILINE, sub

from asyncio import timeout, TimeoutError as AsyncioTimeoutError
from requests import get, Response, Timeout, HTTPError

from homeassistant.core import HomeAssistant, HomeAssistantError

from .deps.mdh import mdh
from .deps.md5 import crypto as md5
from .deps.mcodec import mcodec
from .deps.crypto import encrypt
from .const import (
    LOGGER,
    BASE_HOST,
    TIMEOUT,
    PATHS,
    PRIME,
    ROOT_NUM,
    CAM_TIMEOUT,
    MAX_REQUEST_TRY,
)

mdh = mdh.mdh
mcodec = mcodec.mcodec

class RequestError(HomeAssistantError):
    """Error raised in case of failed request to MIPC."""


def _make_get_request(url: str, verify: bool = False) -> Response:
    """Make request synchronously with hass.async_add_executor_job."""
    response = get(url, timeout=TIMEOUT, verify=verify)

    response.raise_for_status()
    response.close()

    return response


class MIPCAccount:
    """represents an account on MIPC with some methods to fetch data from mipcm.com."""
    def __init__(self, username: str, password: str) -> None:
        self._username: str = username
        self._password: str = password

        self._last_authentication: float | None = None

        self._host: str | None = None

        self._qid: str | None = None
        self._seq: int = 0
        self._private: str = mdh.gen_private()
        self._public: str = mdh.gen_public(self._private)
        self._shared_key: str | None = None
        self._key: str | None = None
        self._lid: str | None = None
        self._shared_key: str | None = None
        self._encrypted_password: str | None = None
        self._sid: str | None = None
        self._nid: str | None = None


    def parse_response(self, response: str) -> dict:
        """
        Parse JS message from mipcm.com as JSON.
        
        Responses from mipcm.com are formatted as follows :
        message({some_json:"but without quotation marks (as in javascript)"})
        """
        response_json = sub(
            r"(?P<b>[\{\[,])(?P<sb>\s?)(?P<k>[a-z0-9_\.]+)(?P<a>:)(?P<sa>\s?)",
            '\\g<b>"\\g<k>"\\g<a>',
            response[8:-2],
            0,
            IGNORECASE | MULTILINE,
        )

        return json_loads(response_json)

    def url(
        self,
        path_name: str,
        params: dict[str, str] | None = None,
        host: str | None = None,
    ) -> str:
        """Generates a URL for making requests to the MIPC service."""
        if not host:
            host = self._host if self._host else BASE_HOST
        if not params:
            params = {}

        self._seq += 1

        params_list = [f"hfrom_handle={self._seq}"]
        for param in params.keys():
            params_list.append(f"{param}={params[param]}")

        return f"{host}{PATHS[path_name]}?{'&'.join(params_list)}"

    async def get(
        self,
        path_name: str,
        hass: HomeAssistant,
        params: dict[str, str] | None = None,
        https: bool = False,
        host: str | None = None,
    ) -> dict | None:
        """
        Performs an HTTP GET request to the specified 
        path and returns the parsed JSON response.
        """
        if not params:
            params = {}

        url = self.url(path_name, params, host=host)
        error: str | None = None
        response_json: dict[str, Any] | None = None

        try:
            async with timeout(TIMEOUT):
                response: Response = await hass.async_add_executor_job(
                    _make_get_request, url, https
                )
                response_data = response.text

                response_json = self.parse_response(response_data)
                if (
                    "data" in response_json
                    and "result" in response_json["data"]
                    and isinstance(response_json["data"]["result"], str)
                    and response_json["data"]["result"] != ""
                ):
                    error = f"Error getting {url} : {response_json['data']['result']}"
                elif (
                    "data" in response_json
                    and "ret" in response_json["data"]
                    and "reason" in response_json["data"]["ret"]
                    and isinstance(response_json["data"]["ret"]["reason"], str)
                    and response_json["data"]["ret"]["reason"] != ""
                ):
                    error = (
                        f"Error getting {url} : {response_json['data']['ret']['reason']}"
                    )
                elif (
                    "data" in response_json
                    and "Result" in response_json["data"]
                    and "Reason" in response_json["data"]["Result"]
                    and isinstance(response_json["data"]["Result"]["Reason"], str)
                    and response_json["data"]["Result"]["Reason"] != ""
                ):
                    error = f"Error getting {url} : {response_json['data']['Result']['Reason']}"
        except AsyncioTimeoutError:
            error = f"Timeout getting '{url}'"
        except Timeout:
            error = f"Timeout getting '{url}'"
        except HTTPError as err:
            error = f"Error getting '{url}' : {err}"

        if error:
            raise RequestError(error)

        return response_json

    async def retry_if_error(
        self, method: str, hass: HomeAssistant, params: dict | None = None
    ) -> Any | None:
        """
        Retries a specified method if an error occurs up to 
        a maximum number of retries MAX_REQUEST_TRY.
        """
        if not params:
            params = {}

        try_count = 0

        while try_count < MAX_REQUEST_TRY:
            try:
                try_count += 1
                return await getattr(self, method)(hass=hass, in_retry_loop=True, **params)
            except HomeAssistantError as err:
                LOGGER.error("(try: %s) %s", method, err)
                await self.clear_values()

        return None

    async def get_mipc_host(self, hass: HomeAssistant) -> str | None:
        """Retrieves the MIPC host."""

        LOGGER.debug("Getting host")

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
        """Retrieves the QID (Query ID) used for authentication."""
        if not in_retry_loop:
            return await self.retry_if_error(method="get_qid", hass=hass)

        await self.check_timeout()
        if not self._host:
            await self.get_mipc_host(hass=hass)

        LOGGER.debug("Getting QID")

        response = await self.get(path_name="CREATE_SESSION", hass=hass)

        if response:
            self._qid = response["data"]["qid"]
            return response["data"]["qid"]

        return None

    async def generate_dh(
        self, hass: HomeAssistant, in_retry_loop: bool = False
    ) -> str | None:
        """Generates Diffie-Hellman keys."""
        if not in_retry_loop:
            return await self.retry_if_error(method="generate_dh", hass=hass)

        await self.check_timeout()
        if not self._qid:
            await self.get_qid(hass=hass)

        LOGGER.debug("Generating DH")

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
        """Performs user authentication with the MIPC service."""
        if not in_retry_loop:
            return await self.retry_if_error(method="auth", hass=hass)

        await self.check_timeout()
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        await self.crypt_password(hass=hass)

        self._nid = await self.generate_nid(self._lid, 2, hass=hass)

        LOGGER.debug("Authentication")

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
        """Retrieves all cameras connected to the MIPC account."""
        if not in_retry_loop:
            return await self.retry_if_error(method="get_devices", hass=hass)

        await self.check_timeout()
        if not self._nid:
            await self.auth(hass=hass)

        LOGGER.debug("Getting devices")

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
        """Retrieves the stream source for a specific device."""
        if not in_retry_loop:
            return await self.retry_if_error(
                method="get_stream_source", params={"device_name": device_name}, hass=hass
            )

        if not device_name:
            return None

        await self.check_timeout()

        if not self._sid:
            await self.auth(hass=hass)

        nid = await self.generate_nid(self._sid, 0, hass=hass)

        LOGGER.debug("Getting stream source")

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
        """Retrieves a still image for a specific device."""
        if not in_retry_loop:
            return await self.retry_if_error(
                method="get_still_image", hass=hass, params={"device_name": device_name}
            )

        if not self._sid:
            await self.auth(hass=hass)

        nid = await self.generate_nid(self._sid, 0, hass=hass)

        LOGGER.debug("Getting still image")

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
                response_data = response.content

                return response_data
        except AsyncioTimeoutError:
            LOGGER.error("Timeout getting '%s'", url)
        except Timeout:
            LOGGER.error("Timeout getting '%s'", url)
        except HTTPError as err:
            LOGGER.error("Error getting '%s' : %s", url, err)

    async def generate_shared_key(self, hass: HomeAssistant) -> str:
        """Generates a shared secret key."""
        if not self._key:
            await self.generate_dh(hass=hass)

        LOGGER.debug("Generating shared key")

        self._shared_key = mdh["gen_shared_secret"](self._private, self._key)

        return self._shared_key

    async def crypt_password(self, hass: HomeAssistant) -> str:
        """Encrypts the user's password."""
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        LOGGER.debug("Encrypting password")

        self._encrypted_password = encrypt(self._password, self._shared_key)

        return self._encrypted_password

    async def generate_nid(self, id_: str, num: int, hass: HomeAssistant) -> str:
        """Generates a NID (Network ID)."""
        await self.check_timeout()
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        LOGGER.debug("Generating NID")

        return mcodec.nid(
            self._seq, id_, self._shared_key, num, None, None, md5, "hex"
        )

    async def clear_values(self) -> None:
        """Clears stored values for new authentication."""
        LOGGER.debug("Clearing values")
        self._qid = None
        self._shared_key = None
        self._key = None
        self._lid = None
        self._shared_key = None
        self._encrypted_password = None
        self._sid = None
        self._nid = None

        self._private = mdh.gen_private()
        self._public = mdh.gen_public(self._private)

    async def check_timeout(self) -> None:
        """Checks if the authentication has timed out and clears session data if necessary."""
        if not self._last_authentication:
            self._last_authentication = time()

        if time() - self._last_authentication >= CAM_TIMEOUT / 1000:
            await self.clear_values()
            self._last_authentication = time()

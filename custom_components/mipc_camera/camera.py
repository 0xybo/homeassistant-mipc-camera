from typing import Any
from json import loads as json_loads
from re import IGNORECASE, MULTILINE, sub
from aiohttp.web import Request, StreamResponse
from requests import get, Response, Timeout, HTTPError
from asyncio import timeout, TimeoutError as AsyncioTimeoutError, sleep, create_task

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.camera import Camera, CameraEntityFeature
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_web,async_get_clientsession

from .deps.mdh import mdh
from .deps.md5 import crypto
from .deps.mcodec import mcodec
from .deps.crypto_js import crypto_js
from .const import LOGGER, BASE_HOST, TIMEOUT, PATHS, PRIME, ROOT_NUM, DOMAIN, DEBUG


def make_get_request(url: str, verify: bool = False):
    response = get(url, timeout=TIMEOUT, verify=verify)

    response.raise_for_status()
    response.close()

    return response


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    camera = MIPCCamera(
        username=entry.options["username"], password=entry.options["password"]
    )

    devices = await camera.get_devices(hass=hass)
    if not devices:
        return None

    entries = []
    for device in devices:
        entries.append(
            MIPCCamera(
                name=device["sn"],
                username=entry.options["username"],
                password=entry.options["password"],
                unique_id=device["sn"],
                device_info=DeviceInfo(
                    name=device["sn"], identifiers={(DOMAIN, device["sn"])}
                ),
            )
        )
    async_add_entities(entries)

    return None


class MIPCCamera(Camera):
    """An implementation of an IP camera that is reachable over a MIPC account"""

    def __init__(
        self,
        *,
        name: str | None = None,
        username: str,
        password: str,
        unique_id: str | None = None,
        device_info: DeviceInfo | None = None,
    ) -> None:
        """Initialize a MIPC Camera"""
        super().__init__()
        self.mdh = mdh.mdh
        self.md5 = crypto
        self.mcodec = mcodec.mcodec
        self.crypto = crypto_js.crypto_js

        self._username: str = username
        self._password: str = password
        self._name: str = name

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
        self._timeout_is_started: bool = False

        if unique_id is not None:
            self._attr_unique_id = unique_id
        if device_info is not None:
            self._attr_device_info = device_info
        self._attr_supported_features = CameraEntityFeature.STREAM

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

        # LOGGER.info(responseJSON)

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
        params: dict[str, str] | None = None,
        https: bool = False,
        host: str | None = None,
        hass: HomeAssistant | None = None,
    ) -> dict | None:
        if not hass:
            hass = self.hass
        if not params:
            params = {}

        url = self.url(path_name, params, host=host)
        try:
            async with timeout(TIMEOUT):
                response: Response = await hass.async_add_executor_job(
                    make_get_request, url, https
                )
                responseData = response.text

                responseJSON = self.parse_response(responseData)
                if (
                    "data" in responseJSON
                    and "result" in responseJSON["data"]
                    and type(responseJSON["data"]["result"]) == str
                    and responseJSON["data"]["result"] != ""
                ):
                    LOGGER.error(
                        "Error getting '%s' : %s", url, responseJSON["data"]["result"]
                    )
                elif (
                    "data" in responseJSON
                    and "ret" in responseJSON["data"]
                    and "reason" in responseJSON["data"]["ret"]
                    and type(responseJSON["data"]["ret"]["reason"]) == str
                    and responseJSON["data"]["ret"]["reason"] != ""
                ):
                    LOGGER.error(
                        "Error getting '%s' : %s",
                        url,
                        responseJSON["data"]["ret"]["reason"],
                    )
                elif (
                    "data" in responseJSON
                    and "Result" in responseJSON["data"]
                    and "Reason" in responseJSON["data"]["Result"]
                    and type(responseJSON["data"]["Result"]["Reason"]) == str
                    and responseJSON["data"]["Result"]["Reason"] != ""
                ):
                    LOGGER.error(
                        "Error getting '%s' : %s",
                        url,
                        responseJSON["data"]["Result"]["Reason"],
                    )
                else:
                    return responseJSON
        except AsyncioTimeoutError:
            LOGGER.error("Timeout getting '%s'", url)
        except Timeout:
            LOGGER.error("Timeout getting '%s'", url)
        except HTTPError as err:
            LOGGER.error("Error getting '%s' : %s", url, err)

        return None

    async def get_mipc_host(self, hass: HomeAssistant | None = None) -> str | None:
        """Return MIPC host"""
        if not hass:
            hass = self.hass

        self.log("Getting host")

        response = await self.get("HOSTS", https=True, host=BASE_HOST, hass=hass)
        if response:
            self._host = response["data"]["server"]["signal"][0]
            return self._host

        return None

    async def get_qid(self, hass: HomeAssistant | None = None) -> str | None:
        if not hass:
            hass = self.hass
        if not self._host:
            await self.get_mipc_host(hass=hass)

        self.log("Getting QID")

        response = await self.get("CREATE_SESSION", hass=hass)

        if response:
            self._qid = response["data"]["qid"]
            return response["data"]["qid"]

        return None

    async def generate_dh(self, hass: HomeAssistant | None = None) -> str | None:
        if not hass:
            hass = self.hass
        if not self._qid:
            await self.get_qid(hass=hass)

        self.log("Generating DH")

        response = await self.get(
            "KEY",
            {
                # "hqid": self._qid,
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

    async def auth(self, hass: HomeAssistant | None = None) -> str | None:
        if not hass:
            hass = self.hass
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        await self.crypt_password(hass=hass)

        self._nid = await self.generate_nid(self._lid, 2, hass=hass)

        self.log("Authentication")

        response = await self.get(
            "LOGIN",
            {
                "hqid": self._qid,
                "dlid": self._lid,
                "dnid": self._nid,
                "duser": self._username,
                "dpass": self._encrypted_password,
                "dsession_req": 1,
            },
            hass=hass,
        )

        create_task(self.start_clear_timeout())

        if response:
            self._sid = response["data"]["sid"]

            return response["data"]["sid"]

        return None

    async def get_devices(self, hass: HomeAssistant | None = None) -> dict | None:
        if not hass:
            hass = self.hass
        if not self._nid:
            await self.auth(hass=hass)

        self.log("Getting devices")

        response = await self.get(
            "DEVICES",
            {
                "hqid": self._qid,
                "dsess": 1,
                "dsess_nid": self._nid,
                "dstart": 0,
                "dcounts": 1024,
            },
            hass=hass,
        )

        create_task(self.start_clear_timeout())

        if response:
            return response["data"]["devs"]

        return None

    async def get_stream_source(
        self, hass: HomeAssistant | None = None, name: str | None = None
    ) -> str | None:
        if not hass:
            hass = self.hass
        if not name:
            name = self._name
        if not name:
            LOGGER.error("Invalid Name")
            return None

        if not self._sid:
            await self.auth(hass=hass)

        nid = await self.generate_nid(self._sid, 0, hass=hass)

        self.log("Getting stream source")

        response = await self.get(
            "PLAY",
            {
                "hqid": self._qid,
                "dsess": 1,
                "dsess_nid": nid,
                "dsess_sn": name,
                "dsetup": 1,
                "dsetup_stream": "RTSP",
                "dsetup_trans": 1,
                "dsetup_trans_proto": "rtsp",
                "dtoken": "p0",
            },
        )

        if response:
            return response["data"]["MediaUri"]["Uri"]

    async def get_still_image(self, hass: HomeAssistant | None) -> bytes | None:
        if not hass:
            hass = self.hass
        if not self._sid:
            await self.auth(hass=hass)

        nid = await self.generate_nid(self._sid, 0, hass=hass)

        self.log("Getting still image")

        url = self.url(
            "STILL_IMAGE",
            {
                "dsess": 1,
                "dsess_nid": nid,
                "dsess_sn": self._name,
                "dtoken": "p1_xxxxxxxxxx",
                "dencode_type": 0,
                "dpic_types_support": 2,
                "dflag": 2,
            },
        )
        try:
            async with timeout(TIMEOUT):
                response: Response = await hass.async_add_executor_job(
                    make_get_request, url
                )
                responseData = response.content

                return responseData
        except AsyncioTimeoutError:
            LOGGER.error("Timeout getting '%s'", url)
        except Timeout:
            LOGGER.error("Timeout getting '%s'", url)
        except HTTPError as err:
            LOGGER.error("Error getting '%s' : %s", url, err)

    async def generate_shared_key(self, hass: HomeAssistant | None = None) -> str:
        if not hass:
            hass = self.hass
        if not self._key:
            await self.generate_dh(hass=hass)

        self.log("Generating shared key")

        self._shared_key = self.mdh["gen_shared_secret"](self._private, self._key)

        return self._shared_key

    async def crypt_password(self, hass: HomeAssistant | None = None) -> str:
        if not hass:
            hass = self.hass
        if not self._shared_key:
            await self.generate_dh(hass=HomeAssistant)

        self.log("Encrypting password")

        self._encrypted_password = self.crypto.DES.encrypt(
            self.crypto.MD5(self._password),
            self.crypto.MD5(self._shared_key),
            {
                "iv": self.crypto.enc.Hex.parse("0000000000000000"),
                "padding": self.crypto.pad.NoPadding,
            },
        ).ciphertext.toString()

        return self._encrypted_password

    async def generate_nid(
        self, id_: str, num: int, hass: HomeAssistant | None = None
    ) -> str:
        if not hass:
            hass = self.hass
        if not self._shared_key:
            await self.generate_dh(hass=hass)

        self.log("Generating NID")

        return self.mcodec.nid(
            self._seq, id_, self._shared_key, num, None, None, self.md5, "hex"
        )

    async def start_clear_timeout(self) -> None:
        if self._timeout_is_started:
            return None

        self._timeout_is_started = True
        self.log("Starting clear timeout")

        await sleep(30)
        await self.clear_values()
        self._timeout_is_started = False

        return None

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

    async def stream_source(self) -> str:
        if not self._name:
            return ""

        source = await self.get_stream_source()

        self.log("Returning stream source")

        return source

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        image = await self.get_still_image(hass=self.hass)

        self.log("Returning still image")

        return image

    # async def handle_async_mjpeg_stream(self, request: Request) -> StreamResponse:
    #     self.log("Handling mjpeg stream")
    #     source = await self.get_stream_source()
    #     if not source:
    #         return await self.handle_async_still_stream(request, self.frame_interval)

    #     websession = async_get_clientsession(self.hass, verify_ssl=False)
    #     stream_coro = websession.get(source)

    #     return await async_aiohttp_proxy_web(self.hass, request, stream_coro)


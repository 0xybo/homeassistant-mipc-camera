from __future__ import annotations

from typing import Any

from homeassistant.components.stream import Stream

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.camera import Camera, CameraEntityFeature

from .account import MIPCAccount
from .const import (
    LOGGER,
    DOMAIN,
    DEBUG,
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    account = MIPCAccount(
        username=entry.options["username"], password=entry.options["password"]
    )

    devices = await account.get_devices(hass=hass)
    if not devices:
        return None

    entries = []
    for device in devices:
        entries.append(
            MIPCCamera(
                account=account,
                name=device["sn"],
                unique_id=device["sn"],
                is_on=device["stat"] == "Online",
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
        account: MIPCAccount,
        name: str | None = None,
        unique_id: str | None = None,
        device_info: DeviceInfo | None = None,
        is_on: bool = False,
    ) -> None:
        """Initialize a MIPC Camera"""
        super().__init__()

        self.__account = account
        self.__name = name

        if unique_id is not None:
            self._attr_unique_id = unique_id
        if device_info is not None:
            self._attr_device_info = device_info
        self._attr_supported_features = CameraEntityFeature.STREAM
        self._attr_force_update = True
        self._attr_should_poll = True
        self._attr_is_on = is_on

    def log(self, msg: Any) -> None:
        if DEBUG:
            LOGGER.info(msg)

    async def async_create_stream(self) -> Stream | None:

        if self.stream:
            await self.stream.stop()
        self.stream = None

        self.stream = await super().async_create_stream()

        return self.stream

    async def stream_source(self) -> str | None:
        if not self.__name:
            return None

        source = await self.__account.get_stream_source(
            hass=self.hass, device_name=self.__name
        )

        self.log("Returning stream source")

        return source

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        if not self.__name:
            return None

        image = await self.__account.get_still_image(
            hass=self.hass, device_name=self.__name
        )

        self.log("Returning still image")

        return image

    async def async_update(self):
        self.log("Updating informations")

        devices = await self.__account.get_devices(hass=self.hass)

        for device in devices:
            if device["sn"] == self.__name:
                self._attr_is_on = device["stat"] == "Online"

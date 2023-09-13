"""
Implement the MIPCCamera class that represents a camera available on an MIPC account.
"""

from __future__ import annotations

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
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """
    Called when a new configuration entry for this integration is added to Home Assistant.
    
    It initializes a MIPCAccount object using the provided username and password from the 
    configuration entry options.

    It retrieves a list of devices associated with the MIPC account using the 
    account.get_devices method.

    It creates instances of MIPCCamera for each device and adds them to Home Assistant 
    using async_add_entities.
    """
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

        self._account = account
        self._name = name

        if unique_id is not None:
            self._attr_unique_id = unique_id
        if device_info is not None:
            self._attr_device_info = device_info
        self._attr_supported_features = CameraEntityFeature.STREAM
        self._attr_force_update = True
        self._attr_should_poll = True
        self._attr_is_on = is_on

    async def async_create_stream(self) -> Stream | None:
        """
        Create a Stream for stream_source.
        Full name: homeassistant.components.camera.Camera.async_create_stream
        """
        if self.stream:
            await self.stream.stop()
        self.stream = None

        self.stream = await super().async_create_stream()

        return self.stream

    async def stream_source(self) -> str | None:
        """
        Return the source of the stream.

        This is used by cameras with CameraEntityFeature.STREAM
        and StreamType.HLS.
        Full name: homeassistant.components.camera.Camera.stream_source
        """
        if not self._name:
            return None

        source = await self._account.get_stream_source(
            hass=self.hass, device_name=self._name
        )

        LOGGER.debug("Returning stream source")

        return source

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """
        Return bytes of camera image.
        
        Full name: homeassistant.components.camera.Camera.async_camera_image
        """
        if not self._name:
            return None

        image = await self._account.get_still_image(
            hass=self.hass, device_name=self._name
        )

        LOGGER.debug("Returning still image")

        return image

    async def async_update(self):
        """
        Called each time camera information is updated. 
        (self._attr_should_poll must be set to True.)
        
        Updates the camera's information, such as its online status. 
        It retrieves the list of devices associated with the MIPC 
        account and updates the is_on attribute based on the device's status.
        """
        LOGGER.debug("Updating informations")

        devices = await self._account.get_devices(hass=self.hass)

        for device in devices:
            if device["sn"] == self._name:
                self._attr_is_on = device["stat"] == "Online"

        if self.stream:
            self.stream.update_source(
                await self._account.get_stream_source(self._name, self.hass)
            )
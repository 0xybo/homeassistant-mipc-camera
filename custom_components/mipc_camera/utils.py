from homeassistant.exceptions import HomeAssistantError

class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""


class SessionError(HomeAssistantError):
    """Error to indicate there is invalid auth."""

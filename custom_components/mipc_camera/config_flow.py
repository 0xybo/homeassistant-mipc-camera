"""
MIPC Camera Configuration Flow

This module defines the configuration flow for setting up MIPC cameras in Home Assistant.
Users can provide their MIPC account credentials to add cameras to their Home Assistant 
configuration.
"""

from types import MappingProxyType
from voluptuous import Schema, Required

from homeassistant.core import callback
from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from .const import DOMAIN, LOGGER
from .account import MIPCAccount

class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""

class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""

class SessionError(HomeAssistantError):
    """Error to indicate there is invalid auth."""


@callback
def get_schema(defaults: dict[str, str] | MappingProxyType[str, str]) -> Schema:
    """
    Generate a schema for a login form with default values.
    
    This function generates a schema for a login form with fields for 'username' and 'password'.
    You can provide default values for these fields in the 'defaults' parameter.
    """
    return Schema(
        {
            Required("username", default=defaults.get("username", "")): str,
            Required("password", default=defaults.get("password", "")): str,
        }
    )


class MIPCFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for MIPC Camera."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, str] | None = None
    ) -> FlowResult:
        """
        Handle the initial step of the MIPC Camera configuration flow for user input.

        This method is responsible for processing user input during the initial step
        of configuring the MIPC Camera integration.
        """
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                account = MIPCAccount(
                    username=user_input["username"],
                    password=user_input["password"],
                )

                if not await account.auth(hass=self.hass):
                    raise CannotConnect

                return self.async_create_entry(
                    title=f"MIPC Account : {user_input['username']}",
                    data={},
                    options={
                        "username": user_input["username"],
                        "password": user_input["password"],
                    },
                )

            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except SessionError:
                errors["base"] = "session_error"
            except Exception:  # pylint: disable=broad-except
                LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
        else:
            user_input = {}

        return self.async_show_form(
            step_id="user", data_schema=get_schema(user_input), errors=errors
        )

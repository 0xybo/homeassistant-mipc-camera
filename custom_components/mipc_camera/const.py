"""Constants for the MIPC Camera integration."""

import logging

from typing import Final, Literal

from homeassistant.const import Platform

DOMAIN: Final[str] = "mipc_camera"
PLATFORMS: Final[list[Platform]] = [Platform.CAMERA]

BASE_HOST: Final[str] = "https://www.mipcm.com:7443"
PRIME: Final[str] = "791658605174853458830696113306796803"
ROOT_NUM: Final[str] = "5"
CAM_TIMEOUT: Final[int] = 30000

PATHS: Final[dict[str, str]] = {
    "HOSTS": "/cmipcgw/cmipcgw_get_req.js",
    "CREATE_SESSION": "/mmq_create.js",
    "KEY": "/cacs_dh_req.js",
    "LOGIN": "/cacs_login_req.js",
    "DEVICES": "/ccm_devs_get.js",
    "PLAY": "/ccm_play.js",
    "CONTROL": "/ccm_ptz_ctl.js",
    "DEVICE_INFO": "/ccm_dev_info_get.js",
    "DEVICE_NETWORK_INFO": "/ccm_ntp_get.js",
    "DEVICE_DATE": "/ccm_date_get.js",
    "STILL_IMAGE": "/ccm_pic_get.jpg",
    "UNKNOW1": "/mmq_pick.js",
    "UNKNOW2": "/ccm_subscribe.js",
}

TIMEOUT: Final[int] = 10

LOGGER = logging.getLogger(__package__)
DEBUG: bool = False

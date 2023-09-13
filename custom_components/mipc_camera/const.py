"""Constants for the MIPC Camera integration."""

import logging

from typing import Final

from homeassistant.const import Platform

DOMAIN: Final = "mipc_camera"
PLATFORMS: Final = [Platform.CAMERA]
DATA_CAMERA_PREFS: Final = "camera_prefs"

BASE_HOST: Final = "https://www.mipcm.com:7443" # Base host to search for the camera host
PRIME: Final = "791658605174853458830696113306796803" # Constant in mipc source code
ROOT_NUM: Final = "5" # Constant in mipc source code
CAM_TIMEOUT: Final = 30000 # MIPC Session timeout in milliseconds
MAX_REQUEST_TRY: Final = 10

PATHS: Final = {
    "HOSTS": "/cmipcgw/cmipcgw_get_req.js", # Return camera host
    "CREATE_SESSION": "/mmq_create.js", # Create a session and return the associated identifier
    "KEY": "/cacs_dh_req.js", # Generates Diffie-Hellman keys and return it
    "LOGIN": "/cacs_login_req.js", # Authenticate user with username and password and return sid
    "DEVICES": "/ccm_devs_get.js", # Return all devices connected to the account
    "PLAY": "/ccm_play.js", # Return stream source associated with a device
    "CONTROL": "/ccm_ptz_ctl.js", # Controls camera movements
    "DEVICE_INFO": "/ccm_dev_info_get.js", # Returns device information, more detailed than DEVICES
    "DEVICE_NETWORK_INFO": "/ccm_ntp_get.js", # Return information about the camera network
    "DEVICE_DATE": "/ccm_date_get.js", # Return internal date of the device
    "DEVICE_DISK_INFO": "/ccm_disk_get.js", # Return information about the camera disk
    "DEVICE_SPEAKER": "/ccm_speaker_get.js", # Return information about the camera speaker
    "DEVICE_VIDEO": "/ccm_video_srcs_get.js", # Return information about the video
    "DEVICE_MICROPHONE": "/ccm_mic_get.js", # Return information about the camera microphone
    "DEVICE_UPDATE": "/ccm_upgrade_get.js", # Returns the current and available version
    "STILL_IMAGE": "/ccm_pic_get.jpg", # Return still image from camera
    "DEVICE_SET_SPEAKER": "/ccm_speaker_set.js", # Set camera speaker settings
    "UNKNOW1": "/mmq_pick.js",
    "UNKNOW2": "/ccm_subscribe.js",
    "UNKNOW3": "/ccm_dev_action_get.js",
    "UNKNOW4": "/ccm_plan_record_get.js",
    "UNKNOW5": "/ccm_action_sche_get.js",
    "UNKNOW6": "/ccm_dev_profile_get.js",
    "UNKNOW7": "/ccm_box_conf_get.js",
    "UNKNOW8": "/ccm_misc_get.js",
    "UNKNOW9": "/ccm_osd_get.js"
}

TIMEOUT: Final = 10

LOGGER = logging.getLogger(__package__)

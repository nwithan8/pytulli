# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:07:40+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class RegisteredDeviceModel(BaseModel):
    server_id: Optional[str] = None
    pms_name: Optional[str] = None
    pms_version: Optional[str] = None
    pms_platform: Optional[str] = None
    pms_ip: Optional[str] = None
    pms_port: Optional[int] = None
    pms_ssl: Optional[int] = None
    pms_is_remote: Optional[int] = None
    pms_is_cloud: Optional[int] = None
    pms_url: Optional[str] = None
    pms_url_manual: Optional[int] = None
    pms_identifier: Optional[str] = None
    pms_plexpass: Optional[int] = None
    tautulli_install_type: Optional[str] = None
    tautulli_version: Optional[str] = None
    tautulli_branch: Optional[str] = None
    tautulli_commit: Optional[str] = None
    tautulli_platform: Optional[str] = None
    tautulli_platform_release: Optional[str] = None
    tautulli_platform_version: Optional[str] = None
    tautulli_platform_linux_distro: Optional[str] = None
    tautulli_platform_device_name: Optional[str] = None
    tautulli_python_version: Optional[str] = None




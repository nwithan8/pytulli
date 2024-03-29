# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:21:25+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class ServerInfoModel(BaseModel):
    pms_name: Optional[str] = None
    pms_version: Optional[str] = None
    pms_platform: Optional[str] = None
    pms_ip: Optional[str] = None
    pms_port: Optional[int] = None
    pms_ssl: Optional[int] = None
    pms_is_remote: Optional[int] = None
    pms_url: Optional[str] = None
    pms_url_manual: Optional[int] = None
    pms_identifier: Optional[str] = None
    pms_plexpass: Optional[int] = None




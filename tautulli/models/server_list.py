# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:22:02+00:00

from __future__ import annotations

from typing import Optional

from tautulli.models._base import _Base


class ServerListEntryModel(_Base):
    httpsRequired: Optional[str] = None
    clientIdentifier: Optional[str] = None
    label: Optional[str] = None
    ip: Optional[str] = None
    port: Optional[str] = None
    uri: Optional[str] = None
    local: Optional[str] = None
    value: Optional[str] = None
    is_cloud: Optional[bool] = None

# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:48:59+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class NotifierModel(BaseModel):
    id: Optional[int] = None
    agent_id: Optional[int] = None
    agent_name: Optional[str] = None
    agent_label: Optional[str] = None
    friendly_name: Optional[str] = None
    active: Optional[int] = None




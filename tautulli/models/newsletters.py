# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T03:52:33+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    id: Optional[int]
    agent_id: Optional[int]
    agent_name: Optional[str]
    agent_label: Optional[str]
    friendly_name: Optional[str]
    cron: Optional[str]
    active: Optional[int]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: List[Datum]


class Model(BaseModel):
    response: Response

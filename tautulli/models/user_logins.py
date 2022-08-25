# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:03:28+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    browser: Optional[str]
    friendly_name: Optional[str]
    host: Optional[str]
    ip_address: Optional[str]
    os: Optional[str]
    timestamp: int
    user: Optional[str]
    user_agent: Optional[str]
    user_group: Optional[str]
    user_id: int


class Data(BaseModel):
    draw: int
    recordsTotal: int
    recordsFiltered: int
    data: List[Datum]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

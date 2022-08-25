# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:45:21+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    id: int
    timestamp: int
    newsletter_id: int
    agent_id: int
    agent_name: Optional[str]
    notify_action: Optional[str]
    subject_text: Optional[str]
    body_text: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    uuid: Optional[str]
    success: int


class Data(BaseModel):
    recordsFiltered: int
    recordsTotal: int
    data: List[Datum]
    draw: int


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

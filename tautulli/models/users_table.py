# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:05:45+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel


class Datum(BaseModel):
    row_id: Optional[int]
    user_id: Optional[int]
    username: Optional[str]
    friendly_name: Optional[str]
    user_thumb: Optional[str]
    plays: Optional[int]
    duration: Optional[int]
    last_seen: Optional[int]
    last_played: Optional[str]
    history_row_id: Optional[int]
    ip_address: Optional[str]
    platform: Optional[str]
    player: Optional[str]
    rating_key: Optional[int]
    media_type: Optional[str]
    thumb: Optional[str]
    parent_title: Optional[str]
    year: Optional[Any]
    media_index: Optional[Union[int, str]]
    parent_media_index: Optional[Union[int, str]]
    live: Optional[int]
    originally_available_at: Optional[str]
    guid: Optional[str]
    transcode_decision: Optional[str]
    do_notify: Optional[int]
    keep_history: Optional[int]
    allow_guest: Optional[int]
    is_active: Optional[int]
    title: Optional[str]
    email: Optional[str]


class Data(BaseModel):
    recordsFiltered: Optional[int]
    recordsTotal: Optional[int]
    data: Optional[List[Datum]]
    draw: Optional[int]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

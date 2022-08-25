# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:37:27+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel


class Datum(BaseModel):
    row_id: int
    server_id: Optional[str]
    section_id: int
    section_name: Optional[str]
    section_type: Optional[str]
    count: Optional[int]
    parent_count: Optional[int]
    child_count: Optional[int]
    library_thumb: Optional[str]
    library_art: Optional[str]
    plays: int
    duration: int
    last_accessed: Optional[int]
    history_row_id: Optional[int]
    last_played: Optional[str]
    rating_key: Optional[int]
    media_type: Optional[str]
    thumb: Optional[str]
    parent_title: Optional[str]
    year: Optional[Union[int, str]]
    media_index: Optional[Union[int, str]]
    parent_media_index: Optional[Union[int, str]]
    content_rating: Optional[str]
    labels: List
    live: Optional[int]
    originally_available_at: Optional[str]
    guid: Optional[str]
    do_notify: int
    do_notify_created: int
    keep_history: int
    is_active: int


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

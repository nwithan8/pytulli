# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:51:11+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    addedAt: Optional[str]
    composite: Optional[str]
    duration: Optional[int]
    guid: Optional[str]
    leafCount: Optional[int]
    librarySectionID: Optional[str]
    playlistType: Optional[str]
    ratingKey: Optional[int]
    smart: Optional[bool]
    summary: Optional[str]
    title: Optional[str]
    type: Optional[str]
    updatedAt: Optional[str]
    userID: Optional[Any]


class PlaylistsTable(BaseModel):
    recordsFiltered: Optional[int]
    recordsTotal: Optional[int]
    data: Optional[List[Datum]]
    draw: Optional[int]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: PlaylistsTable


class Model(BaseModel):
    response: Response

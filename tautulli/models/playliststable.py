# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:51:11+00:00

from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class Datum(BaseModel):
    addedAt: str
    composite: str
    duration: int
    guid: str
    leafCount: int
    librarySectionID: str
    playlistType: str
    ratingKey: int
    smart: bool
    summary: str
    title: str
    type: str
    updatedAt: str
    userID: Any


class Data(BaseModel):
    recordsFiltered: int
    recordsTotal: int
    data: List[Datum]
    draw: int


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2022-08-26T20:59:57+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Series(BaseModel):
    name: Optional[str]
    data: Optional[List]


class Data(BaseModel):
    categories: Optional[List[str]]
    series: Optional[List[Series]]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

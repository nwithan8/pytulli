# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:52:07+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Data(BaseModel):
    recently_added: List


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

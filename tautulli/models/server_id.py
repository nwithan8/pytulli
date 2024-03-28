# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:52:30+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class ServerID(BaseModel):
    identifier: Optional[Any] = None


class Response(BaseModel):
    result: Optional[str] = None
    message: Any = None
    data: ServerID


class Model(BaseModel):
    response: Response

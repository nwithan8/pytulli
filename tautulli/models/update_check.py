# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:26:04+00:00

from __future__ import annotations

from pydantic import BaseModel


class Data(BaseModel):
    update: bool
    install_type: str


class Response(BaseModel):
    result: str
    message: str
    data: Data


class Model(BaseModel):
    response: Response
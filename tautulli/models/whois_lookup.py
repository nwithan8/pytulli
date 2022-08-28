# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:06:32+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Net(BaseModel):
    cidr: Optional[str]
    name: Optional[str]
    handle: Optional[str]
    range: Optional[str]
    description: Optional[str]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    address: Optional[str]
    postal_code: Optional[str]
    emails: Optional[List[str]]
    created: Optional[str]
    updated: Optional[str]


class Data(BaseModel):
    host: Optional[str]
    nets: Optional[List[Net]]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

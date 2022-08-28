# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:34:08+00:00

from __future__ import annotations

from typing import Any, Optional, Union

from pydantic import BaseModel


class Data(BaseModel):
    city: Optional[str]
    code: Optional[str]
    continent: Optional[str]
    country: Optional[str]
    latitude: Optional[Union[float, None]]
    longitude: Optional[Union[float, None]]
    postal_code: Optional[str]
    region: Optional[str]
    timezone: Optional[str]
    accuracy: Optional[Any]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

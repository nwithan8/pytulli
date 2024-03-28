# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:43:17+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class Field0(BaseModel):
    rating_key: Optional[int] = None


class NewRatingKeys(BaseModel):
    field_0: Optional[Field0] = Field(..., alias='0')


class Response(BaseModel):
    result: Optional[str] = None
    message: Any = None
    data: NewRatingKeys


class Model(BaseModel):
    response: Response

# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:43:17+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class Field0Model(BaseModel):
    rating_key: Optional[int] = None


class NewRatingKeysModel(BaseModel):
    field_0: Optional[Field0Model] = Field(..., alias='0')




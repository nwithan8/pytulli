# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2022-08-26T19:37:39+00:00

from __future__ import annotations

from typing import List, Optional, Any

from pydantic import BaseModel


class ItemWatchTimeStat(BaseModel):
    query_days: Optional[int] = None
    total_time: Optional[int] = None
    total_plays: Optional[int] = None


class Response(BaseModel):
    result: Optional[str] = None
    message: Any = None
    data: List[ItemWatchTimeStat]


class Model(BaseModel):
    response: Response

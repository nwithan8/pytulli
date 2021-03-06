# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:59:53+00:00

from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class Data(BaseModel):
    row_id: int
    user_id: int
    username: str
    friendly_name: str
    user_thumb: str
    email: str
    is_active: int
    is_admin: str
    is_home_user: int
    is_allow_sync: int
    is_restricted: int
    do_notify: int
    keep_history: int
    allow_guest: int
    deleted_user: int
    shared_libraries: List


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response

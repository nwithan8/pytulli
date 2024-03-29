# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:45:45+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class DatumModel(BaseModel):
    id: Optional[int] = None
    timestamp: Optional[int] = None
    session_key: Optional[int] = None
    rating_key: Optional[int] = None
    user_id: Optional[int] = None
    user: Optional[str] = None
    notifier_id: Optional[int] = None
    agent_id: Optional[int] = None
    agent_name: Optional[str] = None
    notify_action: Optional[str] = None
    subject_text: Optional[str] = None
    body_text: Optional[str] = None
    success: Optional[int] = None


class NotificationLogModel(BaseModel):
    recordsFiltered: Optional[int] = None
    recordsTotal: Optional[int] = None
    data: Optional[List[DatumModel]] = None
    draw: Optional[int] = None




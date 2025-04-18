# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2022-08-26T19:32:43+00:00

from __future__ import annotations

from typing import Optional

from tautulli.models._base import _Base, EmptyStringNullableInt


class ItemUserStatModel(_Base):
    friendly_name: Optional[str] = None
    user_id: EmptyStringNullableInt = None
    user_thumb: Optional[str] = None
    username: Optional[str] = None
    total_plays: EmptyStringNullableInt = None
    total_time: EmptyStringNullableInt = None




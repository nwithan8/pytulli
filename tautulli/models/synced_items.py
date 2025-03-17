# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:56:39+00:00

from __future__ import annotations

from typing import Optional

from tautulli.models._base import _Base, EmptyStringNullableInt


class SyncedItemsModel(_Base):
    audio_bitrate: Optional[str] = None
    client_id: Optional[str] = None
    content_type: Optional[str] = None
    device_name: Optional[str] = None
    failure: Optional[str] = None
    item_complete_count: Optional[str] = None
    item_count: Optional[str] = None
    item_downloaded_count: Optional[str] = None
    item_downloaded_percent_complete: EmptyStringNullableInt = None
    metadata_type: Optional[str] = None
    photo_quality: Optional[str] = None
    platform: Optional[str] = None
    rating_key: Optional[str] = None
    root_title: Optional[str] = None
    state: Optional[str] = None
    sync_id: Optional[str] = None
    sync_title: Optional[str] = None
    total_size: Optional[str] = None
    user: Optional[str] = None
    user_id: Optional[str] = None
    username: Optional[str] = None
    video_bitrate: Optional[str] = None
    video_quality: Optional[str] = None




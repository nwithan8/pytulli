# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2022-08-26T22:20:41+00:00

from __future__ import annotations

from typing import List, Optional

from tautulli.models._base import _Base, EmptyStringNullableInt


class MetadataFieldModel(_Base):
    field: Optional[str] = None
    level: EmptyStringNullableInt = None


class MediaInfoFieldModel(_Base):
    field: Optional[str] = None
    level: EmptyStringNullableInt = None


class ExportFieldsModel(_Base):
    metadata_fields: Optional[List[MetadataFieldModel]] = None
    media_info_fields: Optional[List[MediaInfoFieldModel]] = None

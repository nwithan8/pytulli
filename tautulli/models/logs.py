# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:40:08+00:00

from __future__ import annotations

from typing import Optional

from tautulli.models._base import _Base


class LogEntryModel(_Base):
    time: Optional[str] = None
    loglevel: Optional[str] = None
    msg: Optional[str] = None
    thread: Optional[str] = None




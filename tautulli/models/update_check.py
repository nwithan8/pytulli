# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:26:04+00:00

from __future__ import annotations

from typing import Optional

from tautulli.models._base import _Base


class UpdateCheckModel(_Base):
    update: Optional[bool] = None
    install_type: Optional[str] = None

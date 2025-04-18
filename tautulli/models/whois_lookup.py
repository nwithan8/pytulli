# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:06:32+00:00

from __future__ import annotations

from typing import List, Optional

from tautulli.models._base import _Base


class NetModel(_Base):
    cidr: Optional[str] = None
    name: Optional[str] = None
    handle: Optional[str] = None
    range: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    postal_code: Optional[str] = None
    emails: Optional[List[str]] = None
    created: Optional[str] = None
    updated: Optional[str] = None


class WHOISLookupModel(_Base):
    host: Optional[str] = None
    nets: Optional[List[NetModel]] = None




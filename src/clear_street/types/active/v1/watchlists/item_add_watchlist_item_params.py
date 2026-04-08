# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ...security_id_source import SecurityIDSource

__all__ = ["ItemAddWatchlistItemParams"]


class ItemAddWatchlistItemParams(TypedDict, total=False):
    instrument_id: Optional[str]
    """OEMS instrument ID (mutually exclusive with security_id/security_id_source)"""

    security_id: Optional[str]
    """Security identifier"""

    security_id_source: Optional[SecurityIDSource]
    """Security identifier source"""

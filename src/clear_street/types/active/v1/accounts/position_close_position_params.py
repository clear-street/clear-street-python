# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...security_id_source import SecurityIDSource

__all__ = ["PositionClosePositionParams"]


class PositionClosePositionParams(TypedDict, total=False):
    account_id: Required[int]

    security_id_source: Required[SecurityIDSource]
    """Security identifier source"""

    cancel_orders: Optional[bool]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SnapshotQuote"]


class SnapshotQuote(BaseModel):
    """L1 quote fields for a market data snapshot."""

    ask: Optional[str] = None
    """Current best ask.

    Absent when no ask is available (one-sided quote). When a null/undefined value
    is observed, it indicates that there is no available data.
    """

    ask_size: Optional[int] = None
    """
    Size at the best ask, in shares. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    bid: Optional[str] = None
    """Current best bid.

    Absent when no bid is available (one-sided quote). When a null/undefined value
    is observed, it indicates that there is no available data.
    """

    bid_size: Optional[int] = None
    """
    Size at the best bid, in shares. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    midpoint: Optional[str] = None
    """Midpoint of bid and ask.

    Absent when either side is missing. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

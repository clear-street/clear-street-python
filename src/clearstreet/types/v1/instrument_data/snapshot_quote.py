# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SnapshotQuote"]


class SnapshotQuote(BaseModel):
    """L1 quote fields for a market data snapshot."""

    ask: str
    """Current best ask."""

    bid: str
    """Current best bid."""

    midpoint: str
    """Midpoint of bid and ask."""

    ask_size: Optional[int] = None
    """
    Size at the best ask, in shares. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    bid_size: Optional[int] = None
    """
    Size at the best bid, in shares. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

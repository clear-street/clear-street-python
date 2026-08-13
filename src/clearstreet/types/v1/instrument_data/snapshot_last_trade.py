# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SnapshotLastTrade"]


class SnapshotLastTrade(BaseModel):
    """Last-trade fields for a market data snapshot.

    For index instruments this carries the current index *level* — a computed
    value, not a trade: `price` is the level and `size` is always `0` (no
    contract changes hands).
    """

    price: str
    """Most recent last-sale eligible trade price.

    For index instruments, the current index level.
    """

    size: int
    """Share quantity of the most recent last-sale eligible trade.

    Always `0` for index instruments, whose level is computed rather than traded.
    """

    timestamp: Optional[datetime] = None
    """Exchange timestamp of the most recent last-sale eligible trade.

    For index instruments, the time the index level was computed. Absent when the
    trade carries no timestamp. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    venue: Optional[str] = None
    """
    ISO 10383 Market Identifier Code (MIC) of the venue where the most recent
    last-sale eligible trade took place. Absent when the trade carries no venue;
    index levels are computed rather than traded and have no venue. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

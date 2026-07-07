# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

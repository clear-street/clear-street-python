# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SnapshotSession"]


class SnapshotSession(BaseModel):
    """Session-level pricing metrics for a market data snapshot."""

    change: str
    """Absolute change from previous close to last trade."""

    change_percent: str
    """Percent change from previous close to last trade."""

    previous_close: str
    """Previous session close price.

    Corporate-action-adjusted (stock dividends, cash dividends, and forward/reverse
    splits) when an adjustment exists for the close date; the raw close otherwise.
    """

    previous_close_unadjusted: Optional[str] = None
    """Unadjusted (raw) previous session close.

    Present only when a corporate-action adjustment exists for the previous close
    date; when no adjustment exists, `previous_close` is the raw close and this
    field is omitted. When a null/undefined value is observed, it indicates that
    there is no available data.
    """

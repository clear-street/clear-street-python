# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .snapshot_quote import SnapshotQuote
from .snapshot_greeks import SnapshotGreeks
from .snapshot_session import SnapshotSession
from .snapshot_last_trade import SnapshotLastTrade

__all__ = ["MarketDataSnapshot"]


class MarketDataSnapshot(BaseModel):
    """Market data snapshot for a single security."""

    instrument_id: str
    """Unique instrument identifier."""

    symbol: str
    """Display symbol for the security."""

    cumulative_volume: Optional[int] = None
    """
    Cumulative traded volume reported on the most recent trade, in shares for
    equities or contracts for options. Absent when no trade is available. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    greeks: Optional[SnapshotGreeks] = None
    """Theoretical price and Greeks for option instruments.

    `None` for equities, and for options whose Greeks have not yet been observed
    When a null/undefined value is observed, it indicates that there is no available
    data.
    """

    last_quote: Optional[SnapshotQuote] = None
    """
    Most recent quote if available. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    last_trade: Optional[SnapshotLastTrade] = None
    """
    Most recent last-sale trade if available. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    name: Optional[str] = None
    """
    Security name if available. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    session: Optional[SnapshotSession] = None
    """
    Session metrics computed from previous close and last trade, if available. When
    a null/undefined value is observed, it indicates that there is no available
    data.
    """

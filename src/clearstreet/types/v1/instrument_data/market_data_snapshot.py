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
    equities or contracts for options. Absent when no trade is available.
    """

    greeks: Optional[SnapshotGreeks] = None
    """Theoretical price and Greeks for option instruments.

    `None` for equities, and for options whose Greeks have not yet been observed
    """

    last_quote: Optional[SnapshotQuote] = None
    """Most recent quote if available."""

    last_trade: Optional[SnapshotLastTrade] = None
    """Most recent last-sale trade if available."""

    name: Optional[str] = None
    """Security name if available."""

    session: Optional[SnapshotSession] = None
    """Session metrics computed from previous close and last trade, if available."""

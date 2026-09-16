# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .snapshot_quote import SnapshotQuote
from .snapshot_greeks import SnapshotGreeks
from .snapshot_rule201 import SnapshotRule201
from .snapshot_session import SnapshotSession
from .snapshot_last_trade import SnapshotLastTrade

__all__ = ["MarketDataSnapshot"]


class MarketDataSnapshot(BaseModel):
    """Market data snapshot for a single security."""

    instrument_id: str
    """Unique instrument identifier."""

    rule_201: SnapshotRule201
    """Live SEC Rule 201 short-sale price test state, from the trading-status feed.

    Always present.

    This is the current market condition, not a statement about whether Clear Street
    will reject your order. It is also distinct from `is_short_prohibited` on the
    instrument endpoints, which is a standing property of the security rather than a
    live circuit breaker.
    """

    session: SnapshotSession
    """Session-level pricing and OHLV metrics.

    Always present; each inner field is independently nullable.
    """

    symbol: str
    """Display symbol for the security."""

    cumulative_volume: Optional[int] = None
    """
    Cumulative traded volume reported on the most recent trade, in shares for
    equities or contracts for options. Absent when no trade is available.

    Deprecated: use `session.cumulative_volume`, the same value from the same
    source. When a null/undefined value is observed, it indicates that there is no
    available data.
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
    """Most recent last-sale-eligible trade if available.

    Omitted when the most recent known print is ineligible (e.g. an odd lot or an
    out-of-sequence report) rather than showing that print's price. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    name: Optional[str] = None
    """
    Security name if available. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    open_interest: Optional[int] = None
    """Open interest (outstanding contracts) as of the most recent OPRA Refresh.

    Populated for options only; absent for equities and indices. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

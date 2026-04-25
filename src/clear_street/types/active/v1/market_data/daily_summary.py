# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ....._models import BaseModel

__all__ = ["DailySummary"]


class DailySummary(BaseModel):
    """Daily aggregate (OHLV) summary for a single instrument.

    Returned by `GET /market-data/daily-summary`. Every field except
    `instrument_id` is `Option`:
    - Unresolvable `instrument_id` → all other fields `None` (including `symbol`).
    - Resolvable `instrument_id` with no realtime cache entry → `symbol`
      populated, OHLV/price/`quote_date` `None`.
    - `quote_date` reflects the session the OHLV represents (today during
      trading hours, the last trading date during weekends/holidays).
    """

    instrument_id: str
    """OEMS instrument identifier. Always populated; echoes the request ID."""

    current_price: Optional[str] = None
    """Current market price."""

    high: Optional[str] = None
    """Session high."""

    low: Optional[str] = None
    """Session low."""

    open: Optional[str] = None
    """Opening price for the session."""

    quote_date: Optional[date] = None
    """Session date the OHLV represents, US/Eastern."""

    symbol: Optional[str] = None
    """Display symbol for the security. `None` for unresolvable IDs."""

    volume: Optional[int] = None
    """Session cumulative trading volume."""

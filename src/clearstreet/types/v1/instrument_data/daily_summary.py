# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["DailySummary"]


class DailySummary(BaseModel):
    """Daily aggregate (OHLV) summary for a single instrument.

    Returned by `GET /market-data/daily-summary`. Every field except
    `instrument_id` is `Option`:
    - Unresolvable `instrument_id` → all other fields `None` (including `symbol`).
    - Resolvable `instrument_id` with no realtime cache entry → `symbol`
      populated, OHLV/`trade_date` `None`.
    - `trade_date` reflects the session the OHLV represents (today during
      trading hours, the last trading date during weekends/holidays).
    """

    instrument_id: str
    """Unique instrument identifier. Always populated; echoes the request ID."""

    high: Optional[str] = None
    """
    Session high. When a null/undefined value is observed, it indicates that there
    is no available data.
    """

    low: Optional[str] = None
    """
    Session low. When a null/undefined value is observed, it indicates that there is
    no available data.
    """

    open: Optional[str] = None
    """
    Opening price for the session. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    symbol: Optional[str] = None
    """Display symbol for the security.

    `None` for unresolvable IDs. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    trade_date: Optional[date] = None
    """
    Session date the OHLV represents, US/Eastern. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    volume: Optional[int] = None
    """
    Session cumulative trading volume. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

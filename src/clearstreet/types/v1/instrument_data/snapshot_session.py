# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["SnapshotSession"]


class SnapshotSession(BaseModel):
    """Session-level pricing and OHLV metrics for a market data snapshot.

    Always
    present on the snapshot row; every field here is independently nullable
    except `ohlv_applicable`.
    """

    ohlv_applicable: bool
    """`false` only for instrument types with no OHLV by definition (e.g.

    an index instrument, whose price is a computed level rather than a traded
    security) -- `open`/`high`/`low`/`ohlv_date`/`cumulative_volume` are then always
    absent. `true` otherwise, even when those fields simply haven't loaded yet.
    Always serialized.
    """

    change: Optional[str] = None
    """Absolute change from previous close to the most recent last-sale-eligible trade.

    Absent when either side of the computation is unavailable. When a null/undefined
    value is observed, it indicates that there is no available data.
    """

    change_percent: Optional[str] = None
    """Percent change from previous close to the most recent last-sale-eligible trade.

    Absent under the same conditions as `change`. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    cumulative_volume: Optional[int] = None
    """
    Cumulative traded volume for the current session, in shares for equities or
    contracts for options. Always reflects the current session, even when
    `ohlv_date` trails it. Absent when `ohlv_applicable` is `false`, or when no
    trade is available. When a null/undefined value is observed, it indicates that
    there is no available data.
    """

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

    ohlv_date: Optional[date] = None
    """Session date the open/high/low values represent, US/Eastern.

    May trail the current session until the upstream feed rolls. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    open: Optional[str] = None
    """Session opening price, from the day's OHLC bar.

    Absent when `ohlv_applicable` is `false`, or when the bar has not loaded yet.
    When a null/undefined value is observed, it indicates that there is no available
    data.
    """

    previous_close: Optional[str] = None
    """Previous session close price.

    Corporate-action-adjusted (stock dividends, cash dividends, and forward/reverse
    splits) when an adjustment exists for the close date; the raw close otherwise.
    An adjustment can carry the price beyond 2 decimal places. Absent when no
    previous close is on record (e.g. an instrument's first session). When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    previous_close_unadjusted: Optional[str] = None
    """Unadjusted (raw) previous session close.

    Present only when a corporate-action adjustment exists for the previous close
    date; when no adjustment exists, `previous_close` is the raw close and this
    field is omitted. When a null/undefined value is observed, it indicates that
    there is no available data.
    """

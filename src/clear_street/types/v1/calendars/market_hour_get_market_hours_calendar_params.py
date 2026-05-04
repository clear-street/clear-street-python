# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .market_type import MarketType

__all__ = ["MarketHourGetMarketHoursCalendarParams"]


class MarketHourGetMarketHoursCalendarParams(TypedDict, total=False):
    date: Required[str]
    """The date to query market hours for (YYYY-MM-DD). Defaults to today."""

    market: MarketType
    """Market type to query (us_equities, us_options).

    If omitted, returns all markets.
    """

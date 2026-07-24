# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CalendarGetMarketHoursCalendarParams"]


class CalendarGetMarketHoursCalendarParams(TypedDict, total=False):
    date: str
    """The date to query market hours for (YYYY-MM-DD). Defaults to today."""

    market: Literal["us_equities", "us_options"]
    """Market type to query (us_equities, us_options).

    If omitted, returns all markets.
    """

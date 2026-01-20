# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MarketHourGetMarketHoursCalendarParams"]


class MarketHourGetMarketHoursCalendarParams(TypedDict, total=False):
    date: Required[str]
    """The date to query market hours for (YYYY-MM-DD)"""

    venue: str
    """The MIC code of the venue"""

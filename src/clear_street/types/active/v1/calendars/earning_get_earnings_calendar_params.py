# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EarningGetEarningsCalendarParams"]


class EarningGetEarningsCalendarParams(TypedDict, total=False):
    from_date: Required[str]
    """The start date for the query range, inclusive (YYYY-MM-DD)"""

    to_date: Required[str]
    """The end date for the query range, inclusive (YYYY-MM-DD)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentDataGetInstrumentEarningsTranscriptsParams", "Date"]


class InstrumentDataGetInstrumentEarningsTranscriptsParams(TypedDict, total=False):
    date: Date

    event_date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """
    Return only transcripts whose call date is within one day of this earnings event
    date (`YYYY-MM-DD`). Use an event's `date` to fetch that event's transcript.
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    period: Literal["Q1", "Q2", "Q3", "Q4"]
    """Only return the transcript for this fiscal quarter."""

    year: int
    """Only return the transcript for this fiscal year."""


class Date(TypedDict, total=False):
    gt: str
    """Return only rows where `date` is strictly after the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    from the start of the following day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    gte: str
    """Return only rows where `date` is on or after the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lt: str
    """Return only rows where `date` is strictly before the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lte: str
    """Return only rows where `date` is on or before the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    through the end of that day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

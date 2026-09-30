# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["CalendarGetEconomicEventsCalendarParams", "Timestamp"]


class CalendarGetEconomicEventsCalendarParams(TypedDict, total=False):
    country: str
    """Comma-separated ISO 3166-1 alpha-2 country codes (or `EU`) to filter by.

    Defaults to `US` when omitted.
    """

    impact: List[Literal["NONE", "LOW", "MEDIUM", "HIGH"]]
    """Comma-separated impact levels to filter by."""

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    timestamp: Timestamp


class Timestamp(TypedDict, total=False):
    gt: str
    """Return only rows where `timestamp` is strictly after the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    from the start of the following day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    gte: str
    """Return only rows where `timestamp` is on or after the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lt: str
    """Return only rows where `timestamp` is strictly before the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lte: str
    """Return only rows where `timestamp` is on or before the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    through the end of that day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentGetPredictionEventsParams", "CloseAt", "OpenAt"]


class InstrumentGetPredictionEventsParams(TypedDict, total=False):
    categories: str
    """Comma-separated categories.

    Keeps events with a listable market in any of them, ignoring case.
    """

    close_at: CloseAt

    include_markets: bool
    """Embed a summary of every market of each event, in any status. Default false."""

    include_settled: bool
    """Also list settled and expired events, not only events with a listable market.

    Every market then counts as listable for the other filters, `title`,
    `categories`, and the open and close times. Default false. A request that takes
    longer than 30 seconds fails with `504`; narrow `search` or the filters and try
    again.
    """

    market_ids: str
    """Comma-separated market ids (UUID) or tickers, 1-100.

    Keeps events of those markets, in any status; the other filters still apply. Ids
    that match no market are reported: `207`, or `404` when none match.
    """

    open_at: OpenAt

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    search: str
    """
    Keeps events whose code, series code, or a market's question or title contains
    every word, matched by prefix and English stem, ignoring case. Searches listable
    events, or every event with `include_settled`. A word of four or more letters
    that matches nothing is replaced by up to three close spellings. Without
    `sort_by`, orders by relevance, closest spellings first.
    """

    series_codes: str
    """Comma-separated series codes. Keeps events of those series, ignoring case."""

    sort_by: Literal["OPEN_AT", "CLOSE_AT"]
    """Sort key.

    Defaults to relevance when `search` is set, else the event code. Ties break on
    event code ascending.
    """

    sort_direction: Literal["ASC", "DESC"]
    """Sort direction. Defaults to ascending. Ignored when sorting by relevance."""


class CloseAt(TypedDict, total=False):
    gt: str
    """Return only rows where `close_at` is strictly after the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    from the start of the following day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    gte: str
    """Return only rows where `close_at` is on or after the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lt: str
    """Return only rows where `close_at` is strictly before the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lte: str
    """Return only rows where `close_at` is on or before the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    through the end of that day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """


class OpenAt(TypedDict, total=False):
    gt: str
    """Return only rows where `open_at` is strictly after the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    from the start of the following day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    gte: str
    """Return only rows where `open_at` is on or after the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lt: str
    """Return only rows where `open_at` is strictly before the given value.

    A bare `YYYY-MM-DD` date expands to the start of that day (UTC). See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

    lte: str
    """Return only rows where `open_at` is on or before the given value.

    A bare `YYYY-MM-DD` date expands to the end of that day (UTC), so this matches
    through the end of that day. See
    [Range filters](https://docs.clearstreet.com/guides/api-fundamentals#range-filters)
    for accepted formats, bare-date expansion, and combining bounds. Returns 400 if
    the resulting range is inverted.
    """

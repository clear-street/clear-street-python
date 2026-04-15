# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr, Base64FileInput
from ...._utils import PropertyInfo

__all__ = ["NewsGetNewsParams"]


class NewsGetNewsParams(TypedDict, total=False):
    exclude_publishers: str
    """
    Comma-separated list of publishers to exclude (mutually exclusive with
    include_publishers).
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Inclusive start timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime."""

    include_publishers: str
    """
    Comma-separated list of publishers to include (mutually exclusive with
    exclude_publishers).
    """

    instrument_ids: SequenceNotStr[str]
    """Comma-delimited OEMS instrument UUIDs to filter by."""

    news_type: Literal["NEWS", "PRESS_RELEASE"]
    """Filter by news type."""

    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    search_query: str
    """Free-text query matched against title/text and associated security IDs."""

    security_id: SequenceNotStr[str]
    """Filter by security ID(s). Accepts single value or indexed array.

    Examples:

    - Single: `security_id=037833100`
    - Multiple: `security_id[0]=037833100&security_id[1]=594918104`
    """

    security_id_source: SequenceNotStr[str]
    """Source(s) for the security ID filter.

    Must match the count and order of security_id.

    Examples:

    - Single: `security_id_source=CUSIP`
    - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`
    """

    to: str
    """Inclusive end timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime."""

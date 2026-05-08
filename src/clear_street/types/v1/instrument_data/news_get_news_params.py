# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
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

    sectors: List[
        Literal[
            "BASIC_MATERIALS",
            "COMMUNICATION_SERVICES",
            "CONSUMER_CYCLICAL",
            "CONSUMER_DEFENSIVE",
            "ENERGY",
            "FINANCIAL_SERVICES",
            "HEALTHCARE",
            "INDUSTRIALS",
            "REAL_ESTATE",
            "TECHNOLOGY",
            "UTILITIES",
        ]
    ]
    """Comma-separated sector values to filter by."""

    to: str
    """Inclusive end timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["OrderGetExecutionsParams"]


class OrderGetExecutionsParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """The start date and time for the query range, inclusive (ISO 8601 format)"""

    instrument_ids: SequenceNotStr[str]
    """Comma-separated instrument identifiers (UUIDs) or symbols (e.g.

    `AAPL`) to filter by. When provided, only executions for any of the listed
    instruments are returned.
    """

    order_ids: SequenceNotStr[str]
    """Comma-separated order IDs to filter by.

    When provided, only executions belonging to an order in this set are returned.
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end date and time for the query range, inclusive (ISO 8601 format)"""

    underlying_instrument_ids: SequenceNotStr[str]
    """
    Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
    symbols). Matches option fills whose resolved underlier is any of the given
    instruments.
    """

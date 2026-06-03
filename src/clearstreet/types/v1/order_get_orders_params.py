# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["OrderGetOrdersParams"]


class OrderGetOrdersParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """The start date and time for the query range, inclusive (ISO 8601 format)"""

    instrument_ids: SequenceNotStr[str]
    """Comma-separated OEMS instrument UUIDs"""

    instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"]
    """Instrument type filter (e.g., COMMON_STOCK, OPTION)"""

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    status: List[
        Literal[
            "PENDING_NEW",
            "NEW",
            "PARTIALLY_FILLED",
            "FILLED",
            "CANCELED",
            "REJECTED",
            "EXPIRED",
            "PENDING_CANCEL",
            "PENDING_REPLACE",
            "REPLACED",
            "DONE_FOR_DAY",
            "STOPPED",
            "SUSPENDED",
            "CALCULATED",
            "OTHER",
        ]
    ]
    """Comma-separated order statuses to filter by"""

    symbol: str
    """Filter by symbol"""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end date and time for the query range, inclusive (ISO 8601 format)"""

    underlying_instrument_ids: SequenceNotStr[str]
    """Comma-separated OEMS instrument UUIDs.

    Matches options orders whose resolved underlier is any of the given IDs.
    """

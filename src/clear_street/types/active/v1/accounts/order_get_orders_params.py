# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr, Base64FileInput
from ....._utils import PropertyInfo

__all__ = ["OrderGetOrdersParams"]


class OrderGetOrdersParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """The start date and time for the query range, inclusive (ISO 8601 format)"""

    instrument_type: Literal[
        "COMMON_STOCK", "PREFERRED_STOCK", "CORPORATE_BOND", "OPTION", "FUTURE", "WARRANT", "CASH", "OTHER"
    ]
    """Instrument type filter (e.g., COMMON_STOCK, OPTION)"""

    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

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

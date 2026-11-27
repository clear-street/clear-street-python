# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["AccountGetNonTradeActivitiesParams"]


class AccountGetNonTradeActivitiesParams(TypedDict, total=False):
    activity_type: List[
        Literal[
            "MONEY_MOVEMENT",
            "INTEREST",
            "FEE",
            "DIVIDEND",
            "OPTION_EVENT",
            "TRANSFER",
            "CORPORATE_ACTION",
            "TAX_WITHHOLDING",
            "ADJUSTMENT",
            "OTHER",
        ]
    ]
    """Filter by activity type(s).

    Comma-delimited list. Example: `activity_type=dividend,fee`.
    """

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """The start date and time for the query range, inclusive (ISO 8601 format)"""

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided. A value of 0 is rejected; a value
    above the maximum is treated as the maximum.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end date and time for the query range, inclusive (ISO 8601 format)"""

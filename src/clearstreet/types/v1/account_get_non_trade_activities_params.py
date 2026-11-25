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
            "money_movement",
            "interest",
            "fee",
            "dividend",
            "option_event",
            "transfer",
            "corporate_action",
            "tax_withholding",
            "adjustment",
            "other",
        ]
    ]
    """Filter by activity type(s).

    Comma-delimited list. Example: `activity_type=dividend,fee`.
    """

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """The start date and time for the query range, inclusive (ISO 8601 format)"""

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

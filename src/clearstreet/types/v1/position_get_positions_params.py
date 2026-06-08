# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["PositionGetPositionsParams"]


class PositionGetPositionsParams(TypedDict, total=False):
    instrument_ids: SequenceNotStr[str]
    """Comma-separated instrument identifiers"""

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    sort_by: Literal[
        "SYMBOL",
        "INSTRUMENT_TYPE",
        "QUANTITY",
        "MARKET_VALUE",
        "POSITION_TYPE",
        "UNREALIZED_PNL",
        "DAILY_UNREALIZED_PNL",
    ]
    """Field to sort by"""

    sort_direction: Literal["ASC", "DESC"]
    """Sort direction"""

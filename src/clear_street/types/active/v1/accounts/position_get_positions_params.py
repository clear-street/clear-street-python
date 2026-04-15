# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr, Base64FileInput
from ....._utils import PropertyInfo

__all__ = ["PositionGetPositionsParams"]


class PositionGetPositionsParams(TypedDict, total=False):
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

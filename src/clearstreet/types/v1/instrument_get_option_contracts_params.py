# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentGetOptionContractsParams"]


class InstrumentGetOptionContractsParams(TypedDict, total=False):
    contract_type: Literal["CALL", "PUT"]
    """Filter by contract type: CALL or PUT"""

    expiry: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter to contracts expiring on this date (YYYY-MM-DD)"""

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    underlier: str
    """Underlier symbol (e.g., AAPL, SPX)"""

    underlying_instrument_id: str
    """Instrument identifier or symbol of the underlying equity/index"""

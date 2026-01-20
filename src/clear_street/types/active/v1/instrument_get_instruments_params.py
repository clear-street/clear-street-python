# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ...._types import Base64FileInput
from ...._utils import PropertyInfo
from ..security_type import SecurityType

__all__ = ["InstrumentGetInstrumentsParams"]


class InstrumentGetInstrumentsParams(TypedDict, total=False):
    easy_to_borrow: bool
    """Filter by easy to borrow status"""

    id_filter: str
    """Filter IDs to those containing this substring.

    For options, this is required and is used to filter exclusively to the
    underlying symbol.
    """

    is_liquidation_only: bool
    """Filter by liquidation only status"""

    is_marginable: bool
    """Filter by marginable status"""

    is_restricted: bool
    """Filter by restricted status"""

    is_short_prohibited: bool
    """filter by short prohibited status"""

    is_threshold_security: bool
    """Filter by threshold security status"""

    page_size: int
    """
    The number of items to return per page (only used when page_token is not
    provided)
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    security_type: SecurityType
    """Filter by security type, required and defaults to `COMMON_STOCK`"""

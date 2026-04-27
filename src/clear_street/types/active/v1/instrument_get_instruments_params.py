# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr, Base64FileInput
from ...._utils import PropertyInfo

__all__ = ["InstrumentGetInstrumentsParams"]


class InstrumentGetInstrumentsParams(TypedDict, total=False):
    easy_to_borrow: bool
    """Filter by easy to borrow status"""

    id_filter: str
    """Filter IDs to those containing this substring.

    For options, and when instrument_type is omitted and no
    security_id/security_id_source filters are provided, this is required.
    """

    instrument_type: Literal[
        "COMMON_STOCK", "PREFERRED_STOCK", "CORPORATE_BOND", "OPTION", "FUTURE", "WARRANT", "CASH", "OTHER"
    ]
    """Filter by instrument type. If omitted, returns all types."""

    is_liquidation_only: bool
    """Filter by liquidation only status"""

    is_marginable: bool
    """Filter by marginable status"""

    is_restricted: bool
    """Filter by restricted status"""

    is_short_prohibited: bool
    """Filter by short prohibited status"""

    is_threshold_security: bool
    """Filter by threshold security status"""

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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentGetInstrumentsParams"]


class InstrumentGetInstrumentsParams(TypedDict, total=False):
    easy_to_borrow: bool
    """Filter by easy to borrow status"""

    instrument_ids: SequenceNotStr[str]
    """Comma-separated OEMS instrument UUIDs"""

    instrument_type: Literal["COMMON_STOCK", "PREFERRED_STOCK", "OPTION", "CASH", "OTHER"]
    """Filter by instrument type.

    OPTION is not supported on this endpoint; use GET /instruments/options/contracts
    to list option contracts. If omitted, returns all supported instrument types
    except options.
    """

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

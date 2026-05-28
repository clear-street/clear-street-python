# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr, Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentGetInstrumentsParams"]


class InstrumentGetInstrumentsParams(TypedDict, total=False):
    easy_to_borrow: bool
    """Filter by easy to borrow status"""

    instrument_ids: SequenceNotStr[str]
    """Comma-separated OEMS instrument UUIDs"""

    is_liquidation_only: bool
    """Filter by liquidation only status"""

    is_marginable: bool
    """Filter by marginable status"""

    is_ptp: bool
    """Filter by publicly traded partnership (PTP) status"""

    is_short_prohibited: bool
    """Filter by short prohibited status"""

    is_threshold_security: bool
    """Filter by threshold security status"""

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

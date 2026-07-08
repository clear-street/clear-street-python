# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentSearchInstrumentsParams"]


class InstrumentSearchInstrumentsParams(TypedDict, total=False):
    q: Required[str]
    """
    Search term applied case-insensitively to ticker symbols, alternate identifiers
    (CUSIP, ISIN, OPRA root), and company names for non-option instruments. Option
    searches match symbols and alternate identifiers.
    """

    asset_class: str
    """Comma-separated asset classes (EQUITY|OPTION|WARRANT|BOND|FX|OTHER).

    Defaults to EQUITY.
    """

    country: str
    """Optional listing-country filter (e.g., US)."""

    currency: str
    """Optional ISO currency filter (e.g., USD)."""

    include_inactive: bool
    """Include inactive instruments. Default false."""

    include_ptp: bool
    """Include publicly traded partnership (PTP) instruments.

    Default true (penalized in ranking).
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

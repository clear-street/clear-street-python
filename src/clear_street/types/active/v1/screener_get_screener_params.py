# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr, Base64FileInput
from ...._utils import PropertyInfo

__all__ = ["ScreenerGetScreenerParams"]


class ScreenerGetScreenerParams(TypedDict, total=False):
    field_filter: SequenceNotStr[str]
    """Comma-separated list of field names to include in the response"""

    filter: Dict[str, str]
    """
    Dynamic filters with dot notation (e.g., filter[price.gte]=50,
    filter[symbol.bw]=A)
    """

    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    sort_by: str
    """Field to sort by"""

    sort_direction: Literal["ASC", "DESC"]
    """Sort direction (ASC or DESC, defaults to DESC)"""

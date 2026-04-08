# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr
from .saved_screener_filter_param import SavedScreenerFilterParam

__all__ = ["SavedScreenerUpdateScreenerParams"]


class SavedScreenerUpdateScreenerParams(TypedDict, total=False):
    field_filter: Optional[SequenceNotStr[str]]
    """List of field names to include when running this screener"""

    filters: Optional[Iterable[SavedScreenerFilterParam]]
    """Filter criteria for this screener"""

    name: Optional[str]
    """The name for this screener configuration"""

    sort_by: Optional[str]
    """Field name to sort results by"""

    sort_direction: Optional[Literal["ASC", "DESC"]]
    """Sort direction for results"""

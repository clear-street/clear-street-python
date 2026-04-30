# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .field_ref_param import FieldRefParam
from .search_filter_param import SearchFilterParam

__all__ = ["SavedScreenerCreateScreenerParams"]


class SavedScreenerCreateScreenerParams(TypedDict, total=False):
    field_filter: Optional[Iterable[FieldRefParam]]
    """Structured field references to include when running this screener"""

    filters: Optional[Iterable[SearchFilterParam]]
    """Structured search filter criteria"""

    name: Optional[str]
    """The name for this screener configuration"""

    sort_by: Optional[FieldRefParam]
    """Structured field reference to sort results by"""

    sort_direction: Optional[Literal["ASC", "DESC"]]
    """Sort direction for results"""

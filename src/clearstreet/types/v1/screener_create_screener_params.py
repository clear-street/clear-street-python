# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .field_ref_param import FieldRefParam
from .sort_spec_param import SortSpecParam
from .search_filter_param import SearchFilterParam

__all__ = ["ScreenerCreateScreenerParams"]


class ScreenerCreateScreenerParams(TypedDict, total=False):
    columns: Optional[Iterable[FieldRefParam]]
    """Structured field references to include when running this screener"""

    filters: Optional[Iterable[SearchFilterParam]]
    """Structured search filter criteria"""

    name: Optional[str]
    """The name for this screener configuration"""

    sorts: Optional[Iterable[SortSpecParam]]
    """Multi-field sort specifications"""

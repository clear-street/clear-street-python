# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .field_ref_param import FieldRefParam
from .search_filter_param import SearchFilterParam

__all__ = ["ScreenerSearchScreenerParams", "Sort"]


class ScreenerSearchScreenerParams(TypedDict, total=False):
    field_filter: Optional[Iterable[FieldRefParam]]
    """Subset of fields to include in the response."""

    filters: Optional[Iterable[SearchFilterParam]]
    """Filter conditions to apply."""

    page_size: Optional[int]
    """Maximum number of results per page."""

    page_token: Optional[str]
    """Opaque token for cursor-based pagination."""

    sort_by: Optional[FieldRefParam]
    """Field to sort results by."""

    sort_case_sensitive: Optional[bool]
    """Whether string sorts should be case-sensitive (default: false)."""

    sort_direction: Literal["ASC", "DESC"]
    """Sort direction (defaults to DESC)."""

    sorts: Optional[Iterable[Sort]]
    """Multi-field sort specifications.

    When present, takes precedence over sort_by/sort_direction.
    """


class Sort(TypedDict, total=False):
    """A sort specification pairing a field with a direction."""

    field: Required[FieldRefParam]
    """The field to sort by."""

    direction: Literal["ASC", "DESC"]
    """Sort direction (defaults to DESC)."""

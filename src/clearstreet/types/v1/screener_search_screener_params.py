# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from .field_ref_param import FieldRefParam
from .sort_spec_param import SortSpecParam
from .search_filter_param import SearchFilterParam

__all__ = ["ScreenerSearchScreenerParams"]


class ScreenerSearchScreenerParams(TypedDict, total=False):
    columns: Optional[Iterable[FieldRefParam]]
    """Subset of fields to include in the response."""

    field_filter: Optional[Iterable[FieldRefParam]]
    """Deprecated: use `columns` instead. Ignored when `columns` is provided."""

    filters: Optional[Iterable[SearchFilterParam]]
    """Filter conditions to apply."""

    page_size: Optional[int]
    """
    The number of items to return per page (only used when page_token is not
    provided)
    """

    page_token: Annotated[Union[str, Base64FileInput, None], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    sort_case_sensitive: Optional[bool]
    """Whether string sorts should be case-sensitive (default: false)."""

    sorts: Optional[Iterable[SortSpecParam]]
    """Multi-field sort specifications."""

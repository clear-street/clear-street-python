# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .field_ref_param import FieldRefParam
from .sort_spec_param import SortSpecParam
from .search_filter_param import SearchFilterParam

__all__ = ["ScreenerPatchScreenerParams"]


class ScreenerPatchScreenerParams(TypedDict, total=False):
    columns: Optional[Iterable[FieldRefParam]]
    """
    Structured field references to include when running this screener. Omit or send
    `null` to leave unchanged; `[]` clears the stored columns.
    """

    filters: Optional[Iterable[SearchFilterParam]]
    """Structured search filter criteria.

    Omit or send `null` to leave unchanged; `[]` clears the stored filters.
    """

    name: Optional[str]
    """The name for this screener configuration.

    Omit or send `null` to leave unchanged. Cannot be set to an empty string.
    """

    shared: Optional[bool]
    """Whether any user may fetch this screener by id.

    Omit or send `null` to leave unchanged. `false` is a value, not a clear.
    """

    sorts: Optional[Iterable[SortSpecParam]]
    """Multi-field sort specifications.

    Omit or send `null` to leave unchanged; `[]` clears the stored sort.
    """

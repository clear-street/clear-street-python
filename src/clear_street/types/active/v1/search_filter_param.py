# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .field_ref_param import FieldRefParam
from .filter_value_param import FilterValueParam
from .filter_op_spec_param import FilterOpSpecParam

__all__ = ["SearchFilterParam"]


class SearchFilterParam(TypedDict, total=False):
    """A single filter condition.

    When `op` and `right` are both absent, the filter is "unenabled":
    it persists a `left` field reference without applying any predicate.
    Unenabled filters are skipped during search execution but still
    round-trip through save/load so callers can preserve draft state.
    """

    left: Required[FieldRefParam]
    """The field to filter on."""

    op: Optional[FilterOpSpecParam]
    """The operator and optional arguments.

    Omit together with `right` for an unenabled filter.
    """

    right: Optional[Iterable[FilterValueParam]]
    """The value(s) to compare against.

    Omit together with `op` for an unenabled filter.
    """

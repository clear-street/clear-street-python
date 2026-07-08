# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .field_ref import FieldRef
from .filter_value import FilterValue
from .filter_op_spec import FilterOpSpec

__all__ = ["SearchFilter"]


class SearchFilter(BaseModel):
    """A single filter condition.

    When `op` and `right` are both absent, the filter is "unenabled":
    it persists a `left` field reference without applying any predicate.
    Unenabled filters are skipped during search execution but still
    round-trip through save/load so callers can preserve draft state.
    """

    left: FieldRef
    """The field to filter on."""

    op: Optional[FilterOpSpec] = None
    """The operator and optional arguments.

    Omit together with `right` for an unenabled filter.
    """

    right: Optional[List[FilterValue]] = None
    """The value(s) to compare against.

    Omit together with `op` for an unenabled filter.
    """

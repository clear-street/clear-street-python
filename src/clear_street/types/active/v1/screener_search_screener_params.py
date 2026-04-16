# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr
from .field_period import FieldPeriod
from .field_lookback import FieldLookback
from .field_ref_param import FieldRefParam

__all__ = [
    "ScreenerSearchScreenerParams",
    "Filter",
    "FilterOp",
    "FilterRight",
    "FilterRightVariable",
    "FilterRightVariableModifier",
    "Sort",
]


class ScreenerSearchScreenerParams(TypedDict, total=False):
    field_filter: Optional[Iterable[FieldRefParam]]
    """Subset of fields to include in the response."""

    filters: Optional[Iterable[Filter]]
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


class FilterOp(TypedDict, total=False):
    """The operator and optional arguments."""

    name: Required[
        Literal[
            "LT",
            "LTE",
            "GT",
            "GTE",
            "EQ",
            "BETWEEN",
            "NOT_BETWEEN",
            "ONE_OF",
            "REGEX",
            "BEGINS_WITH",
            "ENDS_WITH",
            "CONTAINS",
            "IS_NULL",
            "IS_NOT_NULL",
        ]
    ]
    """The operator to apply."""

    args: List[Literal["LEFT_INCLUSIVE", "RIGHT_INCLUSIVE", "LEFT_EXCLUSIVE", "RIGHT_EXCLUSIVE", "CASE_INSENSITIVE"]]
    """Optional arguments that modify operator behavior."""


class FilterRightVariableModifier(TypedDict, total=False):
    """Optional arithmetic modifier."""

    args: Required[SequenceNotStr[Union[float, str]]]

    name: Required[Literal["ADD", "SUB"]]
    """The modifier operation."""


class FilterRightVariable(TypedDict, total=False):
    """A variable reference."""

    name: Required[str]
    """The variable name."""

    lookback: Optional[FieldLookback]
    """Optional historical lookback window."""

    modifier: Optional[FilterRightVariableModifier]
    """Optional arithmetic modifier."""

    period: Optional[FieldPeriod]
    """Optional reporting period."""


class FilterRight(TypedDict, total=False):
    """A filter value: either a literal or a variable reference."""

    value: Union[float, str, None]

    variable: Optional[FilterRightVariable]
    """A variable reference."""


class Filter(TypedDict, total=False):
    """A single filter condition."""

    left: Required[FieldRefParam]
    """The field to filter on."""

    op: Required[FilterOp]
    """The operator and optional arguments."""

    right: Required[Iterable[FilterRight]]
    """The value(s) to compare against."""


class Sort(TypedDict, total=False):
    """A sort specification pairing a field with a direction."""

    field: Required[FieldRefParam]
    """The field to sort by."""

    direction: Literal["ASC", "DESC"]
    """Sort direction (defaults to DESC)."""

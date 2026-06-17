# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .operator_arg import OperatorArg
from .filter_operator import FilterOperator

__all__ = ["FilterOpSpecParam"]


class FilterOpSpecParam(TypedDict, total=False):
    """Operator specification with optional behavioral arguments."""

    name: Required[FilterOperator]
    """The operator to apply."""

    args: List[OperatorArg]
    """Optional arguments that modify operator behavior."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .operator_arg import OperatorArg
from .filter_operator import FilterOperator

__all__ = ["FilterOpSpec"]


class FilterOpSpec(BaseModel):
    """Operator specification with optional behavioral arguments."""

    name: FilterOperator
    """The operator to apply."""

    args: Optional[List[OperatorArg]] = None
    """Optional arguments that modify operator behavior."""

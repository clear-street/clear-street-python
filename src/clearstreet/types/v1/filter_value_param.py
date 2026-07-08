# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypedDict

from .variable_param import VariableParam

__all__ = ["FilterValueParam"]


class FilterValueParam(TypedDict, total=False):
    """A filter value: either a literal or a variable reference."""

    value: Union[float, str, None]

    variable: Optional[VariableParam]
    """A variable reference."""

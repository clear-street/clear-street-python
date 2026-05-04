# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .field_period import FieldPeriod
from .field_lookback import FieldLookback
from .modifier_param import ModifierParam

__all__ = ["VariableParam"]


class VariableParam(TypedDict, total=False):
    """A variable reference (field or built-in like `today`)."""

    name: Required[str]
    """The variable name."""

    lookback: Optional[FieldLookback]
    """Optional historical lookback window."""

    modifier: Optional[ModifierParam]
    """Optional arithmetic modifier."""

    period: Optional[FieldPeriod]
    """Optional reporting period."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .field_type import FieldType
from .field_period import FieldPeriod
from .field_lookback import FieldLookback

__all__ = ["FieldRefParam"]


class FieldRefParam(TypedDict, total=False):
    """A reference to a screener field."""

    name: Required[str]
    """The field name."""

    lookback: Optional[FieldLookback]
    """Optional historical lookback window."""

    period: Optional[FieldPeriod]
    """Optional reporting period (e.g. quarter or TTM)."""

    value_type: Optional[FieldType]
    """The data type of the field value. Present only in responses."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .field_type import FieldType
from .field_period import FieldPeriod
from .field_lookback import FieldLookback

__all__ = ["FieldRef"]


class FieldRef(BaseModel):
    """A reference to a screener field."""

    name: str
    """The field name."""

    lookback: Optional[FieldLookback] = None
    """Optional historical lookback window."""

    period: Optional[FieldPeriod] = None
    """Optional reporting period (e.g. quarter or TTM)."""

    value_type: Optional[FieldType] = None
    """The data type of the field value. Present only in responses."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .modifier import Modifier
from ..._models import BaseModel
from .field_period import FieldPeriod
from .field_lookback import FieldLookback

__all__ = ["Variable"]


class Variable(BaseModel):
    """A variable reference (field or built-in like `today`)."""

    name: str
    """The variable name."""

    lookback: Optional[FieldLookback] = None
    """Optional historical lookback window."""

    modifier: Optional[Modifier] = None
    """Optional arithmetic modifier."""

    period: Optional[FieldPeriod] = None
    """Optional reporting period."""

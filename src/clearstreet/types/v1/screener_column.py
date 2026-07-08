# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from ..._models import BaseModel
from .field_ref import FieldRef

__all__ = ["ScreenerColumn"]


class ScreenerColumn(BaseModel):
    """A single column in the screener search response."""

    field: FieldRef
    """Field reference (same shape as filter/sort field references)"""

    name: str
    """Human-readable display name for this field"""

    value: Union[float, str, None] = None

    type: Optional[str] = None
    """Value format hint: "CURR_USD", "PERCENT", etc.

    Omitted when not applicable. When a null/undefined value is observed, it
    indicates it does not apply.
    """

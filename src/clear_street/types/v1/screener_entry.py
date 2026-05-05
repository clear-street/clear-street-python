# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .field_ref import FieldRef
from .search_filter import SearchFilter

__all__ = ["ScreenerEntry"]


class ScreenerEntry(BaseModel):
    """A saved screener configuration entry"""

    id: str

    created_at: datetime

    filters: List[SearchFilter]

    name: str

    updated_at: datetime

    field_filter: Optional[List[FieldRef]] = None

    sort_by: Optional[FieldRef] = None
    """A reference to a screener field."""

    sort_direction: Optional[str] = None

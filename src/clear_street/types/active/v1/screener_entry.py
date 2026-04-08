# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .saved_screener_filter import SavedScreenerFilter

__all__ = ["ScreenerEntry"]


class ScreenerEntry(BaseModel):
    """A saved screener configuration entry"""

    id: str
    """Unique identifier for this screener"""

    created_at: datetime
    """When this screener was created"""

    filters: List[SavedScreenerFilter]
    """Filter criteria for this screener"""

    name: str
    """The name of this screener configuration"""

    updated_at: datetime
    """When this screener was last updated"""

    field_filter: Optional[List[str]] = None
    """List of field names to include when running this screener"""

    sort_by: Optional[str] = None
    """Field name to sort results by"""

    sort_direction: Optional[str] = None
    """Sort direction for results"""

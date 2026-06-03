# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .screener_filter import ScreenerFilter

__all__ = ["OpenScreenerAction"]


class OpenScreenerAction(BaseModel):
    """Action to open a stock screener with filters."""

    filters: List[ScreenerFilter]
    """Filter criteria for the screener"""

    field_filter: Optional[List[str]] = None
    """Optional field/column selection for screener results."""

    page_size: Optional[int] = None
    """Optional page size."""

    sort_by: Optional[str] = None
    """Optional sort field for screener rows."""

    sort_direction: Optional[str] = None
    """Optional sort direction (`ASC` or `DESC`)."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .watchlist_item_entry import WatchlistItemEntry

__all__ = ["WatchlistDetail"]


class WatchlistDetail(BaseModel):
    """Detailed watchlist with all items"""

    id: str
    """The unique identifier for the watchlist."""

    created_at: datetime
    """The timestamp when the watchlist was created."""

    items: List[WatchlistItemEntry]
    """Items in the watchlist"""

    name: str
    """The user-provided watchlist name."""

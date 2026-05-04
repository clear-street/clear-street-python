# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .watchlist_item_entry import WatchlistItemEntry

__all__ = ["WatchlistDetail"]


class WatchlistDetail(BaseModel):
    """Detailed watchlist with all items"""

    id: str
    """Watchlist ID"""

    created_at: datetime
    """Creation timestamp"""

    items: List[WatchlistItemEntry]
    """Items in the watchlist"""

    name: str
    """Watchlist name"""

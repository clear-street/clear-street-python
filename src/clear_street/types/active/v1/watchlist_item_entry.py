# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .instrument import Instrument

__all__ = ["WatchlistItemEntry"]


class WatchlistItemEntry(BaseModel):
    """A single item in a watchlist"""

    id: str
    """Item ID"""

    added_at: datetime
    """When the item was added"""

    added_price: Optional[str] = None
    """Price when the item was added"""

    instrument: Optional[Instrument] = None
    """Instrument details"""

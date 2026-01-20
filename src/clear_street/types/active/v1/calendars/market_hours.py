# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ....._models import BaseModel

__all__ = ["MarketHours"]


class MarketHours(BaseModel):
    """Trading hours and market status for a specific venue and date"""

    date: datetime.date
    """The date for which market hours are provided"""

    is_open: bool
    """Whether the market is open for trading on this date"""

    timezone: str
    """IANA timezone identifier for the venue"""

    venue: str
    """The MIC code of the venue"""

    close_time: Optional[str] = None
    """Market close time in local venue timezone (HH:MM:SS). Null if market is closed"""

    holiday_name: Optional[str] = None
    """Name of the holiday if market is closed for a holiday. Null otherwise"""

    next_close: Optional[datetime.datetime] = None
    """Next market close timestamp in UTC"""

    next_open: Optional[datetime.datetime] = None
    """Next market open timestamp in UTC"""

    open_time: Optional[str] = None
    """Market open time in local venue timezone (HH:MM:SS). Null if market is closed"""

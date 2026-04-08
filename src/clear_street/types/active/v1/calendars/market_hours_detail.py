# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ....._models import BaseModel
from .market_type import MarketType
from .market_status import MarketStatus
from .trading_sessions import TradingSessions

__all__ = ["MarketHoursDetail"]


class MarketHoursDetail(BaseModel):
    """Comprehensive market hours information for a specific market and date"""

    current_time: datetime.datetime
    """Current time in market timezone with offset"""

    date: datetime.date
    """The date for which market hours are provided"""

    market: MarketType
    """Market type identifier"""

    market_name: str
    """Human-readable market name"""

    next_sessions: TradingSessions
    """Next trading day's session schedules (without time_until fields)"""

    status: MarketStatus
    """Market status information"""

    timezone: str
    """IANA timezone identifier for the market"""

    today_sessions: TradingSessions
    """Trading session schedules for the requested date with time_until fields"""

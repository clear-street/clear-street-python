# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .day_type import DayType
from ....._models import BaseModel
from .market_session_type import MarketSessionType

__all__ = ["MarketStatus"]


class MarketStatus(BaseModel):
    """Market status information"""

    day_type: DayType
    """The type of trading day"""

    is_open: bool
    """Whether the market is currently open (real-time)"""

    current_session: Optional[MarketSessionType] = None
    """Current session type if market is open, null if closed"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .session_schedule import SessionSchedule

__all__ = ["TradingSessions"]


class TradingSessions(BaseModel):
    """Trading sessions for a market day with full timestamps"""

    after_hours: Optional[SessionSchedule] = None
    """After-hours session schedule, null if not available"""

    pre_market: Optional[SessionSchedule] = None
    """Pre-market session schedule, null if not available"""

    regular: Optional[SessionSchedule] = None
    """Regular trading session schedule, null if holiday/weekend"""

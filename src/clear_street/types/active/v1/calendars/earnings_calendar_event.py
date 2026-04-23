# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ....._models import BaseModel

__all__ = ["EarningsCalendarEvent"]


class EarningsCalendarEvent(BaseModel):
    """Represents a single earnings announcement event"""

    date: datetime.date
    """The date of the earnings announcement"""

    last_updated: datetime.date
    """The date of the last update to this event"""

    symbol: str
    """The symbol for the instrument"""

    eps_actual: Optional[str] = None
    """The actual reported earnings per share"""

    eps_estimated: Optional[str] = None
    """The consensus estimated earnings per share"""

    revenue_actual: Optional[str] = None
    """The actual reported revenue"""

    revenue_estimated: Optional[str] = None
    """The consensus estimated revenue"""

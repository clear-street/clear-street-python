# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["EconomicCalendarEvent"]


class EconomicCalendarEvent(BaseModel):
    """Represents a single economic calendar event"""

    country: str
    """The ISO 3166-1 alpha-2 country code"""

    currency: str
    """The ISO 4217 currency code"""

    event_name: str
    """The name of the economic event"""

    event_timestamp: datetime
    """The date and time of the event in UTC"""

    impact: Literal["LOW", "MEDIUM", "HIGH"]
    """The expected market impact of the event"""

    actual_value: Optional[str] = None
    """The actual value reported for the event"""

    change_percent: Optional[str] = None
    """The percentage change between the actual and previous values"""

    estimated_value: Optional[str] = None
    """The market consensus estimate for the event's value"""

    previous_value: Optional[str] = None
    """The previous value for this event"""

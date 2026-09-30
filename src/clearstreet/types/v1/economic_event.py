# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .economic_event_unit import EconomicEventUnit
from .economic_event_impact import EconomicEventImpact

__all__ = ["EconomicEvent"]


class EconomicEvent(BaseModel):
    """A single economic calendar event.

    Coverage spans roughly 365 days back to 90 days forward. `estimate` and
    `actual` are frequently absent for minor releases, speeches, and holidays.
    The calendar refreshes daily (around 7am ET), so `actual` can trail the
    real-world print by up to a day; a null `actual` before the print is
    expected, not missing data.
    """

    country: str
    """ISO 3166-1 alpha-2 country code, or `EU`."""

    name: str
    """Event name as reported by the provider."""

    timestamp: datetime
    """UTC instant of the event."""

    actual: Optional[str] = None
    """Actual reported value.

    Null before the print, or if the provider never reports one for this event. When
    a null/undefined value is observed, it indicates that there is no available
    data.
    """

    change: Optional[str] = None
    """
    Change from the previous value. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    change_percentage: Optional[str] = None
    """
    Change from the previous value, as a percentage. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    currency: Optional[str] = None
    """
    Currency associated with the event, if applicable. When a null/undefined value
    is observed, it indicates that there is no available data.
    """

    estimate: Optional[str] = None
    """
    Analyst-estimated value. When a null/undefined value is observed, it indicates
    that there is no available data.
    """

    impact: Optional[EconomicEventImpact] = None
    """
    Expected market impact, if known. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    previous: Optional[str] = None
    """
    Previous period's reported value. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    unit: Optional[EconomicEventUnit] = None
    """
    Unit of the numeric value fields, if known. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

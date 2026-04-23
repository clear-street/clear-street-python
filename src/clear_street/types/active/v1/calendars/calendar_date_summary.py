# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ....._models import BaseModel

__all__ = ["CalendarDateSummary"]


class CalendarDateSummary(BaseModel):
    """Summary of events for a specific date"""

    date: datetime.date
    """The date of the events"""

    dividends_count: int
    """The number of dividend events on this date"""

    earnings_count: int
    """The number of earnings announcements on this date"""

    economic_events_count: int
    """The number of economic events on this date"""

    mergers_acquisitions_count: int
    """The number of mergers and acquisitions on this date"""

    stock_splits_count: int
    """The number of stock split events on this date"""

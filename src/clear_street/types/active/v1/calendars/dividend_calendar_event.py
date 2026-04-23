# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .dividend_frequency import DividendFrequency

__all__ = ["DividendCalendarEvent"]


class DividendCalendarEvent(BaseModel):
    """Represents a single dividend event"""

    adjusted_dividend: str
    """The dividend amount adjusted for any stock splits"""

    date: datetime.date
    """The ex-dividend date"""

    dividend: str
    """The dividend amount per share"""

    symbol: str
    """The symbol for the instrument"""

    declaration_date: Optional[datetime.date] = None
    """The date the dividend was declared"""

    frequency: Optional[DividendFrequency] = None
    """The frequency of the dividend payment"""

    payment_date: Optional[datetime.date] = None
    """The payment date for the dividend"""

    record_date: Optional[datetime.date] = None
    """The record date for the dividend"""

    yield_: Optional[str] = FieldInfo(alias="yield", default=None)
    """The dividend yield as a percentage decimal"""

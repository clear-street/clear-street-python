# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["InstrumentIpoEvent"]


class InstrumentIpoEvent(BaseModel):
    """Represents an IPO event for an instrument"""

    date: datetime.date
    """The date of the IPO"""

    actions: Optional[str] = None
    """
    IPO action. When a null/undefined value is observed, it indicates that there is
    no available data.
    """

    announced_at: Optional[datetime.datetime] = None
    """
    IPO announced timestamp. When a null/undefined value is observed, it indicates
    that there is no available data.
    """

    company: Optional[str] = None
    """
    IPO company name. When a null/undefined value is observed, it indicates that
    there is no available data.
    """

    exchange: Optional[str] = None
    """
    IPO exchange. When a null/undefined value is observed, it indicates that there
    is no available data.
    """

    market_cap: Optional[str] = None
    """
    IPO market cap. When a null/undefined value is observed, it indicates that there
    is no available data.
    """

    price_range: Optional[str] = None
    """
    IPO price range. When a null/undefined value is observed, it indicates that
    there is no available data.
    """

    shares: Optional[str] = None
    """
    IPO shares offered. When a null/undefined value is observed, it indicates that
    there is no available data.
    """

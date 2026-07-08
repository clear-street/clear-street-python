# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["InstrumentEventIpoItem"]


class InstrumentEventIpoItem(BaseModel):
    """IPO event in the all-events date grouping response."""

    actions: Optional[str] = None
    """
    IPO action. When a null/undefined value is observed, it indicates that there is
    no available data.
    """

    announced_at: Optional[datetime] = None
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

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
    """Deprecated: use `offering_amount`, which carries the same value.

    This is not a market capitalization. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    offering_amount: Optional[str] = None
    """
    IPO maximum aggregate offering value: all offered shares, including
    over-allotment (greenshoe) shares, at the top of the price range. This is an
    upper bound. It assumes full exercise of the over-allotment option and pricing
    at the top of the range. When a null/undefined value is observed, it indicates
    that there is no available data.
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

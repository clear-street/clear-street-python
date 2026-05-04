# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["InstrumentFundamentals"]


class InstrumentFundamentals(BaseModel):
    """Supplemental fundamentals and company profile data for an instrument."""

    average_volume: Optional[int] = None
    """The average daily trading volume over the past 30 days"""

    beta: Optional[str] = None
    """
    The beta value, measuring the instrument's volatility relative to the overall
    market
    """

    description: Optional[str] = None
    """A detailed description of the instrument or company"""

    dividend_yield: Optional[str] = None
    """The trailing twelve months (TTM) dividend yield"""

    earnings_per_share: Optional[str] = None
    """The trailing twelve months (TTM) earnings per share"""

    fifty_two_week_high: Optional[str] = None
    """The highest price over the last 52 weeks"""

    fifty_two_week_low: Optional[str] = None
    """The lowest price over the last 52 weeks"""

    industry: Optional[str] = None
    """The specific industry of the instrument's issuer"""

    list_date: Optional[date] = None
    """The date the instrument was first listed"""

    logo_url: Optional[str] = None
    """URL to a representative logo image for the instrument or issuer"""

    market_cap: Optional[str] = None
    """The total market capitalization"""

    previous_close: Optional[str] = None
    """The closing price from the previous trading day"""

    price_to_earnings: Optional[str] = None
    """The price-to-earnings (P/E) ratio for the trailing twelve months (TTM)"""

    sector: Optional[str] = None
    """The business sector of the instrument's issuer"""

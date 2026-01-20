# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["ScreenerItem"]


class ScreenerItem(BaseModel):
    """An instrument returned by the screener"""

    price: str
    """The latest price for the instrument"""

    security_id: str
    """The identifier for the instrument"""

    security_id_source: str
    """The source of the security identifier"""

    symbol: str
    """The trading symbol for the instrument"""

    volume: str
    """The latest trading volume for the instrument"""

    country_of_issue: Optional[str] = None
    """The ISO country code of the instrument's issue"""

    description: Optional[str] = None
    """A detailed description of the instrument or company"""

    industry: Optional[str] = None
    """The specific industry of the instrument's issuer"""

    list_date: Optional[date] = None
    """The date the instrument was first listed"""

    market_cap: Optional[str] = None
    """The total market capitalization"""

    month_avg_volume: Optional[str] = None
    """The average trading volume over the past month"""

    name: Optional[str] = None
    """The full name of the instrument or its issuer"""

    percent_change: Optional[str] = None
    """The percent change from previous close to current price"""

    sector: Optional[str] = None
    """The business sector of the instrument's issuer"""

    security_type: Optional[str] = None
    """The type of security"""

    ttm_debt_to_equity: Optional[str] = None
    """The TTM debt-to-equity ratio"""

    ttm_dividend_yield: Optional[str] = None
    """The TTM dividend yield percent"""

    ttm_earnings_per_share: Optional[str] = None
    """The TTM earnings per share"""

    ttm_price_to_earnings: Optional[str] = None
    """The TTM price-to-earnings ratio"""

    venue: Optional[str] = None
    """The MIC code of the primary listing venue"""

    week_avg_volume: Optional[str] = None
    """The average trading volume over the past week"""

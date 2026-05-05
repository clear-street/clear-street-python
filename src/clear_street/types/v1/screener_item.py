# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel
from .analyst_rating import AnalystRating

__all__ = ["ScreenerItem"]


class ScreenerItem(BaseModel):
    """An instrument returned by the screener"""

    instrument_id: str
    """The OEMS instrument ID (`instrument.instruments.id`).

    Always present regardless of `field_filter`.
    """

    price: str
    """The latest price for the instrument"""

    symbol: str
    """The trading symbol for the instrument"""

    total_ratings: int
    """The total count of analyst ratings"""

    consensus_price_target: Optional[str] = None
    """The consensus analyst price target"""

    consensus_rating: Optional[AnalystRating] = None
    """The consensus analyst rating"""

    country_of_issue: Optional[str] = None
    """The ISO country code of the instrument's issue"""

    debt_to_equity_ttm: Optional[str] = None
    """The TTM debt-to-equity ratio"""

    description: Optional[str] = None
    """A detailed description of the instrument or company"""

    dividend_yield_ttm: Optional[str] = None
    """The TTM dividend yield percent"""

    earnings_per_share_ttm: Optional[str] = None
    """The TTM earnings per share"""

    exchange: Optional[str] = None
    """The MIC code of the primary listing exchange"""

    fifty_two_week_high: Optional[str] = None
    """The highest price over the last 52 weeks"""

    fifty_two_week_low: Optional[str] = None
    """The lowest price over the last 52 weeks"""

    gap_from_52w_high_pct: Optional[str] = None
    """Percent gap from 52-week high to previous day close (negative = below high)"""

    gap_from_52w_low_pct: Optional[str] = None
    """Percent gap from 52-week low to previous day close (positive = above low)"""

    industry: Optional[str] = None
    """The specific industry of the instrument's issuer"""

    instrument_type: Optional[str] = None
    """The type of instrument"""

    list_date: Optional[date] = None
    """The date the instrument was first listed"""

    market_cap: Optional[str] = None
    """The total market capitalization"""

    month_avg_volume: Optional[str] = None
    """The average trading volume over the past month"""

    name: Optional[str] = None
    """The full name of the instrument or its issuer"""

    one_month_ago_close: Optional[str] = None
    """The closing price approximately one month ago"""

    one_month_ago_open: Optional[str] = None
    """The opening price approximately one month ago"""

    one_month_change_pct: Optional[str] = None
    """Percent change from one month ago close to previous day close"""

    one_week_ago_close: Optional[str] = None
    """The closing price approximately one week ago"""

    one_week_ago_open: Optional[str] = None
    """The opening price approximately one week ago"""

    one_week_change_pct: Optional[str] = None
    """Percent change from one week ago close to previous day close"""

    one_year_ago_close: Optional[str] = None
    """The closing price approximately one year ago"""

    one_year_ago_open: Optional[str] = None
    """The opening price approximately one year ago"""

    one_year_change_pct: Optional[str] = None
    """Percent change from one year ago close to previous day close"""

    percent_change: Optional[str] = None
    """The percent change from previous close to current price"""

    prev_day_close: Optional[str] = None
    """The previous day's closing price"""

    price_to_earnings_ttm: Optional[str] = None
    """The TTM price-to-earnings ratio"""

    sector: Optional[str] = None
    """The business sector of the instrument's issuer"""

    six_month_change_pct: Optional[str] = None
    """Percent change from six months ago close to previous day close"""

    six_months_ago_close: Optional[str] = None
    """The closing price approximately six months ago"""

    six_months_ago_open: Optional[str] = None
    """The opening price approximately six months ago"""

    three_month_change_pct: Optional[str] = None
    """Percent change from three months ago close to previous day close"""

    three_months_ago_close: Optional[str] = None
    """The closing price approximately three months ago"""

    three_months_ago_open: Optional[str] = None
    """The opening price approximately three months ago"""

    volume: Optional[str] = None
    """The latest trading volume for the instrument"""

    week_avg_volume: Optional[str] = None
    """The average trading volume over the past week"""

    year_to_date_open: Optional[str] = None
    """The opening price on the first trading day of the current year"""

    ytd_change_pct: Optional[str] = None
    """Percent change from year-to-date open to previous day close"""

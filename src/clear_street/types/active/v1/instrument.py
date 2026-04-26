# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .instrument_core import InstrumentCore
from .instrument_quote import InstrumentQuote

__all__ = ["Instrument"]


class Instrument(InstrumentCore):
    """Represents a tradable financial instrument, including supplemental information"""

    available_to_borrow: Optional[int] = None
    """The number of shares currently available to borrow"""

    average_volume: Optional[int] = None
    """The average daily trading volume over the past 30 days"""

    beta: Optional[str] = None
    """
    The beta value, measuring the instrument's volatility relative to the overall
    market
    """

    borrow_fee: Optional[str] = None
    """The fee associated with borrowing the instrument, expressed as a decimal"""

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

    long_concentration_limit: Optional[str] = None
    """
    A cap on how much of your equity you can put into a single symbol on the long
    side
    """

    market_cap: Optional[str] = None
    """The total market capitalization"""

    options_expiry_dates: Optional[List[date]] = None
    """
    Available options expiration dates for this instrument. Present only when
    `include_options_expiry_dates=true` in the request.
    """

    previous_close: Optional[str] = None  # type: ignore
    """The closing price from the previous trading day"""

    price_to_earnings: Optional[str] = None
    """The price-to-earnings (P/E) ratio for the trailing twelve months (TTM)"""

    quote: Optional[InstrumentQuote] = None
    """Real-time market quote data for the instrument"""

    sector: Optional[str] = None
    """The business sector of the instrument's issuer"""

    short_concentration_limit: Optional[str] = None
    """
    A cap on how much of your equity you can allocate to a single symbol on the
    short side
    """

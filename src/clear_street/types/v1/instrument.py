# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel
from ..security_type import SecurityType

__all__ = ["Instrument"]


class Instrument(BaseModel):
    """Represents a tradable financial instrument."""

    id: str
    """Unique OEMS instrument identifier (UUID)"""

    country_of_issue: str
    """The ISO country code of the instrument's issue"""

    currency: str
    """The ISO currency code in which the instrument is traded"""

    easy_to_borrow: bool
    """Indicates if the instrument is classified as Easy-To-Borrow"""

    is_fractionable: bool
    """Indicates if the instrument supports fractional-quantity orders"""

    is_liquidation_only: bool
    """Indicates if the instrument is liquidation only and cannot be bought"""

    is_marginable: bool
    """Indicates if the instrument is marginable"""

    is_restricted: bool
    """Indicates if the instrument is restricted from trading"""

    is_short_prohibited: bool
    """Indicates if short selling is prohibited for the instrument"""

    is_threshold_security: bool
    """Indicates if the instrument is on the Regulation SHO Threshold Security List"""

    is_tradable: bool
    """Indicates if the instrument is tradable"""

    symbol: str
    """The trading symbol for the instrument"""

    venue: str
    """The MIC code of the primary listing venue"""

    adv: Optional[str] = None
    """Average daily share volume from the security definition."""

    expiry: Optional[date] = None
    """The expiration date for options instruments"""

    instrument_type: Optional[SecurityType] = None
    """The type of security (e.g., Common Stock, ETF)"""

    long_margin_rate: Optional[str] = None
    """The percent of a long position's value you must post as margin"""

    name: Optional[str] = None
    """The full name of the instrument or its issuer"""

    notional_adv: Optional[str] = None
    """Notional ADV (`adv × previous_close`).

    The primary liquidity signal used by `/instruments/search` ranking. Computed at
    response time so it stays consistent with whatever `adv` and `previous_close`
    show.
    """

    options_expiry_dates: Optional[List[date]] = None
    """
    Available options expiration dates for this instrument. Present only when
    `include_options_expiry_dates=true` in the request.
    """

    previous_close: Optional[str] = None
    """Last close price from the security definition."""

    short_margin_rate: Optional[str] = None
    """The percent of a short position's value you must post as margin"""

    strike_price: Optional[str] = None
    """The strike price for options instruments"""

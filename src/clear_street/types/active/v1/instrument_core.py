# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ...._models import BaseModel
from ..security_type import SecurityType
from ..security_id_source import SecurityIDSource
from .instrument_security_id import InstrumentSecurityID

__all__ = ["InstrumentCore"]


class InstrumentCore(BaseModel):
    id: str
    """Unique instrument identifier"""

    country_of_issue: str
    """The ISO country code of the instrument's issue"""

    currency: str
    """The ISO currency code in which the instrument is traded"""

    easy_to_borrow: bool
    """Indicates if the instrument is classified as Easy-To-Borrow"""

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

    security_id: str
    """Deprecated. Use `security_ids`.

    A primary security identifier for this instrument.
    """

    security_id_source: SecurityIDSource
    """Deprecated. Use `security_ids`.

    The source for `security_id`.
    """

    security_ids: List[InstrumentSecurityID]
    """All known security identifiers for this instrument"""

    symbol: str
    """The trading symbol for the instrument"""

    venue: str
    """The MIC code of the primary listing venue"""

    expiry: Optional[date] = None
    """The expiration date for options instruments"""

    long_margin_rate: Optional[str] = None
    """The percent of a long position's value you must post as margin"""

    name: Optional[str] = None
    """The full name of the instrument or its issuer"""

    security_type: Optional[SecurityType] = None
    """The type of security (e.g., Common Stock, ETF)"""

    short_margin_rate: Optional[str] = None
    """The percent of a short position's value you must post as margin"""

    strike_price: Optional[str] = None
    """The strike price for options instruments"""

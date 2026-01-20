# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..security_type import SecurityType
from ..security_id_source import SecurityIDSource

__all__ = ["InstrumentCore"]


class InstrumentCore(BaseModel):
    """
    Represents a tradable financial instrument, as a more concise item listing
    only key fields.
    """

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
    """A unique Clear Street identifier for the instrument"""

    security_id_source: SecurityIDSource
    """The source system for the security identifier"""

    symbol: str
    """The trading symbol for the instrument"""

    venue: str
    """The MIC code of the primary listing venue"""

    name: Optional[str] = None
    """The full name of the instrument or its issuer"""

    security_type: Optional[SecurityType] = None
    """The type of security (e.g., Common Stock, ETF)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ...._models import BaseModel
from .listing_type import ListingType
from .contract_type import ContractType
from .exercise_style import ExerciseStyle
from .instrument_security_id import InstrumentSecurityID

__all__ = ["OptionsContract"]


class OptionsContract(BaseModel):
    """An options contract with options-specific metadata"""

    id: str
    """OEMS instrument identifier"""

    contract_type: ContractType
    """Whether this is a CALL or PUT"""

    currency: str
    """ISO currency code"""

    exchange: str
    """MIC code of the primary listing venue"""

    exercise_style: ExerciseStyle
    """Exercise style"""

    expiry: date
    """Expiration date"""

    is_liquidation_only: bool
    """Whether the contract is liquidation-only"""

    is_marginable: bool
    """Whether the contract is marginable"""

    is_restricted: bool
    """Whether the contract is restricted from trading"""

    listing_type: ListingType
    """Listing type"""

    multiplier: str
    """Contract multiplier (100 for standard options)"""

    security_ids: List[InstrumentSecurityID]
    """All known security identifiers for this contract"""

    strike_price: str
    """Strike price"""

    symbol: str
    """OSI symbol (e.g. "AAPL 251219C00150000")"""

    underlier_instrument_id: Optional[str] = None
    """OEMS instrument ID of the underlying instrument, if resolvable"""

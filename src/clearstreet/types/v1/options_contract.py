# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel
from .listing_type import ListingType
from .contract_type import ContractType
from .exercise_style import ExerciseStyle

__all__ = ["OptionsContract"]


class OptionsContract(BaseModel):
    """An options contract with options-specific metadata"""

    id: str
    """Instrument identifier"""

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

    is_tradable: bool
    """Whether the contract is tradable"""

    listing_type: ListingType
    """Listing type"""

    multiplier: str
    """Contract multiplier (100 for standard options)"""

    strike_price: str
    """Strike price"""

    symbol: str
    """OSI symbol (e.g. "AAPL 251219C00150000")"""

    open_interest: Optional[int] = None
    """
    Open interest (number of outstanding contracts), if available When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    underlying_instrument_id: Optional[str] = None
    """
    Instrument ID of the underlying instrument, when available When a null/undefined
    value is observed, it indicates that there is no available data.
    """

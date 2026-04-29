# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ....._models import BaseModel
from .position_type import PositionType
from ...security_type import SecurityType
from ...security_id_source import SecurityIDSource

__all__ = ["Position"]


class Position(BaseModel):
    """Represents a holding of a particular instrument in an account"""

    account_id: int
    """The account this position belongs to"""

    available_quantity: str
    """The quantity of a position that is free to be operated on."""

    instrument_type: SecurityType
    """Type of security"""

    market_value: str
    """The current market value of the position"""

    position_type: PositionType
    """The type of position"""

    quantity: str
    """The number of shares or contracts. Can be positive (long) or negative (short)"""

    security_id: str
    """
    An identifier for the instrument which, when paired with `security_id_source`,
    identifies one or more financial instruments.
    """

    security_id_source: SecurityIDSource
    """The source of the security identifier"""

    symbol: str
    """The trading symbol for the instrument"""

    avg_price: Optional[str] = None
    """The average price paid per share or contract for this position"""

    closing_price: Optional[str] = None
    """The closing price used to value the position for the last trading day"""

    closing_price_date: Optional[date] = None
    """The market date associated with `closing_price`"""

    cost_basis: Optional[str] = None
    """The total cost basis for this position"""

    daily_unrealized_pnl: Optional[str] = None
    """The unrealized profit or loss for this position relative to the previous close"""

    daily_unrealized_pnl_pct: Optional[str] = None
    """
    The unrealized profit/loss for the position for the current day, expressed as a
    percentage of the baseline value (range: 0-100).
    """

    market_price: Optional[str] = None
    """The current market price of the instrument"""

    underlier_instrument_id: Optional[str] = None
    """OEMS instrument identifier of the underlying instrument, if resolvable"""

    unrealized_pnl: Optional[str] = None
    """
    The total unrealized profit or loss for this position based on current market
    value
    """

    unrealized_pnl_pct: Optional[str] = None
    """
    The unrealized profit/loss for the position, expressed as a percentage of the
    position's cost basis (range: 0-100).
    """

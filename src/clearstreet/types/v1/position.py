# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel
from .position_type import PositionType
from ..security_type import SecurityType

__all__ = ["Position"]


class Position(BaseModel):
    """Represents a holding of a particular instrument in an account"""

    account_id: int
    """The account this position belongs to"""

    available_quantity: str
    """The quantity of a position that is free to be operated on."""

    instrument_id: str
    """Unique instrument identifier"""

    instrument_type: SecurityType
    """Type of security"""

    market_value: str
    """The current market value of the position"""

    position_type: PositionType
    """The type of position"""

    quantity: str
    """The number of shares or contracts. Can be positive (long) or negative (short)"""

    symbol: str
    """The trading symbol for the instrument"""

    avg_price: Optional[str] = None
    """
    The average price paid per share or contract for this position When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    closing_price: Optional[str] = None
    """
    The closing price used to value the position for the last trading day When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    closing_price_date: Optional[date] = None
    """
    The market date associated with `closing_price` When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    cost_basis: Optional[str] = None
    """
    The total cost basis for this position When a null/undefined value is observed,
    it indicates that there is no available data.
    """

    daily_realized_pnl: Optional[str] = None
    """
    The realized profit or loss for this position for the current day When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    daily_unrealized_pnl: Optional[str] = None
    """
    The unrealized profit or loss for this position relative to the previous close
    When a null/undefined value is observed, it indicates that there is no available
    data.
    """

    daily_unrealized_pnl_pct: Optional[str] = None
    """
    The unrealized profit/loss for the position for the current day, expressed as a
    percentage of the baseline value (range: 0-100). When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    instrument_price: Optional[str] = None
    """
    The current market price of the instrument When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    underlying_instrument_id: Optional[str] = None
    """
    Identifier of the underlying instrument, when available When a null/undefined
    value is observed, it indicates it does not apply.
    """

    unrealized_pnl: Optional[str] = None
    """
    The total unrealized profit or loss for this position based on current market
    value When a null/undefined value is observed, it indicates that there is no
    available data.
    """

    unrealized_pnl_pct: Optional[str] = None
    """
    The unrealized profit/loss for the position, expressed as a percentage of the
    position's cost basis (range: 0-100). When a null/undefined value is observed,
    it indicates that there is no available data.
    """

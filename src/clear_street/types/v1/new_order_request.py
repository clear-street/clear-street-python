# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .side import Side
from ..._models import BaseModel
from ..security_type import SecurityType
from .position_effect import PositionEffect
from .request_order_type import RequestOrderType
from .trailing_offset_type import TrailingOffsetType
from .request_time_in_force import RequestTimeInForce
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["NewOrderRequest"]


class NewOrderRequest(BaseModel):
    """Request to submit a new order (PlaceOrderRequest from spec)"""

    instrument_type: SecurityType
    """Type of security"""

    order_type: RequestOrderType
    """Type of order"""

    quantity: str
    """Quantity to trade.

    For COMMON_STOCK: shares (may be fractional if supported). For OPTION
    (single-leg): contracts (must be an integer)
    """

    side: Side
    """Side of the order"""

    time_in_force: RequestTimeInForce
    """Time in force"""

    id: Optional[str] = None
    """Optional client-provided unique ID (idempotency).

    Required to be unique per account.
    """

    expires_at: Optional[datetime] = None
    """The timestamp when the order should expire (UTC).

    Required when time_in_force is GOOD_TILL_DATE.
    """

    extended_hours: Optional[bool] = None
    """Allow trading outside regular trading hours.

    Some brokers disallow options outside RTH.
    """

    instrument_id: Optional[InstrumentIDOrSymbol] = None
    """OEMS instrument UUID"""

    limit_offset: Optional[str] = None
    """Limit offset for trailing stop-limit orders (signed)"""

    limit_price: Optional[str] = None
    """Limit price (required for LIMIT and STOP_LIMIT orders)"""

    position_effect: Optional[PositionEffect] = None
    """Required when instrument_type is OPTION.

    Specifies whether the order opens or closes a position.
    """

    stop_price: Optional[str] = None
    """Stop price (required for STOP and STOP_LIMIT orders)"""

    symbol: Optional[str] = None
    """Trading symbol.

    For equities, use the ticker symbol (e.g., "AAPL"). For options, use the OSI
    symbol (e.g., "AAPL 250117C00190000"). Either `symbol` or `instrument_id` must
    be provided.
    """

    trailing_offset: Optional[str] = None
    """Trailing offset amount (required for trailing orders)"""

    trailing_offset_type: Optional[TrailingOffsetType] = None
    """Trailing offset type (PRICE or PERCENT_BPS)"""

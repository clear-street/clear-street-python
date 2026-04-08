# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .accounts.side import Side
from ..security_type import SecurityType
from .accounts.order_type import OrderType
from .order_strategy_type import OrderStrategyType
from .accounts.time_in_force import TimeInForce

__all__ = ["OrderPayload"]


class OrderPayload(BaseModel):
    """Order payload for prefilling an order ticket.

    This schema aligns with the NewOrderRequest schema used for order submission,
    containing the fields needed to prefill an order ticket or submit via API.
    """

    order_type: OrderType
    """Order type"""

    quantity: str
    """Quantity (shares for stocks, contracts for options)"""

    security_type: SecurityType
    """Type of security"""

    side: Side
    """Order side"""

    symbol: str
    """Trading symbol (e.g., "AAPL" for equities, OSI for options)"""

    time_in_force: TimeInForce
    """Time in force"""

    limit_price: Optional[str] = None
    """Limit price (required for LIMIT and STOP_LIMIT orders)"""

    stop_price: Optional[str] = None
    """Stop price (required for STOP and STOP_LIMIT orders)"""

    strategy: Optional[OrderStrategyType] = None
    """Execution strategy (simplified enum, not the full strategy params for now)"""

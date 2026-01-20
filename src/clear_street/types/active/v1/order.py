# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .accounts.side import Side
from ..security_type import SecurityType
from ..security_id_source import SecurityIDSource
from .accounts.order_type import OrderType
from .accounts.order_status import OrderStatus
from .accounts.time_in_force import TimeInForce
from .accounts.order_strategy import OrderStrategy

__all__ = ["Order"]


class Order(BaseModel):
    """A trading order with its current state and execution details.

    This is the unified API representation of an order across its lifecycle,
    combining data from execution reports, order status queries, and parent/child tracking.
    """

    account_id: int
    """Account placing the order"""

    created_at: datetime
    """Timestamp when order was created (UTC)"""

    filled_quantity: str
    """Cumulative filled quantity"""

    leaves_quantity: str
    """Remaining unfilled quantity"""

    order_id: str
    """Client-provided unique identifier for this order"""

    order_type: OrderType
    """Type of order (MARKET, LIMIT, etc.)"""

    quantity: str
    """Total order quantity"""

    security_id: str
    """
    The identifier for the traded instrument (CMS/CUSIP/ISIN/FIGI for equities or
    option OPRA OSI)
    """

    security_id_source: SecurityIDSource
    """The source of the security identifier"""

    security_type: SecurityType
    """Type of security"""

    side: Side
    """Side of the order (BUY, SELL, SELL_SHORT)"""

    status: OrderStatus
    """Current status of the order"""

    symbol: str
    """Trading symbol"""

    time_in_force: TimeInForce
    """Time in force instruction"""

    updated_at: datetime
    """Timestamp of the most recent update (UTC)"""

    venue: str
    """MIC code of the venue where the order is routed"""

    average_fill_price: Optional[str] = None
    """Average fill price across all executions"""

    details: Optional[List[str]] = None
    """Contains execution, rejection or cancellation details, if any"""

    expires_at: Optional[datetime] = None
    """Timestamp when the order will expire (UTC).

    Present when time_in_force is GOOD_TILL_DATE.
    """

    limit_price: Optional[str] = None
    """Limit price (for LIMIT and STOP_LIMIT orders)"""

    stop_price: Optional[str] = None
    """Stop price (for STOP and STOP_LIMIT orders)"""

    strategy: Optional[OrderStrategy] = None
    """Execution strategy for this order"""

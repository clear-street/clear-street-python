# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .side import Side
from ..._models import BaseModel
from .order_type import OrderType
from .queue_state import QueueState
from .order_status import OrderStatus
from .time_in_force import TimeInForce
from ..security_type import SecurityType
from .trailing_offset_type import TrailingOffsetType

__all__ = ["Order"]


class Order(BaseModel):
    """A trading order with its current state and execution details.

    This is the unified API representation of an order across its lifecycle,
    combining data from execution reports, order status queries, and parent/child tracking.
    """

    id: str
    """Engine-assigned unique identifier for this order (UUID)."""

    account_id: int
    """Account placing the order"""

    client_order_id: str
    """Client-provided identifier echoed back."""

    created_at: datetime
    """Timestamp when order was created (UTC)"""

    filled_quantity: str
    """Cumulative filled quantity"""

    instrument_id: str
    """Instrument identifier for the traded instrument."""

    instrument_type: SecurityType
    """Type of security"""

    leaves_quantity: str
    """Remaining unfilled quantity"""

    order_type: OrderType
    """Type of order (MARKET, LIMIT, etc.)"""

    quantity: str
    """Total order quantity"""

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
    """
    Average fill price across all executions When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    details: Optional[List[str]] = None
    """Contains execution, rejection or cancellation details, if any"""

    expires_at: Optional[datetime] = None
    """Timestamp when the order will expire (UTC).

    Present when time_in_force is GOOD_TILL_DATE. When a null/undefined value is
    observed, it indicates it does not apply.
    """

    extended_hours: Optional[bool] = None
    """Whether the order is eligible for extended-hours trading."""

    limit_offset: Optional[str] = None
    """
    Limit offset for trailing stop-limit orders (signed) When a null/undefined value
    is observed, it indicates it does not apply.
    """

    limit_price: Optional[str] = None
    """
    Limit price (for LIMIT and STOP_LIMIT orders) When a null/undefined value is
    observed, it indicates it does not apply.
    """

    queue_state: Optional[QueueState] = None
    """
    Parent order queue state, present when the order is awaiting release or
    released. When a null/undefined value is observed, it indicates it does not
    apply.
    """

    releases_at: Optional[datetime] = None
    """
    Scheduled release time for orders awaiting release. When a null/undefined value
    is observed, it indicates it does not apply.
    """

    stop_price: Optional[str] = None
    """
    Stop price (for STOP and STOP_LIMIT orders) When a null/undefined value is
    observed, it indicates it does not apply.
    """

    trailing_limit_px: Optional[str] = None
    """
    Current trailing limit price computed by the trailing strategy When a
    null/undefined value is observed, it indicates it does not apply.
    """

    trailing_offset: Optional[str] = None
    """
    Trailing offset amount for trailing orders When a null/undefined value is
    observed, it indicates it does not apply.
    """

    trailing_offset_type: Optional[TrailingOffsetType] = None
    """
    Trailing offset type for trailing orders When a null/undefined value is
    observed, it indicates it does not apply.
    """

    trailing_stop_px: Optional[str] = None
    """
    Current trailing stop price computed by the trailing strategy When a
    null/undefined value is observed, it indicates it does not apply.
    """

    trailing_watermark_px: Optional[str] = None
    """
    Trailing watermark price for trailing orders When a null/undefined value is
    observed, it indicates it does not apply.
    """

    trailing_watermark_ts: Optional[datetime] = None
    """
    Trailing watermark timestamp for trailing orders When a null/undefined value is
    observed, it indicates it does not apply.
    """

    underlying_instrument_id: Optional[str] = None
    """Instrument ID of the option's underlying instrument.

    Populated only for options orders. A `null` means one of two things: the order
    is not an option, so the field does not apply; or the order is an option whose
    underlier has not yet been resolved. When a null/undefined value is observed, it
    indicates it does not apply.
    """

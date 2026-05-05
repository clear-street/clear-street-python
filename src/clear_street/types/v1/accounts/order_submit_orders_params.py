# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .side import Side
from ...._utils import PropertyInfo
from .order_type import OrderType
from .time_in_force import TimeInForce
from ...security_type import SecurityType
from .order_strategy_param import OrderStrategyParam
from .trailing_offset_type import TrailingOffsetType

__all__ = [
    "OrderSubmitOrdersParams",
    "Order",
    "OrderNewOrderMultilegRequest",
    "OrderNewOrderMultilegRequestLeg",
    "OrderNewOrderRequest",
]


class OrderSubmitOrdersParams(TypedDict, total=False):
    orders: Required[Iterable[Order]]


class OrderNewOrderMultilegRequestLeg(TypedDict, total=False):
    """A single leg in a multileg strategy request."""

    instrument_type: Required[SecurityType]
    """Security type for the leg."""

    ratio: Required[str]
    """Ratio for the leg."""

    security: Required[str]
    """Trading symbol (e.g. "AAPL" or OSI symbol for options)"""

    side: Required[Side]
    """Leg side."""

    id: Optional[str]
    """Optional leg reference identifier."""

    position_effect: Optional[Literal["OPEN", "CLOSE"]]
    """Optional leg position effect."""


class OrderNewOrderMultilegRequest(TypedDict, total=False):
    """Multileg strategy order request"""

    legs: Required[Iterable[OrderNewOrderMultilegRequestLeg]]
    """Legs that compose the strategy."""

    order_type: Required[OrderType]
    """Type of order (currently MARKET or LIMIT for multileg strategy submission)"""

    time_in_force: Required[TimeInForce]
    """Time in force"""

    id: Optional[str]
    """Optional client-provided unique ID (idempotency).

    Required to be unique per account.
    """

    limit_price: Optional[str]
    """Strategy price, required for LIMIT orders."""

    quantity: str
    """Optional strategy-level quantity. Multiplies leg quantities. Defaults to 1."""


class OrderNewOrderRequest(TypedDict, total=False):
    """Single-leg order request"""

    instrument_type: Required[SecurityType]
    """Type of security"""

    order_type: Required[OrderType]
    """Type of order"""

    quantity: Required[str]
    """Quantity to trade.

    For COMMON_STOCK: shares (may be fractional if supported). For OPTION
    (single-leg): contracts (must be an integer)
    """

    side: Required[Side]
    """Side of the order"""

    time_in_force: Required[TimeInForce]
    """Time in force"""

    id: Optional[str]
    """Optional client-provided unique ID (idempotency).

    Required to be unique per account.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the order should expire (UTC).

    Required when time_in_force is GOOD_TILL_DATE.
    """

    extended_hours: Optional[bool]
    """Allow trading outside regular trading hours.

    Some brokers disallow options outside RTH.
    """

    instrument_id: Optional[str]
    """OEMS instrument UUID"""

    limit_offset: Optional[str]
    """Limit offset for trailing stop-limit orders (signed)"""

    limit_price: Optional[str]
    """Limit price (required for LIMIT and STOP_LIMIT orders)"""

    position_effect: Literal["OPEN", "CLOSE"]
    """Required when instrument_type is OPTION.

    Specifies whether the order opens or closes a position.
    """

    stop_price: Optional[str]
    """Stop price (required for STOP and STOP_LIMIT orders)"""

    strategy: Optional[OrderStrategyParam]
    """Execution strategy/router. Defaults to SOR where applicable."""

    symbol: Optional[str]
    """Trading symbol.

    For equities, use the ticker symbol (e.g., "AAPL"). For options, use the OSI
    symbol (e.g., "AAPL 250117C00190000"). Either `symbol` or `instrument_id` must
    be provided.
    """

    trailing_offset_amt: Optional[str]
    """Trailing offset amount (required for trailing orders)"""

    trailing_offset_amt_type: Optional[TrailingOffsetType]
    """Trailing offset type (PRICE or PERCENT_BPS)"""


Order: TypeAlias = Union[OrderNewOrderMultilegRequest, OrderNewOrderRequest]

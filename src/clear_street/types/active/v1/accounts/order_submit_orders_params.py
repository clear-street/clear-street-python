# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .side import Side
from ....._utils import PropertyInfo
from .order_type import OrderType
from .time_in_force import TimeInForce
from ...security_type import SecurityType
from ...security_id_source import SecurityIDSource
from .order_strategy_param import OrderStrategyParam

__all__ = ["OrderSubmitOrdersParams", "Body"]


class OrderSubmitOrdersParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    """Request to submit a new order (PlaceOrderRequest from spec)"""

    order_id: Required[str]
    """Client-provided unique ID (idempotency). Required to be unique per account."""

    order_type: Required[OrderType]
    """Type of order"""

    quantity: Required[str]
    """Quantity to trade.

    For COMMON_STOCK: shares (may be fractional if supported). For OPTION
    (single-leg): contracts (must be an integer)
    """

    security_type: Required[SecurityType]
    """Type of security"""

    side: Required[Side]
    """Side of the order"""

    time_in_force: Required[TimeInForce]
    """Time in force"""

    expire_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the order should expire (UTC).

    Required when time_in_force is GOOD_TILL_DATE.
    """

    extended_hours: Optional[bool]
    """Allow trading outside regular trading hours.

    Some brokers disallow options outside RTH.
    """

    limit_price: Optional[str]
    """Limit price (required for LIMIT and STOP_LIMIT orders)"""

    position_effect: Literal["OPEN", "CLOSE"]
    """Required when security_type is OPTION.

    Specifies whether the order opens or closes a position.
    """

    security_id: Optional[str]
    """
    Unique identifier for the instrument (CMS/CUSIP/ISIN/FIGI for equities or option
    OPRA OSI). Required if symbol is not provided.
    """

    security_id_source: Optional[SecurityIDSource]
    """The source of the security identifier. Required if security_id is provided."""

    stop_price: Optional[str]
    """Stop price (required for STOP and STOP_LIMIT orders)"""

    strategy: Optional[OrderStrategyParam]
    """Execution strategy/router. Defaults to SOR where applicable."""

    symbol: Optional[str]
    """Trading symbol.

    For equities, use the ticker symbol (e.g., "AAPL"). For options, use the OSI
    symbol (e.g., "AAPL 250117C00190000"). If provided without security_id, the
    system will derive security_id and source based on security_type (CMS for
    equities, OPRA for options).
    """

    venue: str
    """Execution venue to route the order to.

    If not specified, the system will choose the best venue.
    """

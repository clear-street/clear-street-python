# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .side import Side
from .request_order_type import RequestOrderType
from .request_time_in_force import RequestTimeInForce
from .new_order_request_param import NewOrderRequestParam
from .request_position_effect import RequestPositionEffect

__all__ = ["OrderSubmitOrdersParams", "Order", "OrderNewOrderMultilegRequest", "OrderNewOrderMultilegRequestLeg"]


class OrderSubmitOrdersParams(TypedDict, total=False):
    orders: Required[Iterable[Order]]


class OrderNewOrderMultilegRequestLeg(TypedDict, total=False):
    """A single leg in a multileg strategy request."""

    ratio: Required[str]
    """Ratio for the leg."""

    side: Required[Side]
    """Leg side (BUY or SELL)."""

    id: Optional[str]
    """Optional leg reference identifier."""

    instrument_id: Optional[str]
    """Trading symbol (e.g. "AAPL" or OSI symbol for options)"""

    position_intent: Optional[RequestPositionEffect]
    """Required. Open/close intent for this leg."""


class OrderNewOrderMultilegRequest(TypedDict, total=False):
    """Request to submit a new multileg order strategy."""

    legs: Required[Iterable[OrderNewOrderMultilegRequestLeg]]
    """Legs that compose the strategy."""

    order_type: Required[RequestOrderType]
    """Type of order (currently MARKET or LIMIT for multileg strategy submission)"""

    time_in_force: Required[RequestTimeInForce]
    """Time in force"""

    id: Optional[str]
    """Optional client-provided unique ID (idempotency).

    Required to be unique per account.
    """

    limit_price: Optional[str]
    """Strategy price, required for LIMIT orders."""

    quantity: str
    """Optional strategy-level quantity. Multiplies leg quantities. Defaults to 1."""


Order: TypeAlias = Union[OrderNewOrderMultilegRequest, NewOrderRequestParam]

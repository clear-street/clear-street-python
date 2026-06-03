# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .side import Side
from .position_effect import PositionEffect
from .request_order_type import RequestOrderType
from .request_time_in_force import RequestTimeInForce
from .new_order_request_param import NewOrderRequestParam

__all__ = ["OrderSubmitOrdersParams", "Order", "OrderNewOrderMultilegRequest", "OrderNewOrderMultilegRequestLeg"]


class OrderSubmitOrdersParams(TypedDict, total=False):
    orders: Required[Iterable[Order]]


class OrderNewOrderMultilegRequestLeg(TypedDict, total=False):
    """A single leg in a multileg strategy request."""

    ratio: Required[str]
    """Ratio for the leg."""

    security: Required[str]
    """Trading symbol (e.g. "AAPL" or OSI symbol for options)"""

    side: Required[Side]
    """Leg side."""

    id: Optional[str]
    """Optional leg reference identifier."""

    position_effect: Optional[PositionEffect]
    """Optional leg position effect."""


class OrderNewOrderMultilegRequest(TypedDict, total=False):
    """Multileg strategy order request"""

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

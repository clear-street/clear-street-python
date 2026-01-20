# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .side import Side
from .order_type import OrderType
from ...security_type import SecurityType
from ...security_id_source import SecurityIDSource

__all__ = ["OrderCancelAllOrdersParams"]


class OrderCancelAllOrdersParams(TypedDict, total=False):
    security_id: str
    """Filter by security identifier (e.g., CUSIP, ISIN).

    Must be provided with security_id_source.
    """

    security_id_source: SecurityIDSource
    """Type of security identifier. Must be provided with security_id."""

    security_type: SecurityType
    """Filter by security type (e.g., COMMON_STOCK, OPTION)"""

    side: Side
    """Filter by order side (BUY or SELL)"""

    type: OrderType
    """Filter by order type (e.g., MARKET, LIMIT)"""

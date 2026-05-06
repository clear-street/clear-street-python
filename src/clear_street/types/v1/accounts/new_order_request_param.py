# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .side import Side
from ...._utils import PropertyInfo
from ...security_type import SecurityType
from .position_effect import PositionEffect
from .request_order_type import RequestOrderType
from .trailing_offset_type import TrailingOffsetType
from .request_time_in_force import RequestTimeInForce
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["NewOrderRequestParam"]


class NewOrderRequestParam(TypedDict, total=False):
    """Request to submit a new order (PlaceOrderRequest from spec)"""

    instrument_type: Required[SecurityType]
    """Type of security"""

    order_type: Required[RequestOrderType]
    """Type of order"""

    quantity: Required[str]
    """Quantity to trade.

    For COMMON_STOCK: shares (may be fractional if supported). For OPTION
    (single-leg): contracts (must be an integer)
    """

    side: Required[Side]
    """Side of the order"""

    time_in_force: Required[RequestTimeInForce]
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

    instrument_id: Optional[InstrumentIDOrSymbol]
    """OEMS instrument UUID"""

    limit_offset: Optional[str]
    """Limit offset for trailing stop-limit orders (signed)"""

    limit_price: Optional[str]
    """Limit price (required for LIMIT and STOP_LIMIT orders)"""

    position_effect: PositionEffect
    """Required when instrument_type is OPTION.

    Specifies whether the order opens or closes a position.
    """

    stop_price: Optional[str]
    """Stop price (required for STOP and STOP_LIMIT orders)"""

    symbol: Optional[str]
    """Trading symbol.

    For equities, use the ticker symbol (e.g., "AAPL"). For options, use the OSI
    symbol (e.g., "AAPL 250117C00190000"). Either `symbol` or `instrument_id` must
    be provided.
    """

    trailing_offset: Optional[str]
    """Trailing offset amount (required for trailing orders)"""

    trailing_offset_type: Optional[TrailingOffsetType]
    """Trailing offset type (PRICE or PERCENT_BPS)"""

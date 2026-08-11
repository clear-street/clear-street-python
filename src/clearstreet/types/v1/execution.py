# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .side import Side
from ..._models import BaseModel

__all__ = ["Execution"]


class Execution(BaseModel):
    """Represents a single fill of an order for an account."""

    id: str
    """Unique identifier for this execution report."""

    order_id: str
    """Identifier of the order this execution belongs to."""

    quantity: str
    """Filled quantity."""

    side: Side
    """Side of the fill."""

    transaction_time: datetime
    """Transaction timestamp in nanosecond precision (UTC)."""

    instrument_id: Optional[str] = None
    """Unique instrument identifier.

    `null` when this fill has no single resolvable instrument. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    price: Optional[str] = None
    """Fill price.

    `null` for multileg fills, whose price lives only at the leg level. When a
    null/undefined value is observed, it indicates it does not apply.
    """

    symbol: Optional[str] = None
    """Trading symbol.

    `null` when this fill has no single resolvable instrument. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    underlying_instrument_id: Optional[str] = None
    """Underlying instrument identifier for a derivative fill.

    `null` for a non-derivative fill, when the underlier could not be resolved, or
    when a multileg fill's legs resolve to different underliers. When a
    null/undefined value is observed, it indicates it does not apply.
    """

    venue: Optional[str] = None
    """Venue where this fill occurred, as reported by that venue.

    Distinct from an order's `venue`, which is the routing destination. Codes are
    not normalized, so the format varies by venue. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

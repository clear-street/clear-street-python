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

    price: str
    """Fill price."""

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

    symbol: Optional[str] = None
    """Trading symbol.

    `null` when this fill has no single resolvable instrument. When a null/undefined
    value is observed, it indicates it does not apply.
    """

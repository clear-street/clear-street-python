# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .side import Side
from ..._models import BaseModel

__all__ = ["Execution"]


class Execution(BaseModel):
    """Represents a single fill of an order for an account."""

    id: str
    """Unique identifier for this execution report."""

    instrument_id: str
    """Unique instrument identifier."""

    order_id: str
    """Identifier of the order this execution belongs to."""

    price: str
    """Fill price."""

    quantity: str
    """Filled quantity."""

    side: Side
    """Side of the fill."""

    symbol: str
    """Trading symbol."""

    transaction_time: datetime
    """Transaction timestamp in nanosecond precision (UTC)."""

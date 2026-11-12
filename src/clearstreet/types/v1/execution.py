# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .side import Side
from ..._models import BaseModel
from .execution_leg import ExecutionLeg
from ..security_type import SecurityType

__all__ = ["Execution"]


class Execution(BaseModel):
    """Represents a single fill of an order for an account."""

    id: str
    """Unique identifier for this execution report."""

    order_id: str
    """Identifier of the order this execution belongs to."""

    quantity: str
    """Filled quantity.

    For a strategy-level multileg fill this is the net strategy quantity, not a
    per-leg quantity.
    """

    side: Side
    """Side of the fill."""

    transaction_time: datetime
    """Transaction timestamp in nanosecond precision (UTC)."""

    instrument_id: Optional[str] = None
    """Unique instrument identifier.

    `null` when this is a strategy-level multileg fill whose legs are reported
    individually in `legs[]`. When a null/undefined value is observed, it indicates
    it does not apply.
    """

    legs: Optional[List[ExecutionLeg]] = None
    """
    > **Alpha** — this field is experimental and may change or be removed at any
    > time.

    Individual legs of a strategy-level multileg fill. Omitted for single-security
    and individual-leg fills.
    """

    price: Optional[str] = None
    """Fill price.

    `null` for multileg fills, whose price lives only at the leg level. When a
    null/undefined value is observed, it indicates it does not apply.
    """

    symbol: Optional[str] = None
    """Trading symbol.

    `null` when this is a strategy-level multileg fill whose legs are reported
    individually in `legs[]`. When a null/undefined value is observed, it indicates
    it does not apply.
    """

    underlying_instrument_id: Optional[str] = None
    """Underlying instrument identifier for an option fill.

    Omitted for a non-derivative fill, when the underlier could not be resolved, or
    for a multileg fill (per-leg underliers live in `legs[]`). When a null/undefined
    value is observed, it indicates it does not apply.
    """

    underlying_instrument_type: Optional[SecurityType] = None
    """
    Type of the underlying instrument, alongside `underlying_instrument_id`. When a
    null/undefined value is observed, it indicates it does not apply.
    """

    venue: Optional[str] = None
    """Venue where this fill occurred, as reported by that venue.

    Distinct from an order's `venue`, which is the routing destination. Codes are
    not normalized, so the format varies by venue. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .side import Side
from ..._models import BaseModel
from ..security_type import SecurityType

__all__ = ["ExecutionLeg"]


class ExecutionLeg(BaseModel):
    """One leg of a strategy-level multileg execution."""

    price: str
    """Fill price for this leg."""

    ratio: str
    """This leg's ratio quantity within the strategy."""

    side: Side
    """Side of this leg's fill."""

    symbol: str
    """Trading symbol for this leg."""

    instrument_id: Optional[str] = None
    """Instrument identifier for this leg.

    `null` when the leg's instrument could not be resolved from its reported symbol.
    When a null/undefined value is observed, it indicates it does not apply.
    """

    instrument_type: Optional[SecurityType] = None
    """Type of security for this leg.

    `null` when the leg's instrument could not be resolved from its reported symbol.
    When a null/undefined value is observed, it indicates it does not apply.
    """

    underlying_instrument_id: Optional[str] = None
    """Underlying instrument identifier for this leg.

    `null` when the leg is not an option, or its underlier could not be resolved.
    When a null/undefined value is observed, it indicates it does not apply.
    """

    underlying_instrument_type: Optional[SecurityType] = None
    """
    Type of this leg's underlying instrument, alongside `underlying_instrument_id`.
    When a null/undefined value is observed, it indicates it does not apply.
    """

    venue: Optional[str] = None
    """Venue where this leg's fill occurred, as reported by that venue.

    Lives per-leg rather than only at the top level (see [`Execution::venue`])
    because a strategy's legs can each fill on a different venue. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

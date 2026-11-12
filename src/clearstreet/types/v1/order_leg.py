# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .side import Side
from ..._models import BaseModel
from ..security_type import SecurityType
from .request_position_effect import RequestPositionEffect

__all__ = ["OrderLeg"]


class OrderLeg(BaseModel):
    """One leg of a multileg strategy order."""

    ratio: str
    """This leg's ratio quantity within the strategy."""

    side: Side
    """Side of this leg (BUY or SELL)."""

    average_fill_price: Optional[str] = None
    """
    Average fill price for this leg across its executions, as reported by the venue
    (FIX 6 on an individual-leg 442=2 execution report). `null` when the leg has no
    fills (no data), not `0`. When a null/undefined value is observed, it indicates
    that there is no available data.
    """

    instrument_id: Optional[str] = None
    """Instrument identifier for this leg.

    `null` when the leg's instrument could not be resolved. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    instrument_type: Optional[SecurityType] = None
    """Type of security for this leg.

    `null` when the leg's instrument could not be resolved. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    position_effect: Optional[RequestPositionEffect] = None
    """
    Client-attested open/close intent for this leg. When a null/undefined value is
    observed, it indicates it does not apply.
    """

    symbol: Optional[str] = None
    """Trading symbol for this leg.

    `null` when the leg's instrument could not be resolved. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    underlying_instrument_id: Optional[str] = None
    """Instrument ID of this leg's underlying instrument.

    Populated only for option legs. When a null/undefined value is observed, it
    indicates it does not apply.
    """

    underlying_instrument_type: Optional[SecurityType] = None
    """
    Type of this leg's underlying instrument, alongside `underlying_instrument_id`.
    When a null/undefined value is observed, it indicates it does not apply.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .side import Side
from ..._models import BaseModel
from .event_contract_side import EventContractSide

__all__ = ["EventContractExecution"]


class EventContractExecution(BaseModel):
    """
    Effective action inherited from the parent order, with a NO-relative fill price.
    This is the order's classification, not a per-fill open/close accounting attribution.
    """

    action: Side
    """BUY or SELL of `contract_side`, inherited from the parent classification."""

    contract_side: EventContractSide
    """Contract the parent order's effective action buys or sells."""

    no_price: Optional[str] = None
    """Contract payout minus the existing YES fill price.

    Omitted when payout data is unavailable. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

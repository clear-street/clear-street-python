# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .side import Side
from ..._models import BaseModel
from .event_contract_side import EventContractSide

__all__ = ["EventContractOrder"]


class EventContractOrder(BaseModel):
    """
    Effective action from the recorded order classification, with NO-relative prices.
    Existing top-level side and prices retain their YES-based meaning.
    """

    action: Side
    """BUY or SELL of `contract_side`, recorded when the order was classified."""

    contract_side: EventContractSide
    """Contract the effective action buys or sells."""

    no_average_fill_price: Optional[str] = None
    """Contract payout minus the existing YES average fill price.

    Omitted before any fill or when payout data is unavailable. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    no_limit_price: Optional[str] = None
    """Contract payout minus the existing YES limit price.

    Omitted for market orders or when payout data is unavailable. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

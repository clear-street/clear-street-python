# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel
from .locate_order_status import LocateOrderStatus

__all__ = ["LocateOrder"]


class LocateOrder(BaseModel):
    """Represents a single locate order and its status"""

    locate_order_id: str
    """The unique system-generated ID for the locate order"""

    located_quantity: int
    """The quantity of shares that have been located"""

    mpid: str
    """The client Market Participant Identifier, assigned by Clear Street"""

    requested_at: datetime
    """The timestamp when the locate order was received from the client in UTC"""

    requested_quantity: int
    """The quantity of shares requested by the client"""

    status: LocateOrderStatus
    """The status of the locate order"""

    symbol: str
    """The symbol of the security to locate"""

    borrow_rate: Optional[str] = None
    """The borrow rate for the security if held overnight, expressed as a decimal"""

    desk_comment: Optional[str] = None
    """Comments provided by the trading desk"""

    expires_at: Optional[datetime] = None
    """
    The timestamp when the locate order will expire, set once the order has been
    processed, in UTC
    """

    locate_id: Optional[str] = None
    """A unique ID for the locate order, available after the order has been `OFFERED`"""

    located_at: Optional[datetime] = None
    """The timestamp when the security was located in UTC"""

    reference_id: Optional[str] = None
    """The reference ID provided when submitting the locate order"""

    total_cost: Optional[str] = None
    """The total cost of the locate"""

    trader_comment: Optional[str] = None
    """Comments provided by the trader when submitting the locate order"""

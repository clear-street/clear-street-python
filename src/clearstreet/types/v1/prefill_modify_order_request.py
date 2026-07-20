# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PrefillModifyOrderRequest"]


class PrefillModifyOrderRequest(BaseModel):
    """Request to replace (modify) an existing order

    At least one field must be provided.
    """

    account_id: Optional[int] = None
    """Account ID that owns the order."""

    limit_price: Optional[str] = None
    """New limit price for the order"""

    order_id: Optional[str] = None
    """Order ID to modify."""

    quantity: Optional[str] = None
    """New quantity for the order"""

    stop_price: Optional[str] = None
    """New stop price for the order"""

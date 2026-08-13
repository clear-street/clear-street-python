# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .trailing_offset_type import TrailingOffsetType

__all__ = ["PrefillModifyOrderRequest"]


class PrefillModifyOrderRequest(BaseModel):
    """Request to replace (modify) an existing order

    At least one field must be provided.
    """

    account_id: Optional[int] = None
    """Account ID that owns the order."""

    limit_offset: Optional[str] = None
    """New limit offset for trailing stop-limit orders (signed)"""

    limit_price: Optional[str] = None
    """New limit price for the order"""

    order_id: Optional[str] = None
    """Order ID to modify."""

    quantity: Optional[str] = None
    """New quantity for the order"""

    stop_price: Optional[str] = None
    """New stop price for the order"""

    trailing_offset: Optional[str] = None
    """New trailing offset for trailing orders"""

    trailing_offset_type: Optional[TrailingOffsetType] = None
    """New trailing offset type (PRICE or BPS)"""

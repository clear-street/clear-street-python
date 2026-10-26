# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .order_preview_delta import OrderPreviewDelta

__all__ = ["OrderPreviewPosition"]


class OrderPreviewPosition(BaseModel):
    """One instrument's position before and after the previewed order.

    Only the
    traded instruments appear; cash effects are carried by the monetary fields.
    """

    instrument_id: str
    """The instrument's identifier."""

    quantity: OrderPreviewDelta
    """Net position quantity before and after the order."""

    symbol: str
    """The instrument's symbol."""

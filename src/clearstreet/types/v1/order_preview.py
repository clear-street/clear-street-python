# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .order_preview_delta import OrderPreviewDelta
from .order_preview_error import OrderPreviewError
from .order_preview_amount import OrderPreviewAmount
from .order_preview_position import OrderPreviewPosition
from .order_preview_margin_details import OrderPreviewMarginDetails

__all__ = ["OrderPreview"]


class OrderPreview(BaseModel):
    """The projected impact of an order, as if it were submitted and fully filled."""

    account_id: int
    """The account the order was previewed for."""

    amount: OrderPreviewAmount
    """Monetary size of the previewed order."""

    buying_power: OrderPreviewDelta
    """Buying power before and after the order."""

    currency: str
    """Currency for all monetary values."""

    equity: OrderPreviewDelta
    """Account equity before and after the order."""

    errors: List[OrderPreviewError]
    """Risk-check errors that would prevent the order from being accepted.

    Empty when the order would pass every pre-trade risk check.
    """

    margin_details: OrderPreviewMarginDetails
    """Margin requirements and excess before and after the order."""

    positions: List[OrderPreviewPosition]
    """Positions in the traded instruments before and after the order."""

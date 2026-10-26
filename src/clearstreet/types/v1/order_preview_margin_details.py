# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .order_preview_delta import OrderPreviewDelta

__all__ = ["OrderPreviewMarginDetails"]


class OrderPreviewMarginDetails(BaseModel):
    """Margin requirements and excess before and after the previewed order."""

    initial_margin_excess: OrderPreviewDelta
    """Initial margin excess."""

    initial_margin_requirement: OrderPreviewDelta
    """Initial margin requirement."""

    maintenance_margin_excess: OrderPreviewDelta
    """Maintenance margin excess."""

    maintenance_margin_requirement: OrderPreviewDelta
    """Maintenance margin requirement."""

    overnight_margin_excess: OrderPreviewDelta
    """Overnight margin excess."""

    overnight_margin_requirement: OrderPreviewDelta
    """Overnight margin requirement."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["OrderPreviewAmount"]


class OrderPreviewAmount(BaseModel):
    """Monetary size of the previewed order."""

    gross_amount: str
    """Total cash impact of the order before estimated fees and commissions."""

    net_amount: str
    """Total cash impact of the order after estimated fees and commissions."""

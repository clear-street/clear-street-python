# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CancelOrderRequest"]


class CancelOrderRequest(BaseModel):
    """Request to cancel an existing order

    Note: In the API, order cancellation is done via DELETE request without a body.
    The order_id and account_id come from the URL path parameters.
    """

    account_id: int
    """Account ID (from path parameter)"""

    order_id: str
    """Order ID to cancel (from path parameter)"""

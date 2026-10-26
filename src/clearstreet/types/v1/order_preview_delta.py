# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["OrderPreviewDelta"]


class OrderPreviewDelta(BaseModel):
    """Before/after values for one metric, as if the previewed order fully filled."""

    after: str
    """The value with the previewed order also fully filled."""

    before: str
    """
    The value before the order, as the risk engine evaluates it: the account's open
    orders are projected as filled.
    """

    change: str
    """The previewed order's isolated impact: `after - before`."""

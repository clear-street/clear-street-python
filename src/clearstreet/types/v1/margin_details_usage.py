# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MarginDetailsUsage"]


class MarginDetailsUsage(BaseModel):
    total: str
    """The total margin available in the current model."""

    used: str
    """The amount of margin that is currently being utilized."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ChartPoint"]


class ChartPoint(BaseModel):
    """Single chart coordinate."""

    x: str

    y: float

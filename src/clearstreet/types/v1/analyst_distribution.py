# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AnalystDistribution"]


class AnalystDistribution(BaseModel):
    """Analyst recommendation distribution"""

    buy: int
    """Number of buy recommendations"""

    hold: int
    """Number of hold recommendations"""

    sell: int
    """Number of sell recommendations"""

    strong_buy: int
    """Number of strong buy recommendations"""

    strong_sell: int
    """Number of strong sell recommendations"""

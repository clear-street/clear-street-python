# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .chart_point import ChartPoint

__all__ = ["ChartSeries"]


class ChartSeries(BaseModel):
    """Named data series within a chart."""

    name: str

    points: Optional[List[ChartPoint]] = None

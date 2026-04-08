# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .chart_point import ChartPoint

__all__ = ["ChartSeries"]


class ChartSeries(BaseModel):
    name: str

    points: List[ChartPoint]

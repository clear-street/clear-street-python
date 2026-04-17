# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .chart_series import ChartSeries

__all__ = ["DataChart"]


class DataChart(BaseModel):
    series: List[ChartSeries]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .chart_series import ChartSeries

__all__ = ["DataChart"]


class DataChart(BaseModel):
    """Chart represented by explicit data series."""

    series: Optional[List[ChartSeries]] = None

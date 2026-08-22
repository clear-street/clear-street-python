# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .metric_key import MetricKey
from .metric_unit import MetricUnit
from .metric_frequency import MetricFrequency
from .company_metric_point import CompanyMetricPoint

__all__ = ["CompanyMetricSeries"]


class CompanyMetricSeries(BaseModel):
    """A historical or estimated company metric series."""

    frequency: MetricFrequency
    """Observation cadence."""

    label: str
    """Display label."""

    metric_key: MetricKey
    """Canonical metric key."""

    source: str
    """Publisher/provider name."""

    unit: MetricUnit
    """Value unit."""

    external_id: Optional[str] = None
    """Optional source identifier retained for reconciliation."""

    points: Optional[List[CompanyMetricPoint]] = None
    """Ordered observations."""

    source_url: Optional[str] = None
    """Source URL, when available."""

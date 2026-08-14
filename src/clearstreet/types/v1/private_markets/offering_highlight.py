# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .metric_unit import MetricUnit
from .metric_value_type import MetricValueType

__all__ = ["OfferingHighlight"]


class OfferingHighlight(BaseModel):
    """A curated highlight, resolved against the company profile's metric series."""

    label: str
    """Display label (the highlight's override, else the series' own label)."""

    metric_key: str
    """Canonical metric key selected by the highlight (e.g. `REVENUE_GROWTH`)."""

    unit: MetricUnit
    """Value unit."""

    observed_at: Optional[datetime] = None
    """Observation time of the latest value."""

    value: Optional[str] = None
    """Latest observed value, when the series carries any points."""

    value_type: Optional[MetricValueType] = None
    """Whether the latest value is historical or estimated."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel
from .metric_value_type import MetricValueType

__all__ = ["CompanyMetricPoint"]


class CompanyMetricPoint(BaseModel):
    """One metric observation."""

    observed_at: datetime
    """Observation time."""

    value: str
    """Exact decimal value, serialized as a string."""

    value_type: MetricValueType
    """Historical or estimated classification."""

    citation_ids: Optional[List[str]] = None
    """Profile-local citation ids supporting this point."""

    source_event_id: Optional[str] = None
    """Optional source event identifier."""

    source_metadata: Optional[Dict[str, str]] = None
    """Optional provider reconciliation metadata."""

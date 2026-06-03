# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .chart_payload import ChartPayload

__all__ = ["ContentPartChartPayload"]


class ContentPartChartPayload(BaseModel):
    """Chart payload content part."""

    payload: ChartPayload
    """Typed chart payload rendered inline in assistant content."""

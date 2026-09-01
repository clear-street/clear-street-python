# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .feed_metric_type import FeedMetricType

__all__ = ["FeedItemMetric"]


class FeedItemMetric(BaseModel):
    """A feed item's headline number."""

    type: FeedMetricType
    """What the number measures."""

    value: str
    """The number itself, as a decimal string."""

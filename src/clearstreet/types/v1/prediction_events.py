# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .prediction_event import PredictionEvent

__all__ = ["PredictionEvents"]


class PredictionEvents(BaseModel):
    """Prediction market events with at least one market that can currently be listed."""

    events: List[PredictionEvent]
    """Events in the requested order."""

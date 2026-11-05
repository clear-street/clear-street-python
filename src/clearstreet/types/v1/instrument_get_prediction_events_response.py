# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .prediction_events import PredictionEvents
from ..shared.base_response import BaseResponse

__all__ = ["InstrumentGetPredictionEventsResponse"]


class InstrumentGetPredictionEventsResponse(BaseResponse):
    data: PredictionEvents
    """Prediction market events with at least one market that can currently be listed."""

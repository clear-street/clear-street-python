# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .prediction_series_list import PredictionSeriesList

__all__ = ["InstrumentGetPredictionSeriesResponse"]


class InstrumentGetPredictionSeriesResponse(BaseResponse):
    data: PredictionSeriesList
    """Prediction market series with at least one market that can currently be listed."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .prediction_markets import PredictionMarkets
from ..shared.base_response import BaseResponse

__all__ = ["InstrumentGetPredictionMarketsResponse"]


class InstrumentGetPredictionMarketsResponse(BaseResponse):
    data: PredictionMarkets
    """Prediction markets matching the request."""

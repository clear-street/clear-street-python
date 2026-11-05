# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .prediction_market import PredictionMarket

__all__ = ["PredictionMarkets"]


class PredictionMarkets(BaseModel):
    """Prediction markets matching the request."""

    markets: List[PredictionMarket]
    """Markets ordered by symbol."""

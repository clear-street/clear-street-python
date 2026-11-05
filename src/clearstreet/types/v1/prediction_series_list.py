# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .prediction_series import PredictionSeries

__all__ = ["PredictionSeriesList"]


class PredictionSeriesList(BaseModel):
    """Prediction market series with at least one market that can currently be listed."""

    series: List[PredictionSeries]
    """Series ordered by code."""

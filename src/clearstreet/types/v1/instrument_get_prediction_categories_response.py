# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .prediction_categories import PredictionCategories

__all__ = ["InstrumentGetPredictionCategoriesResponse"]


class InstrumentGetPredictionCategoriesResponse(BaseResponse):
    data: PredictionCategories
    """Categories of the prediction market contracts that can currently be listed."""

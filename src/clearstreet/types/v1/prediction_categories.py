# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["PredictionCategories"]


class PredictionCategories(BaseModel):
    """Categories of the prediction market contracts that can currently be listed."""

    categories: List[str]
    """Distinct categories, sorted alphabetically."""

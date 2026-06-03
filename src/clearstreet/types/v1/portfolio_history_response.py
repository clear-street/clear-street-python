# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .portfolio_history_segment import PortfolioHistorySegment

__all__ = ["PortfolioHistoryResponse"]


class PortfolioHistoryResponse(BaseModel):
    segments: List[PortfolioHistorySegment]

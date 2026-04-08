# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .portfolio_history_response import PortfolioHistoryResponse

__all__ = ["PortfolioHistoryGetPortfolioHistoryResponse"]


class PortfolioHistoryGetPortfolioHistoryResponse(BaseResponse):
    data: PortfolioHistoryResponse

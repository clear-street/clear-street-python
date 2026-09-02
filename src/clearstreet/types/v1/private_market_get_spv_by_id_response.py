# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .private_markets.spv_detail import SpvDetail

__all__ = ["PrivateMarketGetSpvByIDResponse"]


class PrivateMarketGetSpvByIDResponse(BaseResponse):
    data: SpvDetail
    """An OPEN SPV's identity, exact economics, and typed fee schedule."""

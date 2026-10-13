# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .spv_detail import SpvDetail
from ..shared.base_response import BaseResponse

__all__ = ["PrivateMarketGetSpvByIDResponse"]


class PrivateMarketGetSpvByIDResponse(BaseResponse):
    data: SpvDetail
    """An OPEN SPV's identity, exact economics, and typed fee schedule."""

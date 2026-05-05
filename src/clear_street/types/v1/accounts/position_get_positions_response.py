# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .position_list import PositionList
from ...shared.base_response import BaseResponse

__all__ = ["PositionGetPositionsResponse"]


class PositionGetPositionsResponse(BaseResponse):
    data: PositionList

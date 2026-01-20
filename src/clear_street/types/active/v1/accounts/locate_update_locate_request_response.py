# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .locate_order import LocateOrder
from ....shared.base_response import BaseResponse

__all__ = ["LocateUpdateLocateRequestResponse"]


class LocateUpdateLocateRequestResponse(BaseResponse):
    data: LocateOrder
    """Represents a single locate order and its status"""

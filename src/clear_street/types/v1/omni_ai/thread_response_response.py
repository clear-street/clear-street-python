# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..response import Response
from ...shared.base_response import BaseResponse

__all__ = ["ThreadResponseResponse"]


class ThreadResponseResponse(BaseResponse):
    data: Response
    """Dynamic pollable response."""

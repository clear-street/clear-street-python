# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .response import Response
from ...shared.base_response import BaseResponse

__all__ = ["ThreadGetThreadResponseResponse"]


class ThreadGetThreadResponseResponse(BaseResponse):
    data: Optional[Response] = None
    """Dynamic pollable response."""

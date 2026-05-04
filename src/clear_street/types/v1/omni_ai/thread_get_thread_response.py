# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..thread import Thread
from ...shared.base_response import BaseResponse

__all__ = ["ThreadGetThreadResponse"]


class ThreadGetThreadResponse(BaseResponse):
    data: Thread
    """Thread metadata returned by list/get thread endpoints."""

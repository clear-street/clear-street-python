# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .create_thread_response import CreateThreadResponse

__all__ = ["ThreadCreateThreadResponse"]


class ThreadCreateThreadResponse(BaseResponse):
    data: CreateThreadResponse
    """Response payload for thread creation."""

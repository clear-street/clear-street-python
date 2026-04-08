# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..get_thread_response import GetThreadResponse
from ....shared.base_response import BaseResponse

__all__ = ["ThreadGetThreadDeprecatedResponse"]


class ThreadGetThreadDeprecatedResponse(BaseResponse):
    data: GetThreadResponse

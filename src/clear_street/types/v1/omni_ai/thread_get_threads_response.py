# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..thread_list import ThreadList
from ...shared.base_response import BaseResponse

__all__ = ["ThreadGetThreadsResponse"]


class ThreadGetThreadsResponse(BaseResponse):
    data: ThreadList

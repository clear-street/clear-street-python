# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..list_threads_response import ListThreadsResponse
from ....shared.base_response import BaseResponse

__all__ = ["ThreadListThreadsResponse"]


class ThreadListThreadsResponse(BaseResponse):
    data: ListThreadsResponse

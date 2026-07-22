# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .message_list import MessageList
from ...shared.base_response import BaseResponse

__all__ = ["ThreadGetMessagesResponse"]


class ThreadGetMessagesResponse(BaseResponse):
    data: MessageList

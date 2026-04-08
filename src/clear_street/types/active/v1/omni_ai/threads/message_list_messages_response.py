# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .....shared.base_response import BaseResponse
from ...list_messages_response import ListMessagesResponse

__all__ = ["MessageListMessagesResponse"]


class MessageListMessagesResponse(BaseResponse):
    data: ListMessagesResponse

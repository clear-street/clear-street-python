# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from ...create_message_response import CreateMessageResponse

__all__ = ["MessageCreateMessageResponse"]


class MessageCreateMessageResponse(BaseResponse):
    data: CreateMessageResponse
    """Response payload for continuing a thread with a new message."""

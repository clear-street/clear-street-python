# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .message import Message
from ...shared.base_response import BaseResponse

__all__ = ["MessageGetMessageByIDResponse"]


class MessageGetMessageByIDResponse(BaseResponse):
    data: Message
    """Final immutable message."""

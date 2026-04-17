# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .error_status import ErrorStatus
from .response_status import ResponseStatus
from .response_content import ResponseContent

__all__ = ["Response"]


class Response(BaseModel):
    """Dynamic pollable response."""

    id: str

    status: ResponseStatus
    """Dynamic lifecycle status for a pollable response."""

    thread_id: str

    user_message_id: str

    content: Optional[ResponseContent] = None
    """Dynamic response content container. May include thinking parts."""

    error: Optional[ErrorStatus] = None
    """Shared sanitized error payload."""

    output_message_id: Optional[str] = None

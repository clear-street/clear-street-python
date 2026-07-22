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
    """
    When a null/undefined value is observed, it indicates that there is no available
    data.
    """

    error: Optional[ErrorStatus] = None
    """When a null/undefined value is observed, it indicates it does not apply."""

    output_message_id: Optional[str] = None
    """When a null/undefined value is observed, it indicates it does not apply."""

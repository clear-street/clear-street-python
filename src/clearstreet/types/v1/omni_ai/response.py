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
    """Dynamic lifecycle status for a pollable response.

    `succeeded`, `failed`, `canceled`, `steered` and `merged` are terminal.
    `steered`: the response ended as written because the user sent a newer message,
    and a later response in the thread continues the work. `merged`: the response
    ended without text, and a later response answers its message. Treat an unknown
    status as terminal.
    """

    thread_id: str

    content: Optional[ResponseContent] = None
    """
    When a null/undefined value is observed, it indicates that there is no available
    data.
    """

    error: Optional[ErrorStatus] = None
    """When a null/undefined value is observed, it indicates it does not apply."""

    output_message_id: Optional[str] = None
    """When a null/undefined value is observed, it indicates it does not apply."""

    user_message_id: Optional[str] = None
    """The user message this response answers.

    Omitted when the response presents a background result, such as a subagent's
    report, and answers no user message; its output message then appears in the
    thread without a preceding request. When a null/undefined value is observed, it
    indicates it does not apply.
    """

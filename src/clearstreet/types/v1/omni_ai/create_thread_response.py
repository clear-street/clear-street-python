# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CreateThreadResponse"]


class CreateThreadResponse(BaseModel):
    """Response payload for thread creation."""

    response_id: str

    thread_id: str

    user_message_id: str

    user_message_seq: int
    """The `seq` the user message has in the thread's message list.

    Always present. Use it to place the sent prompt among the listed messages before
    a list refresh includes it.
    """

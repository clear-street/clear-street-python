# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CreateMessageResponse"]


class CreateMessageResponse(BaseModel):
    """Response payload for continuing a thread with a new message."""

    response_id: str

    thread_id: str

    user_message_id: str

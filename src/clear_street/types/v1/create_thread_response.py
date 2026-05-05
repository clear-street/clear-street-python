# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CreateThreadResponse"]


class CreateThreadResponse(BaseModel):
    """Response payload for thread creation."""

    response_id: str

    thread_id: str

    user_message_id: str

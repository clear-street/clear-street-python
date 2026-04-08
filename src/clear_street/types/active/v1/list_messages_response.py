# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .message import Message
from ...._models import BaseModel

__all__ = ["ListMessagesResponse"]


class ListMessagesResponse(BaseModel):
    messages: List[Message]

    next_page_token: Optional[str] = None

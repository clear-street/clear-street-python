# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .message_content_part import MessageContentPart

__all__ = ["MessageContent"]


class MessageContent(BaseModel):
    """Finalized immutable message content container. Never includes thinking parts."""

    parts: List[MessageContentPart]

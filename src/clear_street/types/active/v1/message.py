# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .message_role import MessageRole
from .message_content import MessageContent

__all__ = ["Message"]


class Message(BaseModel):
    content_text: str
    """Denormalized text content for search/display"""

    created_at: str

    role: MessageRole

    seq: int

    id: Optional[str] = None

    author_user_id: Optional[str] = None

    content: Optional[MessageContent] = None
    """Parsed content parts (text, thinking, and structured actions)"""

    metadata: Optional[object] = None

    run_id: Optional[str] = None

    thread_id: Optional[str] = None

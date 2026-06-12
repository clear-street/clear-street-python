# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .error_status import ErrorStatus
from .message_role import MessageRole
from .message_content import MessageContent
from .message_outcome import MessageOutcome

__all__ = ["Message"]


class Message(BaseModel):
    """Final immutable message."""

    id: str

    content: MessageContent
    """Finalized immutable message content container. Never includes thinking parts."""

    created_at: str

    outcome: MessageOutcome
    """Immutable terminal outcome for a finalized assistant message."""

    role: MessageRole
    """Finalized message role in the public contract."""

    seq: int

    thread_id: str

    error: Optional[ErrorStatus] = None
    """When a null/undefined value is observed, it indicates it does not apply."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .error_status import ErrorStatus
from .message_role import MessageRole
from .turn_context import TurnContext
from .message_content import MessageContent
from .message_outcome import MessageOutcome

__all__ = ["Message"]


class Message(BaseModel):
    """Final immutable message."""

    id: str

    content: MessageContent
    """Finalized immutable message content container. Never includes thinking parts."""

    created_at: datetime

    outcome: MessageOutcome
    """Immutable terminal outcome for a finalized assistant message.

    `steered`: the message is complete as written; the user sent a newer message
    before it finished. `merged`: the message has no content, and a later answer
    covers its turn. Hide `merged` messages.
    """

    role: MessageRole
    """Finalized message role in the public contract."""

    seq: int

    thread_id: str

    context: Optional[TurnContext] = None
    """Immutable snapshots attached to this user message.

    Omitted when none were supplied. When a null/undefined value is observed, it
    indicates that there is no available data.
    """

    error: Optional[ErrorStatus] = None
    """When a null/undefined value is observed, it indicates it does not apply."""

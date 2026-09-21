# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .context_item import ContextItem

__all__ = ["TurnContext"]


class TurnContext(BaseModel):
    """Client snapshots attached to one instant-chat user message.

    Context is separate from visible message text and does not grant account access.
    The compact JSON representation must not exceed 64 KiB.
    """

    items: List[ContextItem]
    """One to four snapshots.

    Each snapshot's data may contain at most 32 levels of nesting.
    """

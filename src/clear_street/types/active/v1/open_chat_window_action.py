# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["OpenChatWindowAction"]


class OpenChatWindowAction(BaseModel):
    """Action to open a chat window."""

    extras: Optional[object] = None
    """Additional configuration"""

    thread_id: Optional[str] = None
    """Thread ID to open (None to open a new chat window)"""

    title: Optional[str] = None
    """Window title"""

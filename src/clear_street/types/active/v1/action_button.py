# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .button_action import ButtonAction

__all__ = ["ActionButton"]


class ActionButton(BaseModel):
    button_id: str

    label: str

    action: Optional[ButtonAction] = None
    """Send a follow-up prompt as the next user message"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .prompt_button_action import PromptButtonAction
from .structured_action_button_action import StructuredActionButtonAction

__all__ = ["ActionButton"]


class ActionButton(BaseModel):
    """Button metadata shared by chart and suggested-actions payloads."""

    button_id: str = FieldInfo(alias="buttonId")
    """Stable button identifier within the content part."""

    label: str
    """User-visible label."""

    prompt: Optional[PromptButtonAction] = None
    """
    Follow-up prompt to submit as the next user message. When a null/undefined value
    is observed, it indicates it does not apply.
    """

    structured_action: Optional[StructuredActionButtonAction] = FieldInfo(alias="structuredAction", default=None)
    """
    Structured action in the same message to execute on click. When a null/undefined
    value is observed, it indicates it does not apply.
    """

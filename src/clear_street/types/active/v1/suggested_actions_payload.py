# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .action_button import ActionButton

__all__ = ["SuggestedActionsPayload"]


class SuggestedActionsPayload(BaseModel):
    """Suggested follow-up buttons rendered at the end of an assistant message."""

    action_buttons: Optional[List[ActionButton]] = FieldInfo(alias="actionButtons", default=None)
    """Ordered message-level buttons."""

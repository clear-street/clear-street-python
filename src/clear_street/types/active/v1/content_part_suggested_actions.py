# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .action_button import ActionButton

__all__ = ["ContentPartSuggestedActions"]


class ContentPartSuggestedActions(BaseModel):
    action_buttons: List[ActionButton]

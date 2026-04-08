# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .prompt_button_action import PromptButtonAction
from .structured_action_button_action import StructuredActionButtonAction

__all__ = ["ButtonAction", "Prompt", "StructuredAction"]


class Prompt(PromptButtonAction):
    """Send a follow-up prompt as the next user message"""

    action_type: Literal["prompt"]


class StructuredAction(StructuredActionButtonAction):
    """Trigger a structured action already present in the same message"""

    action_type: Literal["structured_action"]


ButtonAction: TypeAlias = Union[Prompt, StructuredAction]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["PromptButtonAction"]


class PromptButtonAction(BaseModel):
    """Prompt-style button behavior."""

    prompt: str
    """Prompt text to submit as the next user turn."""

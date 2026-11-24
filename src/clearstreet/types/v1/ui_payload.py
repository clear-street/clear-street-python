# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .ui_node import UiNode
from ..._models import BaseModel

__all__ = ["UiPayload"]


class UiPayload(BaseModel):
    """Model-composed UI, built only from Omni's built-in component catalog."""

    root: UiNode
    """Root of the component tree."""

    ui_id: str
    """Stable identifier of this UI within the message."""

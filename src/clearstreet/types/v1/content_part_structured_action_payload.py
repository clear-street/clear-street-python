# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .structured_action import StructuredAction

__all__ = ["ContentPartStructuredActionPayload"]


class ContentPartStructuredActionPayload(BaseModel):
    """Structured action content part."""

    action: StructuredAction
    """Structured actions that Omni AI can return to clients.

    These actions provide machine-readable instructions for the client to execute,
    such as prefilling an order ticket, opening a chart, or navigating to a route.
    """

    action_id: str

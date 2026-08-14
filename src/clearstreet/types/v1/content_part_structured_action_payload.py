# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

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

    clicked: bool
    """Whether the current user clicked this action."""

    clicked_item_ids: Optional[List[str]] = None
    """IDs of nested items clicked by the current user."""

    item_id: Optional[str] = None
    """Interaction-tracking identity.

    Absent on messages created before tracking. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .suggested_actions_payload import SuggestedActionsPayload

__all__ = ["ContentPartSuggestedActionsPayload"]


class ContentPartSuggestedActionsPayload(BaseModel):
    """Suggested actions payload content part."""

    payload: SuggestedActionsPayload
    """Suggested follow-up buttons rendered at the end of an assistant message."""

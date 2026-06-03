# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StructuredActionButtonAction"]


class StructuredActionButtonAction(BaseModel):
    """Structured-action button behavior."""

    action_id: Optional[str] = FieldInfo(alias="actionId", default=None)
    """UUID of a `structured_action` content part in the same message."""

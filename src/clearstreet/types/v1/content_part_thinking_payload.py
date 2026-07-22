# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ContentPartThinkingPayload"]


class ContentPartThinkingPayload(BaseModel):
    """Thinking content part shown on dynamic response polling."""

    thoughts: List[str]

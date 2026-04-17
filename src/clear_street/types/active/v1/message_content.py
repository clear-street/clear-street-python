# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .content_part import ContentPart

__all__ = ["MessageContent"]


class MessageContent(BaseModel):
    """Message content containing text and structured action parts."""

    parts: List[ContentPart]

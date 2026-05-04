# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .response_content_part import ResponseContentPart

__all__ = ["ResponseContent"]


class ResponseContent(BaseModel):
    """Dynamic response content container. May include thinking parts."""

    parts: List[ResponseContentPart]

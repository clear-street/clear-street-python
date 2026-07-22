# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .api_error import APIError
from .response_metadata import ResponseMetadata

__all__ = ["BaseResponse"]


class BaseResponse(BaseModel):
    metadata: ResponseMetadata
    """Response metadata, including the request ID and optional pagination info."""

    error: Optional[APIError] = None
    """Structured error details when the request is unsuccessful."""

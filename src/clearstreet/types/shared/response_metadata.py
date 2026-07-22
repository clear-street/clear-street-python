# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResponseMetadata"]


class ResponseMetadata(BaseModel):
    """Metadata for the response.

    This will always contain a request ID which can be used to identify
    the request to Clear Street for tracing, and optionally may include pagination data.
    """

    request_id: str
    """A unique ID for this request, generated upon ingestion of the request."""

    next_page_token: Optional[str] = None
    """Base64URL-encoded pagination token"""

    page_number: Optional[int] = None
    """Pagination. Included if this was a GET (list) response"""

    previous_page_token: Optional[str] = None
    """Base64URL-encoded pagination token"""

    total_items: Optional[int] = None
    """Total number of items available (not just in this page)."""

    total_pages: Optional[int] = None
    """Total number of pages available."""

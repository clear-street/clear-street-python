# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .offering_document_type import OfferingDocumentType

__all__ = ["OfferingDocumentResource"]


class OfferingDocumentResource(BaseModel):
    """A campaign document's display metadata.

    Exactly one of `url`/`object_key`
    is set; an object key is resolved and signed elsewhere.
    """

    id: str
    """Stable identifier."""

    display_order: int
    """Stable display position."""

    document_type: OfferingDocumentType
    """Document kind."""

    title: str
    """Display title."""

    object_key: Optional[str] = None
    """Object-store key, when the document is stored internally."""

    published_at: Optional[datetime] = None
    """Publication time, when known."""

    source: Optional[str] = None
    """Source publisher/provider."""

    source_url: Optional[str] = None
    """Source URL."""

    url: Optional[str] = None
    """Externally reachable URL, when the document lives at one."""

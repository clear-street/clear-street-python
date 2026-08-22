# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CompanyCitation"]


class CompanyCitation(BaseModel):
    """A cited source."""

    id: str
    """Stable profile-local citation identifier."""

    source: str
    """Source publisher or provider."""

    title: str
    """Human-readable source title."""

    url: str
    """Source URL."""

    published_at: Optional[datetime] = None
    """Source publication time, when known."""

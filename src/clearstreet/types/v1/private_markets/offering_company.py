# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["OfferingCompany"]


class OfferingCompany(BaseModel):
    """Company identity carried on an offering card/detail."""

    id: str
    """Stable company identifier."""

    name: str
    """Display name."""

    short_description: str
    """Short card/search description."""

    slug: str
    """Lowercase URL slug."""

    logo_url: Optional[str] = None
    """Company logo URL, when known."""

    primary_domain: Optional[str] = None
    """Canonical lowercase domain, when known."""

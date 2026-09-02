# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .company_profile_resource import CompanyProfileResource

__all__ = ["CompanyDetail"]


class CompanyDetail(BaseModel):
    """A company's identity and its complete published profile."""

    id: str
    """Stable company identifier."""

    name: str
    """Display name."""

    profile: CompanyProfileResource
    """The complete versioned company profile."""

    profile_schema_version: int
    """Profile schema version discriminator."""

    short_description: str
    """Short card/search description."""

    slug: str
    """Lowercase URL slug."""

    logo_url: Optional[str] = None
    """Company logo URL, when known."""

    primary_domain: Optional[str] = None
    """Canonical lowercase domain, when known."""

    published_at: Optional[datetime] = None
    """Publication time."""

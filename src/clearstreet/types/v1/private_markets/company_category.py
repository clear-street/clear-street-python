# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CompanyCategory"]


class CompanyCategory(BaseModel):
    """A company category."""

    name: str
    """Display name."""

    slug: str
    """Stable lowercase category slug."""

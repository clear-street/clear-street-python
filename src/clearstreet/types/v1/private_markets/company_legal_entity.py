# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CompanyLegalEntity"]


class CompanyLegalEntity(BaseModel):
    """A legal entity associated with the company."""

    country: str
    """Country name or ISO country code supplied by the source."""

    name: str
    """Legal name."""

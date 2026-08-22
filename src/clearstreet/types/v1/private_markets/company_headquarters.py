# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CompanyHeadquarters"]


class CompanyHeadquarters(BaseModel):
    """Company headquarters."""

    city: str
    """City."""

    country: str
    """Country."""

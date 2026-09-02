# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CompanyCustomer"]


class CompanyCustomer(BaseModel):
    """A named company customer."""

    name: str
    """Customer name."""

    logo_url: Optional[str] = None
    """Customer logo, when supplied."""

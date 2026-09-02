# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CompanyDocumentPreview"]


class CompanyDocumentPreview(BaseModel):
    """Optional document card preview."""

    description: Optional[str] = None
    """Preview description."""

    image_url: Optional[str] = None
    """Preview image URL."""

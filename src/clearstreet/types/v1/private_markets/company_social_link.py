# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .company_social_type import CompanySocialType

__all__ = ["CompanySocialLink"]


class CompanySocialLink(BaseModel):
    """A company social/profile link."""

    type: CompanySocialType
    """Link type."""

    url: str
    """Link URL."""

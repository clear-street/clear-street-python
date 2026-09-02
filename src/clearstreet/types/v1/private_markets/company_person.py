# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .company_person_role import CompanyPersonRole

__all__ = ["CompanyPerson"]


class CompanyPerson(BaseModel):
    """A key person associated with the company."""

    name: str
    """Display name."""

    external_id: Optional[str] = None
    """Optional source identifier retained for reconciliation."""

    roles: Optional[List[CompanyPersonRole]] = None
    """One or more curated company roles."""

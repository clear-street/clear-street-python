# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["CompanyNarrativeSection"]


class CompanyNarrativeSection(BaseModel):
    """One ordered durable narrative block."""

    body: str
    """Plain-text section body."""

    display_order: int
    """Stable display position within the profile."""

    title: str
    """Section heading."""

    citation_ids: Optional[List[str]] = None
    """Profile-local citation ids supporting this block."""

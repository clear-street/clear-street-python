# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["OfferingKeyRisk"]


class OfferingKeyRisk(BaseModel):
    """One ordered key-risk block."""

    body: str
    """Plain-text risk body."""

    title: str
    """Risk heading."""

    citation_ids: Optional[List[str]] = None
    """Profile-local citation ids supporting the risk."""

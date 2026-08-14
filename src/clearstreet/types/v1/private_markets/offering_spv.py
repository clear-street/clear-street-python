# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .spv_status import SpvStatus

__all__ = ["OfferingSpv"]


class OfferingSpv(BaseModel):
    """The attached SPV's identity and lifecycle.

    Exact economics surface once the
    SPV opens; an upcoming offering's indicative ranges describe the terms until
    then.
    """

    id: str
    """Stable SPV identifier."""

    name: str
    """Legal/display name."""

    status: SpvStatus
    """Lifecycle state."""

    custodian_name: Optional[str] = None
    """Custodian."""

    manager_name: Optional[str] = None
    """SPV manager."""

    share_class: Optional[str] = None
    """Underlying share class, when specified."""

    structure_description: Optional[str] = None
    """Plain-text vehicle structure."""

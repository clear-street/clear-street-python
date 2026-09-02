# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .participant_role import ParticipantRole

__all__ = ["OfferingParticipantResource"]


class OfferingParticipantResource(BaseModel):
    """An offering participant's display data."""

    id: str
    """Stable identifier."""

    display_order: int
    """Stable display position."""

    name: str
    """Display name."""

    role: ParticipantRole
    """Presentation role."""

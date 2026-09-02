# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .offering_card import OfferingCard
from .offering_key_risk import OfferingKeyRisk
from .offering_highlight import OfferingHighlight
from .offering_document_resource import OfferingDocumentResource
from .offering_participant_resource import OfferingParticipantResource

__all__ = ["OfferingDetail"]


class OfferingDetail(OfferingCard):
    """One offering with everything needed to render its detail payload."""

    disclosures: Optional[str] = None
    """Important disclosures."""

    documents: Optional[List[OfferingDocumentResource]] = None
    """Campaign documents in display order."""

    highlights: Optional[List[OfferingHighlight]] = None
    """Ordered resolved highlights."""

    investment_thesis: Optional[str] = None
    """Campaign-specific investment framing."""

    key_risks: Optional[List[OfferingKeyRisk]] = None
    """Ordered key risks."""

    participants: Optional[List[OfferingParticipantResource]] = None
    """Campaign participants in display order."""

    structure_description: Optional[str] = None
    """Vehicle/structure framing shown before typed SPV terms exist."""

    why_now: Optional[str] = None
    """Why-now framing."""

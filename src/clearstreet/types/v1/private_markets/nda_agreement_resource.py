# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["NdaAgreementResource"]


class NdaAgreementResource(BaseModel):
    """Current NDA agreement for an SPV-backed deal."""

    acceptance_text: str
    """Exact assent and authority representation shown to the signer."""

    acceptance_text_version: int
    """Version of the acceptance representation."""

    agreement_id: str
    """Stable agreement identifier submitted with an IOI acceptance."""

    document_reference: str
    """Durable reference to the immutable NDA artifact."""

    document_sha256: str
    """Lowercase SHA-256 digest of the artifact bytes."""

    effective_at: datetime
    """Time this version became effective."""

    version: int
    """Strictly increasing SPV-local agreement version."""

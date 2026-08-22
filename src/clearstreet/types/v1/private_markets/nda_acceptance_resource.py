# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["NdaAcceptanceResource"]


class NdaAcceptanceResource(BaseModel):
    """Public evidence that an NDA version was accepted.

    Signing IP and other
    provenance remain audit-only and are never returned by this API.
    """

    accepted_at: datetime

    agreement_id: str

    version: int

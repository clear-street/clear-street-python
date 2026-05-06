# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ..entitlement_code import EntitlementCode
from ..entitlement_agreement_key import EntitlementAgreementKey

__all__ = ["EntitlementAgreementResource"]


class EntitlementAgreementResource(BaseModel):
    agreement_id: str

    agreement_key: EntitlementAgreementKey
    """Stable entitlement agreement family key."""

    document_content: str

    document_sha256: str

    entitlement_codes: List[EntitlementCode]

    title: str

    version: int

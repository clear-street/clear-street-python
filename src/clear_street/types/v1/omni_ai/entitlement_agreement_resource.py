# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["EntitlementAgreementResource"]


class EntitlementAgreementResource(BaseModel):
    agreement_id: str

    agreement_key: str

    document_content: str

    document_sha256: str

    entitlement_codes: List[str]

    title: str

    version: int

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .omni_ai.entitlement_code import EntitlementCode
from .omni_ai.entitlement_agreement_key import EntitlementAgreementKey

__all__ = ["OpenEntitlementConsentAction"]


class OpenEntitlementConsentAction(BaseModel):
    """Action to open entitlement consent flow for one or more accounts."""

    account_ids: List[int]

    agreement_key: EntitlementAgreementKey
    """Stable entitlement agreement family key."""

    entitlement_codes: List[EntitlementCode]

    reason: str

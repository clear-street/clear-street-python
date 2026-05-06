# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .entitlement_code import EntitlementCode
from .entitlement_agreement_key import EntitlementAgreementKey

__all__ = ["OpenEntitlementConsentAction"]


class OpenEntitlementConsentAction(BaseModel):
    """Action to open entitlement consent flow for one or more accounts."""

    agreement_key: EntitlementAgreementKey
    """Stable entitlement agreement family key."""

    reason: str

    requested_entitlement_codes: List[EntitlementCode]

    trading_account_ids: List[int]

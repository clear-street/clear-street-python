# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["OpenEntitlementConsentAction"]


class OpenEntitlementConsentAction(BaseModel):
    """Action to open entitlement consent flow for one or more accounts."""

    agreement_key: str

    reason: str

    requested_entitlement_codes: List[str]

    trading_account_ids: List[int]

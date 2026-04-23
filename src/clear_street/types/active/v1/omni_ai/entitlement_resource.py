# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["EntitlementResource"]


class EntitlementResource(BaseModel):
    agreement_id: str

    entitlement_code: str

    entitlement_id: str

    granted_at: str

    trading_account_id: int

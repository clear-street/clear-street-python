# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..entitlement_code import EntitlementCode

__all__ = ["EntitlementResource"]


class EntitlementResource(BaseModel):
    agreement_id: str

    entitlement_code: EntitlementCode
    """Stable entitlement code granted by an agreement."""

    entitlement_id: str

    granted_at: str

    trading_account_id: int

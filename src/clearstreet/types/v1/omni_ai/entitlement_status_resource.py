# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..entitlement_code import EntitlementCode

__all__ = ["EntitlementStatusResource"]


class EntitlementStatusResource(BaseModel):
    """Whether an entitlement is enabled for one account.

    Accounts the user never
    chose for are enabled by default.
    """

    account_id: int

    enabled: bool

    entitlement_code: EntitlementCode
    """Stable entitlement code granted by an agreement."""

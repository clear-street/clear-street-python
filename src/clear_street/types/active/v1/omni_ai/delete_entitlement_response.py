# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["DeleteEntitlementResponse"]


class DeleteEntitlementResponse(BaseModel):
    entitlement_id: str

    revoked: bool

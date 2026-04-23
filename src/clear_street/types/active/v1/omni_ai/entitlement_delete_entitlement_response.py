# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .delete_entitlement_response import DeleteEntitlementResponse

__all__ = ["EntitlementDeleteEntitlementResponse"]


class EntitlementDeleteEntitlementResponse(BaseResponse):
    data: DeleteEntitlementResponse

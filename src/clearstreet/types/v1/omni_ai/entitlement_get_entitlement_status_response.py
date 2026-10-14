# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .entitlement_status_resource_list import EntitlementStatusResourceList

__all__ = ["EntitlementGetEntitlementStatusResponse"]


class EntitlementGetEntitlementStatusResponse(BaseResponse):
    data: EntitlementStatusResourceList

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .entitlement_resource_list import EntitlementResourceList

__all__ = ["EntitlementListEntitlementsResponse"]


class EntitlementListEntitlementsResponse(BaseResponse):
    data: EntitlementResourceList

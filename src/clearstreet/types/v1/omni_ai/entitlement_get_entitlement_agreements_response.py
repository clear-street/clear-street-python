# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .entitlement_agreement_resource_list import EntitlementAgreementResourceList

__all__ = ["EntitlementGetEntitlementAgreementsResponse"]


class EntitlementGetEntitlementAgreementsResponse(BaseResponse):
    data: EntitlementAgreementResourceList

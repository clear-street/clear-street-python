# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .entitlement_agreement_resource_list import EntitlementAgreementResourceList

__all__ = ["EntitlementAgreementListEntitlementAgreementsResponse"]


class EntitlementAgreementListEntitlementAgreementsResponse(BaseResponse):
    data: EntitlementAgreementResourceList

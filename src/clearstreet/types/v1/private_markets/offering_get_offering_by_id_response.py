# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .offering_detail import OfferingDetail
from ...shared.base_response import BaseResponse

__all__ = ["OfferingGetOfferingByIDResponse"]


class OfferingGetOfferingByIDResponse(BaseResponse):
    data: OfferingDetail
    """One offering with everything needed to render its detail payload."""

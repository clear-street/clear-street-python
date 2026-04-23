# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .mergers_acquisitions_event_list import MergersAcquisitionsEventList

__all__ = ["MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse"]


class MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse(BaseResponse):
    data: MergersAcquisitionsEventList

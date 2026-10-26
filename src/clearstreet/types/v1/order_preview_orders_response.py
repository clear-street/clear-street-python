# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .order_preview_entry_list import OrderPreviewEntryList

__all__ = ["OrderPreviewOrdersResponse"]


class OrderPreviewOrdersResponse(BaseResponse):
    data: OrderPreviewEntryList

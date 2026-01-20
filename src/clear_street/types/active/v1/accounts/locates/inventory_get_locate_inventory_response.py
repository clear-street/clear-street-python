# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .....shared.base_response import BaseResponse
from .locate_inventory_item_list import LocateInventoryItemList

__all__ = ["InventoryGetLocateInventoryResponse"]


class InventoryGetLocateInventoryResponse(BaseResponse):
    data: LocateInventoryItemList

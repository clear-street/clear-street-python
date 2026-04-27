# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .api_key_list_entry_list import APIKeyListEntryList

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseResponse):
    data: APIKeyListEntryList

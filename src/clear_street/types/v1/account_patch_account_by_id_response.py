# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .account_settings import AccountSettings
from ..shared.base_response import BaseResponse

__all__ = ["AccountPatchAccountByIDResponse"]


class AccountPatchAccountByIDResponse(BaseResponse):
    data: AccountSettings

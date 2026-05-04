# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .account_list import AccountList
from ..shared.base_response import BaseResponse

__all__ = ["AccountGetAccountsResponse"]


class AccountGetAccountsResponse(BaseResponse):
    data: AccountList

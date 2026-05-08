# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .account_balances import AccountBalances
from ..shared.base_response import BaseResponse

__all__ = ["AccountGetAccountBalancesResponse"]


class AccountGetAccountBalancesResponse(BaseResponse):
    data: AccountBalances
    """Represents the balance details for a trading account"""

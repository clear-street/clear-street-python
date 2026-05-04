# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .account import Account
from ..shared.base_response import BaseResponse

__all__ = ["AccountGetAccountByIDResponse"]


class AccountGetAccountByIDResponse(BaseResponse):
    data: Account
    """Represents a trading account"""

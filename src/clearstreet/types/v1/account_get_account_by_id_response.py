# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .account_with_personal_details import AccountWithPersonalDetails

__all__ = ["AccountGetAccountByIDResponse"]


class AccountGetAccountByIDResponse(BaseResponse):
    data: AccountWithPersonalDetails
    """Represents a trading account"""

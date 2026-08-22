# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .private_markets.company_detail import CompanyDetail

__all__ = ["PrivateMarketGetCompanyByIDResponse"]


class PrivateMarketGetCompanyByIDResponse(BaseResponse):
    data: CompanyDetail
    """A company's identity and its complete published profile."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...options_contract_list import OptionsContractList
from .....shared.base_response import BaseResponse

__all__ = ["ContractGetOptionContractsResponse"]


class ContractGetOptionContractsResponse(BaseResponse):
    data: OptionsContractList

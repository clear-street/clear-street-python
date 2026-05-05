# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from ..options_contract_list import OptionsContractList

__all__ = ["OptionGetOptionContractsResponse"]


class OptionGetOptionContractsResponse(BaseResponse):
    data: OptionsContractList

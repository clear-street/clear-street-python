# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instrument_core_list import InstrumentCoreList
from ..shared.base_response import BaseResponse

__all__ = ["InstrumentSearchInstrumentsResponse"]


class InstrumentSearchInstrumentsResponse(BaseResponse):
    data: InstrumentCoreList

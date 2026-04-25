# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .instrument_fundamentals import InstrumentFundamentals

__all__ = ["FundamentalGetInstrumentFundamentalsResponse"]


class FundamentalGetInstrumentFundamentalsResponse(BaseResponse):
    data: InstrumentFundamentals
    """Supplemental fundamentals and company profile data for an instrument."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .instrument_earnings_transcript_list import InstrumentEarningsTranscriptList

__all__ = ["InstrumentDataGetInstrumentEarningsTranscriptsResponse"]


class InstrumentDataGetInstrumentEarningsTranscriptsResponse(BaseResponse):
    data: InstrumentEarningsTranscriptList

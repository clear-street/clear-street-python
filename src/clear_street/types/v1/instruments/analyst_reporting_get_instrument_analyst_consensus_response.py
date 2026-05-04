# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .instrument_analyst_consensus import InstrumentAnalystConsensus

__all__ = ["AnalystReportingGetInstrumentAnalystConsensusResponse"]


class AnalystReportingGetInstrumentAnalystConsensusResponse(BaseResponse):
    data: InstrumentAnalystConsensus
    """Aggregated analyst consensus metrics"""

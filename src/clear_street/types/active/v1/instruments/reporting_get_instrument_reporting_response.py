# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instrument_earnings import InstrumentEarnings
from ....shared.base_response import BaseResponse

__all__ = ["ReportingGetInstrumentReportingResponse"]


class ReportingGetInstrumentReportingResponse(BaseResponse):
    data: InstrumentEarnings
    """Represents instrument earnings data"""

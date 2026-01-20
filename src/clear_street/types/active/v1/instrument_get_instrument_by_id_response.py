# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instrument import Instrument
from ...shared.base_response import BaseResponse

__all__ = ["InstrumentGetInstrumentByIDResponse"]


class InstrumentGetInstrumentByIDResponse(BaseResponse):
    data: Instrument
    """Represents a tradable financial instrument, including supplemental information"""

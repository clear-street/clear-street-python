# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.base_response import BaseResponse
from .instrument_cash_flow_statement_list import InstrumentCashFlowStatementList

__all__ = ["InstrumentDataGetInstrumentCashFlowStatementsResponse"]


class InstrumentDataGetInstrumentCashFlowStatementsResponse(BaseResponse):
    data: InstrumentCashFlowStatementList

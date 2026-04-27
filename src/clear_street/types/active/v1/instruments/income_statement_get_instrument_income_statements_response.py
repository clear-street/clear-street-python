# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .instrument_income_statement_list import InstrumentIncomeStatementList

__all__ = ["IncomeStatementGetInstrumentIncomeStatementsResponse"]


class IncomeStatementGetInstrumentIncomeStatementsResponse(BaseResponse):
    data: InstrumentIncomeStatementList

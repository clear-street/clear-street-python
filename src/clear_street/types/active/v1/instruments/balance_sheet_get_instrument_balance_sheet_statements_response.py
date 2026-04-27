# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from .instrument_balance_sheet_statement_list import InstrumentBalanceSheetStatementList

__all__ = ["BalanceSheetGetInstrumentBalanceSheetStatementsResponse"]


class BalanceSheetGetInstrumentBalanceSheetStatementsResponse(BaseResponse):
    data: InstrumentBalanceSheetStatementList

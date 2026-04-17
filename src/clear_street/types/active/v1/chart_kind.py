# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from . import data_chart, symbol_chart

__all__ = ["ChartKind", "SymbolChart", "DataChart"]


class SymbolChart(symbol_chart.SymbolChart):
    """Chart for a specific ticker symbol"""

    chart_type: Literal["symbol_chart"]


class DataChart(data_chart.DataChart):
    """Chart built from explicit data series"""

    chart_type: Literal["data_chart"]


ChartKind: TypeAlias = Union[SymbolChart, DataChart]

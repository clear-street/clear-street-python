# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .data_chart import DataChart
from .symbol_chart import SymbolChart
from .action_button import ActionButton

__all__ = ["ChartPayload"]


class ChartPayload(BaseModel):
    """Typed chart payload rendered inline in assistant content."""

    chart_id: str = FieldInfo(alias="chartId")
    """Stable chart identifier scoped to the content part."""

    action_buttons: Optional[List[ActionButton]] = FieldInfo(alias="actionButtons", default=None)
    """Buttons associated with this chart."""

    data_chart: Optional[DataChart] = FieldInfo(alias="dataChart", default=None)
    """Explicit series-driven chart definition."""

    symbol_chart: Optional[SymbolChart] = FieldInfo(alias="symbolChart", default=None)
    """Symbol-driven chart definition."""

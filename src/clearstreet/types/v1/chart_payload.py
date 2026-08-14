# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .data_chart import DataChart
from .action_button import ActionButton

__all__ = ["ChartPayload"]


class ChartPayload(BaseModel):
    """Typed chart payload rendered inline in assistant content."""

    chart_id: str = FieldInfo(alias="chartId")
    """Stable chart identifier scoped to the content part."""

    clicked: bool
    """Whether the current user clicked this chart."""

    action_buttons: Optional[List[ActionButton]] = FieldInfo(alias="actionButtons", default=None)
    """Buttons associated with this chart."""

    data_chart: Optional[DataChart] = FieldInfo(alias="dataChart", default=None)
    """
    Explicit series-driven chart definition. When a null/undefined value is
    observed, it indicates it does not apply.
    """

    item_id: Optional[str] = FieldInfo(alias="itemId", default=None)
    """Interaction-tracking identity.

    Absent on messages created before tracking. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

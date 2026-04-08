# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .chart_kind import ChartKind
from .action_button import ActionButton

__all__ = ["ContentPartChart"]


class ContentPartChart(BaseModel):
    chart_id: str

    action_buttons: Optional[List[ActionButton]] = None

    chart_kind: Optional[ChartKind] = None
    """Chart for a specific ticker symbol"""

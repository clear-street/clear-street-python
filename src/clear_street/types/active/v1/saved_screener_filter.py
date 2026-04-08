# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["SavedScreenerFilter"]


class SavedScreenerFilter(BaseModel):
    """A single filter criterion for a screener"""

    field_name: str
    """The field name to filter on"""

    operation: str
    """The filter operation (lt, lte, gt, gte, eq, rgx, bw, ew)"""

    value: str
    """The filter value"""

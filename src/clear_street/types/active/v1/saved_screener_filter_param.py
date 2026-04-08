# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SavedScreenerFilterParam"]


class SavedScreenerFilterParam(TypedDict, total=False):
    """A single filter criterion for a screener"""

    field_name: Required[str]
    """The field name to filter on"""

    operation: Required[str]
    """The filter operation (lt, lte, gt, gte, eq, rgx, bw, ew)"""

    value: Required[str]
    """The filter value"""

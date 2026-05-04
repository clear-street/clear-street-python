# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DailySummaryGetDailySummariesParams"]


class DailySummaryGetDailySummariesParams(TypedDict, total=False):
    instrument_ids: Required[str]
    """Comma-separated OEMS instrument UUIDs (required, 1..=100)"""

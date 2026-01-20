# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .base_strategy_params_param import BaseStrategyParamsParam

__all__ = ["TwapStrategyParam"]


class TwapStrategyParam(BaseStrategyParamsParam, total=False):
    """Time Weighted Average Price strategy"""

    max_percent: Optional[int]
    """Maximum percentage of market volume to participate in (0-50)"""

    min_percent: Optional[int]
    """Minimum percentage of market volume to participate in (0-100)"""

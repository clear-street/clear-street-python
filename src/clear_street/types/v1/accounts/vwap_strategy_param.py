# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...api_decimal64 import APIDecimal64
from .base_strategy_params_param import BaseStrategyParamsParam

__all__ = ["VwapStrategyParam"]


class VwapStrategyParam(BaseStrategyParamsParam, total=False):
    """Volume Weighted Average Price strategy"""

    max_percent: Optional[APIDecimal64]
    """Maximum percentage of market volume to participate in (0-50)"""

    min_percent: Optional[APIDecimal64]
    """Minimum percentage of market volume to participate in (0-100)"""

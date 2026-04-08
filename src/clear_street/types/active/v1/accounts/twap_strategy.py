# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...api_decimal64 import APIDecimal64
from .base_strategy_params import BaseStrategyParams

__all__ = ["TwapStrategy"]


class TwapStrategy(BaseStrategyParams):
    """Time Weighted Average Price strategy"""

    max_percent: Optional[APIDecimal64] = None
    """Maximum percentage of market volume to participate in (0-50)"""

    min_percent: Optional[APIDecimal64] = None
    """Minimum percentage of market volume to participate in (0-100)"""

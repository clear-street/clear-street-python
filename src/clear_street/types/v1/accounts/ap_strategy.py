# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...api_decimal64 import APIDecimal64
from .base_strategy_params import BaseStrategyParams

__all__ = ["ApStrategy"]


class ApStrategy(BaseStrategyParams):
    """Arrival Price strategy"""

    max_percent: Optional[APIDecimal64] = None
    """Maximum percentage of market volume to participate in (0-100)"""

    min_percent: Optional[APIDecimal64] = None
    """Minimum percentage of market volume to participate in (0-100)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .base_strategy_params import BaseStrategyParams

__all__ = ["VwapStrategy"]


class VwapStrategy(BaseStrategyParams):
    """Volume Weighted Average Price strategy"""

    max_percent: Optional[int] = None
    """Maximum percentage of market volume to participate in (0-50)"""

    min_percent: Optional[int] = None
    """Minimum percentage of market volume to participate in (0-100)"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...api_decimal64 import APIDecimal64
from .base_strategy_params import BaseStrategyParams

__all__ = ["PovStrategy"]


class PovStrategy(BaseStrategyParams):
    """Percentage of Volume strategy"""

    target_percent: APIDecimal64
    """Target percentage of market volume to participate in (0-100)"""

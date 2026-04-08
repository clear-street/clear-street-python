# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required

from ...api_decimal64 import APIDecimal64
from .base_strategy_params_param import BaseStrategyParamsParam

__all__ = ["PovStrategyParam"]


class PovStrategyParam(BaseStrategyParamsParam, total=False):
    """Percentage of Volume strategy"""

    target_percent: Required[APIDecimal64]
    """Target percentage of market volume to participate in (0-100)"""

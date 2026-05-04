# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias

from .ap_strategy_param import ApStrategyParam
from .dma_strategy_param import DmaStrategyParam
from .pov_strategy_param import PovStrategyParam
from .dark_strategy_param import DarkStrategyParam
from .twap_strategy_param import TwapStrategyParam
from .vwap_strategy_param import VwapStrategyParam
from .base_strategy_params_param import BaseStrategyParamsParam

__all__ = ["OrderStrategyParam", "Sor", "Vwap", "Twap", "Ap", "Pov", "Dark", "Dma"]


class Sor(BaseStrategyParamsParam, total=False):
    """Smart Order Router (default) - routes to best available venue"""

    type: Required[Literal["SOR"]]


class Vwap(VwapStrategyParam, total=False):
    """Volume Weighted Average Price - matches VWAP over a period"""

    type: Required[Literal["VWAP"]]


class Twap(TwapStrategyParam, total=False):
    """Time Weighted Average Price - spreads execution evenly over time"""

    type: Required[Literal["TWAP"]]


class Ap(ApStrategyParam, total=False):
    """Arrival Price - aims to match price at order placement time"""

    type: Required[Literal["AP"]]


class Pov(PovStrategyParam, total=False):
    """Percentage of Volume - participates as a percentage of market volume"""

    type: Required[Literal["POV"]]


class Dark(DarkStrategyParam, total=False):
    """Dark Pool - routes to dark pool venues"""

    type: Required[Literal["DARK"]]


class Dma(DmaStrategyParam, total=False):
    """Direct Market Access - sends directly to a specified exchange"""

    type: Required[Literal["DMA"]]


OrderStrategyParam: TypeAlias = Union[Sor, Vwap, Twap, Ap, Pov, Dark, Dma]

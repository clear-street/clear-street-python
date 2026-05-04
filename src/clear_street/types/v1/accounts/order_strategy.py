# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .ap_strategy import ApStrategy
from .dma_strategy import DmaStrategy
from .pov_strategy import PovStrategy
from .dark_strategy import DarkStrategy
from .twap_strategy import TwapStrategy
from .vwap_strategy import VwapStrategy
from .base_strategy_params import BaseStrategyParams

__all__ = ["OrderStrategy", "Sor", "Vwap", "Twap", "Ap", "Pov", "Dark", "Dma"]


class Sor(BaseStrategyParams):
    """Smart Order Router (default) - routes to best available venue"""

    type: Literal["SOR"]


class Vwap(VwapStrategy):
    """Volume Weighted Average Price - matches VWAP over a period"""

    type: Literal["VWAP"]


class Twap(TwapStrategy):
    """Time Weighted Average Price - spreads execution evenly over time"""

    type: Literal["TWAP"]


class Ap(ApStrategy):
    """Arrival Price - aims to match price at order placement time"""

    type: Literal["AP"]


class Pov(PovStrategy):
    """Percentage of Volume - participates as a percentage of market volume"""

    type: Literal["POV"]


class Dark(DarkStrategy):
    """Dark Pool - routes to dark pool venues"""

    type: Literal["DARK"]


class Dma(DmaStrategy):
    """Direct Market Access - sends directly to a specified exchange"""

    type: Literal["DMA"]


OrderStrategy: TypeAlias = Union[Sor, Vwap, Twap, Ap, Pov, Dark, Dma]

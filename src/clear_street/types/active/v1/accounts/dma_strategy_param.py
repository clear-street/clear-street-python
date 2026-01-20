# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .destination import Destination

__all__ = ["DmaStrategyParam"]


class DmaStrategyParam(TypedDict, total=False):
    """Direct Market Access strategy"""

    destination: Required[Destination]
    """Destination exchange (MIC code)"""

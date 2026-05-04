# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .screener_column import ScreenerColumn

__all__ = ["ScreenerRow"]

ScreenerRow: TypeAlias = List[ScreenerColumn]

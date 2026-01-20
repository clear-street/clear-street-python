# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from .destination import Destination

__all__ = ["DmaStrategy"]


class DmaStrategy(BaseModel):
    """Direct Market Access strategy"""

    destination: Destination
    """Destination exchange (MIC code)"""

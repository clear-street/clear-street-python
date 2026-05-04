# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["DmaStrategy"]


class DmaStrategy(BaseModel):
    """Direct Market Access strategy"""

    destination: str
    """Destination exchange (MIC code)"""

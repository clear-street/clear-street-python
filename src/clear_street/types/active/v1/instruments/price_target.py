# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["PriceTarget"]


class PriceTarget(BaseModel):
    """Analyst price target statistics"""

    average: str
    """Average analyst price target"""

    currency: str
    """ISO 4217 currency code of the price targets"""

    high: str
    """Highest analyst price target"""

    low: str
    """Lowest analyst price target"""

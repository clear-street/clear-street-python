# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime

from ....._models import BaseModel
from .price_target import PriceTarget
from .analyst_rating import AnalystRating
from .analyst_distribution import AnalystDistribution

__all__ = ["InstrumentAnalystConsensus"]


class InstrumentAnalystConsensus(BaseModel):
    """Aggregated analyst consensus metrics"""

    date: datetime.date
    """The date the consensus snapshot was generated"""

    distribution: AnalystDistribution
    """Count of individual analyst recommendations by category"""

    price_target: PriceTarget
    """Aggregated analyst price target statistics"""

    rating: AnalystRating
    """Consensus analyst rating"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel
from .price_target import PriceTarget
from .analyst_rating import AnalystRating
from .analyst_distribution import AnalystDistribution

__all__ = ["InstrumentAnalystConsensus"]


class InstrumentAnalystConsensus(BaseModel):
    """Aggregated analyst consensus metrics"""

    date: datetime.date
    """The date the consensus snapshot was generated"""

    distribution: Optional[AnalystDistribution] = None
    """
    Count of individual analyst recommendations by category When a null/undefined
    value is observed, it indicates that there is no available data.
    """

    price_target: Optional[PriceTarget] = None
    """
    Aggregated analyst price target statistics When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    rating: Optional[AnalystRating] = None
    """
    Consensus analyst rating When a null/undefined value is observed, it indicates
    that there is no available data.
    """

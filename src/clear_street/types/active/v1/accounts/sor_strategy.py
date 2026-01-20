# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .urgency import Urgency
from ....._models import BaseModel

__all__ = ["SorStrategy"]


class SorStrategy(BaseModel):
    """Base parameters common to most algorithmic strategies"""

    end_at: Optional[datetime] = None
    """UTC timestamp to end execution (defaults to market close)"""

    start_at: Optional[datetime] = None
    """UTC timestamp to start execution (defaults to order placement time)"""

    urgency: Optional[Urgency] = None
    """Urgency level for execution aggressiveness"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ....._models import BaseModel

__all__ = ["MergersAcquisitionsEvent"]


class MergersAcquisitionsEvent(BaseModel):
    """Represents a merger or acquisition event"""

    acquirer_symbol: str
    """The symbol of the acquiring company"""

    target_symbol: str
    """The symbol of the target company being acquired"""

    transaction_date: date
    """The date of the transaction"""

    accepted_at: Optional[datetime] = None
    """The timestamp when the merger or acquisition was accepted in UTC"""

    acquirer_cik: Optional[str] = None
    """The CIK of the acquiring company"""

    acquirer_name: Optional[str] = None
    """The name of the acquiring company"""

    link: Optional[str] = None
    """A URL link to more details about the merger or acquisition"""

    target_cik: Optional[str] = None
    """The CIK of the target company"""

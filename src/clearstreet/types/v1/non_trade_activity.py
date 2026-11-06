# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ..._models import BaseModel
from .activity_type import ActivityType
from ..security_type import SecurityType
from .activity_state import ActivityState

__all__ = ["NonTradeActivity"]


class NonTradeActivity(BaseModel):
    id: str
    """ID for the activity, in UUID-v7 format."""

    account_id: str
    """Account ID"""

    activity_subtype: str
    """Subtype within its `activity_type`."""

    activity_type: ActivityType
    """Categorization for the activity."""

    amount: str
    """Cash amount change."""

    created_at: datetime
    """The creation time at UTC, when this activity became part of the ledger"""

    currency: str
    """Currency of the cash amount. Always USD for now."""

    effective_date: date
    """Effective date for the activity"""

    instrument_type: SecurityType
    """The security type."""

    memo: str
    """Memo"""

    qty: str
    """Quantity change in the instrument."""

    state: ActivityState
    """State for this activity."""

    cancelled_reference_id: Optional[str] = None
    """Reference ID for the record that is being cancelled.

    Present only on records where the activity state is 'cancelled'. The contents of
    this fields points at the reference_id of the original record that is being
    cancelled by this record.
    """

    instrument_id: Optional[str] = None
    """Instrument identifier.

    Omitted when the activity has no single resolvable instrument.
    """

    reference_id: Optional[str] = None
    """Reference ID for the activity, in ULID format.

    Present only on records where activity state is 'settled'. When a activity is
    cancelled, the cancelation record is pointing at this reference_id.
    """

    symbol: Optional[str] = None
    """Symbol of the instrument.

    Omitted when the activity has no single resolvable instrument.
    """

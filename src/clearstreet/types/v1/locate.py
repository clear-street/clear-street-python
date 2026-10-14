# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel
from .locate_status import LocateStatus

__all__ = ["Locate"]


class Locate(BaseModel):
    """A locate request joined with the locate granted for it, if any."""

    account_id: int
    """Account the locate is booked to."""

    client_request_id: str
    """Caller-assigned id of the locate request."""

    effective_date: date
    """New York calendar date the locate is in force for."""

    instrument_id: str
    """Instrument id."""

    locate_request_id: str
    """Engine-assigned locate request id."""

    requested_quantity: int
    """Number of shares requested."""

    status: LocateStatus
    """Presented status of the locate."""

    locate_id: Optional[str] = None
    """
    Engine-assigned locate id; set once the locate is granted. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    quantity: Optional[int] = None
    """
    Number of shares granted; set once the locate is granted. When a null/undefined
    value is observed, it indicates it does not apply.
    """

    related_order_id: Optional[str] = None
    """
    Client order id the request relates to, if any. When a null/undefined value is
    observed, it indicates it does not apply.
    """

    reserved_quantity: Optional[int] = None
    """
    Number of granted shares reserved. When a null/undefined value is observed, it
    indicates it does not apply.
    """

    used_quantity: Optional[int] = None
    """
    Number of granted shares already used. When a null/undefined value is observed,
    it indicates it does not apply.
    """

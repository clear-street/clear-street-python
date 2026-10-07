# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .locate_rate import LocateRate
from ..shared.api_error import APIError
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["LocateRateResult"]


class LocateRateResult(BaseModel):
    """A requested instrument with either its cached borrow rate or an error."""

    instrument: InstrumentIDOrSymbol
    """
    The instrument id (UUID) or symbol, echoed exactly as requested, so each result
    maps back to its request.
    """

    error: Optional[APIError] = None
    """
    Why no rate is present — a `404` when the instrument is unknown or has no cached
    rate. Omitted when `rate` is present.
    """

    rate: Optional[LocateRate] = None
    """The cached borrow rate.

    Present when a rate was found; omitted when `error` is present.
    """

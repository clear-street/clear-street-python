# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["MarketDataGetSnapshotsParams"]


class MarketDataGetSnapshotsParams(TypedDict, total=False):
    expiry: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter the option chain to contracts expiring on this date (YYYY-MM-DD).

    Must be provided together with `underlying_instrument_id`.
    """

    instrument_ids: SequenceNotStr[InstrumentIDOrSymbol]
    """
    Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
    symbols). Accepts 1 to 100 IDs; duplicate resolved ids collapse to a single row.
    Required unless `underlying_instrument_id` and `expiry` are provided; mutually
    exclusive with that pair.
    """

    underlying_instrument_id: str
    """
    Instrument identifier or symbol of the underlying equity/index for an option
    chain. Must be provided together with `expiry`; mutually exclusive with
    `instrument_ids`.
    """

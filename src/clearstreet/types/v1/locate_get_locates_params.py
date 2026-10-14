# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .instrument_id_or_symbol import InstrumentIDOrSymbol

__all__ = ["LocateGetLocatesParams"]


class LocateGetLocatesParams(TypedDict, total=False):
    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Effective date to list; defaults to today's New York calendar date.

    Explicit dates are used unchanged, including weekends and holidays.
    """

    instrument_ids: SequenceNotStr[InstrumentIDOrSymbol]
    """Comma-separated instrument IDs (UUID) or symbols."""

    status: List[Literal["REQUESTED", "ACCEPTED", "REJECTED", "EXPIRED"]]
    """Comma-separated locate statuses to filter by"""

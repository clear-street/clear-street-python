# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InstrumentGetInstrumentByIDParams"]


class InstrumentGetInstrumentByIDParams(TypedDict, total=False):
    include_options_expiry_dates: Optional[bool]
    """When true, include unique options expiry dates for this instrument"""

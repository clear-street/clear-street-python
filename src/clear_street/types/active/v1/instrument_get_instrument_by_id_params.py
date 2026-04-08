# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..security_id_source import SecurityIDSource

__all__ = ["InstrumentGetInstrumentByIDParams"]


class InstrumentGetInstrumentByIDParams(TypedDict, total=False):
    security_id_source: Required[SecurityIDSource]
    """Security identifier source"""

    include_options_expiry_dates: Optional[bool]
    """When true, include unique options expiry dates for this instrument"""

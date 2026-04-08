# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...security_id_source import SecurityIDSource

__all__ = ["EventGetInstrumentEventsParams"]


class EventGetInstrumentEventsParams(TypedDict, total=False):
    security_id_source: Required[SecurityIDSource]
    """Security identifier source"""

    from_date: str
    """The start date for the query range, inclusive (YYYY-MM-DD)."""

    to_date: str
    """The end date for the query range, inclusive (YYYY-MM-DD)."""

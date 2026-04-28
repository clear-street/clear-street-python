# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ....._types import SequenceNotStr

__all__ = ["SnapshotGetSnapshotsParams"]


class SnapshotGetSnapshotsParams(TypedDict, total=False):
    ids: str
    """Comma-separated OEMS instrument UUIDs."""

    security_id: SequenceNotStr[str]
    """Filter by security ID(s). Accepts single value or indexed array.

    Examples:

    - Single: `security_id=037833100`
    - Multiple: `security_id[0]=037833100&security_id[1]=594918104`
    """

    security_id_source: SequenceNotStr[str]
    """Source(s) for the security ID filter.

    Must match the count and order of security_id.

    Examples:

    - Single: `security_id_source=CUSIP`
    - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`
    """

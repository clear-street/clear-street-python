# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LocateCreateLocateRequestParams", "Body"]


class LocateCreateLocateRequestParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    """Request to create a new locate order"""

    quantity: Required[int]
    """The quantity of shares to locate"""

    symbol: Required[str]
    """The symbol of the security to locate"""

    comments: Optional[str]
    """Optional comments to associate with the locate request"""

    reference_id: Optional[str]
    """A client-provided reference ID to identify the locate order"""

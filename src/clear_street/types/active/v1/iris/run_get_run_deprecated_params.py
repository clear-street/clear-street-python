# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunGetRunDeprecatedParams"]


class RunGetRunDeprecatedParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID for the request"""

    page_size: int
    """Maximum events to return"""

    page_token: str
    """Page token for incremental polling"""

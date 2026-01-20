# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LocateUpdateLocateRequestParams"]


class LocateUpdateLocateRequestParams(TypedDict, total=False):
    accept: Required[bool]
    """Whether to accept (`true`) or decline (`false`) the locate offer"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountGetAccountBalancesParams"]


class AccountGetAccountBalancesParams(TypedDict, total=False):
    top_margin_contributors_limit: int
    """Limit the number of top margin contributors returned."""

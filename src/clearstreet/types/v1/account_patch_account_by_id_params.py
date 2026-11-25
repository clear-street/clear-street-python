# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .margin_multiplier import MarginMultiplier

__all__ = ["AccountPatchAccountByIDParams", "Risk"]


class AccountPatchAccountByIDParams(TypedDict, total=False):
    risk: Optional[Risk]
    """Risk settings for the account"""


class Risk(TypedDict, total=False):
    """Risk settings for the account"""

    margin_multiplier: MarginMultiplier
    """
    The margin multiplier of a Reg T margin account: `"1"` for cash only, `"4"` for
    full Reg T margin. Only a Reg T margin account may set it. `"4"` replaces a
    `"1"` the account chose, never a limit Clear Street set, so the response can
    give `"1"` after a request for `"4"`. It cannot be `null`.
    """

    max_notional: Optional[str]
    """The maximum notional value available to the account: 0 or greater.

    `null` clears the limit.
    """

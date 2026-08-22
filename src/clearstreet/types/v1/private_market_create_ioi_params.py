# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PrivateMarketCreateIoiParams", "NdaAcceptance"]


class PrivateMarketCreateIoiParams(TypedDict, total=False):
    account_id: Required[int]

    notional_amount: Required[str]

    offering_id: Required[str]

    nda_acceptance: Optional[NdaAcceptance]
    """Required only when the offering's attached SPV has an NDA agreement."""


class NdaAcceptance(TypedDict, total=False):
    """Required only when the offering's attached SPV has an NDA agreement."""

    accepted: Required[bool]
    """Must be true; confirms affirmative assent."""

    agreement_id: Required[str]
    """Exact agreement id returned by offering detail."""

    authority_confirmed: Required[bool]
    """Must be true; confirms the signer may bind the account-holder entity."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PrivateMarketUpdateIoiParams", "NdaAcceptance"]


class PrivateMarketUpdateIoiParams(TypedDict, total=False):
    account_id: Required[int]

    notional_amount: Required[str]

    nda_acceptance: Optional[NdaAcceptance]
    """
    Required when the SPV's current NDA version is newer than the IOI's latest
    acceptance. Irrelevant acceptances are rejected.
    """


class NdaAcceptance(TypedDict, total=False):
    """
    Required when the SPV's current NDA version is newer than the IOI's
    latest acceptance. Irrelevant acceptances are rejected.
    """

    accepted: Required[bool]
    """Must be true; confirms affirmative assent."""

    agreement_id: Required[str]
    """Exact agreement id returned by offering detail."""

    authority_confirmed: Required[bool]
    """Must be true; confirms the signer may bind the account-holder entity."""

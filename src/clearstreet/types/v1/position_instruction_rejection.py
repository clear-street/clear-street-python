# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PositionInstructionRejection"]


class PositionInstructionRejection(BaseModel):
    """Machine-readable detail for a rejected position instruction.

    Populated on the submit and cancel responses for a row rejected with a
    structured reason. Branch on `reason` for programmatic handling and render
    your own copy; `rejection_reason` remains the human-readable fallback and is
    the field to use when listing historical instructions.
    """

    domain: str
    """
    Namespacing domain of the `reason` code — `com.clearstreet.oems.exercise` for
    reasons OEMS validates, `com.clearstreet.oems.clearing` for clearing-owned
    reasons.
    """

    metadata: object
    """Reason-specific parameters as string key/value pairs (e.g.

    `available` / `requested`, `expiry` / `business_date`, `required_level` /
    `account_level`). May be empty.
    """

    reason: str
    """Stable, machine-readable reason code, e.g.

    `DNE_NOT_ON_EXPIRY`, `INSUFFICIENT_POSITION`, `OPTIONS_LEVEL_EXCEEDED`,
    `EXERCISE_PAST_CUTOFF`.
    """

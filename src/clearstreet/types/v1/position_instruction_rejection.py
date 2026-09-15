# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["PositionInstructionRejection"]


class PositionInstructionRejection(BaseModel):
    """Machine-readable detail for a rejected position instruction.

    Present on every rejected row that carries a `rejection_reason`, across the
    full lifecycle — submit, cancel, get, and list. Branch on `reason` for
    programmatic handling and template your own copy from `metadata`;
    `rejection_reason` remains the human-readable fallback. Forward-only:
    instructions rejected before this field shipped may carry only
    `rejection_reason`.
    """

    domain: str
    """
    Namespacing domain of the `reason` code — `com.clearstreet.oems.exercise` for
    reasons OEMS validates, `com.clearstreet.oems.clearing` for clearing-owned
    reasons.
    """

    metadata: Dict[str, str]
    """Reason-specific parameters as a string→string map.

    Which keys are present depends on `reason`:

    - `INSUFFICIENT_POSITION` → `available`, `requested`
    - `DNE_NOT_ON_EXPIRY` / `CEA_NOT_ON_EXPIRY` → `expiry`, `business_date`
    - `EXERCISE_PAST_CUTOFF` → `cutoff_time`
    - `DUPLICATE_INSTRUCTION` → `existing_id`

    Empty for reasons that carry no parameters. New keys may be added over time, so
    treat unknown keys leniently.
    """

    reason: str
    """Stable, machine-readable reason code, e.g.

    `DNE_NOT_ON_EXPIRY`, `INSUFFICIENT_POSITION`, `OPTIONS_LEVEL_EXCEEDED`,
    `EXERCISE_PAST_CUTOFF`.
    """

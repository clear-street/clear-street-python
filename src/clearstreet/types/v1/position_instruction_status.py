# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PositionInstructionStatus"]

PositionInstructionStatus: TypeAlias = Literal[
    "SENT", "ACCEPTED", "REJECTED", "CANCEL_REQUESTED", "CANCELLED", "CANCEL_FAILED", "UNKNOWN"
]

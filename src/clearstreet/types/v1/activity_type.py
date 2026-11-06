# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ActivityType"]

ActivityType: TypeAlias = Literal[
    "money_movement",
    "interest",
    "fee",
    "dividend",
    "option_event",
    "transfer",
    "corporate_action",
    "tax_withholding",
    "adjustment",
    "other",
]

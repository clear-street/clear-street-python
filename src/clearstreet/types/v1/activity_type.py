# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ActivityType"]

ActivityType: TypeAlias = Literal[
    "MONEY_MOVEMENT",
    "INTEREST",
    "FEE",
    "DIVIDEND",
    "OPTION_EVENT",
    "TRANSFER",
    "CORPORATE_ACTION",
    "TAX_WITHHOLDING",
    "ADJUSTMENT",
    "OTHER",
]

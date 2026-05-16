# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["MarginType"]

MarginType: TypeAlias = Literal[
    "OTHER",
    "NONE",
    "PORTFOLIO_MARGIN",
    "RISK_BASED_HAIRCUT_BROKER_DEALER",
    "REG_T",
    "RISK_BASED_HAIRCUT_MARKET_MAKER",
    "CIRO",
    "FUTURES_NLV",
    "FUTURES_TOT_EQ",
]

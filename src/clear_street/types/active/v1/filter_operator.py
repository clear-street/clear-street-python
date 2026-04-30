# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FilterOperator"]

FilterOperator: TypeAlias = Literal[
    "LT",
    "LTE",
    "GT",
    "GTE",
    "EQ",
    "BETWEEN",
    "NOT_BETWEEN",
    "ONE_OF",
    "REGEX",
    "BEGINS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "IS_NULL",
    "IS_NOT_NULL",
]

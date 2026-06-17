# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FilterOperator"]

FilterOperator: TypeAlias = Literal[
    "LESS_THAN",
    "LESS_OR_EQUAL",
    "GREATER_THAN",
    "GREATER_OR_EQUAL",
    "EQUAL",
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

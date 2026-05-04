# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ...._types import Base64FileInput
from ...._utils import PropertyInfo

__all__ = ["IncomeStatementGetInstrumentIncomeStatementsParams"]


class IncomeStatementGetInstrumentIncomeStatementsParams(TypedDict, total=False):
    from_date: str
    """The start date for the query range, inclusive (YYYY-MM-DD)."""

    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    to_date: str
    """The end date for the query range, inclusive (YYYY-MM-DD)."""

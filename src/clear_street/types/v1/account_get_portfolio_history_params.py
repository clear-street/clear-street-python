# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountGetPortfolioHistoryParams"]


class AccountGetPortfolioHistoryParams(TypedDict, total=False):
    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Start date for the portfolio history range, in YYYY-MM-DD format."""

    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Defaults to today in America/New_York when omitted."""

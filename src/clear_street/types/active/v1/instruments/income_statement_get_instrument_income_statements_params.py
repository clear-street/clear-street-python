# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ....._types import Base64FileInput
from ....._utils import PropertyInfo
from ...security_id_source import SecurityIDSource

__all__ = ["IncomeStatementGetInstrumentIncomeStatementsParams"]


class IncomeStatementGetInstrumentIncomeStatementsParams(TypedDict, total=False):
    security_id_source: Required[SecurityIDSource]
    """Security identifier source"""

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

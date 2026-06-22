# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["AccountGetAccountsParams"]


class AccountGetAccountsParams(TypedDict, total=False):
    account_id: str
    """
    Filter to accounts whose id starts with this value (lexicographic prefix match
    on the decimal id, e.g. `100` matches `100345`).
    """

    account_name: str
    """
    Filter to accounts whose full name contains this value (case-insensitive
    substring match).
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

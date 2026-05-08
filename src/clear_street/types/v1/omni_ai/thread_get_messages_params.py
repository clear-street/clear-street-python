# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ...._types import Base64FileInput
from ...._utils import PropertyInfo

__all__ = ["ThreadGetMessagesParams"]


class ThreadGetMessagesParams(TypedDict, total=False):
    account_id: Required[int]
    """Account ID for the request"""

    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

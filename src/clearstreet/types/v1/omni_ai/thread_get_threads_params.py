# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ...._types import Base64FileInput
from ...._utils import PropertyInfo

__all__ = ["ThreadGetThreadsParams"]


class ThreadGetThreadsParams(TypedDict, total=False):
    account_id: int
    """
    Lists only conversations for this account, or unlinked conversations when
    omitted. Other reads authorize the resource's linked account. Omit when no
    account is selected; empty values and the string null are invalid.
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

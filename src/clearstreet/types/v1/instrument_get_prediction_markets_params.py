# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo

__all__ = ["InstrumentGetPredictionMarketsParams"]


class InstrumentGetPredictionMarketsParams(TypedDict, total=False):
    event_code: str
    """Event code; returns the markets of the event.

    Mutually exclusive with `market_ids`.
    """

    market_ids: str
    """Comma-separated market ids (UUID) or tickers, 1-100, in any status.

    Mutually exclusive with `event_code`.
    """

    page_size: int
    """The number of items to return per page.

    Only used when page_token is not provided.
    """

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next or previous page of results.

    Contains encoded pagination state; when provided, page_size is ignored.
    """

    statuses: str
    """
    Comma-separated statuses to keep: `OPEN`, `UNOPENED`, `PAUSED`, `CLOSED`,
    `SETTLED`. Defaults to `OPEN` with `event_code` and to every status with
    `market_ids`. Unrecognized values are ignored.
    """

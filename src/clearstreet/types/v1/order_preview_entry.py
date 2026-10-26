# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .order_preview import OrderPreview
from ..shared.api_error import APIError

__all__ = ["OrderPreviewEntry", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    """The order was previewed successfully."""

    preview: OrderPreview
    """The projected impact of the order."""

    id: Optional[str] = None
    """
    The client-provided `id` of the order this entry belongs to, echoed from the
    request. Always present when the request contains more than one order, since ids
    are required there.
    """


class UnionMember1(BaseModel):
    """The order could not be previewed.

    Shaped exactly like the top-level
    `error` object on rejected submissions.
    """

    error: APIError
    """Why this order's preview failed."""

    id: Optional[str] = None
    """
    The client-provided `id` of the order this entry belongs to, echoed from the
    request. Always present when the request contains more than one order, since ids
    are required there.
    """


OrderPreviewEntry: TypeAlias = Union[UnionMember0, UnionMember1]

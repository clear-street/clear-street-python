# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .field_ref import FieldRef
from .sort_spec import SortSpec
from .search_filter import SearchFilter

__all__ = ["OpenScreenerAction"]


class OpenScreenerAction(BaseModel):
    """Action to open a stock screener with filters.

    `filters`, `sorts` and `columns` use the same shapes as the
    `POST /saved-screeners` request body, so a client can save the screener
    the user is looking at by forwarding them unchanged.
    """

    filters: List[SearchFilter]
    """Filter criteria for the screener."""

    columns: Optional[List[FieldRef]] = None
    """Optional field/column selection for screener results.

    Absent means the default column set. When a null/undefined value is observed, it
    indicates it does not apply.
    """

    item_id: Optional[str] = None
    """Interaction-tracking identity.

    Absent on messages created before tracking. When a null/undefined value is
    observed, it indicates that there is no available data.
    """

    page_size: Optional[int] = None
    """
    Optional page size. When a null/undefined value is observed, it indicates it
    does not apply.
    """

    sorts: Optional[List[SortSpec]] = None
    """Optional sort specification.

    Absent means the screener's default order. When a null/undefined value is
    observed, it indicates it does not apply.
    """

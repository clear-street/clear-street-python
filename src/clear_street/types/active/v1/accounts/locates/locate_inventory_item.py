# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

__all__ = ["LocateInventoryItem"]


class LocateInventoryItem(BaseModel):
    """Represents the available locate inventory for a symbol"""

    account_id: int
    """The account the locate inventory belongs to"""

    available: int
    """The available quantity of shares that can be located to borrow"""

    reserved: int
    """
    The quantity of shares reserved for locate orders that have been `OFFERED` but
    not yet `FILLED`
    """

    symbol: str
    """The symbol of the security"""

    used: int
    """The quantity of shares that have been `FILLED` and are currently borrowed"""

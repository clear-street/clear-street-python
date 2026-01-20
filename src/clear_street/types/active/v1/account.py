# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel
from .account_kind import AccountKind
from .account_status import AccountStatus
from .account_subkind import AccountSubkind

__all__ = ["Account"]


class Account(BaseModel):
    """Represents a trading account"""

    id: int
    """The unique identifier for the account"""

    full_name: str
    """The full legal name of the account"""

    kind: AccountKind
    """The type of account"""

    open_date: date
    """The date the account was opened"""

    short_name: str
    """The short name of the account"""

    status: AccountStatus
    """The current status of the account"""

    subkind: AccountSubkind
    """The sub-type of account"""

    close_date: Optional[date] = None
    """The date the account was closed, if applicable"""

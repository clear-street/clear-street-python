# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from .address import Address
from ..._models import BaseModel
from .account_type import AccountType
from .account_status import AccountStatus
from .account_subtype import AccountSubtype

__all__ = ["AccountWithPersonalDetails"]


class AccountWithPersonalDetails(BaseModel):
    """Represents a trading account"""

    id: int
    """The unique identifier for the account"""

    account_holder_entity_id: int
    """The account holder entity identifier"""

    full_name: str
    """The full legal name of the account"""

    open_date: date
    """The date the account was opened"""

    options_level: int
    """The options level of the account"""

    short_name: str
    """The short name of the account"""

    status: AccountStatus
    """The current status of the account"""

    subtype: AccountSubtype
    """The sub-type of account"""

    type: AccountType
    """The type of account"""

    close_date: Optional[date] = None
    """
    The date the account was closed, if applicable When a null/undefined value is
    observed, it indicates it does not apply.
    """

    country_of_tax_residency: Optional[str] = None
    """The country of tax residency of the account-holder entity.

    `null` when not on file or entity reference data is unavailable. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    date_of_birth: Optional[date] = None
    """The date of birth of the account holder's primary contact.

    `null` when not on file or entity reference data is unavailable. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

    mailing_address: Optional[Address] = None
    """The mailing address of the account-holder entity.

    `null` when no mailing address is on file or entity reference data is
    unavailable. When a null/undefined value is observed, it indicates that there is
    no available data.
    """

    phone_number: Optional[str] = None
    """The phone number of the account holder's primary contact.

    `null` when not on file or entity reference data is unavailable. When a
    null/undefined value is observed, it indicates that there is no available data.
    """

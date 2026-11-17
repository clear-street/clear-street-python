# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .fees import Fees
from ..._models import BaseModel

__all__ = ["OrderPreviewAmount"]


class OrderPreviewAmount(BaseModel):
    """Monetary size of the previewed order."""

    gross_amount: str
    """Total cash impact of the order before estimated fees and commissions."""

    net_amount: str
    """
    Total cash impact of the order after estimated fees and commissions:
    `gross_amount` with `fees.total` applied.
    """

    fees: Optional[Fees] = None
    """Fees charged to the account, broken out by kind.

    Amounts are in the instrument's currency, at the full precision the venue
    reports. Statements round each fill's fee to the cent, so they can differ by a
    fraction of a cent. A positive amount is charged to the account; a negative
    amount is a rebate. New kinds of fee are added as new optional fields, and
    `total` always includes them.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Fees"]


class Fees(BaseModel):
    """Fees charged to the account, broken out by kind.

    Amounts are in the instrument's currency, at the full precision the venue reports.
    Statements round each fill's fee to the cent, so they can differ by a fraction of a
    cent. A positive amount is charged to the account; a negative amount is a rebate. New
    kinds of fee are added as new optional fields, and `total` always includes them.
    """

    total: str
    """
    Sum of every fee component, including kinds this API version does not break out.
    """

    exchange_fee: Optional[str] = None
    """
    Fee charged by the execution venue. When a null/undefined value is observed, it
    indicates it does not apply.
    """

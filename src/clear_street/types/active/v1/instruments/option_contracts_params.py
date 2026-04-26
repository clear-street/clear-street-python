# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ....._types import Base64FileInput
from ....._utils import PropertyInfo
from ..contract_type import ContractType
from ...security_id_source import SecurityIDSource

__all__ = ["OptionContractsParams"]


class OptionContractsParams(TypedDict, total=False):
    contract_type: ContractType
    """Filter by contract type: CALL or PUT"""

    expiry: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter to contracts expiring on this date (YYYY-MM-DD)"""

    page_size: int

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Token for retrieving the next page of results.

    Contains encoded pagination state (limit + offset). When provided, page_size is
    ignored.
    """

    underlier: str
    """Underlier symbol (e.g., AAPL, SPX)"""

    underlier_instrument_id: str
    """OEMS instrument UUID of the underlying equity/index"""

    underlier_security_id: str
    """Security identifier of the underlying (e.g., CUSIP, ISIN).

    Must be paired with underlier_security_id_source.
    """

    underlier_security_id_source: SecurityIDSource
    """Security ID source for the underlier (e.g., CMS, CUSIP).

    Must be paired with underlier_security_id.
    """

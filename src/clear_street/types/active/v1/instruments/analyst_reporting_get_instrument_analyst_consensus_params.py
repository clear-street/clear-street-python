# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ...security_id_source import SecurityIDSource

__all__ = ["AnalystReportingGetInstrumentAnalystConsensusParams"]


class AnalystReportingGetInstrumentAnalystConsensusParams(TypedDict, total=False):
    security_id_source: Required[SecurityIDSource]
    """Security identifier source"""

    from_: Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]
    """The start date for the query range, inclusive (YYYY-MM-DD)"""

    to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The end date for the query range, inclusive (YYYY-MM-DD)"""

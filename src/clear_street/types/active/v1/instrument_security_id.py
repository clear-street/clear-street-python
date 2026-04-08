# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ..security_id_source import SecurityIDSource

__all__ = ["InstrumentSecurityID"]


class InstrumentSecurityID(BaseModel):
    """
    Represents a tradable financial instrument, as a more concise item listing
    only key fields.
    """

    security_id: str
    """The identifier for the instrument"""

    security_id_source: SecurityIDSource
    """The source system for the security identifier"""

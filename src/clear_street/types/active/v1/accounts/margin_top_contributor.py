# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["MarginTopContributor"]


class MarginTopContributor(BaseModel):
    initial_margin_requirement: str
    """Initial margin requirement attributable to this underlying."""

    maintenance_margin_requirement: str
    """Maintenance margin requirement attributable to this underlying."""

    market_value: str
    """Net market value attributable to this underlying."""

    underlying_instrument_id: str
    """UUID of the underlying security contributing to margin requirement."""

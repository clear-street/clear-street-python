# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .currency import Currency
from .fee_type import FeeType
from ...._models import BaseModel
from .charged_by import ChargedBy
from .fee_frequency import FeeFrequency

__all__ = ["SpvFeeTermResource"]


class SpvFeeTermResource(BaseModel):
    """One typed SPV fee term."""

    charged_by: ChargedBy
    """Charging party."""

    currency: Currency
    """Terms currency."""

    description: str
    """Plain-text fee disclosure."""

    fee_type: FeeType
    """Fee kind."""

    frequency: FeeFrequency
    """Timing/cadence."""

    amount: Optional[str] = None
    """Exact fixed amount, when amount-based."""

    duration_years: Optional[str] = None
    """Charge duration in years, when specified."""

    hurdle_rate: Optional[str] = None
    """Carry hurdle as a decimal fraction, when specified."""

    rate: Optional[str] = None
    """Decimal fraction between zero and one, when percentage-based."""

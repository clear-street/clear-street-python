# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PredictionMarketBalances"]


class PredictionMarketBalances(BaseModel):
    """Prediction-market buying power in the same currency as the account balances."""

    buying_power: str
    """
    Unlevered prediction-market buying power from the shared cash pool, after order
    and withdrawal holds. This draws on the same funds as Securities buying power;
    the two values must not be added together.
    """

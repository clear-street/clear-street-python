# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .urgency import Urgency
from ...._utils import PropertyInfo

__all__ = ["BaseStrategyParamsParam"]


class BaseStrategyParamsParam(TypedDict, total=False):
    """Base parameters common to most algorithmic strategies"""

    end_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """UTC timestamp to end execution (defaults to market close)"""

    start_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """UTC timestamp to start execution (defaults to order placement time)"""

    urgency: Urgency
    """Urgency level for execution aggressiveness"""

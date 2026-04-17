# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["NavigateAction"]


class NavigateAction(BaseModel):
    """Action to navigate to a client route."""

    route: str
    """Route path or key"""

    params: Optional[object] = None
    """Route parameters"""

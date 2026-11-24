# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .ui_payload import UiPayload

__all__ = ["ContentPartUiPayload"]


class ContentPartUiPayload(BaseModel):
    """Model-composed UI content part.

    Present only when the turn declared `RENDER_UI`.
    """

    payload: UiPayload
    """Model-composed UI, built only from Omni's built-in component catalog."""

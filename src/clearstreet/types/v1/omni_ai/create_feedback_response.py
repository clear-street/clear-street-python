# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CreateFeedbackResponse"]


class CreateFeedbackResponse(BaseModel):
    created_at: str

    feedback_id: Optional[str] = None
    """
    When a null/undefined value is observed, it indicates that there is no available
    data.
    """

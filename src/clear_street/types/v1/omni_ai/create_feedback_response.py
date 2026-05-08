# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CreateFeedbackResponse"]


class CreateFeedbackResponse(BaseModel):
    created_at: str

    feedback_id: Optional[str] = None

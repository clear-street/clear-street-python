# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .prompt_status import PromptStatus

__all__ = ["RunPromptResponse"]


class RunPromptResponse(BaseModel):
    request_id: str

    response: str

    status: PromptStatus

    error: Optional[str] = None

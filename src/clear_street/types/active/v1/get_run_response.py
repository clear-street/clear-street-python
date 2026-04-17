# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .run import Run
from ...._models import BaseModel

__all__ = ["GetRunResponse"]


class GetRunResponse(BaseModel):
    events: List[object]

    run: Run

    next_page_token: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .thread import Thread
from ...._models import BaseModel

__all__ = ["ListThreadsResponse"]


class ListThreadsResponse(BaseModel):
    threads: List[Thread]

    next_page_token: Optional[str] = None

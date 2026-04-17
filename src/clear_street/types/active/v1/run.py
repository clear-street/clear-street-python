# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .capability import Capability
from .run_status import RunStatus

__all__ = ["Run"]


class Run(BaseModel):
    created_at: str

    status: RunStatus

    id: Optional[str] = None

    capabilities: Optional[List[Capability]] = None

    ended_at: Optional[str] = None

    error: Optional[object] = None

    started_at: Optional[str] = None

    thread_id: Optional[str] = None

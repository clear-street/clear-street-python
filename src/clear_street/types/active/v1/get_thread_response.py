# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .thread import Thread
from ...._models import BaseModel

__all__ = ["GetThreadResponse"]


class GetThreadResponse(BaseModel):
    thread: Thread

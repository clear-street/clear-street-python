# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .run import Run
from .thread import Thread
from .message import Message
from ...._models import BaseModel

__all__ = ["StartRunResponse"]


class StartRunResponse(BaseModel):
    run: Run

    thread: Thread

    user_message: Message

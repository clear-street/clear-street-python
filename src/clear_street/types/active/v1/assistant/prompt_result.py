# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ....._models import BaseModel
from .prompt_status import PromptStatus

__all__ = ["PromptResult", "Outputs"]


class Outputs(BaseModel):
    is_output_node: bool

    status: str

    display_value: Optional[object] = None

    error_message: Optional[str] = None

    raw_error_message: Optional[object] = None

    value: Optional[object] = None


class PromptResult(BaseModel):
    prompt_id: str

    response: str

    status: PromptStatus

    error: Optional[str] = None

    outputs: Optional[Dict[str, Outputs]] = None

    raw: Optional[object] = None

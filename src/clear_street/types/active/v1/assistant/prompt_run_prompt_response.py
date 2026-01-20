# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .run_prompt_response import RunPromptResponse
from ....shared.base_response import BaseResponse

__all__ = ["PromptRunPromptResponse"]


class PromptRunPromptResponse(BaseResponse):
    data: RunPromptResponse

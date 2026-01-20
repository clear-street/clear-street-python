# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .prompt_result import PromptResult
from ....shared.base_response import BaseResponse

__all__ = ["PromptGetPromptResultResponse"]


class PromptGetPromptResultResponse(BaseResponse):
    data: PromptResult

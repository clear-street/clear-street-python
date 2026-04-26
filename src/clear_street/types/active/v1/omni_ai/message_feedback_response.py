# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....shared.base_response import BaseResponse
from ..create_feedback_response import CreateFeedbackResponse

__all__ = ["MessageFeedbackResponse"]


class MessageFeedbackResponse(BaseResponse):
    data: CreateFeedbackResponse

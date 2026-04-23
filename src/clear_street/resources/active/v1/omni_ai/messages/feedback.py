# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.active.v1.omni_ai.messages import feedback_create_feedback_params
from ......types.active.v1.omni_ai.messages.feedback_create_feedback_response import FeedbackCreateFeedbackResponse

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def create_feedback(
        self,
        message_id: str,
        *,
        account_id: int,
        score: int,
        comment: str | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedbackCreateFeedbackResponse:
        """
        Create feedback on a finalized assistant message.

        Attaches a score and optional comment to a finalized assistant message. Feedback
        is only valid for messages with role `ASSISTANT` that have reached a terminal
        outcome.

        Args:
          account_id: Account ID for the request

          score: Feedback score (-1, 0, +1 or 1-5)

          comment: Optional feedback comment

          metadata: Optional metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/active/v1/omni-ai/messages/{message_id}/feedback", message_id=message_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "score": score,
                    "comment": comment,
                    "metadata": metadata,
                },
                feedback_create_feedback_params.FeedbackCreateFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateFeedbackResponse,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def create_feedback(
        self,
        message_id: str,
        *,
        account_id: int,
        score: int,
        comment: str | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedbackCreateFeedbackResponse:
        """
        Create feedback on a finalized assistant message.

        Attaches a score and optional comment to a finalized assistant message. Feedback
        is only valid for messages with role `ASSISTANT` that have reached a terminal
        outcome.

        Args:
          account_id: Account ID for the request

          score: Feedback score (-1, 0, +1 or 1-5)

          comment: Optional feedback comment

          metadata: Optional metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/active/v1/omni-ai/messages/{message_id}/feedback", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "score": score,
                    "comment": comment,
                    "metadata": metadata,
                },
                feedback_create_feedback_params.FeedbackCreateFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateFeedbackResponse,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create_feedback = to_raw_response_wrapper(
            feedback.create_feedback,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create_feedback = async_to_raw_response_wrapper(
            feedback.create_feedback,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create_feedback = to_streamed_response_wrapper(
            feedback.create_feedback,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create_feedback = async_to_streamed_response_wrapper(
            feedback.create_feedback,
        )

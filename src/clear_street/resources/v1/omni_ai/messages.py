# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.omni_ai import message_feedback_params, message_get_message_params
from ....types.v1.omni_ai.message_feedback_response import MessageFeedbackResponse
from ....types.v1.omni_ai.message_get_message_response import MessageGetMessageResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def feedback(
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
    ) -> MessageFeedbackResponse:
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
            path_template("/v1/omni-ai/messages/{message_id}/feedback", message_id=message_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "score": score,
                    "comment": comment,
                    "metadata": metadata,
                },
                message_feedback_params.MessageFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageFeedbackResponse,
        )

    def get_message(
        self,
        message_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetMessageResponse:
        """Get a finalized message by ID.

        Returns a single finalized message.

        Returns **404** if the message belongs to an
        in-progress assistant turn (use the response endpoint for live output). Once the
        turn completes, the message becomes available here.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v1/omni-ai/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, message_get_message_params.MessageGetMessageParams),
            ),
            cast_to=MessageGetMessageResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/message/response endpoints require an explicit account_id. Entitlement endpoints are caller-scoped and use trading_account_ids.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def feedback(
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
    ) -> MessageFeedbackResponse:
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
            path_template("/v1/omni-ai/messages/{message_id}/feedback", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "score": score,
                    "comment": comment,
                    "metadata": metadata,
                },
                message_feedback_params.MessageFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageFeedbackResponse,
        )

    async def get_message(
        self,
        message_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetMessageResponse:
        """Get a finalized message by ID.

        Returns a single finalized message.

        Returns **404** if the message belongs to an
        in-progress assistant turn (use the response endpoint for live output). Once the
        turn completes, the message becomes available here.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v1/omni-ai/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, message_get_message_params.MessageGetMessageParams
                ),
            ),
            cast_to=MessageGetMessageResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.feedback = to_raw_response_wrapper(
            messages.feedback,
        )
        self.get_message = to_raw_response_wrapper(
            messages.get_message,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.feedback = async_to_raw_response_wrapper(
            messages.feedback,
        )
        self.get_message = async_to_raw_response_wrapper(
            messages.get_message,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.feedback = to_streamed_response_wrapper(
            messages.feedback,
        )
        self.get_message = to_streamed_response_wrapper(
            messages.get_message,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.feedback = async_to_streamed_response_wrapper(
            messages.feedback,
        )
        self.get_message = async_to_streamed_response_wrapper(
            messages.get_message,
        )

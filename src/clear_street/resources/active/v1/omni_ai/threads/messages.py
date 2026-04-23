# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
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
from ......types.active.v1.omni_ai.threads import message_list_messages_params, message_create_message_params
from ......types.active.v1.omni_ai.threads.message_list_messages_response import MessageListMessagesResponse
from ......types.active.v1.omni_ai.threads.message_create_message_response import MessageCreateMessageResponse

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

    def create_message(
        self,
        thread_id: str,
        *,
        account_id: int,
        text: str,
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateMessageResponse:
        """
        Continue an existing conversation thread.

        Appends a new user message to the thread and starts an assistant response. Only
        one response may be active per thread at a time — if the previous turn is still
        in progress, this endpoint returns **409 Conflict**. Wait for the active
        response to reach a terminal status before submitting the next turn.

        Poll the returned `response_id` via `GET /omni-ai/responses/{response_id}` for
        assistant output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._post(
            path_template("/active/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                    "capabilities": capabilities,
                },
                message_create_message_params.MessageCreateMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateMessageResponse,
        )

    def list_messages(
        self,
        thread_id: str,
        *,
        account_id: int,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListMessagesResponse:
        """
        List finalized messages in a thread.

        Returns **finalized** messages in chronological order. Messages from in-progress
        assistant turns are excluded — use `GET /omni-ai/threads/{thread_id}/response`
        or `GET /omni-ai/responses/{response_id}` for live output.

        If the last finalized message has role `USER`, an active response likely exists
        and should be polled separately.

        Args:
          account_id: Account ID for the request

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/active/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    message_list_messages_params.MessageListMessagesParams,
                ),
            ),
            cast_to=MessageListMessagesResponse,
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

    async def create_message(
        self,
        thread_id: str,
        *,
        account_id: int,
        text: str,
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER", "OPEN_ENTITLEMENT_CONSENT"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateMessageResponse:
        """
        Continue an existing conversation thread.

        Appends a new user message to the thread and starts an assistant response. Only
        one response may be active per thread at a time — if the previous turn is still
        in progress, this endpoint returns **409 Conflict**. Wait for the active
        response to reach a terminal status before submitting the next turn.

        Poll the returned `response_id` via `GET /omni-ai/responses/{response_id}` for
        assistant output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._post(
            path_template("/active/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "text": text,
                    "capabilities": capabilities,
                },
                message_create_message_params.MessageCreateMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateMessageResponse,
        )

    async def list_messages(
        self,
        thread_id: str,
        *,
        account_id: int,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListMessagesResponse:
        """
        List finalized messages in a thread.

        Returns **finalized** messages in chronological order. Messages from in-progress
        assistant turns are excluded — use `GET /omni-ai/threads/{thread_id}/response`
        or `GET /omni-ai/responses/{response_id}` for live output.

        If the last finalized message has role `USER`, an active response likely exists
        and should be polled separately.

        Args:
          account_id: Account ID for the request

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/active/v1/omni-ai/threads/{thread_id}/messages", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    message_list_messages_params.MessageListMessagesParams,
                ),
            ),
            cast_to=MessageListMessagesResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create_message = to_raw_response_wrapper(
            messages.create_message,
        )
        self.list_messages = to_raw_response_wrapper(
            messages.list_messages,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create_message = async_to_raw_response_wrapper(
            messages.create_message,
        )
        self.list_messages = async_to_raw_response_wrapper(
            messages.list_messages,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create_message = to_streamed_response_wrapper(
            messages.create_message,
        )
        self.list_messages = to_streamed_response_wrapper(
            messages.list_messages,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create_message = async_to_streamed_response_wrapper(
            messages.create_message,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            messages.list_messages,
        )

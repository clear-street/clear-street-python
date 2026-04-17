# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from .response import (
    ResponseResource,
    AsyncResponseResource,
    ResponseResourceWithRawResponse,
    AsyncResponseResourceWithRawResponse,
    ResponseResourceWithStreamingResponse,
    AsyncResponseResourceWithStreamingResponse,
)
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
from ......types.active.v1.omni_ai import (
    thread_get_thread_params,
    thread_list_threads_params,
    thread_create_thread_params,
)
from ......types.active.v1.omni_ai.thread_get_thread_response import ThreadGetThreadResponse
from ......types.active.v1.omni_ai.thread_list_threads_response import ThreadListThreadsResponse
from ......types.active.v1.omni_ai.thread_create_thread_response import ThreadCreateThreadResponse

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
    """

    @cached_property
    def messages(self) -> MessagesResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return MessagesResource(self._client)

    @cached_property
    def response(self) -> ResponseResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return ResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> ThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ThreadsResourceWithStreamingResponse(self)

    def create_thread(
        self,
        *,
        account_id: int,
        type: Literal["instant", "deep_insights"],
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER"]] | Omit = omit,
        target: Optional[thread_create_thread_params.Target] | Omit = omit,
        text: Optional[str] | Omit = omit,
        thesis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadCreateThreadResponse:
        """Atomically creates a new thread and submits the first user turn.

        The response
        contains a `response_id` that should be polled via
        `GET /omni-ai/responses/{response_id}` for assistant output.

        Two creation modes are supported:

        - **instant** — provide `text` with a natural-language prompt.
        - **deep_insights** — provide a `target` ticker and optional `thesis` for
          long-form research.

        Args:
          type: Thread creation mode.

          target: Deep-insights target payload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/active/v1/omni-ai/threads",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "type": type,
                    "capabilities": capabilities,
                    "target": target,
                    "text": text,
                    "thesis": thesis,
                },
                thread_create_thread_params.ThreadCreateThreadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateThreadResponse,
        )

    def get_thread(
        self,
        thread_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadResponse:
        """Returns metadata (title, timestamps) for a single thread.

        Does not include
        messages — use `GET /omni-ai/threads/{thread_id}/messages` for conversation
        history.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/active/v1/omni-ai/threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, thread_get_thread_params.ThreadGetThreadParams),
            ),
            cast_to=ThreadGetThreadResponse,
        )

    def list_threads(
        self,
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
    ) -> ThreadListThreadsResponse:
        """Returns thread metadata ordered by most recently created first.

        Use `page_size`
        and `page_token` for pagination. Thread objects contain only metadata (title,
        timestamps) — use the messages endpoint for conversation history.

        Args:
          account_id: Account ID for the request

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/omni-ai/threads",
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
                    thread_list_threads_params.ThreadListThreadsParams,
                ),
            ),
            cast_to=ThreadListThreadsResponse,
        )


class AsyncThreadsResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
    """

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return AsyncMessagesResource(self._client)

    @cached_property
    def response(self) -> AsyncResponseResource:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return AsyncResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncThreadsResourceWithStreamingResponse(self)

    async def create_thread(
        self,
        *,
        account_id: int,
        type: Literal["instant", "deep_insights"],
        capabilities: List[Literal["PREFILL_ORDER", "OPEN_CHART", "OPEN_SCREENER"]] | Omit = omit,
        target: Optional[thread_create_thread_params.Target] | Omit = omit,
        text: Optional[str] | Omit = omit,
        thesis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadCreateThreadResponse:
        """Atomically creates a new thread and submits the first user turn.

        The response
        contains a `response_id` that should be polled via
        `GET /omni-ai/responses/{response_id}` for assistant output.

        Two creation modes are supported:

        - **instant** — provide `text` with a natural-language prompt.
        - **deep_insights** — provide a `target` ticker and optional `thesis` for
          long-form research.

        Args:
          type: Thread creation mode.

          target: Deep-insights target payload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/active/v1/omni-ai/threads",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "type": type,
                    "capabilities": capabilities,
                    "target": target,
                    "text": text,
                    "thesis": thesis,
                },
                thread_create_thread_params.ThreadCreateThreadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreadCreateThreadResponse,
        )

    async def get_thread(
        self,
        thread_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadResponse:
        """Returns metadata (title, timestamps) for a single thread.

        Does not include
        messages — use `GET /omni-ai/threads/{thread_id}/messages` for conversation
        history.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/active/v1/omni-ai/threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, thread_get_thread_params.ThreadGetThreadParams
                ),
            ),
            cast_to=ThreadGetThreadResponse,
        )

    async def list_threads(
        self,
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
    ) -> ThreadListThreadsResponse:
        """Returns thread metadata ordered by most recently created first.

        Use `page_size`
        and `page_token` for pagination. Thread objects contain only metadata (title,
        timestamps) — use the messages endpoint for conversation history.

        Args:
          account_id: Account ID for the request

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/omni-ai/threads",
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
                    thread_list_threads_params.ThreadListThreadsParams,
                ),
            ),
            cast_to=ThreadListThreadsResponse,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create_thread = to_raw_response_wrapper(
            threads.create_thread,
        )
        self.get_thread = to_raw_response_wrapper(
            threads.get_thread,
        )
        self.list_threads = to_raw_response_wrapper(
            threads.list_threads,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return MessagesResourceWithRawResponse(self._threads.messages)

    @cached_property
    def response(self) -> ResponseResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return ResponseResourceWithRawResponse(self._threads.response)


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create_thread = async_to_raw_response_wrapper(
            threads.create_thread,
        )
        self.get_thread = async_to_raw_response_wrapper(
            threads.get_thread,
        )
        self.list_threads = async_to_raw_response_wrapper(
            threads.list_threads,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return AsyncMessagesResourceWithRawResponse(self._threads.messages)

    @cached_property
    def response(self) -> AsyncResponseResourceWithRawResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return AsyncResponseResourceWithRawResponse(self._threads.response)


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.create_thread = to_streamed_response_wrapper(
            threads.create_thread,
        )
        self.get_thread = to_streamed_response_wrapper(
            threads.get_thread,
        )
        self.list_threads = to_streamed_response_wrapper(
            threads.list_threads,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return MessagesResourceWithStreamingResponse(self._threads.messages)

    @cached_property
    def response(self) -> ResponseResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return ResponseResourceWithStreamingResponse(self._threads.response)


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.create_thread = async_to_streamed_response_wrapper(
            threads.create_thread,
        )
        self.get_thread = async_to_streamed_response_wrapper(
            threads.get_thread,
        )
        self.list_threads = async_to_streamed_response_wrapper(
            threads.list_threads,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return AsyncMessagesResourceWithStreamingResponse(self._threads.messages)

    @cached_property
    def response(self) -> AsyncResponseResourceWithStreamingResponse:
        """Thread-centric AI assistant for conversational trading.

        Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
        """
        return AsyncResponseResourceWithStreamingResponse(self._threads.response)

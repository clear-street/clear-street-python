# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
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
from ......types.active.v1.iris import thread_get_thread_deprecated_params, thread_list_threads_deprecated_params
from ......types.active.v1.iris.thread_get_thread_deprecated_response import ThreadGetThreadDeprecatedResponse
from ......types.active.v1.iris.thread_list_threads_deprecated_response import ThreadListThreadsDeprecatedResponse

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    """Deprecated /iris/* routes. Use /omni-ai/* instead."""

    @cached_property
    def messages(self) -> MessagesResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return MessagesResource(self._client)

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

    @typing_extensions.deprecated("deprecated")
    def get_thread_deprecated(
        self,
        thread_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/threads/{thread_id}` instead.

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
            path_template("/active/v1/iris/threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, thread_get_thread_deprecated_params.ThreadGetThreadDeprecatedParams
                ),
            ),
            cast_to=ThreadGetThreadDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list_threads_deprecated(
        self,
        *,
        account_id: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadListThreadsDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/threads` instead.

        Args:
          account_id: Account ID for the request

          page_size: Maximum threads to return

          page_token: Page token for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/iris/threads",
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
                    thread_list_threads_deprecated_params.ThreadListThreadsDeprecatedParams,
                ),
            ),
            cast_to=ThreadListThreadsDeprecatedResponse,
        )


class AsyncThreadsResource(AsyncAPIResource):
    """Deprecated /iris/* routes. Use /omni-ai/* instead."""

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncMessagesResource(self._client)

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

    @typing_extensions.deprecated("deprecated")
    async def get_thread_deprecated(
        self,
        thread_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadGetThreadDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/threads/{thread_id}` instead.

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
            path_template("/active/v1/iris/threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, thread_get_thread_deprecated_params.ThreadGetThreadDeprecatedParams
                ),
            ),
            cast_to=ThreadGetThreadDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def list_threads_deprecated(
        self,
        *,
        account_id: str,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreadListThreadsDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/threads` instead.

        Args:
          account_id: Account ID for the request

          page_size: Maximum threads to return

          page_token: Page token for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/iris/threads",
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
                    thread_list_threads_deprecated_params.ThreadListThreadsDeprecatedParams,
                ),
            ),
            cast_to=ThreadListThreadsDeprecatedResponse,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.get_thread_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                threads.get_thread_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_threads_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                threads.list_threads_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return MessagesResourceWithRawResponse(self._threads.messages)


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.get_thread_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                threads.get_thread_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_threads_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                threads.list_threads_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncMessagesResourceWithRawResponse(self._threads.messages)


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.get_thread_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                threads.get_thread_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_threads_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                threads.list_threads_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return MessagesResourceWithStreamingResponse(self._threads.messages)


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.get_thread_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                threads.get_thread_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list_threads_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                threads.list_threads_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        """Deprecated /iris/* routes. Use /omni-ai/* instead."""
        return AsyncMessagesResourceWithStreamingResponse(self._threads.messages)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

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
from ......types.active.v1.iris.threads import message_list_messages_deprecated_params
from ......types.active.v1.iris.threads.message_list_messages_deprecated_response import (
    MessageListMessagesDeprecatedResponse,
)

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """Deprecated /iris/* routes. Use /omni-ai/* instead."""

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def list_messages_deprecated(
        self,
        thread_id: str,
        *,
        account_id: str,
        after_seq: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListMessagesDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/threads/{thread_id}/messages` instead.

        Args:
          account_id: Account ID for the request

          after_seq: Return messages after this sequence number

          page_size: Maximum messages to return

          page_token: Page token for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/active/v1/iris/threads/{thread_id}/messages", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after_seq": after_seq,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    message_list_messages_deprecated_params.MessageListMessagesDeprecatedParams,
                ),
            ),
            cast_to=MessageListMessagesDeprecatedResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    """Deprecated /iris/* routes. Use /omni-ai/* instead."""

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def list_messages_deprecated(
        self,
        thread_id: str,
        *,
        account_id: str,
        after_seq: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListMessagesDeprecatedResponse:
        """
        **Deprecated**: Use `GET /omni-ai/threads/{thread_id}/messages` instead.

        Args:
          account_id: Account ID for the request

          after_seq: Return messages after this sequence number

          page_size: Maximum messages to return

          page_token: Page token for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/active/v1/iris/threads/{thread_id}/messages", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "after_seq": after_seq,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    message_list_messages_deprecated_params.MessageListMessagesDeprecatedParams,
                ),
            ),
            cast_to=MessageListMessagesDeprecatedResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list_messages_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                messages.list_messages_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list_messages_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                messages.list_messages_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list_messages_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                messages.list_messages_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list_messages_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                messages.list_messages_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )

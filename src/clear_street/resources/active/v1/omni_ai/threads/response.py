# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Query, Headers, NotGiven, not_given
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
from ......types.active.v1.omni_ai.threads import response_get_thread_response_params
from ......types.active.v1.omni_ai.threads.response_get_thread_response_response import (
    ResponseGetThreadResponseResponse,
)

__all__ = ["ResponseResource", "AsyncResponseResource"]


class ResponseResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
    """

    @cached_property
    def with_raw_response(self) -> ResponseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ResponseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ResponseResourceWithStreamingResponse(self)

    def get_thread_response(
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
    ) -> ResponseGetThreadResponseResponse:
        """
        Get the active response for a thread.

        Convenience endpoint to look up the currently active response for a thread
        without knowing the `response_id`. Useful when reloading a thread whose last
        finalized message is a `USER` message — this indicates an assistant turn is
        likely in progress.

        Returns **404** if no active response exists (the thread is idle).

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
            path_template("/active/v1/omni-ai/threads/{thread_id}/response", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, response_get_thread_response_params.ResponseGetThreadResponseParams
                ),
            ),
            cast_to=ResponseGetThreadResponseResponse,
        )


class AsyncResponseResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResponseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncResponseResourceWithStreamingResponse(self)

    async def get_thread_response(
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
    ) -> ResponseGetThreadResponseResponse:
        """
        Get the active response for a thread.

        Convenience endpoint to look up the currently active response for a thread
        without knowing the `response_id`. Useful when reloading a thread whose last
        finalized message is a `USER` message — this indicates an assistant turn is
        likely in progress.

        Returns **404** if no active response exists (the thread is idle).

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
            path_template("/active/v1/omni-ai/threads/{thread_id}/response", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, response_get_thread_response_params.ResponseGetThreadResponseParams
                ),
            ),
            cast_to=ResponseGetThreadResponseResponse,
        )


class ResponseResourceWithRawResponse:
    def __init__(self, response: ResponseResource) -> None:
        self._response = response

        self.get_thread_response = to_raw_response_wrapper(
            response.get_thread_response,
        )


class AsyncResponseResourceWithRawResponse:
    def __init__(self, response: AsyncResponseResource) -> None:
        self._response = response

        self.get_thread_response = async_to_raw_response_wrapper(
            response.get_thread_response,
        )


class ResponseResourceWithStreamingResponse:
    def __init__(self, response: ResponseResource) -> None:
        self._response = response

        self.get_thread_response = to_streamed_response_wrapper(
            response.get_thread_response,
        )


class AsyncResponseResourceWithStreamingResponse:
    def __init__(self, response: AsyncResponseResource) -> None:
        self._response = response

        self.get_thread_response = async_to_streamed_response_wrapper(
            response.get_thread_response,
        )

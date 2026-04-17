# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active.v1.omni_ai import response_get_response_params, response_cancel_response_params
from .....types.active.v1.omni_ai.response_get_response_response import ResponseGetResponseResponse
from .....types.active.v1.omni_ai.response_cancel_response_response import ResponseCancelResponseResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
    """

    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    def cancel_response(
        self,
        response_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCancelResponseResponse:
        """Requests cancellation of a queued or running response.

        If the response has
        already reached a terminal status, this is an idempotent success. A canceled
        turn still produces a final assistant message with outcome `canceled` in the
        thread history.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._delete(
            path_template("/active/v1/omni-ai/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, response_cancel_response_params.ResponseCancelResponseParams
                ),
            ),
            cast_to=ResponseCancelResponseResponse,
        )

    def get_response(
        self,
        response_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseGetResponseResponse:
        """Returns the current snapshot of an in-progress or completed response.

        While the
        status is `queued` or `running`, the content may be partial and may include
        `thinking` parts. Poll this endpoint periodically until the status reaches a
        terminal value (`succeeded`, `failed`, or `canceled`).

        Once terminal, the finalized assistant message is available in thread history
        via `GET /omni-ai/threads/{thread_id}/messages`.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            path_template("/active/v1/omni-ai/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, response_get_response_params.ResponseGetResponseParams
                ),
            ),
            cast_to=ResponseGetResponseResponse,
        )


class AsyncResponsesResource(AsyncAPIResource):
    """Thread-centric AI assistant for conversational trading.

    Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Every endpoint requires an explicit account_id.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    async def cancel_response(
        self,
        response_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCancelResponseResponse:
        """Requests cancellation of a queued or running response.

        If the response has
        already reached a terminal status, this is an idempotent success. A canceled
        turn still produces a final assistant message with outcome `canceled` in the
        thread history.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._delete(
            path_template("/active/v1/omni-ai/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, response_cancel_response_params.ResponseCancelResponseParams
                ),
            ),
            cast_to=ResponseCancelResponseResponse,
        )

    async def get_response(
        self,
        response_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseGetResponseResponse:
        """Returns the current snapshot of an in-progress or completed response.

        While the
        status is `queued` or `running`, the content may be partial and may include
        `thinking` parts. Poll this endpoint periodically until the status reaches a
        terminal value (`succeeded`, `failed`, or `canceled`).

        Once terminal, the finalized assistant message is available in thread history
        via `GET /omni-ai/threads/{thread_id}/messages`.

        Args:
          account_id: Account ID for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            path_template("/active/v1/omni-ai/responses/{response_id}", response_id=response_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, response_get_response_params.ResponseGetResponseParams
                ),
            ),
            cast_to=ResponseGetResponseResponse,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.cancel_response = to_raw_response_wrapper(
            responses.cancel_response,
        )
        self.get_response = to_raw_response_wrapper(
            responses.get_response,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.cancel_response = async_to_raw_response_wrapper(
            responses.cancel_response,
        )
        self.get_response = async_to_raw_response_wrapper(
            responses.get_response,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.cancel_response = to_streamed_response_wrapper(
            responses.cancel_response,
        )
        self.get_response = to_streamed_response_wrapper(
            responses.get_response,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.cancel_response = async_to_streamed_response_wrapper(
            responses.cancel_response,
        )
        self.get_response = async_to_streamed_response_wrapper(
            responses.get_response,
        )

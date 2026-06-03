# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["WebsocketResource", "AsyncWebsocketResource"]


class WebsocketResource(SyncAPIResource):
    """Active Websocket."""

    @cached_property
    def with_raw_response(self) -> WebsocketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return WebsocketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebsocketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return WebsocketResourceWithStreamingResponse(self)

    def websocket_handler(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Upgrade the HTTP connection to a WebSocket and echo incoming messages."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v1/ws",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWebsocketResource(AsyncAPIResource):
    """Active Websocket."""

    @cached_property
    def with_raw_response(self) -> AsyncWebsocketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebsocketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebsocketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncWebsocketResourceWithStreamingResponse(self)

    async def websocket_handler(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Upgrade the HTTP connection to a WebSocket and echo incoming messages."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v1/ws",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WebsocketResourceWithRawResponse:
    def __init__(self, websocket: WebsocketResource) -> None:
        self._websocket = websocket

        self.websocket_handler = to_raw_response_wrapper(
            websocket.websocket_handler,
        )


class AsyncWebsocketResourceWithRawResponse:
    def __init__(self, websocket: AsyncWebsocketResource) -> None:
        self._websocket = websocket

        self.websocket_handler = async_to_raw_response_wrapper(
            websocket.websocket_handler,
        )


class WebsocketResourceWithStreamingResponse:
    def __init__(self, websocket: WebsocketResource) -> None:
        self._websocket = websocket

        self.websocket_handler = to_streamed_response_wrapper(
            websocket.websocket_handler,
        )


class AsyncWebsocketResourceWithStreamingResponse:
    def __init__(self, websocket: AsyncWebsocketResource) -> None:
        self._websocket = websocket

        self.websocket_handler = async_to_streamed_response_wrapper(
            websocket.websocket_handler,
        )

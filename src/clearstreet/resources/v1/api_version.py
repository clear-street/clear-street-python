# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.api_version_get_version_response import APIVersionGetVersionResponse

__all__ = ["APIVersionResource", "AsyncAPIVersionResource"]


class APIVersionResource(SyncAPIResource):
    """Endpoints for API service metadata."""

    @cached_property
    def with_raw_response(self) -> APIVersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return APIVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIVersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return APIVersionResourceWithStreamingResponse(self)

    def get_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIVersionGetVersionResponse:
        """Returns the current version string for this API endpoint."""
        return self._get(
            "/v1/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIVersionGetVersionResponse,
        )


class AsyncAPIVersionResource(AsyncAPIResource):
    """Endpoints for API service metadata."""

    @cached_property
    def with_raw_response(self) -> AsyncAPIVersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIVersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncAPIVersionResourceWithStreamingResponse(self)

    async def get_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIVersionGetVersionResponse:
        """Returns the current version string for this API endpoint."""
        return await self._get(
            "/v1/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIVersionGetVersionResponse,
        )


class APIVersionResourceWithRawResponse:
    def __init__(self, api_version: APIVersionResource) -> None:
        self._api_version = api_version

        self.get_version = to_raw_response_wrapper(
            api_version.get_version,
        )


class AsyncAPIVersionResourceWithRawResponse:
    def __init__(self, api_version: AsyncAPIVersionResource) -> None:
        self._api_version = api_version

        self.get_version = async_to_raw_response_wrapper(
            api_version.get_version,
        )


class APIVersionResourceWithStreamingResponse:
    def __init__(self, api_version: APIVersionResource) -> None:
        self._api_version = api_version

        self.get_version = to_streamed_response_wrapper(
            api_version.get_version,
        )


class AsyncAPIVersionResourceWithStreamingResponse:
    def __init__(self, api_version: AsyncAPIVersionResource) -> None:
        self._api_version = api_version

        self.get_version = async_to_streamed_response_wrapper(
            api_version.get_version,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ActiveResource", "AsyncActiveResource"]


class ActiveResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """Active Websocket."""
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> ActiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ActiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ActiveResourceWithStreamingResponse(self)


class AsyncActiveResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """Active Websocket."""
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncActiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncActiveResourceWithStreamingResponse(self)


class ActiveResourceWithRawResponse:
    def __init__(self, active: ActiveResource) -> None:
        self._active = active

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """Active Websocket."""
        return V1ResourceWithRawResponse(self._active.v1)


class AsyncActiveResourceWithRawResponse:
    def __init__(self, active: AsyncActiveResource) -> None:
        self._active = active

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """Active Websocket."""
        return AsyncV1ResourceWithRawResponse(self._active.v1)


class ActiveResourceWithStreamingResponse:
    def __init__(self, active: ActiveResource) -> None:
        self._active = active

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """Active Websocket."""
        return V1ResourceWithStreamingResponse(self._active.v1)


class AsyncActiveResourceWithStreamingResponse:
    def __init__(self, active: AsyncActiveResource) -> None:
        self._active = active

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """Active Websocket."""
        return AsyncV1ResourceWithStreamingResponse(self._active.v1)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
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
from .....types.active.v1 import watchlist_create_watchlist_params
from .....types.active.v1.watchlist_get_watchlists_response import WatchlistGetWatchlistsResponse
from .....types.active.v1.watchlist_create_watchlist_response import WatchlistCreateWatchlistResponse
from .....types.active.v1.watchlist_get_watchlist_by_id_response import WatchlistGetWatchlistByIDResponse

__all__ = ["WatchlistsResource", "AsyncWatchlistsResource"]


class WatchlistsResource(SyncAPIResource):
    """Create and manage watchlists."""

    @cached_property
    def items(self) -> ItemsResource:
        """Create and manage watchlists."""
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WatchlistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return WatchlistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchlistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return WatchlistsResourceWithStreamingResponse(self)

    def create_watchlist(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistCreateWatchlistResponse:
        """
        Create Watchlist

        Args:
          name: The desired watchlist name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/active/v1/watchlists",
            body=maybe_transform({"name": name}, watchlist_create_watchlist_params.WatchlistCreateWatchlistParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistCreateWatchlistResponse,
        )

    def delete_watchlist(
        self,
        watchlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a watchlist and all its items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        return self._delete(
            path_template("/active/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_watchlist_by_id(
        self,
        watchlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistGetWatchlistByIDResponse:
        """
        Get a watchlist by ID with all its items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        return self._get(
            path_template("/active/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistGetWatchlistByIDResponse,
        )

    def get_watchlists(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistGetWatchlistsResponse:
        """List watchlists for the authenticated user"""
        return self._get(
            "/active/v1/watchlists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistGetWatchlistsResponse,
        )


class AsyncWatchlistsResource(AsyncAPIResource):
    """Create and manage watchlists."""

    @cached_property
    def items(self) -> AsyncItemsResource:
        """Create and manage watchlists."""
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWatchlistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchlistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchlistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncWatchlistsResourceWithStreamingResponse(self)

    async def create_watchlist(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistCreateWatchlistResponse:
        """
        Create Watchlist

        Args:
          name: The desired watchlist name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/active/v1/watchlists",
            body=await async_maybe_transform(
                {"name": name}, watchlist_create_watchlist_params.WatchlistCreateWatchlistParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistCreateWatchlistResponse,
        )

    async def delete_watchlist(
        self,
        watchlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a watchlist and all its items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        return await self._delete(
            path_template("/active/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_watchlist_by_id(
        self,
        watchlist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistGetWatchlistByIDResponse:
        """
        Get a watchlist by ID with all its items

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        return await self._get(
            path_template("/active/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistGetWatchlistByIDResponse,
        )

    async def get_watchlists(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistGetWatchlistsResponse:
        """List watchlists for the authenticated user"""
        return await self._get(
            "/active/v1/watchlists",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistGetWatchlistsResponse,
        )


class WatchlistsResourceWithRawResponse:
    def __init__(self, watchlists: WatchlistsResource) -> None:
        self._watchlists = watchlists

        self.create_watchlist = to_raw_response_wrapper(
            watchlists.create_watchlist,
        )
        self.delete_watchlist = to_raw_response_wrapper(
            watchlists.delete_watchlist,
        )
        self.get_watchlist_by_id = to_raw_response_wrapper(
            watchlists.get_watchlist_by_id,
        )
        self.get_watchlists = to_raw_response_wrapper(
            watchlists.get_watchlists,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        """Create and manage watchlists."""
        return ItemsResourceWithRawResponse(self._watchlists.items)


class AsyncWatchlistsResourceWithRawResponse:
    def __init__(self, watchlists: AsyncWatchlistsResource) -> None:
        self._watchlists = watchlists

        self.create_watchlist = async_to_raw_response_wrapper(
            watchlists.create_watchlist,
        )
        self.delete_watchlist = async_to_raw_response_wrapper(
            watchlists.delete_watchlist,
        )
        self.get_watchlist_by_id = async_to_raw_response_wrapper(
            watchlists.get_watchlist_by_id,
        )
        self.get_watchlists = async_to_raw_response_wrapper(
            watchlists.get_watchlists,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        """Create and manage watchlists."""
        return AsyncItemsResourceWithRawResponse(self._watchlists.items)


class WatchlistsResourceWithStreamingResponse:
    def __init__(self, watchlists: WatchlistsResource) -> None:
        self._watchlists = watchlists

        self.create_watchlist = to_streamed_response_wrapper(
            watchlists.create_watchlist,
        )
        self.delete_watchlist = to_streamed_response_wrapper(
            watchlists.delete_watchlist,
        )
        self.get_watchlist_by_id = to_streamed_response_wrapper(
            watchlists.get_watchlist_by_id,
        )
        self.get_watchlists = to_streamed_response_wrapper(
            watchlists.get_watchlists,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        """Create and manage watchlists."""
        return ItemsResourceWithStreamingResponse(self._watchlists.items)


class AsyncWatchlistsResourceWithStreamingResponse:
    def __init__(self, watchlists: AsyncWatchlistsResource) -> None:
        self._watchlists = watchlists

        self.create_watchlist = async_to_streamed_response_wrapper(
            watchlists.create_watchlist,
        )
        self.delete_watchlist = async_to_streamed_response_wrapper(
            watchlists.delete_watchlist,
        )
        self.get_watchlist_by_id = async_to_streamed_response_wrapper(
            watchlists.get_watchlist_by_id,
        )
        self.get_watchlists = async_to_streamed_response_wrapper(
            watchlists.get_watchlists,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        """Create and manage watchlists."""
        return AsyncItemsResourceWithStreamingResponse(self._watchlists.items)

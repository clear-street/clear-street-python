# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    InstrumentIDOrSymbol,
    watchlist_get_watchlists_params,
    watchlist_create_watchlist_params,
    watchlist_add_watchlist_item_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ...types.v1.watchlist_get_watchlists_response import WatchlistGetWatchlistsResponse
from ...types.v1.watchlist_create_watchlist_response import WatchlistCreateWatchlistResponse
from ...types.v1.watchlist_delete_watchlist_response import WatchlistDeleteWatchlistResponse
from ...types.v1.watchlist_add_watchlist_item_response import WatchlistAddWatchlistItemResponse
from ...types.v1.watchlist_get_watchlist_by_id_response import WatchlistGetWatchlistByIDResponse
from ...types.v1.watchlist_delete_watchlist_item_response import WatchlistDeleteWatchlistItemResponse

__all__ = ["WatchlistResource", "AsyncWatchlistResource"]


class WatchlistResource(SyncAPIResource):
    """Create and manage watchlists."""

    @cached_property
    def with_raw_response(self) -> WatchlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return WatchlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return WatchlistResourceWithStreamingResponse(self)

    def add_watchlist_item(
        self,
        watchlist_id: str,
        *,
        instrument_id: InstrumentIDOrSymbol,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistAddWatchlistItemResponse:
        """
        Add an instrument to a watchlist

        Args:
          instrument_id: OEMS instrument UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        return self._post(
            path_template("/v1/watchlists/{watchlist_id}/items", watchlist_id=watchlist_id),
            body=maybe_transform(
                {"instrument_id": instrument_id}, watchlist_add_watchlist_item_params.WatchlistAddWatchlistItemParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistAddWatchlistItemResponse,
        )

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
            "/v1/watchlists",
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
    ) -> WatchlistDeleteWatchlistResponse:
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
            path_template("/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistDeleteWatchlistResponse,
        )

    def delete_watchlist_item(
        self,
        item_id: str,
        *,
        watchlist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistDeleteWatchlistItemResponse:
        """
        Delete an instrument from a watchlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._delete(
            path_template("/v1/watchlists/{watchlist_id}/items/{item_id}", watchlist_id=watchlist_id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistDeleteWatchlistItemResponse,
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
            path_template("/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistGetWatchlistByIDResponse,
        )

    def get_watchlists(
        self,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistGetWatchlistsResponse:
        """
        List watchlists for the authenticated user

        Args:
          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/watchlists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    watchlist_get_watchlists_params.WatchlistGetWatchlistsParams,
                ),
            ),
            cast_to=WatchlistGetWatchlistsResponse,
        )


class AsyncWatchlistResource(AsyncAPIResource):
    """Create and manage watchlists."""

    @cached_property
    def with_raw_response(self) -> AsyncWatchlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncWatchlistResourceWithStreamingResponse(self)

    async def add_watchlist_item(
        self,
        watchlist_id: str,
        *,
        instrument_id: InstrumentIDOrSymbol,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistAddWatchlistItemResponse:
        """
        Add an instrument to a watchlist

        Args:
          instrument_id: OEMS instrument UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        return await self._post(
            path_template("/v1/watchlists/{watchlist_id}/items", watchlist_id=watchlist_id),
            body=await async_maybe_transform(
                {"instrument_id": instrument_id}, watchlist_add_watchlist_item_params.WatchlistAddWatchlistItemParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistAddWatchlistItemResponse,
        )

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
            "/v1/watchlists",
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
    ) -> WatchlistDeleteWatchlistResponse:
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
            path_template("/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistDeleteWatchlistResponse,
        )

    async def delete_watchlist_item(
        self,
        item_id: str,
        *,
        watchlist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistDeleteWatchlistItemResponse:
        """
        Delete an instrument from a watchlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not watchlist_id:
            raise ValueError(f"Expected a non-empty value for `watchlist_id` but received {watchlist_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._delete(
            path_template("/v1/watchlists/{watchlist_id}/items/{item_id}", watchlist_id=watchlist_id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistDeleteWatchlistItemResponse,
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
            path_template("/v1/watchlists/{watchlist_id}", watchlist_id=watchlist_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchlistGetWatchlistByIDResponse,
        )

    async def get_watchlists(
        self,
        *,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchlistGetWatchlistsResponse:
        """
        List watchlists for the authenticated user

        Args:
          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/watchlists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    watchlist_get_watchlists_params.WatchlistGetWatchlistsParams,
                ),
            ),
            cast_to=WatchlistGetWatchlistsResponse,
        )


class WatchlistResourceWithRawResponse:
    def __init__(self, watchlist: WatchlistResource) -> None:
        self._watchlist = watchlist

        self.add_watchlist_item = to_raw_response_wrapper(
            watchlist.add_watchlist_item,
        )
        self.create_watchlist = to_raw_response_wrapper(
            watchlist.create_watchlist,
        )
        self.delete_watchlist = to_raw_response_wrapper(
            watchlist.delete_watchlist,
        )
        self.delete_watchlist_item = to_raw_response_wrapper(
            watchlist.delete_watchlist_item,
        )
        self.get_watchlist_by_id = to_raw_response_wrapper(
            watchlist.get_watchlist_by_id,
        )
        self.get_watchlists = to_raw_response_wrapper(
            watchlist.get_watchlists,
        )


class AsyncWatchlistResourceWithRawResponse:
    def __init__(self, watchlist: AsyncWatchlistResource) -> None:
        self._watchlist = watchlist

        self.add_watchlist_item = async_to_raw_response_wrapper(
            watchlist.add_watchlist_item,
        )
        self.create_watchlist = async_to_raw_response_wrapper(
            watchlist.create_watchlist,
        )
        self.delete_watchlist = async_to_raw_response_wrapper(
            watchlist.delete_watchlist,
        )
        self.delete_watchlist_item = async_to_raw_response_wrapper(
            watchlist.delete_watchlist_item,
        )
        self.get_watchlist_by_id = async_to_raw_response_wrapper(
            watchlist.get_watchlist_by_id,
        )
        self.get_watchlists = async_to_raw_response_wrapper(
            watchlist.get_watchlists,
        )


class WatchlistResourceWithStreamingResponse:
    def __init__(self, watchlist: WatchlistResource) -> None:
        self._watchlist = watchlist

        self.add_watchlist_item = to_streamed_response_wrapper(
            watchlist.add_watchlist_item,
        )
        self.create_watchlist = to_streamed_response_wrapper(
            watchlist.create_watchlist,
        )
        self.delete_watchlist = to_streamed_response_wrapper(
            watchlist.delete_watchlist,
        )
        self.delete_watchlist_item = to_streamed_response_wrapper(
            watchlist.delete_watchlist_item,
        )
        self.get_watchlist_by_id = to_streamed_response_wrapper(
            watchlist.get_watchlist_by_id,
        )
        self.get_watchlists = to_streamed_response_wrapper(
            watchlist.get_watchlists,
        )


class AsyncWatchlistResourceWithStreamingResponse:
    def __init__(self, watchlist: AsyncWatchlistResource) -> None:
        self._watchlist = watchlist

        self.add_watchlist_item = async_to_streamed_response_wrapper(
            watchlist.add_watchlist_item,
        )
        self.create_watchlist = async_to_streamed_response_wrapper(
            watchlist.create_watchlist,
        )
        self.delete_watchlist = async_to_streamed_response_wrapper(
            watchlist.delete_watchlist,
        )
        self.delete_watchlist_item = async_to_streamed_response_wrapper(
            watchlist.delete_watchlist_item,
        )
        self.get_watchlist_by_id = async_to_streamed_response_wrapper(
            watchlist.get_watchlist_by_id,
        )
        self.get_watchlists = async_to_streamed_response_wrapper(
            watchlist.get_watchlists,
        )

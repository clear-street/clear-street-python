# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, Base64FileInput, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    screener_create_screener_params,
    screener_search_screener_params,
    screener_replace_screener_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.field_ref_param import FieldRefParam
from ...types.v1.sort_spec_param import SortSpecParam
from ...types.v1.search_filter_param import SearchFilterParam
from ...types.v1.screener_get_screeners_response import ScreenerGetScreenersResponse
from ...types.v1.screener_create_screener_response import ScreenerCreateScreenerResponse
from ...types.v1.screener_search_screener_response import ScreenerSearchScreenerResponse
from ...types.v1.screener_replace_screener_response import ScreenerReplaceScreenerResponse
from ...types.v1.screener_get_screener_by_id_response import ScreenerGetScreenerByIDResponse

__all__ = ["ScreenerResource", "AsyncScreenerResource"]


class ScreenerResource(SyncAPIResource):
    """Search instruments and manage saved screeners."""

    @cached_property
    def with_raw_response(self) -> ScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ScreenerResourceWithStreamingResponse(self)

    def create_screener(
        self,
        *,
        columns: Optional[Iterable[FieldRefParam]] | Omit = omit,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[SearchFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sorts: Optional[Iterable[SortSpecParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerCreateScreenerResponse:
        """
        Create a saved screener configuration.

        Persists a screener configuration for the authenticated user.

        Args:
          columns: Structured field references to include when running this screener

          field_filter: Deprecated: use `columns` instead. Ignored when `columns` is provided.

          filters: Structured search filter criteria

          name: The name for this screener configuration

          sorts: Multi-field sort specifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/saved-screeners",
            body=maybe_transform(
                {
                    "columns": columns,
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sorts": sorts,
                },
                screener_create_screener_params.ScreenerCreateScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerCreateScreenerResponse,
        )

    def delete_screener(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a saved screener configuration.

        Deletes the screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_screener_by_id(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerGetScreenerByIDResponse:
        """
        Get a saved screener configuration by ID.

        Returns a single screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return self._get(
            path_template("/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerGetScreenerByIDResponse,
        )

    def get_screeners(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerGetScreenersResponse:
        """
        List saved screener configurations.

        Returns all screener configurations for the authenticated user.
        """
        return self._get(
            "/v1/saved-screeners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerGetScreenersResponse,
        )

    def replace_screener(
        self,
        screener_id: str,
        *,
        columns: Optional[Iterable[FieldRefParam]] | Omit = omit,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[SearchFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sorts: Optional[Iterable[SortSpecParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerReplaceScreenerResponse:
        """
        Update a saved screener configuration.

        Replaces the screener configuration for the authenticated user. If `name` is
        null, the existing name is preserved.

        Args:
          columns: Structured field references to include when running this screener

          field_filter: Deprecated: use `columns` instead. Ignored when `columns` is provided.

          filters: Structured search filter criteria

          name: The name for this screener configuration

          sorts: Multi-field sort specifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return self._put(
            path_template("/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            body=maybe_transform(
                {
                    "columns": columns,
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sorts": sorts,
                },
                screener_replace_screener_params.ScreenerReplaceScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerReplaceScreenerResponse,
        )

    def search_screener(
        self,
        *,
        columns: Optional[Iterable[FieldRefParam]] | Omit = omit,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[SearchFilterParam]] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Union[str, Base64FileInput, None] | Omit = omit,
        sort_case_sensitive: Optional[bool] | Omit = omit,
        sorts: Optional[Iterable[SortSpecParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerSearchScreenerResponse:
        """
        Search instruments using structured filters.

        Returns a columnar response where each row is an array of column objects. Each
        column contains a human-readable name, a field reference, an optional type hint
        (e.g. `CURR_USD`, `PERCENT`), and the value.

        Use `columns` to select which columns appear in each row. When omitted, the
        default field set is returned.

        Args:
          columns: Subset of fields to include in the response.

          field_filter: Deprecated: use `columns` instead. Ignored when `columns` is provided.

          filters: Filter conditions to apply.

          page_size: The number of items to return per page (only used when page_token is not
              provided)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          sort_case_sensitive: Whether string sorts should be case-sensitive (default: false).

          sorts: Multi-field sort specifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/screener",
            body=maybe_transform(
                {
                    "columns": columns,
                    "field_filter": field_filter,
                    "filters": filters,
                    "page_size": page_size,
                    "page_token": page_token,
                    "sort_case_sensitive": sort_case_sensitive,
                    "sorts": sorts,
                },
                screener_search_screener_params.ScreenerSearchScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerSearchScreenerResponse,
        )


class AsyncScreenerResource(AsyncAPIResource):
    """Search instruments and manage saved screeners."""

    @cached_property
    def with_raw_response(self) -> AsyncScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncScreenerResourceWithStreamingResponse(self)

    async def create_screener(
        self,
        *,
        columns: Optional[Iterable[FieldRefParam]] | Omit = omit,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[SearchFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sorts: Optional[Iterable[SortSpecParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerCreateScreenerResponse:
        """
        Create a saved screener configuration.

        Persists a screener configuration for the authenticated user.

        Args:
          columns: Structured field references to include when running this screener

          field_filter: Deprecated: use `columns` instead. Ignored when `columns` is provided.

          filters: Structured search filter criteria

          name: The name for this screener configuration

          sorts: Multi-field sort specifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/saved-screeners",
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sorts": sorts,
                },
                screener_create_screener_params.ScreenerCreateScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerCreateScreenerResponse,
        )

    async def delete_screener(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a saved screener configuration.

        Deletes the screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_screener_by_id(
        self,
        screener_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerGetScreenerByIDResponse:
        """
        Get a saved screener configuration by ID.

        Returns a single screener configuration for the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return await self._get(
            path_template("/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerGetScreenerByIDResponse,
        )

    async def get_screeners(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerGetScreenersResponse:
        """
        List saved screener configurations.

        Returns all screener configurations for the authenticated user.
        """
        return await self._get(
            "/v1/saved-screeners",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerGetScreenersResponse,
        )

    async def replace_screener(
        self,
        screener_id: str,
        *,
        columns: Optional[Iterable[FieldRefParam]] | Omit = omit,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[SearchFilterParam]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sorts: Optional[Iterable[SortSpecParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerReplaceScreenerResponse:
        """
        Update a saved screener configuration.

        Replaces the screener configuration for the authenticated user. If `name` is
        null, the existing name is preserved.

        Args:
          columns: Structured field references to include when running this screener

          field_filter: Deprecated: use `columns` instead. Ignored when `columns` is provided.

          filters: Structured search filter criteria

          name: The name for this screener configuration

          sorts: Multi-field sort specifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not screener_id:
            raise ValueError(f"Expected a non-empty value for `screener_id` but received {screener_id!r}")
        return await self._put(
            path_template("/v1/saved-screeners/{screener_id}", screener_id=screener_id),
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "field_filter": field_filter,
                    "filters": filters,
                    "name": name,
                    "sorts": sorts,
                },
                screener_replace_screener_params.ScreenerReplaceScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerReplaceScreenerResponse,
        )

    async def search_screener(
        self,
        *,
        columns: Optional[Iterable[FieldRefParam]] | Omit = omit,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[SearchFilterParam]] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Union[str, Base64FileInput, None] | Omit = omit,
        sort_case_sensitive: Optional[bool] | Omit = omit,
        sorts: Optional[Iterable[SortSpecParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerSearchScreenerResponse:
        """
        Search instruments using structured filters.

        Returns a columnar response where each row is an array of column objects. Each
        column contains a human-readable name, a field reference, an optional type hint
        (e.g. `CURR_USD`, `PERCENT`), and the value.

        Use `columns` to select which columns appear in each row. When omitted, the
        default field set is returned.

        Args:
          columns: Subset of fields to include in the response.

          field_filter: Deprecated: use `columns` instead. Ignored when `columns` is provided.

          filters: Filter conditions to apply.

          page_size: The number of items to return per page (only used when page_token is not
              provided)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          sort_case_sensitive: Whether string sorts should be case-sensitive (default: false).

          sorts: Multi-field sort specifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/screener",
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "field_filter": field_filter,
                    "filters": filters,
                    "page_size": page_size,
                    "page_token": page_token,
                    "sort_case_sensitive": sort_case_sensitive,
                    "sorts": sorts,
                },
                screener_search_screener_params.ScreenerSearchScreenerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenerSearchScreenerResponse,
        )


class ScreenerResourceWithRawResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.create_screener = to_raw_response_wrapper(
            screener.create_screener,
        )
        self.delete_screener = to_raw_response_wrapper(
            screener.delete_screener,
        )
        self.get_screener_by_id = to_raw_response_wrapper(
            screener.get_screener_by_id,
        )
        self.get_screeners = to_raw_response_wrapper(
            screener.get_screeners,
        )
        self.replace_screener = to_raw_response_wrapper(
            screener.replace_screener,
        )
        self.search_screener = to_raw_response_wrapper(
            screener.search_screener,
        )


class AsyncScreenerResourceWithRawResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.create_screener = async_to_raw_response_wrapper(
            screener.create_screener,
        )
        self.delete_screener = async_to_raw_response_wrapper(
            screener.delete_screener,
        )
        self.get_screener_by_id = async_to_raw_response_wrapper(
            screener.get_screener_by_id,
        )
        self.get_screeners = async_to_raw_response_wrapper(
            screener.get_screeners,
        )
        self.replace_screener = async_to_raw_response_wrapper(
            screener.replace_screener,
        )
        self.search_screener = async_to_raw_response_wrapper(
            screener.search_screener,
        )


class ScreenerResourceWithStreamingResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.create_screener = to_streamed_response_wrapper(
            screener.create_screener,
        )
        self.delete_screener = to_streamed_response_wrapper(
            screener.delete_screener,
        )
        self.get_screener_by_id = to_streamed_response_wrapper(
            screener.get_screener_by_id,
        )
        self.get_screeners = to_streamed_response_wrapper(
            screener.get_screeners,
        )
        self.replace_screener = to_streamed_response_wrapper(
            screener.replace_screener,
        )
        self.search_screener = to_streamed_response_wrapper(
            screener.search_screener,
        )


class AsyncScreenerResourceWithStreamingResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.create_screener = async_to_streamed_response_wrapper(
            screener.create_screener,
        )
        self.delete_screener = async_to_streamed_response_wrapper(
            screener.delete_screener,
        )
        self.get_screener_by_id = async_to_streamed_response_wrapper(
            screener.get_screener_by_id,
        )
        self.get_screeners = async_to_streamed_response_wrapper(
            screener.get_screeners,
        )
        self.replace_screener = async_to_streamed_response_wrapper(
            screener.replace_screener,
        )
        self.search_screener = async_to_streamed_response_wrapper(
            screener.search_screener,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    Base64FileInput,
    omit,
    not_given,
)
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.active.v1 import screener_get_screener_params, screener_search_screener_params
from ....types.active.v1.field_ref_param import FieldRefParam
from ....types.active.v1.screener_get_screener_response import ScreenerGetScreenerResponse
from ....types.active.v1.screener_search_screener_response import ScreenerSearchScreenerResponse

__all__ = ["ScreenerResource", "AsyncScreenerResource"]


class ScreenerResource(SyncAPIResource):
    """Search and manage saved screeners."""

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

    def get_screener(
        self,
        *,
        field_filter: SequenceNotStr[str] | Omit = omit,
        filter: Dict[str, str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        sort_by: str | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerGetScreenerResponse:
        """
        Screen instruments.

        Searches for instruments matching specified criteria.

        Args:
          field_filter: Comma-separated list of field names to include in the response

          filter: Dynamic filters with dot notation (e.g., filter[price.gte]=50,
              filter[symbol.bw]=A)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          sort_by: Field to sort by

          sort_direction: Sort direction (ASC or DESC, defaults to DESC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "field_filter": field_filter,
                        "filter": filter,
                        "page_size": page_size,
                        "page_token": page_token,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    screener_get_screener_params.ScreenerGetScreenerParams,
                ),
            ),
            cast_to=ScreenerGetScreenerResponse,
        )

    def search_screener(
        self,
        *,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[screener_search_screener_params.Filter]] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        sort_by: Optional[FieldRefParam] | Omit = omit,
        sort_case_sensitive: Optional[bool] | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        sorts: Optional[Iterable[screener_search_screener_params.Sort]] | Omit = omit,
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

        Use `field_filter` to select which columns appear in each row. When omitted, the
        default field set is returned.

        Args:
          field_filter: Subset of fields to include in the response.

          filters: Filter conditions to apply.

          page_size: Maximum number of results per page.

          page_token: Opaque token for cursor-based pagination.

          sort_by: Field to sort results by.

          sort_case_sensitive: Whether string sorts should be case-sensitive (default: false).

          sort_direction: Sort direction (defaults to DESC).

          sorts: Multi-field sort specifications. When present, takes precedence over
              sort_by/sort_direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/active/v1/screener",
            body=maybe_transform(
                {
                    "field_filter": field_filter,
                    "filters": filters,
                    "page_size": page_size,
                    "page_token": page_token,
                    "sort_by": sort_by,
                    "sort_case_sensitive": sort_case_sensitive,
                    "sort_direction": sort_direction,
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
    """Search and manage saved screeners."""

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

    async def get_screener(
        self,
        *,
        field_filter: SequenceNotStr[str] | Omit = omit,
        filter: Dict[str, str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        sort_by: str | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScreenerGetScreenerResponse:
        """
        Screen instruments.

        Searches for instruments matching specified criteria.

        Args:
          field_filter: Comma-separated list of field names to include in the response

          filter: Dynamic filters with dot notation (e.g., filter[price.gte]=50,
              filter[symbol.bw]=A)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          sort_by: Field to sort by

          sort_direction: Sort direction (ASC or DESC, defaults to DESC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "field_filter": field_filter,
                        "filter": filter,
                        "page_size": page_size,
                        "page_token": page_token,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                    },
                    screener_get_screener_params.ScreenerGetScreenerParams,
                ),
            ),
            cast_to=ScreenerGetScreenerResponse,
        )

    async def search_screener(
        self,
        *,
        field_filter: Optional[Iterable[FieldRefParam]] | Omit = omit,
        filters: Optional[Iterable[screener_search_screener_params.Filter]] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        sort_by: Optional[FieldRefParam] | Omit = omit,
        sort_case_sensitive: Optional[bool] | Omit = omit,
        sort_direction: Literal["ASC", "DESC"] | Omit = omit,
        sorts: Optional[Iterable[screener_search_screener_params.Sort]] | Omit = omit,
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

        Use `field_filter` to select which columns appear in each row. When omitted, the
        default field set is returned.

        Args:
          field_filter: Subset of fields to include in the response.

          filters: Filter conditions to apply.

          page_size: Maximum number of results per page.

          page_token: Opaque token for cursor-based pagination.

          sort_by: Field to sort results by.

          sort_case_sensitive: Whether string sorts should be case-sensitive (default: false).

          sort_direction: Sort direction (defaults to DESC).

          sorts: Multi-field sort specifications. When present, takes precedence over
              sort_by/sort_direction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/active/v1/screener",
            body=await async_maybe_transform(
                {
                    "field_filter": field_filter,
                    "filters": filters,
                    "page_size": page_size,
                    "page_token": page_token,
                    "sort_by": sort_by,
                    "sort_case_sensitive": sort_case_sensitive,
                    "sort_direction": sort_direction,
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

        self.get_screener = to_raw_response_wrapper(
            screener.get_screener,
        )
        self.search_screener = to_raw_response_wrapper(
            screener.search_screener,
        )


class AsyncScreenerResourceWithRawResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.get_screener = async_to_raw_response_wrapper(
            screener.get_screener,
        )
        self.search_screener = async_to_raw_response_wrapper(
            screener.search_screener,
        )


class ScreenerResourceWithStreamingResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.get_screener = to_streamed_response_wrapper(
            screener.get_screener,
        )
        self.search_screener = to_streamed_response_wrapper(
            screener.search_screener,
        )


class AsyncScreenerResourceWithStreamingResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.get_screener = async_to_streamed_response_wrapper(
            screener.get_screener,
        )
        self.search_screener = async_to_streamed_response_wrapper(
            screener.search_screener,
        )

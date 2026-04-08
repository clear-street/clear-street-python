# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
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
from ....types.active.v1 import screener_get_screener_params
from ....types.active.v1.screener_get_screener_response import ScreenerGetScreenerResponse

__all__ = ["ScreenerResource", "AsyncScreenerResource"]


class ScreenerResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> ScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
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
        Searches for instruments matching specified criteria.

        Args:
          field_filter: Comma-separated list of field names to include in the response

          filter: Dynamic filters with dot notation (e.g., filter[price.gte]=50,
              filter[symbol.bw]=A)

          page_size: Number of items to return per page (default: 100, max: 10000)

          page_token: Token for retrieving the next page of results. Contains encoded pagination
              state.

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


class AsyncScreenerResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
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
        Searches for instruments matching specified criteria.

        Args:
          field_filter: Comma-separated list of field names to include in the response

          filter: Dynamic filters with dot notation (e.g., filter[price.gte]=50,
              filter[symbol.bw]=A)

          page_size: Number of items to return per page (default: 100, max: 10000)

          page_token: Token for retrieving the next page of results. Contains encoded pagination
              state.

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


class ScreenerResourceWithRawResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.get_screener = to_raw_response_wrapper(
            screener.get_screener,
        )


class AsyncScreenerResourceWithRawResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.get_screener = async_to_raw_response_wrapper(
            screener.get_screener,
        )


class ScreenerResourceWithStreamingResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.get_screener = to_streamed_response_wrapper(
            screener.get_screener,
        )


class AsyncScreenerResourceWithStreamingResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.get_screener = async_to_streamed_response_wrapper(
            screener.get_screener,
        )

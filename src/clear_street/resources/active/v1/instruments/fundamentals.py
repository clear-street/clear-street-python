# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active.v1.instruments.fundamental_get_instrument_fundamentals_response import (
    FundamentalGetInstrumentFundamentalsResponse,
)

__all__ = ["FundamentalsResource", "AsyncFundamentalsResource"]


class FundamentalsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> FundamentalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return FundamentalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FundamentalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return FundamentalsResourceWithStreamingResponse(self)

    def get_instrument_fundamentals(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundamentalGetInstrumentFundamentalsResponse:
        """
        Retrieves supplemental fundamentals and company profile data for an instrument.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/active/v1/instruments/{id}/fundamentals", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundamentalGetInstrumentFundamentalsResponse,
        )


class AsyncFundamentalsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncFundamentalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFundamentalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFundamentalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncFundamentalsResourceWithStreamingResponse(self)

    async def get_instrument_fundamentals(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundamentalGetInstrumentFundamentalsResponse:
        """
        Retrieves supplemental fundamentals and company profile data for an instrument.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/active/v1/instruments/{id}/fundamentals", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundamentalGetInstrumentFundamentalsResponse,
        )


class FundamentalsResourceWithRawResponse:
    def __init__(self, fundamentals: FundamentalsResource) -> None:
        self._fundamentals = fundamentals

        self.get_instrument_fundamentals = to_raw_response_wrapper(
            fundamentals.get_instrument_fundamentals,
        )


class AsyncFundamentalsResourceWithRawResponse:
    def __init__(self, fundamentals: AsyncFundamentalsResource) -> None:
        self._fundamentals = fundamentals

        self.get_instrument_fundamentals = async_to_raw_response_wrapper(
            fundamentals.get_instrument_fundamentals,
        )


class FundamentalsResourceWithStreamingResponse:
    def __init__(self, fundamentals: FundamentalsResource) -> None:
        self._fundamentals = fundamentals

        self.get_instrument_fundamentals = to_streamed_response_wrapper(
            fundamentals.get_instrument_fundamentals,
        )


class AsyncFundamentalsResourceWithStreamingResponse:
    def __init__(self, fundamentals: AsyncFundamentalsResource) -> None:
        self._fundamentals = fundamentals

        self.get_instrument_fundamentals = async_to_streamed_response_wrapper(
            fundamentals.get_instrument_fundamentals,
        )

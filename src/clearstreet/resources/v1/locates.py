# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import InstrumentIDOrSymbol, locate_get_locate_rates_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ...types.v1.locate_get_locate_rates_response import LocateGetLocateRatesResponse
from ...types.v1.locate_get_locate_rate_by_id_response import LocateGetLocateRateByIDResponse

__all__ = ["LocatesResource", "AsyncLocatesResource"]


class LocatesResource(SyncAPIResource):
    """Query locate requests, granted locates, and cached locate borrow rates."""

    @cached_property
    def with_raw_response(self) -> LocatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return LocatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return LocatesResourceWithStreamingResponse(self)

    def get_locate_rate_by_id(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateGetLocateRateByIDResponse:
        """
        > **Beta** — this endpoint may change before general availability.

        Fetch the cached locate borrow rate for one instrument. Rates refresh
        periodically; `404` means no rate is currently cached for the instrument.

        Args:
          instrument_id: Instrument identifier: either an instrument UUID or a symbol (symbol for
              equities, OSI for options). Non-UUID inputs are resolved server-side.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/locates/rates/{instrument_id}", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateGetLocateRateByIDResponse,
        )

    def get_locate_rates(
        self,
        *,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateGetLocateRatesResponse:
        """
        > **Beta** — this endpoint may change before general availability.

        Fetch the cached locate borrow rates for up to 1,000 instruments. The response
        returns one row per requested instrument, in request order. Each row carries
        either the `rate` or an `error` — a `404` when the instrument is unknown or has
        no cached rate. The status is `207` when any row has an error, `200` when every
        instrument resolved to a rate.

        Args:
          instrument_ids: Comma-separated instrument IDs (UUID) or symbols; at least one, at most 1,000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/locates/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"instrument_ids": instrument_ids}, locate_get_locate_rates_params.LocateGetLocateRatesParams
                ),
            ),
            cast_to=LocateGetLocateRatesResponse,
        )


class AsyncLocatesResource(AsyncAPIResource):
    """Query locate requests, granted locates, and cached locate borrow rates."""

    @cached_property
    def with_raw_response(self) -> AsyncLocatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncLocatesResourceWithStreamingResponse(self)

    async def get_locate_rate_by_id(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateGetLocateRateByIDResponse:
        """
        > **Beta** — this endpoint may change before general availability.

        Fetch the cached locate borrow rate for one instrument. Rates refresh
        periodically; `404` means no rate is currently cached for the instrument.

        Args:
          instrument_id: Instrument identifier: either an instrument UUID or a symbol (symbol for
              equities, OSI for options). Non-UUID inputs are resolved server-side.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/locates/rates/{instrument_id}", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateGetLocateRateByIDResponse,
        )

    async def get_locate_rates(
        self,
        *,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocateGetLocateRatesResponse:
        """
        > **Beta** — this endpoint may change before general availability.

        Fetch the cached locate borrow rates for up to 1,000 instruments. The response
        returns one row per requested instrument, in request order. Each row carries
        either the `rate` or an `error` — a `404` when the instrument is unknown or has
        no cached rate. The status is `207` when any row has an error, `200` when every
        instrument resolved to a rate.

        Args:
          instrument_ids: Comma-separated instrument IDs (UUID) or symbols; at least one, at most 1,000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/locates/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"instrument_ids": instrument_ids}, locate_get_locate_rates_params.LocateGetLocateRatesParams
                ),
            ),
            cast_to=LocateGetLocateRatesResponse,
        )


class LocatesResourceWithRawResponse:
    def __init__(self, locates: LocatesResource) -> None:
        self._locates = locates

        self.get_locate_rate_by_id = to_raw_response_wrapper(
            locates.get_locate_rate_by_id,
        )
        self.get_locate_rates = to_raw_response_wrapper(
            locates.get_locate_rates,
        )


class AsyncLocatesResourceWithRawResponse:
    def __init__(self, locates: AsyncLocatesResource) -> None:
        self._locates = locates

        self.get_locate_rate_by_id = async_to_raw_response_wrapper(
            locates.get_locate_rate_by_id,
        )
        self.get_locate_rates = async_to_raw_response_wrapper(
            locates.get_locate_rates,
        )


class LocatesResourceWithStreamingResponse:
    def __init__(self, locates: LocatesResource) -> None:
        self._locates = locates

        self.get_locate_rate_by_id = to_streamed_response_wrapper(
            locates.get_locate_rate_by_id,
        )
        self.get_locate_rates = to_streamed_response_wrapper(
            locates.get_locate_rates,
        )


class AsyncLocatesResourceWithStreamingResponse:
    def __init__(self, locates: AsyncLocatesResource) -> None:
        self._locates = locates

        self.get_locate_rate_by_id = async_to_streamed_response_wrapper(
            locates.get_locate_rate_by_id,
        )
        self.get_locate_rates = async_to_streamed_response_wrapper(
            locates.get_locate_rates,
        )

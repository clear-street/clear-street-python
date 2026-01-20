# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from .news import (
    NewsResource,
    AsyncNewsResource,
    NewsResourceWithRawResponse,
    AsyncNewsResourceWithRawResponse,
    NewsResourceWithStreamingResponse,
    AsyncNewsResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .venues import (
    VenuesResource,
    AsyncVenuesResource,
    VenuesResourceWithRawResponse,
    AsyncVenuesResourceWithRawResponse,
    VenuesResourceWithStreamingResponse,
    AsyncVenuesResourceWithStreamingResponse,
)
from .reporting import (
    ReportingResource,
    AsyncReportingResource,
    ReportingResourceWithRawResponse,
    AsyncReportingResourceWithRawResponse,
    ReportingResourceWithStreamingResponse,
    AsyncReportingResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.active import SecurityType, SecurityIDSource
from .analyst_reporting import (
    AnalystReportingResource,
    AsyncAnalystReportingResource,
    AnalystReportingResourceWithRawResponse,
    AsyncAnalystReportingResourceWithRawResponse,
    AnalystReportingResourceWithStreamingResponse,
    AsyncAnalystReportingResourceWithStreamingResponse,
)
from .....types.active.v1 import instrument_get_instruments_params
from .....types.active.security_type import SecurityType
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instrument_get_instruments_response import InstrumentGetInstrumentsResponse
from .....types.active.v1.instrument_get_instrument_by_id_response import InstrumentGetInstrumentByIDResponse

__all__ = ["InstrumentsResource", "AsyncInstrumentsResource"]


class InstrumentsResource(SyncAPIResource):
    @cached_property
    def analyst_reporting(self) -> AnalystReportingResource:
        return AnalystReportingResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def news(self) -> NewsResource:
        return NewsResource(self._client)

    @cached_property
    def reporting(self) -> ReportingResource:
        return ReportingResource(self._client)

    @cached_property
    def venues(self) -> VenuesResource:
        return VenuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstrumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return InstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstrumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return InstrumentsResourceWithStreamingResponse(self)

    def get_instrument_by_id(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentByIDResponse:
        """
        Retrieves detailed information for a specific instrument.

        Args:
          security_id_source: Security identifier source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not security_id_source:
            raise ValueError(f"Expected a non-empty value for `security_id_source` but received {security_id_source!r}")
        if not security_id:
            raise ValueError(f"Expected a non-empty value for `security_id` but received {security_id!r}")
        return self._get(
            f"/active/v1/instruments/{security_id_source}/{security_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstrumentGetInstrumentByIDResponse,
        )

    def get_instruments(
        self,
        *,
        easy_to_borrow: bool | Omit = omit,
        id_filter: str | Omit = omit,
        is_liquidation_only: bool | Omit = omit,
        is_marginable: bool | Omit = omit,
        is_restricted: bool | Omit = omit,
        is_short_prohibited: bool | Omit = omit,
        is_threshold_security: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        security_type: SecurityType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentsResponse:
        """
        Retrieves a list of tradeable instruments.

        Args:
          easy_to_borrow: Filter by easy to borrow status

          id_filter: Filter IDs to those containing this substring. For options, this is required and
              is used to filter exclusively to the underlying symbol.

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_restricted: Filter by restricted status

          is_short_prohibited: filter by short prohibited status

          is_threshold_security: Filter by threshold security status

          page_size: The number of items to return per page (only used when page_token is not
              provided)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_type: Filter by security type, required and defaults to `COMMON_STOCK`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/instruments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "easy_to_borrow": easy_to_borrow,
                        "id_filter": id_filter,
                        "is_liquidation_only": is_liquidation_only,
                        "is_marginable": is_marginable,
                        "is_restricted": is_restricted,
                        "is_short_prohibited": is_short_prohibited,
                        "is_threshold_security": is_threshold_security,
                        "page_size": page_size,
                        "page_token": page_token,
                        "security_type": security_type,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )


class AsyncInstrumentsResource(AsyncAPIResource):
    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResource:
        return AsyncAnalystReportingResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def news(self) -> AsyncNewsResource:
        return AsyncNewsResource(self._client)

    @cached_property
    def reporting(self) -> AsyncReportingResource:
        return AsyncReportingResource(self._client)

    @cached_property
    def venues(self) -> AsyncVenuesResource:
        return AsyncVenuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstrumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstrumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncInstrumentsResourceWithStreamingResponse(self)

    async def get_instrument_by_id(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentByIDResponse:
        """
        Retrieves detailed information for a specific instrument.

        Args:
          security_id_source: Security identifier source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not security_id_source:
            raise ValueError(f"Expected a non-empty value for `security_id_source` but received {security_id_source!r}")
        if not security_id:
            raise ValueError(f"Expected a non-empty value for `security_id` but received {security_id!r}")
        return await self._get(
            f"/active/v1/instruments/{security_id_source}/{security_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstrumentGetInstrumentByIDResponse,
        )

    async def get_instruments(
        self,
        *,
        easy_to_borrow: bool | Omit = omit,
        id_filter: str | Omit = omit,
        is_liquidation_only: bool | Omit = omit,
        is_marginable: bool | Omit = omit,
        is_restricted: bool | Omit = omit,
        is_short_prohibited: bool | Omit = omit,
        is_threshold_security: bool | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        security_type: SecurityType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstrumentGetInstrumentsResponse:
        """
        Retrieves a list of tradeable instruments.

        Args:
          easy_to_borrow: Filter by easy to borrow status

          id_filter: Filter IDs to those containing this substring. For options, this is required and
              is used to filter exclusively to the underlying symbol.

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_restricted: Filter by restricted status

          is_short_prohibited: filter by short prohibited status

          is_threshold_security: Filter by threshold security status

          page_size: The number of items to return per page (only used when page_token is not
              provided)

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_type: Filter by security type, required and defaults to `COMMON_STOCK`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/instruments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "easy_to_borrow": easy_to_borrow,
                        "id_filter": id_filter,
                        "is_liquidation_only": is_liquidation_only,
                        "is_marginable": is_marginable,
                        "is_restricted": is_restricted,
                        "is_short_prohibited": is_short_prohibited,
                        "is_threshold_security": is_threshold_security,
                        "page_size": page_size,
                        "page_token": page_token,
                        "security_type": security_type,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )


class InstrumentsResourceWithRawResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = to_raw_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = to_raw_response_wrapper(
            instruments.get_instruments,
        )

    @cached_property
    def analyst_reporting(self) -> AnalystReportingResourceWithRawResponse:
        return AnalystReportingResourceWithRawResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._instruments.events)

    @cached_property
    def news(self) -> NewsResourceWithRawResponse:
        return NewsResourceWithRawResponse(self._instruments.news)

    @cached_property
    def reporting(self) -> ReportingResourceWithRawResponse:
        return ReportingResourceWithRawResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> VenuesResourceWithRawResponse:
        return VenuesResourceWithRawResponse(self._instruments.venues)


class AsyncInstrumentsResourceWithRawResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = async_to_raw_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = async_to_raw_response_wrapper(
            instruments.get_instruments,
        )

    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResourceWithRawResponse:
        return AsyncAnalystReportingResourceWithRawResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._instruments.events)

    @cached_property
    def news(self) -> AsyncNewsResourceWithRawResponse:
        return AsyncNewsResourceWithRawResponse(self._instruments.news)

    @cached_property
    def reporting(self) -> AsyncReportingResourceWithRawResponse:
        return AsyncReportingResourceWithRawResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> AsyncVenuesResourceWithRawResponse:
        return AsyncVenuesResourceWithRawResponse(self._instruments.venues)


class InstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: InstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = to_streamed_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = to_streamed_response_wrapper(
            instruments.get_instruments,
        )

    @cached_property
    def analyst_reporting(self) -> AnalystReportingResourceWithStreamingResponse:
        return AnalystReportingResourceWithStreamingResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._instruments.events)

    @cached_property
    def news(self) -> NewsResourceWithStreamingResponse:
        return NewsResourceWithStreamingResponse(self._instruments.news)

    @cached_property
    def reporting(self) -> ReportingResourceWithStreamingResponse:
        return ReportingResourceWithStreamingResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> VenuesResourceWithStreamingResponse:
        return VenuesResourceWithStreamingResponse(self._instruments.venues)


class AsyncInstrumentsResourceWithStreamingResponse:
    def __init__(self, instruments: AsyncInstrumentsResource) -> None:
        self._instruments = instruments

        self.get_instrument_by_id = async_to_streamed_response_wrapper(
            instruments.get_instrument_by_id,
        )
        self.get_instruments = async_to_streamed_response_wrapper(
            instruments.get_instruments,
        )

    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResourceWithStreamingResponse:
        return AsyncAnalystReportingResourceWithStreamingResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._instruments.events)

    @cached_property
    def news(self) -> AsyncNewsResourceWithStreamingResponse:
        return AsyncNewsResourceWithStreamingResponse(self._instruments.news)

    @cached_property
    def reporting(self) -> AsyncReportingResourceWithStreamingResponse:
        return AsyncReportingResourceWithStreamingResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> AsyncVenuesResourceWithStreamingResponse:
        return AsyncVenuesResourceWithStreamingResponse(self._instruments.venues)

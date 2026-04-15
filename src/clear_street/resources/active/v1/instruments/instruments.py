# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

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
from ....._types import (
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
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .options.options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.active import SecurityIDSource
from .analyst_reporting import (
    AnalystReportingResource,
    AsyncAnalystReportingResource,
    AnalystReportingResourceWithRawResponse,
    AsyncAnalystReportingResourceWithRawResponse,
    AnalystReportingResourceWithStreamingResponse,
    AsyncAnalystReportingResourceWithStreamingResponse,
)
from .....types.active.v1 import instrument_get_instruments_params, instrument_get_instrument_by_id_params
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instrument_get_instruments_response import InstrumentGetInstrumentsResponse
from .....types.active.v1.instrument_get_instrument_by_id_response import InstrumentGetInstrumentByIDResponse

__all__ = ["InstrumentsResource", "AsyncInstrumentsResource"]


class InstrumentsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def analyst_reporting(self) -> AnalystReportingResource:
        """Retrieve details and lists of tradable instruments."""
        return AnalystReportingResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        """Retrieve details and lists of tradable instruments."""
        return EventsResource(self._client)

    @cached_property
    def options(self) -> OptionsResource:
        return OptionsResource(self._client)

    @cached_property
    def reporting(self) -> ReportingResource:
        """Retrieve details and lists of tradable instruments."""
        return ReportingResource(self._client)

    @cached_property
    def venues(self) -> VenuesResource:
        """Retrieve details and lists of tradable instruments."""
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
        include_options_expiry_dates: Optional[bool] | Omit = omit,
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

          include_options_expiry_dates: When true, include unique options expiry dates for this instrument

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
            path_template(
                "/active/v1/instruments/{security_id_source}/{security_id}",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_options_expiry_dates": include_options_expiry_dates},
                    instrument_get_instrument_by_id_params.InstrumentGetInstrumentByIDParams,
                ),
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
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        security_type: Literal[
            "COMMON_STOCK", "PREFERRED_STOCK", "CORPORATE_BOND", "OPTION", "FUTURE", "WARRANT", "CASH", "OTHER"
        ]
        | Omit = omit,
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

          id_filter: Filter IDs to those containing this substring. For options, and when
              security_type is omitted and no security_id/security_id_source filters are
              provided, this is required.

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_restricted: Filter by restricted status

          is_short_prohibited: Filter by short prohibited status

          is_threshold_security: Filter by threshold security status

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          security_type: Filter by security type. If omitted, returns all types.

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
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "security_type": security_type,
                    },
                    instrument_get_instruments_params.InstrumentGetInstrumentsParams,
                ),
            ),
            cast_to=InstrumentGetInstrumentsResponse,
        )


class AsyncInstrumentsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def analyst_reporting(self) -> AsyncAnalystReportingResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncAnalystReportingResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncEventsResource(self._client)

    @cached_property
    def options(self) -> AsyncOptionsResource:
        return AsyncOptionsResource(self._client)

    @cached_property
    def reporting(self) -> AsyncReportingResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncReportingResource(self._client)

    @cached_property
    def venues(self) -> AsyncVenuesResource:
        """Retrieve details and lists of tradable instruments."""
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
        include_options_expiry_dates: Optional[bool] | Omit = omit,
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

          include_options_expiry_dates: When true, include unique options expiry dates for this instrument

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
            path_template(
                "/active/v1/instruments/{security_id_source}/{security_id}",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_options_expiry_dates": include_options_expiry_dates},
                    instrument_get_instrument_by_id_params.InstrumentGetInstrumentByIDParams,
                ),
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
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        security_type: Literal[
            "COMMON_STOCK", "PREFERRED_STOCK", "CORPORATE_BOND", "OPTION", "FUTURE", "WARRANT", "CASH", "OTHER"
        ]
        | Omit = omit,
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

          id_filter: Filter IDs to those containing this substring. For options, and when
              security_type is omitted and no security_id/security_id_source filters are
              provided, this is required.

          is_liquidation_only: Filter by liquidation only status

          is_marginable: Filter by marginable status

          is_restricted: Filter by restricted status

          is_short_prohibited: Filter by short prohibited status

          is_threshold_security: Filter by threshold security status

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          security_type: Filter by security type. If omitted, returns all types.

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
                        "security_id": security_id,
                        "security_id_source": security_id_source,
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
        """Retrieve details and lists of tradable instruments."""
        return AnalystReportingResourceWithRawResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return EventsResourceWithRawResponse(self._instruments.events)

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        return OptionsResourceWithRawResponse(self._instruments.options)

    @cached_property
    def reporting(self) -> ReportingResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return ReportingResourceWithRawResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> VenuesResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
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
        """Retrieve details and lists of tradable instruments."""
        return AsyncAnalystReportingResourceWithRawResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncEventsResourceWithRawResponse(self._instruments.events)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        return AsyncOptionsResourceWithRawResponse(self._instruments.options)

    @cached_property
    def reporting(self) -> AsyncReportingResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncReportingResourceWithRawResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> AsyncVenuesResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
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
        """Retrieve details and lists of tradable instruments."""
        return AnalystReportingResourceWithStreamingResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return EventsResourceWithStreamingResponse(self._instruments.events)

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        return OptionsResourceWithStreamingResponse(self._instruments.options)

    @cached_property
    def reporting(self) -> ReportingResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return ReportingResourceWithStreamingResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> VenuesResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
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
        """Retrieve details and lists of tradable instruments."""
        return AsyncAnalystReportingResourceWithStreamingResponse(self._instruments.analyst_reporting)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncEventsResourceWithStreamingResponse(self._instruments.events)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        return AsyncOptionsResourceWithStreamingResponse(self._instruments.options)

    @cached_property
    def reporting(self) -> AsyncReportingResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncReportingResourceWithStreamingResponse(self._instruments.reporting)

    @cached_property
    def venues(self) -> AsyncVenuesResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncVenuesResourceWithStreamingResponse(self._instruments.venues)

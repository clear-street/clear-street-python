# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.active import SecurityIDSource
from .....types.active.v1.instruments import event_get_instrument_events_params, event_get_all_instrument_events_params
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instruments.all_events_event_type import AllEventsEventType
from .....types.active.v1.instruments.event_get_instrument_events_response import EventGetInstrumentEventsResponse
from .....types.active.v1.instruments.event_get_all_instrument_events_response import (
    EventGetAllInstrumentEventsResponse,
)

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def get_all_instrument_events(
        self,
        *,
        event_types: List[AllEventsEventType] | Omit = omit,
        from_date: str | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetAllInstrumentEventsResponse:
        """
        List instrument events across all securities.

        Retrieves all instrument events grouped by date.

        Args:
          event_types:
              Filter by event type(s). Comma-delimited list. Example:
              `event_types=EARNINGS,IPO`.

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          instrument_ids:
              Filter by OEMS instrument ID(s). Comma-delimited list of UUIDs. Example:
              `instrument_ids=550e8400-e29b-41d4-a716-446655440000`.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/instruments/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_types": event_types,
                        "from_date": from_date,
                        "instrument_ids": instrument_ids,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "to_date": to_date,
                    },
                    event_get_all_instrument_events_params.EventGetAllInstrumentEventsParams,
                ),
            ),
            cast_to=EventGetAllInstrumentEventsResponse,
        )

    def get_instrument_events(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetInstrumentEventsResponse:
        """
        Retrieves corporate events (dividends, splits, etc.) for an instrument, grouped
        by event type.

        Date range defaults:

        - `from_date`: today - 365 days
        - `to_date`: today + 60 days

        Args:
          security_id_source: Security identifier source

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

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
                "/active/v1/instruments/{security_id_source}/{security_id}/events",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    event_get_instrument_events_params.EventGetInstrumentEventsParams,
                ),
            ),
            cast_to=EventGetInstrumentEventsResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def get_all_instrument_events(
        self,
        *,
        event_types: List[AllEventsEventType] | Omit = omit,
        from_date: str | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetAllInstrumentEventsResponse:
        """
        List instrument events across all securities.

        Retrieves all instrument events grouped by date.

        Args:
          event_types:
              Filter by event type(s). Comma-delimited list. Example:
              `event_types=EARNINGS,IPO`.

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          instrument_ids:
              Filter by OEMS instrument ID(s). Comma-delimited list of UUIDs. Example:
              `instrument_ids=550e8400-e29b-41d4-a716-446655440000`.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/instruments/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_types": event_types,
                        "from_date": from_date,
                        "instrument_ids": instrument_ids,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "to_date": to_date,
                    },
                    event_get_all_instrument_events_params.EventGetAllInstrumentEventsParams,
                ),
            ),
            cast_to=EventGetAllInstrumentEventsResponse,
        )

    async def get_instrument_events(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        from_date: str | Omit = omit,
        to_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetInstrumentEventsResponse:
        """
        Retrieves corporate events (dividends, splits, etc.) for an instrument, grouped
        by event type.

        Date range defaults:

        - `from_date`: today - 365 days
        - `to_date`: today + 60 days

        Args:
          security_id_source: Security identifier source

          from_date: The start date for the query range, inclusive (YYYY-MM-DD).

          to_date: The end date for the query range, inclusive (YYYY-MM-DD).

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
                "/active/v1/instruments/{security_id_source}/{security_id}/events",
                security_id_source=security_id_source,
                security_id=security_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    event_get_instrument_events_params.EventGetInstrumentEventsParams,
                ),
            ),
            cast_to=EventGetInstrumentEventsResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get_all_instrument_events = to_raw_response_wrapper(
            events.get_all_instrument_events,
        )
        self.get_instrument_events = to_raw_response_wrapper(
            events.get_instrument_events,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get_all_instrument_events = async_to_raw_response_wrapper(
            events.get_all_instrument_events,
        )
        self.get_instrument_events = async_to_raw_response_wrapper(
            events.get_instrument_events,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get_all_instrument_events = to_streamed_response_wrapper(
            events.get_all_instrument_events,
        )
        self.get_instrument_events = to_streamed_response_wrapper(
            events.get_instrument_events,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get_all_instrument_events = async_to_streamed_response_wrapper(
            events.get_all_instrument_events,
        )
        self.get_instrument_events = async_to_streamed_response_wrapper(
            events.get_instrument_events,
        )

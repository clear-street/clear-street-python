# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
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
from .....types.active import SecurityIDSource
from .....types.active.v1.instruments import event_get_instrument_events_params
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instruments.event_get_instrument_events_response import EventGetInstrumentEventsResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def get_instrument_events(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        from_date: str,
        to_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetInstrumentEventsResponse:
        """
        Retrieves corporate events (dividends, splits, etc.) for an instrument.

        Args:
          security_id_source: Security identifier source

          from_date: The start date for the query range, inclusive (YYYY-MM-DD)

          to_date: The end date for the query range, inclusive (YYYY-MM-DD)

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
            f"/active/v1/instruments/{security_id_source}/{security_id}/events",
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
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def get_instrument_events(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        from_date: str,
        to_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetInstrumentEventsResponse:
        """
        Retrieves corporate events (dividends, splits, etc.) for an instrument.

        Args:
          security_id_source: Security identifier source

          from_date: The start date for the query range, inclusive (YYYY-MM-DD)

          to_date: The end date for the query range, inclusive (YYYY-MM-DD)

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
            f"/active/v1/instruments/{security_id_source}/{security_id}/events",
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

        self.get_instrument_events = to_raw_response_wrapper(
            events.get_instrument_events,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get_instrument_events = async_to_raw_response_wrapper(
            events.get_instrument_events,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get_instrument_events = to_streamed_response_wrapper(
            events.get_instrument_events,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get_instrument_events = async_to_streamed_response_wrapper(
            events.get_instrument_events,
        )

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
from .....types.active.v1.instruments import analyst_reporting_get_instrument_analyst_consensus_params
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instruments.analyst_reporting_get_instrument_analyst_consensus_response import (
    AnalystReportingGetInstrumentAnalystConsensusResponse,
)

__all__ = ["AnalystReportingResource", "AsyncAnalystReportingResource"]


class AnalystReportingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalystReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AnalystReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalystReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AnalystReportingResourceWithStreamingResponse(self)

    def get_instrument_analyst_consensus(
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
    ) -> AnalystReportingGetInstrumentAnalystConsensusResponse:
        """
        Retrieves analyst ratings and price targets for an instrument.

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
            f"/active/v1/instruments/{security_id_source}/{security_id}/analyst-reporting",
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
                    analyst_reporting_get_instrument_analyst_consensus_params.AnalystReportingGetInstrumentAnalystConsensusParams,
                ),
            ),
            cast_to=AnalystReportingGetInstrumentAnalystConsensusResponse,
        )


class AsyncAnalystReportingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalystReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalystReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalystReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncAnalystReportingResourceWithStreamingResponse(self)

    async def get_instrument_analyst_consensus(
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
    ) -> AnalystReportingGetInstrumentAnalystConsensusResponse:
        """
        Retrieves analyst ratings and price targets for an instrument.

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
            f"/active/v1/instruments/{security_id_source}/{security_id}/analyst-reporting",
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
                    analyst_reporting_get_instrument_analyst_consensus_params.AnalystReportingGetInstrumentAnalystConsensusParams,
                ),
            ),
            cast_to=AnalystReportingGetInstrumentAnalystConsensusResponse,
        )


class AnalystReportingResourceWithRawResponse:
    def __init__(self, analyst_reporting: AnalystReportingResource) -> None:
        self._analyst_reporting = analyst_reporting

        self.get_instrument_analyst_consensus = to_raw_response_wrapper(
            analyst_reporting.get_instrument_analyst_consensus,
        )


class AsyncAnalystReportingResourceWithRawResponse:
    def __init__(self, analyst_reporting: AsyncAnalystReportingResource) -> None:
        self._analyst_reporting = analyst_reporting

        self.get_instrument_analyst_consensus = async_to_raw_response_wrapper(
            analyst_reporting.get_instrument_analyst_consensus,
        )


class AnalystReportingResourceWithStreamingResponse:
    def __init__(self, analyst_reporting: AnalystReportingResource) -> None:
        self._analyst_reporting = analyst_reporting

        self.get_instrument_analyst_consensus = to_streamed_response_wrapper(
            analyst_reporting.get_instrument_analyst_consensus,
        )


class AsyncAnalystReportingResourceWithStreamingResponse:
    def __init__(self, analyst_reporting: AsyncAnalystReportingResource) -> None:
        self._analyst_reporting = analyst_reporting

        self.get_instrument_analyst_consensus = async_to_streamed_response_wrapper(
            analyst_reporting.get_instrument_analyst_consensus,
        )

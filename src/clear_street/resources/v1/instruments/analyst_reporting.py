# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.accounts import InstrumentIDOrSymbol
from ....types.v1.instruments import analyst_reporting_get_instrument_analyst_consensus_params
from ....types.v1.accounts.instrument_id_or_symbol import InstrumentIDOrSymbol
from ....types.v1.instruments.analyst_reporting_get_instrument_analyst_consensus_response import (
    AnalystReportingGetInstrumentAnalystConsensusResponse,
)

__all__ = ["AnalystReportingResource", "AsyncAnalystReportingResource"]


class AnalystReportingResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AnalystReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AnalystReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalystReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AnalystReportingResourceWithStreamingResponse(self)

    def get_instrument_analyst_consensus(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
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
          instrument_id: OEMS instrument UUID

          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return self._get(
            path_template("/v1/instruments/{instrument_id}/analyst-reporting", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    analyst_reporting_get_instrument_analyst_consensus_params.AnalystReportingGetInstrumentAnalystConsensusParams,
                ),
            ),
            cast_to=AnalystReportingGetInstrumentAnalystConsensusResponse,
        )


class AsyncAnalystReportingResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncAnalystReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalystReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalystReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncAnalystReportingResourceWithStreamingResponse(self)

    async def get_instrument_analyst_consensus(
        self,
        instrument_id: InstrumentIDOrSymbol,
        *,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
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
          instrument_id: OEMS instrument UUID

          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instrument_id:
            raise ValueError(f"Expected a non-empty value for `instrument_id` but received {instrument_id!r}")
        return await self._get(
            path_template("/v1/instruments/{instrument_id}/analyst-reporting", instrument_id=instrument_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
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

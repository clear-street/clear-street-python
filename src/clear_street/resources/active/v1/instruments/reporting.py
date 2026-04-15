# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.active.v1.instruments import reporting_get_instrument_reporting_params
from .....types.active.security_id_source import SecurityIDSource
from .....types.active.v1.instruments.reporting_get_instrument_reporting_response import (
    ReportingGetInstrumentReportingResponse,
)

__all__ = ["ReportingResource", "AsyncReportingResource"]


class ReportingResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> ReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return ReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return ReportingResourceWithStreamingResponse(self)

    def get_instrument_reporting(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportingGetInstrumentReportingResponse:
        """
        Retrieves fundamental and financial reporting data for an instrument.

        Args:
          security_id_source: Security identifier source

          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

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
                "/active/v1/instruments/{security_id_source}/{security_id}/reporting",
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
                        "from_": from_,
                        "to": to,
                    },
                    reporting_get_instrument_reporting_params.ReportingGetInstrumentReportingParams,
                ),
            ),
            cast_to=ReportingGetInstrumentReportingResponse,
        )


class AsyncReportingResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncReportingResourceWithStreamingResponse(self)

    async def get_instrument_reporting(
        self,
        security_id: str,
        *,
        security_id_source: SecurityIDSource,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportingGetInstrumentReportingResponse:
        """
        Retrieves fundamental and financial reporting data for an instrument.

        Args:
          security_id_source: Security identifier source

          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

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
                "/active/v1/instruments/{security_id_source}/{security_id}/reporting",
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
                        "from_": from_,
                        "to": to,
                    },
                    reporting_get_instrument_reporting_params.ReportingGetInstrumentReportingParams,
                ),
            ),
            cast_to=ReportingGetInstrumentReportingResponse,
        )


class ReportingResourceWithRawResponse:
    def __init__(self, reporting: ReportingResource) -> None:
        self._reporting = reporting

        self.get_instrument_reporting = to_raw_response_wrapper(
            reporting.get_instrument_reporting,
        )


class AsyncReportingResourceWithRawResponse:
    def __init__(self, reporting: AsyncReportingResource) -> None:
        self._reporting = reporting

        self.get_instrument_reporting = async_to_raw_response_wrapper(
            reporting.get_instrument_reporting,
        )


class ReportingResourceWithStreamingResponse:
    def __init__(self, reporting: ReportingResource) -> None:
        self._reporting = reporting

        self.get_instrument_reporting = to_streamed_response_wrapper(
            reporting.get_instrument_reporting,
        )


class AsyncReportingResourceWithStreamingResponse:
    def __init__(self, reporting: AsyncReportingResource) -> None:
        self._reporting = reporting

        self.get_instrument_reporting = async_to_streamed_response_wrapper(
            reporting.get_instrument_reporting,
        )

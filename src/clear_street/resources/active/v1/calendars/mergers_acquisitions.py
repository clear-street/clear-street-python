# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.active.v1.calendars import mergers_acquisition_get_mergers_and_acquisitions_calendar_params
from .....types.active.v1.calendars.mergers_acquisition_get_mergers_and_acquisitions_calendar_response import (
    MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse,
)

__all__ = ["MergersAcquisitionsResource", "AsyncMergersAcquisitionsResource"]


class MergersAcquisitionsResource(SyncAPIResource):
    """Access financial calendars for events like earnings, dividends, and splits."""

    @cached_property
    def with_raw_response(self) -> MergersAcquisitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return MergersAcquisitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MergersAcquisitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return MergersAcquisitionsResourceWithStreamingResponse(self)

    def get_mergers_and_acquisitions_calendar(
        self,
        *,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse:
        """
        Retrieves upcoming M&A events.

        Args:
          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/calendars/mergers-acquisitions",
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
                    mergers_acquisition_get_mergers_and_acquisitions_calendar_params.MergersAcquisitionGetMergersAndAcquisitionsCalendarParams,
                ),
            ),
            cast_to=MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse,
        )


class AsyncMergersAcquisitionsResource(AsyncAPIResource):
    """Access financial calendars for events like earnings, dividends, and splits."""

    @cached_property
    def with_raw_response(self) -> AsyncMergersAcquisitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMergersAcquisitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMergersAcquisitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncMergersAcquisitionsResourceWithStreamingResponse(self)

    async def get_mergers_and_acquisitions_calendar(
        self,
        *,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse:
        """
        Retrieves upcoming M&A events.

        Args:
          from_: The start date for the query range, inclusive (YYYY-MM-DD)

          to: The end date for the query range, inclusive (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/calendars/mergers-acquisitions",
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
                    mergers_acquisition_get_mergers_and_acquisitions_calendar_params.MergersAcquisitionGetMergersAndAcquisitionsCalendarParams,
                ),
            ),
            cast_to=MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse,
        )


class MergersAcquisitionsResourceWithRawResponse:
    def __init__(self, mergers_acquisitions: MergersAcquisitionsResource) -> None:
        self._mergers_acquisitions = mergers_acquisitions

        self.get_mergers_and_acquisitions_calendar = to_raw_response_wrapper(
            mergers_acquisitions.get_mergers_and_acquisitions_calendar,
        )


class AsyncMergersAcquisitionsResourceWithRawResponse:
    def __init__(self, mergers_acquisitions: AsyncMergersAcquisitionsResource) -> None:
        self._mergers_acquisitions = mergers_acquisitions

        self.get_mergers_and_acquisitions_calendar = async_to_raw_response_wrapper(
            mergers_acquisitions.get_mergers_and_acquisitions_calendar,
        )


class MergersAcquisitionsResourceWithStreamingResponse:
    def __init__(self, mergers_acquisitions: MergersAcquisitionsResource) -> None:
        self._mergers_acquisitions = mergers_acquisitions

        self.get_mergers_and_acquisitions_calendar = to_streamed_response_wrapper(
            mergers_acquisitions.get_mergers_and_acquisitions_calendar,
        )


class AsyncMergersAcquisitionsResourceWithStreamingResponse:
    def __init__(self, mergers_acquisitions: AsyncMergersAcquisitionsResource) -> None:
        self._mergers_acquisitions = mergers_acquisitions

        self.get_mergers_and_acquisitions_calendar = async_to_streamed_response_wrapper(
            mergers_acquisitions.get_mergers_and_acquisitions_calendar,
        )

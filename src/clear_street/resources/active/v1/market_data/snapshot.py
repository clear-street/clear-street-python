# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.active.v1.market_data import snapshot_get_snapshots_params
from .....types.active.v1.market_data.snapshot_get_snapshots_response import SnapshotGetSnapshotsResponse

__all__ = ["SnapshotResource", "AsyncSnapshotResource"]


class SnapshotResource(SyncAPIResource):
    """Real-time market data snapshots."""

    @cached_property
    def with_raw_response(self) -> SnapshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return SnapshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return SnapshotResourceWithStreamingResponse(self)

    def get_snapshots(
        self,
        *,
        ids: str | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotGetSnapshotsResponse:
        """
        Get market data snapshots for one or more securities.

        Args:
          ids: Comma-separated OEMS instrument UUIDs.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/market-data/snapshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                    },
                    snapshot_get_snapshots_params.SnapshotGetSnapshotsParams,
                ),
            ),
            cast_to=SnapshotGetSnapshotsResponse,
        )


class AsyncSnapshotResource(AsyncAPIResource):
    """Real-time market data snapshots."""

    @cached_property
    def with_raw_response(self) -> AsyncSnapshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncSnapshotResourceWithStreamingResponse(self)

    async def get_snapshots(
        self,
        *,
        ids: str | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapshotGetSnapshotsResponse:
        """
        Get market data snapshots for one or more securities.

        Args:
          ids: Comma-separated OEMS instrument UUIDs.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/market-data/snapshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                    },
                    snapshot_get_snapshots_params.SnapshotGetSnapshotsParams,
                ),
            ),
            cast_to=SnapshotGetSnapshotsResponse,
        )


class SnapshotResourceWithRawResponse:
    def __init__(self, snapshot: SnapshotResource) -> None:
        self._snapshot = snapshot

        self.get_snapshots = to_raw_response_wrapper(
            snapshot.get_snapshots,
        )


class AsyncSnapshotResourceWithRawResponse:
    def __init__(self, snapshot: AsyncSnapshotResource) -> None:
        self._snapshot = snapshot

        self.get_snapshots = async_to_raw_response_wrapper(
            snapshot.get_snapshots,
        )


class SnapshotResourceWithStreamingResponse:
    def __init__(self, snapshot: SnapshotResource) -> None:
        self._snapshot = snapshot

        self.get_snapshots = to_streamed_response_wrapper(
            snapshot.get_snapshots,
        )


class AsyncSnapshotResourceWithStreamingResponse:
    def __init__(self, snapshot: AsyncSnapshotResource) -> None:
        self._snapshot = snapshot

        self.get_snapshots = async_to_streamed_response_wrapper(
            snapshot.get_snapshots,
        )

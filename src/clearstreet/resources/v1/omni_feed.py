# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import omni_feed_get_feed_params, omni_feed_post_feed_event_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.omni_feed_get_feed_response import OmniFeedGetFeedResponse

__all__ = ["OmniFeedResource", "AsyncOmniFeedResource"]


class OmniFeedResource(SyncAPIResource):
    """
    Personalized feed of market stories: upcoming earnings, dividends, and splits, plus market news. Served per caller in a stable order; item ids double as pagination cursors, so any previously returned page can be re-read.
    """

    @cached_property
    def with_raw_response(self) -> OmniFeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return OmniFeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OmniFeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return OmniFeedResourceWithStreamingResponse(self)

    def get_feed(
        self,
        *,
        account_id: int | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OmniFeedGetFeedResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Returns the caller's personalized feed of market stories: upcoming earnings,
        dividends, and splits, plus market news.

        The feed is a stable, append-only sequence per caller. Without a `cursor`, the
        response resumes from the caller's oldest unseen item and continues forward;
        passing the id of the last item received as `cursor` returns the items after it.
        Either way, when the known sequence runs short of `limit`, fresh stories are
        appended and included. Re-requesting an earlier cursor replays the same items in
        the same order.

        Args:
          account_id: Trading account to serve as context. Optional — the feed works without one.

          cursor: Id of the last item already received; the response continues from the item after
              it. Omit to resume from the oldest unseen item.

          limit: Maximum number of items to return (1–100, default 20).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/omni-ai/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    omni_feed_get_feed_params.OmniFeedGetFeedParams,
                ),
            ),
            cast_to=OmniFeedGetFeedResponse,
        )

    def post_feed_event(
        self,
        *,
        event: omni_feed_post_feed_event_params.Event,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Records one of the caller's interactions with a feed item: the item rendered on
        screen (`seen`), expanded from its headline to its summary (`click`), or voted
        on (`upvote`, `downvote`). Marking an item `seen` excludes it from the caller's
        next feed response.

        Each request records a new event, so a request that is retried after a failure
        of unknown outcome may be recorded twice. That is harmless for `seen` and for
        votes — the first is a yes-or-no exclusion and the latest vote is the one that
        counts — so retry freely for those. The event is wrapped in an `event` field so
        that a future request may carry several at once without breaking this one.

        Args:
          event: The event to record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/omni-ai/feed/events",
            body=maybe_transform({"event": event}, omni_feed_post_feed_event_params.OmniFeedPostFeedEventParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOmniFeedResource(AsyncAPIResource):
    """
    Personalized feed of market stories: upcoming earnings, dividends, and splits, plus market news. Served per caller in a stable order; item ids double as pagination cursors, so any previously returned page can be re-read.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOmniFeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOmniFeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOmniFeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncOmniFeedResourceWithStreamingResponse(self)

    async def get_feed(
        self,
        *,
        account_id: int | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OmniFeedGetFeedResponse:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Returns the caller's personalized feed of market stories: upcoming earnings,
        dividends, and splits, plus market news.

        The feed is a stable, append-only sequence per caller. Without a `cursor`, the
        response resumes from the caller's oldest unseen item and continues forward;
        passing the id of the last item received as `cursor` returns the items after it.
        Either way, when the known sequence runs short of `limit`, fresh stories are
        appended and included. Re-requesting an earlier cursor replays the same items in
        the same order.

        Args:
          account_id: Trading account to serve as context. Optional — the feed works without one.

          cursor: Id of the last item already received; the response continues from the item after
              it. Omit to resume from the oldest unseen item.

          limit: Maximum number of items to return (1–100, default 20).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/omni-ai/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    omni_feed_get_feed_params.OmniFeedGetFeedParams,
                ),
            ),
            cast_to=OmniFeedGetFeedResponse,
        )

    async def post_feed_event(
        self,
        *,
        event: omni_feed_post_feed_event_params.Event,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        > **Alpha** — this endpoint is experimental and may change or be removed at any
        > time.

        Records one of the caller's interactions with a feed item: the item rendered on
        screen (`seen`), expanded from its headline to its summary (`click`), or voted
        on (`upvote`, `downvote`). Marking an item `seen` excludes it from the caller's
        next feed response.

        Each request records a new event, so a request that is retried after a failure
        of unknown outcome may be recorded twice. That is harmless for `seen` and for
        votes — the first is a yes-or-no exclusion and the latest vote is the one that
        counts — so retry freely for those. The event is wrapped in an `event` field so
        that a future request may carry several at once without breaking this one.

        Args:
          event: The event to record.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/omni-ai/feed/events",
            body=await async_maybe_transform(
                {"event": event}, omni_feed_post_feed_event_params.OmniFeedPostFeedEventParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OmniFeedResourceWithRawResponse:
    def __init__(self, omni_feed: OmniFeedResource) -> None:
        self._omni_feed = omni_feed

        self.get_feed = to_raw_response_wrapper(
            omni_feed.get_feed,
        )
        self.post_feed_event = to_raw_response_wrapper(
            omni_feed.post_feed_event,
        )


class AsyncOmniFeedResourceWithRawResponse:
    def __init__(self, omni_feed: AsyncOmniFeedResource) -> None:
        self._omni_feed = omni_feed

        self.get_feed = async_to_raw_response_wrapper(
            omni_feed.get_feed,
        )
        self.post_feed_event = async_to_raw_response_wrapper(
            omni_feed.post_feed_event,
        )


class OmniFeedResourceWithStreamingResponse:
    def __init__(self, omni_feed: OmniFeedResource) -> None:
        self._omni_feed = omni_feed

        self.get_feed = to_streamed_response_wrapper(
            omni_feed.get_feed,
        )
        self.post_feed_event = to_streamed_response_wrapper(
            omni_feed.post_feed_event,
        )


class AsyncOmniFeedResourceWithStreamingResponse:
    def __init__(self, omni_feed: AsyncOmniFeedResource) -> None:
        self._omni_feed = omni_feed

        self.get_feed = async_to_streamed_response_wrapper(
            omni_feed.get_feed,
        )
        self.post_feed_event = async_to_streamed_response_wrapper(
            omni_feed.post_feed_event,
        )

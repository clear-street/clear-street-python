# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ...._types import (
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
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.active.v1 import news_get_news_params
from ....types.active.v1.news_get_news_response import NewsGetNewsResponse

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)

    def get_news(
        self,
        *,
        exclude_publishers: str | Omit = omit,
        from_: str | Omit = omit,
        include_publishers: str | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        news_type: Literal["NEWS", "PRESS_RELEASE"] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        search_query: str | Omit = omit,
        sectors: List[
            Literal[
                "BASIC_MATERIALS",
                "COMMUNICATION_SERVICES",
                "CONSUMER_CYCLICAL",
                "CONSUMER_DEFENSIVE",
                "ENERGY",
                "FINANCIAL_SERVICES",
                "HEALTHCARE",
                "INDUSTRIALS",
                "REAL_ESTATE",
                "TECHNOLOGY",
                "UTILITIES",
            ]
        ]
        | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsGetNewsResponse:
        """
        Retrieves news items with optional filtering by security IDs, time range,
        publisher, type, and text query.

        Args:
          exclude_publishers: Comma-separated list of publishers to exclude (mutually exclusive with
              include_publishers).

          from_: Inclusive start timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime.

          include_publishers: Comma-separated list of publishers to include (mutually exclusive with
              exclude_publishers).

          instrument_ids: Comma-delimited OEMS instrument UUIDs to filter by.

          news_type: Filter by news type.

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          search_query: Free-text query matched against title/text and associated security IDs.

          sectors: Comma-separated sector values to filter by.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          to: Inclusive end timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/active/v1/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_publishers": exclude_publishers,
                        "from_": from_,
                        "include_publishers": include_publishers,
                        "instrument_ids": instrument_ids,
                        "news_type": news_type,
                        "page_size": page_size,
                        "page_token": page_token,
                        "search_query": search_query,
                        "sectors": sectors,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "to": to,
                    },
                    news_get_news_params.NewsGetNewsParams,
                ),
            ),
            cast_to=NewsGetNewsResponse,
        )


class AsyncNewsResource(AsyncAPIResource):
    """Retrieve details and lists of tradable instruments."""

    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)

    async def get_news(
        self,
        *,
        exclude_publishers: str | Omit = omit,
        from_: str | Omit = omit,
        include_publishers: str | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        news_type: Literal["NEWS", "PRESS_RELEASE"] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        search_query: str | Omit = omit,
        sectors: List[
            Literal[
                "BASIC_MATERIALS",
                "COMMUNICATION_SERVICES",
                "CONSUMER_CYCLICAL",
                "CONSUMER_DEFENSIVE",
                "ENERGY",
                "FINANCIAL_SERVICES",
                "HEALTHCARE",
                "INDUSTRIALS",
                "REAL_ESTATE",
                "TECHNOLOGY",
                "UTILITIES",
            ]
        ]
        | Omit = omit,
        security_id: SequenceNotStr[str] | Omit = omit,
        security_id_source: SequenceNotStr[str] | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsGetNewsResponse:
        """
        Retrieves news items with optional filtering by security IDs, time range,
        publisher, type, and text query.

        Args:
          exclude_publishers: Comma-separated list of publishers to exclude (mutually exclusive with
              include_publishers).

          from_: Inclusive start timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime.

          include_publishers: Comma-separated list of publishers to include (mutually exclusive with
              exclude_publishers).

          instrument_ids: Comma-delimited OEMS instrument UUIDs to filter by.

          news_type: Filter by news type.

          page_token: Token for retrieving the next page of results. Contains encoded pagination state
              (limit + offset). When provided, page_size is ignored.

          search_query: Free-text query matched against title/text and associated security IDs.

          sectors: Comma-separated sector values to filter by.

          security_id: Filter by security ID(s). Accepts single value or indexed array.

              Examples:

              - Single: `security_id=037833100`
              - Multiple: `security_id[0]=037833100&security_id[1]=594918104`

          security_id_source: Source(s) for the security ID filter. Must match the count and order of
              security_id.

              Examples:

              - Single: `security_id_source=CUSIP`
              - Multiple: `security_id_source[0]=CUSIP&security_id_source[1]=FIGI`

          to: Inclusive end timestamp. Accepts `YYYY-MM-DD` or RFC3339 datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/active/v1/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_publishers": exclude_publishers,
                        "from_": from_,
                        "include_publishers": include_publishers,
                        "instrument_ids": instrument_ids,
                        "news_type": news_type,
                        "page_size": page_size,
                        "page_token": page_token,
                        "search_query": search_query,
                        "sectors": sectors,
                        "security_id": security_id,
                        "security_id_source": security_id_source,
                        "to": to,
                    },
                    news_get_news_params.NewsGetNewsParams,
                ),
            ),
            cast_to=NewsGetNewsResponse,
        )


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.get_news = to_raw_response_wrapper(
            news.get_news,
        )


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.get_news = async_to_raw_response_wrapper(
            news.get_news,
        )


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.get_news = to_streamed_response_wrapper(
            news.get_news,
        )


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.get_news = async_to_streamed_response_wrapper(
            news.get_news,
        )

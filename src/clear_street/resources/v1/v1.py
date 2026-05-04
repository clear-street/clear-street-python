# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .news import (
    NewsResource,
    AsyncNewsResource,
    NewsResourceWithRawResponse,
    AsyncNewsResourceWithRawResponse,
    NewsResourceWithStreamingResponse,
    AsyncNewsResourceWithStreamingResponse,
)
from .clock import (
    ClockResource,
    AsyncClockResource,
    ClockResourceWithRawResponse,
    AsyncClockResourceWithRawResponse,
    ClockResourceWithStreamingResponse,
    AsyncClockResourceWithStreamingResponse,
)
from .version import (
    VersionResource,
    AsyncVersionResource,
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .screener import (
    ScreenerResource,
    AsyncScreenerResource,
    ScreenerResourceWithRawResponse,
    AsyncScreenerResourceWithRawResponse,
    ScreenerResourceWithStreamingResponse,
    AsyncScreenerResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .omni_ai.omni_ai import (
    OmniAIResource,
    AsyncOmniAIResource,
    OmniAIResourceWithRawResponse,
    AsyncOmniAIResourceWithRawResponse,
    OmniAIResourceWithStreamingResponse,
    AsyncOmniAIResourceWithStreamingResponse,
)
from .saved_screeners import (
    SavedScreenersResource,
    AsyncSavedScreenersResource,
    SavedScreenersResourceWithRawResponse,
    AsyncSavedScreenersResourceWithRawResponse,
    SavedScreenersResourceWithStreamingResponse,
    AsyncSavedScreenersResourceWithStreamingResponse,
)
from .accounts.accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .calendars.calendars import (
    CalendarsResource,
    AsyncCalendarsResource,
    CalendarsResourceWithRawResponse,
    AsyncCalendarsResourceWithRawResponse,
    CalendarsResourceWithStreamingResponse,
    AsyncCalendarsResourceWithStreamingResponse,
)
from .watchlists.watchlists import (
    WatchlistsResource,
    AsyncWatchlistsResource,
    WatchlistsResourceWithRawResponse,
    AsyncWatchlistsResourceWithRawResponse,
    WatchlistsResourceWithStreamingResponse,
    AsyncWatchlistsResourceWithStreamingResponse,
)
from .instruments.instruments import (
    InstrumentsResource,
    AsyncInstrumentsResource,
    InstrumentsResourceWithRawResponse,
    AsyncInstrumentsResourceWithRawResponse,
    InstrumentsResourceWithStreamingResponse,
    AsyncInstrumentsResourceWithStreamingResponse,
)
from .market_data.market_data import (
    MarketDataResource,
    AsyncMarketDataResource,
    MarketDataResourceWithRawResponse,
    AsyncMarketDataResourceWithRawResponse,
    MarketDataResourceWithStreamingResponse,
    AsyncMarketDataResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """Active Websocket."""

    @cached_property
    def accounts(self) -> AccountsResource:
        """Manage trading accounts, balances, and portfolio history."""
        return AccountsResource(self._client)

    @cached_property
    def calendars(self) -> CalendarsResource:
        return CalendarsResource(self._client)

    @cached_property
    def clock(self) -> ClockResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return ClockResource(self._client)

    @cached_property
    def instruments(self) -> InstrumentsResource:
        """Retrieve details and lists of tradable instruments."""
        return InstrumentsResource(self._client)

    @cached_property
    def market_data(self) -> MarketDataResource:
        return MarketDataResource(self._client)

    @cached_property
    def news(self) -> NewsResource:
        """Retrieve market news and related instrument metadata."""
        return NewsResource(self._client)

    @cached_property
    def omni_ai(self) -> OmniAIResource:
        return OmniAIResource(self._client)

    @cached_property
    def saved_screeners(self) -> SavedScreenersResource:
        """Search and manage saved screeners."""
        return SavedScreenersResource(self._client)

    @cached_property
    def screener(self) -> ScreenerResource:
        """Search and manage saved screeners."""
        return ScreenerResource(self._client)

    @cached_property
    def version(self) -> VersionResource:
        """Endpoints for API service metadata."""
        return VersionResource(self._client)

    @cached_property
    def watchlists(self) -> WatchlistsResource:
        """Create and manage watchlists."""
        return WatchlistsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def ws(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Upgrade the HTTP connection to a WebSocket and echo incoming messages."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v1/ws",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV1Resource(AsyncAPIResource):
    """Active Websocket."""

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Manage trading accounts, balances, and portfolio history."""
        return AsyncAccountsResource(self._client)

    @cached_property
    def calendars(self) -> AsyncCalendarsResource:
        return AsyncCalendarsResource(self._client)

    @cached_property
    def clock(self) -> AsyncClockResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncClockResource(self._client)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncInstrumentsResource(self._client)

    @cached_property
    def market_data(self) -> AsyncMarketDataResource:
        return AsyncMarketDataResource(self._client)

    @cached_property
    def news(self) -> AsyncNewsResource:
        """Retrieve market news and related instrument metadata."""
        return AsyncNewsResource(self._client)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResource:
        return AsyncOmniAIResource(self._client)

    @cached_property
    def saved_screeners(self) -> AsyncSavedScreenersResource:
        """Search and manage saved screeners."""
        return AsyncSavedScreenersResource(self._client)

    @cached_property
    def screener(self) -> AsyncScreenerResource:
        """Search and manage saved screeners."""
        return AsyncScreenerResource(self._client)

    @cached_property
    def version(self) -> AsyncVersionResource:
        """Endpoints for API service metadata."""
        return AsyncVersionResource(self._client)

    @cached_property
    def watchlists(self) -> AsyncWatchlistsResource:
        """Create and manage watchlists."""
        return AsyncWatchlistsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def ws(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Upgrade the HTTP connection to a WebSocket and echo incoming messages."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v1/ws",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.ws = to_raw_response_wrapper(
            v1.ws,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def calendars(self) -> CalendarsResourceWithRawResponse:
        return CalendarsResourceWithRawResponse(self._v1.calendars)

    @cached_property
    def clock(self) -> ClockResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return ClockResourceWithRawResponse(self._v1.clock)

    @cached_property
    def instruments(self) -> InstrumentsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return InstrumentsResourceWithRawResponse(self._v1.instruments)

    @cached_property
    def market_data(self) -> MarketDataResourceWithRawResponse:
        return MarketDataResourceWithRawResponse(self._v1.market_data)

    @cached_property
    def news(self) -> NewsResourceWithRawResponse:
        """Retrieve market news and related instrument metadata."""
        return NewsResourceWithRawResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> OmniAIResourceWithRawResponse:
        return OmniAIResourceWithRawResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> SavedScreenersResourceWithRawResponse:
        """Search and manage saved screeners."""
        return SavedScreenersResourceWithRawResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> ScreenerResourceWithRawResponse:
        """Search and manage saved screeners."""
        return ScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        """Endpoints for API service metadata."""
        return VersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> WatchlistsResourceWithRawResponse:
        """Create and manage watchlists."""
        return WatchlistsResourceWithRawResponse(self._v1.watchlists)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.ws = async_to_raw_response_wrapper(
            v1.ws,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def calendars(self) -> AsyncCalendarsResourceWithRawResponse:
        return AsyncCalendarsResourceWithRawResponse(self._v1.calendars)

    @cached_property
    def clock(self) -> AsyncClockResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncClockResourceWithRawResponse(self._v1.clock)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncInstrumentsResourceWithRawResponse(self._v1.instruments)

    @cached_property
    def market_data(self) -> AsyncMarketDataResourceWithRawResponse:
        return AsyncMarketDataResourceWithRawResponse(self._v1.market_data)

    @cached_property
    def news(self) -> AsyncNewsResourceWithRawResponse:
        """Retrieve market news and related instrument metadata."""
        return AsyncNewsResourceWithRawResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResourceWithRawResponse:
        return AsyncOmniAIResourceWithRawResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> AsyncSavedScreenersResourceWithRawResponse:
        """Search and manage saved screeners."""
        return AsyncSavedScreenersResourceWithRawResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithRawResponse:
        """Search and manage saved screeners."""
        return AsyncScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        """Endpoints for API service metadata."""
        return AsyncVersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> AsyncWatchlistsResourceWithRawResponse:
        """Create and manage watchlists."""
        return AsyncWatchlistsResourceWithRawResponse(self._v1.watchlists)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.ws = to_streamed_response_wrapper(
            v1.ws,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def calendars(self) -> CalendarsResourceWithStreamingResponse:
        return CalendarsResourceWithStreamingResponse(self._v1.calendars)

    @cached_property
    def clock(self) -> ClockResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return ClockResourceWithStreamingResponse(self._v1.clock)

    @cached_property
    def instruments(self) -> InstrumentsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return InstrumentsResourceWithStreamingResponse(self._v1.instruments)

    @cached_property
    def market_data(self) -> MarketDataResourceWithStreamingResponse:
        return MarketDataResourceWithStreamingResponse(self._v1.market_data)

    @cached_property
    def news(self) -> NewsResourceWithStreamingResponse:
        """Retrieve market news and related instrument metadata."""
        return NewsResourceWithStreamingResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> OmniAIResourceWithStreamingResponse:
        return OmniAIResourceWithStreamingResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> SavedScreenersResourceWithStreamingResponse:
        """Search and manage saved screeners."""
        return SavedScreenersResourceWithStreamingResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> ScreenerResourceWithStreamingResponse:
        """Search and manage saved screeners."""
        return ScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        """Endpoints for API service metadata."""
        return VersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> WatchlistsResourceWithStreamingResponse:
        """Create and manage watchlists."""
        return WatchlistsResourceWithStreamingResponse(self._v1.watchlists)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.ws = async_to_streamed_response_wrapper(
            v1.ws,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def calendars(self) -> AsyncCalendarsResourceWithStreamingResponse:
        return AsyncCalendarsResourceWithStreamingResponse(self._v1.calendars)

    @cached_property
    def clock(self) -> AsyncClockResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncClockResourceWithStreamingResponse(self._v1.clock)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncInstrumentsResourceWithStreamingResponse(self._v1.instruments)

    @cached_property
    def market_data(self) -> AsyncMarketDataResourceWithStreamingResponse:
        return AsyncMarketDataResourceWithStreamingResponse(self._v1.market_data)

    @cached_property
    def news(self) -> AsyncNewsResourceWithStreamingResponse:
        """Retrieve market news and related instrument metadata."""
        return AsyncNewsResourceWithStreamingResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResourceWithStreamingResponse:
        return AsyncOmniAIResourceWithStreamingResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> AsyncSavedScreenersResourceWithStreamingResponse:
        """Search and manage saved screeners."""
        return AsyncSavedScreenersResourceWithStreamingResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithStreamingResponse:
        """Search and manage saved screeners."""
        return AsyncScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        """Endpoints for API service metadata."""
        return AsyncVersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> AsyncWatchlistsResourceWithStreamingResponse:
        """Create and manage watchlists."""
        return AsyncWatchlistsResourceWithStreamingResponse(self._v1.watchlists)

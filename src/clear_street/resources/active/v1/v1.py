# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ws import (
    WsResource,
    AsyncWsResource,
    WsResourceWithRawResponse,
    AsyncWsResourceWithRawResponse,
    WsResourceWithStreamingResponse,
    AsyncWsResourceWithStreamingResponse,
)
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
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from .screener import (
    ScreenerResource,
    AsyncScreenerResource,
    ScreenerResourceWithRawResponse,
    AsyncScreenerResourceWithRawResponse,
    ScreenerResourceWithStreamingResponse,
    AsyncScreenerResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
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
    @cached_property
    def accounts(self) -> AccountsResource:
        """Manage trading accounts and view balances."""
        return AccountsResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        """Manage API keys for authentication."""
        return APIKeysResource(self._client)

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
        """Retrieve details and lists of tradable instruments."""
        return NewsResource(self._client)

    @cached_property
    def omni_ai(self) -> OmniAIResource:
        return OmniAIResource(self._client)

    @cached_property
    def saved_screeners(self) -> SavedScreenersResource:
        """Retrieve details and lists of tradable instruments."""
        return SavedScreenersResource(self._client)

    @cached_property
    def screener(self) -> ScreenerResource:
        """Retrieve details and lists of tradable instruments."""
        return ScreenerResource(self._client)

    @cached_property
    def version(self) -> VersionResource:
        """Endpoints for API service metadata."""
        return VersionResource(self._client)

    @cached_property
    def watchlists(self) -> WatchlistsResource:
        """Retrieve details and lists of tradable instruments."""
        return WatchlistsResource(self._client)

    @cached_property
    def ws(self) -> WsResource:
        """Active Websocket."""
        return WsResource(self._client)

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


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Manage trading accounts and view balances."""
        return AsyncAccountsResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        """Manage API keys for authentication."""
        return AsyncAPIKeysResource(self._client)

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
        """Retrieve details and lists of tradable instruments."""
        return AsyncNewsResource(self._client)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResource:
        return AsyncOmniAIResource(self._client)

    @cached_property
    def saved_screeners(self) -> AsyncSavedScreenersResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncSavedScreenersResource(self._client)

    @cached_property
    def screener(self) -> AsyncScreenerResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncScreenerResource(self._client)

    @cached_property
    def version(self) -> AsyncVersionResource:
        """Endpoints for API service metadata."""
        return AsyncVersionResource(self._client)

    @cached_property
    def watchlists(self) -> AsyncWatchlistsResource:
        """Retrieve details and lists of tradable instruments."""
        return AsyncWatchlistsResource(self._client)

    @cached_property
    def ws(self) -> AsyncWsResource:
        """Active Websocket."""
        return AsyncWsResource(self._client)

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


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """Manage trading accounts and view balances."""
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        """Manage API keys for authentication."""
        return APIKeysResourceWithRawResponse(self._v1.api_keys)

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
        """Retrieve details and lists of tradable instruments."""
        return NewsResourceWithRawResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> OmniAIResourceWithRawResponse:
        return OmniAIResourceWithRawResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> SavedScreenersResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return SavedScreenersResourceWithRawResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> ScreenerResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return ScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        """Endpoints for API service metadata."""
        return VersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> WatchlistsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return WatchlistsResourceWithRawResponse(self._v1.watchlists)

    @cached_property
    def ws(self) -> WsResourceWithRawResponse:
        """Active Websocket."""
        return WsResourceWithRawResponse(self._v1.ws)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Manage trading accounts and view balances."""
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        """Manage API keys for authentication."""
        return AsyncAPIKeysResourceWithRawResponse(self._v1.api_keys)

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
        """Retrieve details and lists of tradable instruments."""
        return AsyncNewsResourceWithRawResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResourceWithRawResponse:
        return AsyncOmniAIResourceWithRawResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> AsyncSavedScreenersResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncSavedScreenersResourceWithRawResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        """Endpoints for API service metadata."""
        return AsyncVersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> AsyncWatchlistsResourceWithRawResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncWatchlistsResourceWithRawResponse(self._v1.watchlists)

    @cached_property
    def ws(self) -> AsyncWsResourceWithRawResponse:
        """Active Websocket."""
        return AsyncWsResourceWithRawResponse(self._v1.ws)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Manage trading accounts and view balances."""
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        """Manage API keys for authentication."""
        return APIKeysResourceWithStreamingResponse(self._v1.api_keys)

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
        """Retrieve details and lists of tradable instruments."""
        return NewsResourceWithStreamingResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> OmniAIResourceWithStreamingResponse:
        return OmniAIResourceWithStreamingResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> SavedScreenersResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return SavedScreenersResourceWithStreamingResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> ScreenerResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return ScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        """Endpoints for API service metadata."""
        return VersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> WatchlistsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return WatchlistsResourceWithStreamingResponse(self._v1.watchlists)

    @cached_property
    def ws(self) -> WsResourceWithStreamingResponse:
        """Active Websocket."""
        return WsResourceWithStreamingResponse(self._v1.ws)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Manage trading accounts and view balances."""
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """Manage API keys for authentication."""
        return AsyncAPIKeysResourceWithStreamingResponse(self._v1.api_keys)

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
        """Retrieve details and lists of tradable instruments."""
        return AsyncNewsResourceWithStreamingResponse(self._v1.news)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResourceWithStreamingResponse:
        return AsyncOmniAIResourceWithStreamingResponse(self._v1.omni_ai)

    @cached_property
    def saved_screeners(self) -> AsyncSavedScreenersResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncSavedScreenersResourceWithStreamingResponse(self._v1.saved_screeners)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        """Endpoints for API service metadata."""
        return AsyncVersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def watchlists(self) -> AsyncWatchlistsResourceWithStreamingResponse:
        """Retrieve details and lists of tradable instruments."""
        return AsyncWatchlistsResourceWithStreamingResponse(self._v1.watchlists)

    @cached_property
    def ws(self) -> AsyncWsResourceWithStreamingResponse:
        """Active Websocket."""
        return AsyncWsResourceWithStreamingResponse(self._v1.ws)

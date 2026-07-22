# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .calendar import (
    CalendarResource,
    AsyncCalendarResource,
    CalendarResourceWithRawResponse,
    AsyncCalendarResourceWithRawResponse,
    CalendarResourceWithStreamingResponse,
    AsyncCalendarResourceWithStreamingResponse,
)
from .screener import (
    ScreenerResource,
    AsyncScreenerResource,
    ScreenerResourceWithRawResponse,
    AsyncScreenerResourceWithRawResponse,
    ScreenerResourceWithStreamingResponse,
    AsyncScreenerResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .positions import (
    PositionsResource,
    AsyncPositionsResource,
    PositionsResourceWithRawResponse,
    AsyncPositionsResourceWithRawResponse,
    PositionsResourceWithStreamingResponse,
    AsyncPositionsResourceWithStreamingResponse,
)
from .watchlist import (
    WatchlistResource,
    AsyncWatchlistResource,
    WatchlistResourceWithRawResponse,
    AsyncWatchlistResourceWithRawResponse,
    WatchlistResourceWithStreamingResponse,
    AsyncWatchlistResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .api_version import (
    APIVersionResource,
    AsyncAPIVersionResource,
    APIVersionResourceWithRawResponse,
    AsyncAPIVersionResourceWithRawResponse,
    APIVersionResourceWithStreamingResponse,
    AsyncAPIVersionResourceWithStreamingResponse,
)
from .instruments import (
    InstrumentsResource,
    AsyncInstrumentsResource,
    InstrumentsResourceWithRawResponse,
    AsyncInstrumentsResourceWithRawResponse,
    InstrumentsResourceWithStreamingResponse,
    AsyncInstrumentsResourceWithStreamingResponse,
)
from .omni_ai.omni_ai import (
    OmniAIResource,
    AsyncOmniAIResource,
    OmniAIResourceWithRawResponse,
    AsyncOmniAIResourceWithRawResponse,
    OmniAIResourceWithStreamingResponse,
    AsyncOmniAIResourceWithStreamingResponse,
)
from .instrument_data.instrument_data import (
    InstrumentDataResource,
    AsyncInstrumentDataResource,
    InstrumentDataResourceWithRawResponse,
    AsyncInstrumentDataResourceWithRawResponse,
    InstrumentDataResourceWithStreamingResponse,
    AsyncInstrumentDataResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        """Manage trading accounts, balances, and portfolio history."""
        return AccountsResource(self._client)

    @cached_property
    def api_version(self) -> APIVersionResource:
        """Endpoints for API service metadata."""
        return APIVersionResource(self._client)

    @cached_property
    def calendar(self) -> CalendarResource:
        """Access clocks and financial calendars for market sessions and events."""
        return CalendarResource(self._client)

    @cached_property
    def instrument_data(self) -> InstrumentDataResource:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return InstrumentDataResource(self._client)

    @cached_property
    def instruments(self) -> InstrumentsResource:
        """Retrieve core details and discovery endpoints for tradable instruments."""
        return InstrumentsResource(self._client)

    @cached_property
    def omni_ai(self) -> OmniAIResource:
        return OmniAIResource(self._client)

    @cached_property
    def orders(self) -> OrdersResource:
        """Place, monitor, and manage trading orders."""
        return OrdersResource(self._client)

    @cached_property
    def positions(self) -> PositionsResource:
        """View positions and manage position instructions."""
        return PositionsResource(self._client)

    @cached_property
    def screener(self) -> ScreenerResource:
        """Search instruments and manage saved screeners."""
        return ScreenerResource(self._client)

    @cached_property
    def watchlist(self) -> WatchlistResource:
        """Create and manage watchlists."""
        return WatchlistResource(self._client)

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
        """Manage trading accounts, balances, and portfolio history."""
        return AsyncAccountsResource(self._client)

    @cached_property
    def api_version(self) -> AsyncAPIVersionResource:
        """Endpoints for API service metadata."""
        return AsyncAPIVersionResource(self._client)

    @cached_property
    def calendar(self) -> AsyncCalendarResource:
        """Access clocks and financial calendars for market sessions and events."""
        return AsyncCalendarResource(self._client)

    @cached_property
    def instrument_data(self) -> AsyncInstrumentDataResource:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncInstrumentDataResource(self._client)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResource:
        """Retrieve core details and discovery endpoints for tradable instruments."""
        return AsyncInstrumentsResource(self._client)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResource:
        return AsyncOmniAIResource(self._client)

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        """Place, monitor, and manage trading orders."""
        return AsyncOrdersResource(self._client)

    @cached_property
    def positions(self) -> AsyncPositionsResource:
        """View positions and manage position instructions."""
        return AsyncPositionsResource(self._client)

    @cached_property
    def screener(self) -> AsyncScreenerResource:
        """Search instruments and manage saved screeners."""
        return AsyncScreenerResource(self._client)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResource:
        """Create and manage watchlists."""
        return AsyncWatchlistResource(self._client)

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
        """Manage trading accounts, balances, and portfolio history."""
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def api_version(self) -> APIVersionResourceWithRawResponse:
        """Endpoints for API service metadata."""
        return APIVersionResourceWithRawResponse(self._v1.api_version)

    @cached_property
    def calendar(self) -> CalendarResourceWithRawResponse:
        """Access clocks and financial calendars for market sessions and events."""
        return CalendarResourceWithRawResponse(self._v1.calendar)

    @cached_property
    def instrument_data(self) -> InstrumentDataResourceWithRawResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return InstrumentDataResourceWithRawResponse(self._v1.instrument_data)

    @cached_property
    def instruments(self) -> InstrumentsResourceWithRawResponse:
        """Retrieve core details and discovery endpoints for tradable instruments."""
        return InstrumentsResourceWithRawResponse(self._v1.instruments)

    @cached_property
    def omni_ai(self) -> OmniAIResourceWithRawResponse:
        return OmniAIResourceWithRawResponse(self._v1.omni_ai)

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        """Place, monitor, and manage trading orders."""
        return OrdersResourceWithRawResponse(self._v1.orders)

    @cached_property
    def positions(self) -> PositionsResourceWithRawResponse:
        """View positions and manage position instructions."""
        return PositionsResourceWithRawResponse(self._v1.positions)

    @cached_property
    def screener(self) -> ScreenerResourceWithRawResponse:
        """Search instruments and manage saved screeners."""
        return ScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def watchlist(self) -> WatchlistResourceWithRawResponse:
        """Create and manage watchlists."""
        return WatchlistResourceWithRawResponse(self._v1.watchlist)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def api_version(self) -> AsyncAPIVersionResourceWithRawResponse:
        """Endpoints for API service metadata."""
        return AsyncAPIVersionResourceWithRawResponse(self._v1.api_version)

    @cached_property
    def calendar(self) -> AsyncCalendarResourceWithRawResponse:
        """Access clocks and financial calendars for market sessions and events."""
        return AsyncCalendarResourceWithRawResponse(self._v1.calendar)

    @cached_property
    def instrument_data(self) -> AsyncInstrumentDataResourceWithRawResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncInstrumentDataResourceWithRawResponse(self._v1.instrument_data)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResourceWithRawResponse:
        """Retrieve core details and discovery endpoints for tradable instruments."""
        return AsyncInstrumentsResourceWithRawResponse(self._v1.instruments)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResourceWithRawResponse:
        return AsyncOmniAIResourceWithRawResponse(self._v1.omni_ai)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        """Place, monitor, and manage trading orders."""
        return AsyncOrdersResourceWithRawResponse(self._v1.orders)

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithRawResponse:
        """View positions and manage position instructions."""
        return AsyncPositionsResourceWithRawResponse(self._v1.positions)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithRawResponse:
        """Search instruments and manage saved screeners."""
        return AsyncScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResourceWithRawResponse:
        """Create and manage watchlists."""
        return AsyncWatchlistResourceWithRawResponse(self._v1.watchlist)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def api_version(self) -> APIVersionResourceWithStreamingResponse:
        """Endpoints for API service metadata."""
        return APIVersionResourceWithStreamingResponse(self._v1.api_version)

    @cached_property
    def calendar(self) -> CalendarResourceWithStreamingResponse:
        """Access clocks and financial calendars for market sessions and events."""
        return CalendarResourceWithStreamingResponse(self._v1.calendar)

    @cached_property
    def instrument_data(self) -> InstrumentDataResourceWithStreamingResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return InstrumentDataResourceWithStreamingResponse(self._v1.instrument_data)

    @cached_property
    def instruments(self) -> InstrumentsResourceWithStreamingResponse:
        """Retrieve core details and discovery endpoints for tradable instruments."""
        return InstrumentsResourceWithStreamingResponse(self._v1.instruments)

    @cached_property
    def omni_ai(self) -> OmniAIResourceWithStreamingResponse:
        return OmniAIResourceWithStreamingResponse(self._v1.omni_ai)

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        """Place, monitor, and manage trading orders."""
        return OrdersResourceWithStreamingResponse(self._v1.orders)

    @cached_property
    def positions(self) -> PositionsResourceWithStreamingResponse:
        """View positions and manage position instructions."""
        return PositionsResourceWithStreamingResponse(self._v1.positions)

    @cached_property
    def screener(self) -> ScreenerResourceWithStreamingResponse:
        """Search instruments and manage saved screeners."""
        return ScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def watchlist(self) -> WatchlistResourceWithStreamingResponse:
        """Create and manage watchlists."""
        return WatchlistResourceWithStreamingResponse(self._v1.watchlist)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Manage trading accounts, balances, and portfolio history."""
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def api_version(self) -> AsyncAPIVersionResourceWithStreamingResponse:
        """Endpoints for API service metadata."""
        return AsyncAPIVersionResourceWithStreamingResponse(self._v1.api_version)

    @cached_property
    def calendar(self) -> AsyncCalendarResourceWithStreamingResponse:
        """Access clocks and financial calendars for market sessions and events."""
        return AsyncCalendarResourceWithStreamingResponse(self._v1.calendar)

    @cached_property
    def instrument_data(self) -> AsyncInstrumentDataResourceWithStreamingResponse:
        """Retrieve instrument analytics, market data, news, and related reference data."""
        return AsyncInstrumentDataResourceWithStreamingResponse(self._v1.instrument_data)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResourceWithStreamingResponse:
        """Retrieve core details and discovery endpoints for tradable instruments."""
        return AsyncInstrumentsResourceWithStreamingResponse(self._v1.instruments)

    @cached_property
    def omni_ai(self) -> AsyncOmniAIResourceWithStreamingResponse:
        return AsyncOmniAIResourceWithStreamingResponse(self._v1.omni_ai)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        """Place, monitor, and manage trading orders."""
        return AsyncOrdersResourceWithStreamingResponse(self._v1.orders)

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithStreamingResponse:
        """View positions and manage position instructions."""
        return AsyncPositionsResourceWithStreamingResponse(self._v1.positions)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithStreamingResponse:
        """Search instruments and manage saved screeners."""
        return AsyncScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResourceWithStreamingResponse:
        """Create and manage watchlists."""
        return AsyncWatchlistResourceWithStreamingResponse(self._v1.watchlist)

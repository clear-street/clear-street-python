# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .splits import (
    SplitsResource,
    AsyncSplitsResource,
    SplitsResourceWithRawResponse,
    AsyncSplitsResourceWithRawResponse,
    SplitsResourceWithStreamingResponse,
    AsyncSplitsResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from .earnings import (
    EarningsResource,
    AsyncEarningsResource,
    EarningsResourceWithRawResponse,
    AsyncEarningsResourceWithRawResponse,
    EarningsResourceWithStreamingResponse,
    AsyncEarningsResourceWithStreamingResponse,
)
from .economic import (
    EconomicResource,
    AsyncEconomicResource,
    EconomicResourceWithRawResponse,
    AsyncEconomicResourceWithRawResponse,
    EconomicResourceWithStreamingResponse,
    AsyncEconomicResourceWithStreamingResponse,
)
from .dividends import (
    DividendsResource,
    AsyncDividendsResource,
    DividendsResourceWithRawResponse,
    AsyncDividendsResourceWithRawResponse,
    DividendsResourceWithStreamingResponse,
    AsyncDividendsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .market_hours import (
    MarketHoursResource,
    AsyncMarketHoursResource,
    MarketHoursResourceWithRawResponse,
    AsyncMarketHoursResourceWithRawResponse,
    MarketHoursResourceWithStreamingResponse,
    AsyncMarketHoursResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from .mergers_acquisitions import (
    MergersAcquisitionsResource,
    AsyncMergersAcquisitionsResource,
    MergersAcquisitionsResourceWithRawResponse,
    AsyncMergersAcquisitionsResourceWithRawResponse,
    MergersAcquisitionsResourceWithStreamingResponse,
    AsyncMergersAcquisitionsResourceWithStreamingResponse,
)

__all__ = ["CalendarsResource", "AsyncCalendarsResource"]


class CalendarsResource(SyncAPIResource):
    @cached_property
    def dividends(self) -> DividendsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return DividendsResource(self._client)

    @cached_property
    def earnings(self) -> EarningsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return EarningsResource(self._client)

    @cached_property
    def economic(self) -> EconomicResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return EconomicResource(self._client)

    @cached_property
    def market_hours(self) -> MarketHoursResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MarketHoursResource(self._client)

    @cached_property
    def mergers_acquisitions(self) -> MergersAcquisitionsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MergersAcquisitionsResource(self._client)

    @cached_property
    def splits(self) -> SplitsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return SplitsResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return CalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return CalendarsResourceWithStreamingResponse(self)


class AsyncCalendarsResource(AsyncAPIResource):
    @cached_property
    def dividends(self) -> AsyncDividendsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncDividendsResource(self._client)

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncEarningsResource(self._client)

    @cached_property
    def economic(self) -> AsyncEconomicResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncEconomicResource(self._client)

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMarketHoursResource(self._client)

    @cached_property
    def mergers_acquisitions(self) -> AsyncMergersAcquisitionsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMergersAcquisitionsResource(self._client)

    @cached_property
    def splits(self) -> AsyncSplitsResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncSplitsResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncCalendarsResourceWithStreamingResponse(self)


class CalendarsResourceWithRawResponse:
    def __init__(self, calendars: CalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> DividendsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return DividendsResourceWithRawResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return EarningsResourceWithRawResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> EconomicResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return EconomicResourceWithRawResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> MarketHoursResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MarketHoursResourceWithRawResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> MergersAcquisitionsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MergersAcquisitionsResourceWithRawResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> SplitsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return SplitsResourceWithRawResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return SummaryResourceWithRawResponse(self._calendars.summary)


class AsyncCalendarsResourceWithRawResponse:
    def __init__(self, calendars: AsyncCalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> AsyncDividendsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncDividendsResourceWithRawResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncEarningsResourceWithRawResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> AsyncEconomicResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncEconomicResourceWithRawResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMarketHoursResourceWithRawResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> AsyncMergersAcquisitionsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMergersAcquisitionsResourceWithRawResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> AsyncSplitsResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncSplitsResourceWithRawResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncSummaryResourceWithRawResponse(self._calendars.summary)


class CalendarsResourceWithStreamingResponse:
    def __init__(self, calendars: CalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> DividendsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return DividendsResourceWithStreamingResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return EarningsResourceWithStreamingResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> EconomicResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return EconomicResourceWithStreamingResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> MarketHoursResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MarketHoursResourceWithStreamingResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> MergersAcquisitionsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return MergersAcquisitionsResourceWithStreamingResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> SplitsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return SplitsResourceWithStreamingResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return SummaryResourceWithStreamingResponse(self._calendars.summary)


class AsyncCalendarsResourceWithStreamingResponse:
    def __init__(self, calendars: AsyncCalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> AsyncDividendsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncDividendsResourceWithStreamingResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncEarningsResourceWithStreamingResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> AsyncEconomicResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncEconomicResourceWithStreamingResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMarketHoursResourceWithStreamingResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> AsyncMergersAcquisitionsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncMergersAcquisitionsResourceWithStreamingResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> AsyncSplitsResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncSplitsResourceWithStreamingResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        """Access financial calendars for events like earnings, dividends, and splits."""
        return AsyncSummaryResourceWithStreamingResponse(self._calendars.summary)

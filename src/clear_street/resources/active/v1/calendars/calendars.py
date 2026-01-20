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
        return DividendsResource(self._client)

    @cached_property
    def earnings(self) -> EarningsResource:
        return EarningsResource(self._client)

    @cached_property
    def economic(self) -> EconomicResource:
        return EconomicResource(self._client)

    @cached_property
    def market_hours(self) -> MarketHoursResource:
        return MarketHoursResource(self._client)

    @cached_property
    def mergers_acquisitions(self) -> MergersAcquisitionsResource:
        return MergersAcquisitionsResource(self._client)

    @cached_property
    def splits(self) -> SplitsResource:
        return SplitsResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return CalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return CalendarsResourceWithStreamingResponse(self)


class AsyncCalendarsResource(AsyncAPIResource):
    @cached_property
    def dividends(self) -> AsyncDividendsResource:
        return AsyncDividendsResource(self._client)

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        return AsyncEarningsResource(self._client)

    @cached_property
    def economic(self) -> AsyncEconomicResource:
        return AsyncEconomicResource(self._client)

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResource:
        return AsyncMarketHoursResource(self._client)

    @cached_property
    def mergers_acquisitions(self) -> AsyncMergersAcquisitionsResource:
        return AsyncMergersAcquisitionsResource(self._client)

    @cached_property
    def splits(self) -> AsyncSplitsResource:
        return AsyncSplitsResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncCalendarsResourceWithStreamingResponse(self)


class CalendarsResourceWithRawResponse:
    def __init__(self, calendars: CalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> DividendsResourceWithRawResponse:
        return DividendsResourceWithRawResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        return EarningsResourceWithRawResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> EconomicResourceWithRawResponse:
        return EconomicResourceWithRawResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> MarketHoursResourceWithRawResponse:
        return MarketHoursResourceWithRawResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> MergersAcquisitionsResourceWithRawResponse:
        return MergersAcquisitionsResourceWithRawResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> SplitsResourceWithRawResponse:
        return SplitsResourceWithRawResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._calendars.summary)


class AsyncCalendarsResourceWithRawResponse:
    def __init__(self, calendars: AsyncCalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> AsyncDividendsResourceWithRawResponse:
        return AsyncDividendsResourceWithRawResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        return AsyncEarningsResourceWithRawResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> AsyncEconomicResourceWithRawResponse:
        return AsyncEconomicResourceWithRawResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResourceWithRawResponse:
        return AsyncMarketHoursResourceWithRawResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> AsyncMergersAcquisitionsResourceWithRawResponse:
        return AsyncMergersAcquisitionsResourceWithRawResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> AsyncSplitsResourceWithRawResponse:
        return AsyncSplitsResourceWithRawResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._calendars.summary)


class CalendarsResourceWithStreamingResponse:
    def __init__(self, calendars: CalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> DividendsResourceWithStreamingResponse:
        return DividendsResourceWithStreamingResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        return EarningsResourceWithStreamingResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> EconomicResourceWithStreamingResponse:
        return EconomicResourceWithStreamingResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> MarketHoursResourceWithStreamingResponse:
        return MarketHoursResourceWithStreamingResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> MergersAcquisitionsResourceWithStreamingResponse:
        return MergersAcquisitionsResourceWithStreamingResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> SplitsResourceWithStreamingResponse:
        return SplitsResourceWithStreamingResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._calendars.summary)


class AsyncCalendarsResourceWithStreamingResponse:
    def __init__(self, calendars: AsyncCalendarsResource) -> None:
        self._calendars = calendars

    @cached_property
    def dividends(self) -> AsyncDividendsResourceWithStreamingResponse:
        return AsyncDividendsResourceWithStreamingResponse(self._calendars.dividends)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        return AsyncEarningsResourceWithStreamingResponse(self._calendars.earnings)

    @cached_property
    def economic(self) -> AsyncEconomicResourceWithStreamingResponse:
        return AsyncEconomicResourceWithStreamingResponse(self._calendars.economic)

    @cached_property
    def market_hours(self) -> AsyncMarketHoursResourceWithStreamingResponse:
        return AsyncMarketHoursResourceWithStreamingResponse(self._calendars.market_hours)

    @cached_property
    def mergers_acquisitions(self) -> AsyncMergersAcquisitionsResourceWithStreamingResponse:
        return AsyncMergersAcquisitionsResourceWithStreamingResponse(self._calendars.mergers_acquisitions)

    @cached_property
    def splits(self) -> AsyncSplitsResourceWithStreamingResponse:
        return AsyncSplitsResourceWithStreamingResponse(self._calendars.splits)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._calendars.summary)

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
from .version import (
    VersionResource,
    AsyncVersionResource,
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
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
from .accounts.accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .assistant.assistant import (
    AssistantResource,
    AsyncAssistantResource,
    AssistantResourceWithRawResponse,
    AsyncAssistantResourceWithRawResponse,
    AssistantResourceWithStreamingResponse,
    AsyncAssistantResourceWithStreamingResponse,
)
from .calendars.calendars import (
    CalendarsResource,
    AsyncCalendarsResource,
    CalendarsResourceWithRawResponse,
    AsyncCalendarsResourceWithRawResponse,
    CalendarsResourceWithStreamingResponse,
    AsyncCalendarsResourceWithStreamingResponse,
)
from .instruments.instruments import (
    InstrumentsResource,
    AsyncInstrumentsResource,
    InstrumentsResourceWithRawResponse,
    AsyncInstrumentsResourceWithRawResponse,
    InstrumentsResourceWithStreamingResponse,
    AsyncInstrumentsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def assistant(self) -> AssistantResource:
        return AssistantResource(self._client)

    @cached_property
    def calendars(self) -> CalendarsResource:
        return CalendarsResource(self._client)

    @cached_property
    def instruments(self) -> InstrumentsResource:
        return InstrumentsResource(self._client)

    @cached_property
    def screener(self) -> ScreenerResource:
        return ScreenerResource(self._client)

    @cached_property
    def version(self) -> VersionResource:
        return VersionResource(self._client)

    @cached_property
    def ws(self) -> WsResource:
        return WsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def assistant(self) -> AsyncAssistantResource:
        return AsyncAssistantResource(self._client)

    @cached_property
    def calendars(self) -> AsyncCalendarsResource:
        return AsyncCalendarsResource(self._client)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResource:
        return AsyncInstrumentsResource(self._client)

    @cached_property
    def screener(self) -> AsyncScreenerResource:
        return AsyncScreenerResource(self._client)

    @cached_property
    def version(self) -> AsyncVersionResource:
        return AsyncVersionResource(self._client)

    @cached_property
    def ws(self) -> AsyncWsResource:
        return AsyncWsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/clear-street-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def assistant(self) -> AssistantResourceWithRawResponse:
        return AssistantResourceWithRawResponse(self._v1.assistant)

    @cached_property
    def calendars(self) -> CalendarsResourceWithRawResponse:
        return CalendarsResourceWithRawResponse(self._v1.calendars)

    @cached_property
    def instruments(self) -> InstrumentsResourceWithRawResponse:
        return InstrumentsResourceWithRawResponse(self._v1.instruments)

    @cached_property
    def screener(self) -> ScreenerResourceWithRawResponse:
        return ScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def ws(self) -> WsResourceWithRawResponse:
        return WsResourceWithRawResponse(self._v1.ws)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._v1.accounts)

    @cached_property
    def assistant(self) -> AsyncAssistantResourceWithRawResponse:
        return AsyncAssistantResourceWithRawResponse(self._v1.assistant)

    @cached_property
    def calendars(self) -> AsyncCalendarsResourceWithRawResponse:
        return AsyncCalendarsResourceWithRawResponse(self._v1.calendars)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResourceWithRawResponse:
        return AsyncInstrumentsResourceWithRawResponse(self._v1.instruments)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithRawResponse:
        return AsyncScreenerResourceWithRawResponse(self._v1.screener)

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def ws(self) -> AsyncWsResourceWithRawResponse:
        return AsyncWsResourceWithRawResponse(self._v1.ws)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def assistant(self) -> AssistantResourceWithStreamingResponse:
        return AssistantResourceWithStreamingResponse(self._v1.assistant)

    @cached_property
    def calendars(self) -> CalendarsResourceWithStreamingResponse:
        return CalendarsResourceWithStreamingResponse(self._v1.calendars)

    @cached_property
    def instruments(self) -> InstrumentsResourceWithStreamingResponse:
        return InstrumentsResourceWithStreamingResponse(self._v1.instruments)

    @cached_property
    def screener(self) -> ScreenerResourceWithStreamingResponse:
        return ScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def ws(self) -> WsResourceWithStreamingResponse:
        return WsResourceWithStreamingResponse(self._v1.ws)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._v1.accounts)

    @cached_property
    def assistant(self) -> AsyncAssistantResourceWithStreamingResponse:
        return AsyncAssistantResourceWithStreamingResponse(self._v1.assistant)

    @cached_property
    def calendars(self) -> AsyncCalendarsResourceWithStreamingResponse:
        return AsyncCalendarsResourceWithStreamingResponse(self._v1.calendars)

    @cached_property
    def instruments(self) -> AsyncInstrumentsResourceWithStreamingResponse:
        return AsyncInstrumentsResourceWithStreamingResponse(self._v1.instruments)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithStreamingResponse:
        return AsyncScreenerResourceWithStreamingResponse(self._v1.screener)

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def ws(self) -> AsyncWsResourceWithStreamingResponse:
        return AsyncWsResourceWithStreamingResponse(self._v1.ws)

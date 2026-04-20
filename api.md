# Shared Types

```python
from clear_street.types import APIError, BaseResponse, ResponseMetadata
```

# Active

## V1

Types:

```python
from clear_street.types.active import APIDecimal64, SecurityIDSource, SecurityType
```

### Accounts

Types:

```python
from clear_street.types.active.v1 import (
    Account,
    AccountKind,
    AccountList,
    AccountSettings,
    AccountStatus,
    AccountSubkind,
    RiskSettings,
    AccountGetAccountByIDResponse,
    AccountGetAccountsResponse,
    AccountPatchAccountByIDResponse,
)
```

Methods:

- <code title="get /active/v1/accounts/{account_id}">client.active.v1.accounts.<a href="./src/clear_street/resources/active/v1/accounts/accounts.py">get_account_by_id</a>(account_id) -> <a href="./src/clear_street/types/active/v1/account_get_account_by_id_response.py">AccountGetAccountByIDResponse</a></code>
- <code title="get /active/v1/accounts">client.active.v1.accounts.<a href="./src/clear_street/resources/active/v1/accounts/accounts.py">get_accounts</a>(\*\*<a href="src/clear_street/types/active/v1/account_get_accounts_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/account_get_accounts_response.py">AccountGetAccountsResponse</a></code>
- <code title="patch /active/v1/accounts/{account_id}">client.active.v1.accounts.<a href="./src/clear_street/resources/active/v1/accounts/accounts.py">patch_account_by_id</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/account_patch_account_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/account_patch_account_by_id_response.py">AccountPatchAccountByIDResponse</a></code>

#### Balances

Types:

```python
from clear_street.types.active.v1.accounts import (
    AccountBalances,
    AccountBalancesSod,
    MarginDetails,
    MarginDetailsUsage,
    MarginTopContributor,
    MarginType,
    BalanceGetAccountBalancesResponse,
)
```

Methods:

- <code title="get /active/v1/accounts/{account_id}/balances">client.active.v1.accounts.balances.<a href="./src/clear_street/resources/active/v1/accounts/balances.py">get_account_balances</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/balance_get_account_balances_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/balance_get_account_balances_response.py">BalanceGetAccountBalancesResponse</a></code>

#### Locates

Types:

```python
from clear_street.types.active.v1.accounts import (
    LocateOrder,
    LocateOrderList,
    LocateOrderStatus,
    LocateCreateLocateRequestResponse,
    LocateGetLocateRequestsResponse,
    LocateUpdateLocateRequestResponse,
)
```

Methods:

- <code title="post /active/v1/accounts/{account_id}/locates">client.active.v1.accounts.locates.<a href="./src/clear_street/resources/active/v1/accounts/locates/locates.py">create_locate_request</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/locate_create_locate_request_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/locate_create_locate_request_response.py">LocateCreateLocateRequestResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/locates">client.active.v1.accounts.locates.<a href="./src/clear_street/resources/active/v1/accounts/locates/locates.py">get_locate_requests</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/locate_get_locate_requests_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/locate_get_locate_requests_response.py">LocateGetLocateRequestsResponse</a></code>
- <code title="patch /active/v1/accounts/{account_id}/locates">client.active.v1.accounts.locates.<a href="./src/clear_street/resources/active/v1/accounts/locates/locates.py">update_locate_request</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/locate_update_locate_request_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/locate_update_locate_request_response.py">LocateUpdateLocateRequestResponse</a></code>

##### Inventory

Types:

```python
from clear_street.types.active.v1.accounts.locates import (
    LocateInventoryItem,
    LocateInventoryItemList,
    InventoryGetLocateInventoryResponse,
)
```

Methods:

- <code title="get /active/v1/accounts/{account_id}/locates/inventory">client.active.v1.accounts.locates.inventory.<a href="./src/clear_street/resources/active/v1/accounts/locates/inventory.py">get_locate_inventory</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/locates/inventory_get_locate_inventory_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/locates/inventory_get_locate_inventory_response.py">InventoryGetLocateInventoryResponse</a></code>

#### Orders

Types:

```python
from clear_street.types.active.v1.accounts import (
    ApStrategy,
    BaseStrategyParams,
    DarkStrategy,
    DmaStrategy,
    Order,
    OrderList,
    OrderStatus,
    OrderStrategy,
    OrderType,
    PovStrategy,
    Side,
    SorStrategy,
    TimeInForce,
    TrailingOffsetType,
    TwapStrategy,
    Urgency,
    VwapStrategy,
    OrderCancelAllOpenOrdersResponse,
    OrderCancelOpenOrderResponse,
    OrderGetOrderByIDResponse,
    OrderGetOrdersResponse,
    OrderReplaceOrderResponse,
    OrderSubmitOrdersResponse,
)
```

Methods:

- <code title="delete /active/v1/accounts/{account_id}/orders">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">cancel_all_open_orders</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_cancel_all_open_orders_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_cancel_all_open_orders_response.py">OrderCancelAllOpenOrdersResponse</a></code>
- <code title="delete /active/v1/accounts/{account_id}/orders/{order_id}">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">cancel_open_order</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/active/v1/accounts/order_cancel_open_order_response.py">OrderCancelOpenOrderResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/orders/{order_id}">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">get_order_by_id</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/active/v1/accounts/order_get_order_by_id_response.py">OrderGetOrderByIDResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/orders">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">get_orders</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_get_orders_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_get_orders_response.py">OrderGetOrdersResponse</a></code>
- <code title="patch /active/v1/accounts/{account_id}/orders/{order_id}">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">replace_order</a>(order_id, \*, account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_replace_order_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_replace_order_response.py">OrderReplaceOrderResponse</a></code>
- <code title="post /active/v1/accounts/{account_id}/orders">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">submit_orders</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_submit_orders_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_submit_orders_response.py">OrderSubmitOrdersResponse</a></code>

#### PortfolioHistory

Types:

```python
from clear_street.types.active.v1.accounts import (
    PortfolioHistoryResponse,
    PortfolioHistorySegment,
    PortfolioHistoryGetPortfolioHistoryResponse,
)
```

Methods:

- <code title="get /active/v1/accounts/{account_id}/portfolio-history">client.active.v1.accounts.portfolio_history.<a href="./src/clear_street/resources/active/v1/accounts/portfolio_history.py">get_portfolio_history</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/portfolio_history_get_portfolio_history_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/portfolio_history_get_portfolio_history_response.py">PortfolioHistoryGetPortfolioHistoryResponse</a></code>

#### Positions

Types:

```python
from clear_street.types.active.v1.accounts import (
    Position,
    PositionList,
    PositionType,
    PositionClosePositionResponse,
    PositionClosePositionsResponse,
    PositionGetPositionsResponse,
)
```

Methods:

- <code title="delete /active/v1/accounts/{account_id}/positions/{security_id_source}/{security_id}">client.active.v1.accounts.positions.<a href="./src/clear_street/resources/active/v1/accounts/positions.py">close_position</a>(security_id, \*, account_id, security_id_source, \*\*<a href="src/clear_street/types/active/v1/accounts/position_close_position_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/position_close_position_response.py">PositionClosePositionResponse</a></code>
- <code title="delete /active/v1/accounts/{account_id}/positions">client.active.v1.accounts.positions.<a href="./src/clear_street/resources/active/v1/accounts/positions.py">close_positions</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/position_close_positions_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/position_close_positions_response.py">PositionClosePositionsResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/positions">client.active.v1.accounts.positions.<a href="./src/clear_street/resources/active/v1/accounts/positions.py">get_positions</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/position_get_positions_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/position_get_positions_response.py">PositionGetPositionsResponse</a></code>

### APIKeys

Types:

```python
from clear_street.types.active.v1 import (
    APIKey,
    APIKeyListEntry,
    APIKeyListEntryList,
    Revocation,
    RevocationList,
    APIKeyCreateResponse,
    APIKeyListResponse,
    APIKeyRevokeResponse,
    APIKeyRevokeAllResponse,
)
```

Methods:

- <code title="post /active/v1/api_keys">client.active.v1.api_keys.<a href="./src/clear_street/resources/active/v1/api_keys.py">create</a>(\*\*<a href="src/clear_street/types/active/v1/api_key_create_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /active/v1/api_keys">client.active.v1.api_keys.<a href="./src/clear_street/resources/active/v1/api_keys.py">list</a>() -> <a href="./src/clear_street/types/active/v1/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /active/v1/api_keys/{id}">client.active.v1.api_keys.<a href="./src/clear_street/resources/active/v1/api_keys.py">revoke</a>(id) -> <a href="./src/clear_street/types/active/v1/api_key_revoke_response.py">APIKeyRevokeResponse</a></code>
- <code title="delete /active/v1/api_keys">client.active.v1.api_keys.<a href="./src/clear_street/resources/active/v1/api_keys.py">revoke_all</a>() -> <a href="./src/clear_street/types/active/v1/api_key_revoke_all_response.py">APIKeyRevokeAllResponse</a></code>

### Calendars

#### Dividends

Types:

```python
from clear_street.types.active.v1.calendars import (
    DividendCalendarEvent,
    DividendCalendarEventList,
    DividendFrequency,
    DividendGetDividendsCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/dividends">client.active.v1.calendars.dividends.<a href="./src/clear_street/resources/active/v1/calendars/dividends.py">get_dividends_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/dividend_get_dividends_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/dividend_get_dividends_calendar_response.py">DividendGetDividendsCalendarResponse</a></code>

#### Earnings

Types:

```python
from clear_street.types.active.v1.calendars import (
    EarningsCalendarEvent,
    EarningsCalendarEventList,
    EarningGetEarningsCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/earnings">client.active.v1.calendars.earnings.<a href="./src/clear_street/resources/active/v1/calendars/earnings.py">get_earnings_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/earning_get_earnings_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/earning_get_earnings_calendar_response.py">EarningGetEarningsCalendarResponse</a></code>

#### Economic

Types:

```python
from clear_street.types.active.v1.calendars import (
    EconomicCalendarEvent,
    EconomicCalendarEventList,
    EconomicEventImpact,
    EconomicGetEconomicCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/economic">client.active.v1.calendars.economic.<a href="./src/clear_street/resources/active/v1/calendars/economic.py">get_economic_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/economic_get_economic_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/economic_get_economic_calendar_response.py">EconomicGetEconomicCalendarResponse</a></code>

#### MarketHours

Types:

```python
from clear_street.types.active.v1.calendars import (
    DayType,
    MarketHoursDetail,
    MarketHoursDetailList,
    MarketSessionType,
    MarketStatus,
    MarketType,
    SessionSchedule,
    TradingSessions,
    MarketHourGetMarketHoursCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/market-hours">client.active.v1.calendars.market_hours.<a href="./src/clear_street/resources/active/v1/calendars/market_hours.py">get_market_hours_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/market_hour_get_market_hours_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/market_hour_get_market_hours_calendar_response.py">MarketHourGetMarketHoursCalendarResponse</a></code>

#### MergersAcquisitions

Types:

```python
from clear_street.types.active.v1.calendars import (
    MergersAcquisitionsEvent,
    MergersAcquisitionsEventList,
    MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/mergers-acquisitions">client.active.v1.calendars.mergers_acquisitions.<a href="./src/clear_street/resources/active/v1/calendars/mergers_acquisitions.py">get_mergers_and_acquisitions_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/mergers_acquisition_get_mergers_and_acquisitions_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/mergers_acquisition_get_mergers_and_acquisitions_calendar_response.py">MergersAcquisitionGetMergersAndAcquisitionsCalendarResponse</a></code>

#### Splits

Types:

```python
from clear_street.types.active.v1.calendars import (
    StockSplitEvent,
    StockSplitEventList,
    SplitGetSplitsCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/splits">client.active.v1.calendars.splits.<a href="./src/clear_street/resources/active/v1/calendars/splits.py">get_splits_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/split_get_splits_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/split_get_splits_calendar_response.py">SplitGetSplitsCalendarResponse</a></code>

#### Summary

Types:

```python
from clear_street.types.active.v1.calendars import (
    CalendarDateSummary,
    CalendarDateSummaryList,
    SummaryGetCalendarSummaryResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/summary">client.active.v1.calendars.summary.<a href="./src/clear_street/resources/active/v1/calendars/summary.py">get_calendar_summary</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/summary_get_calendar_summary_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/summary_get_calendar_summary_response.py">SummaryGetCalendarSummaryResponse</a></code>

### Clock

Types:

```python
from clear_street.types.active.v1 import ClockDetail, ClockGetClockResponse
```

Methods:

- <code title="get /active/v1/clock">client.active.v1.clock.<a href="./src/clear_street/resources/active/v1/clock.py">get_clock</a>() -> <a href="./src/clear_street/types/active/v1/clock_get_clock_response.py">ClockGetClockResponse</a></code>

### Instruments

Types:

```python
from clear_street.types.active.v1 import (
    AnalystRating,
    ContractType,
    ExerciseStyle,
    Instrument,
    InstrumentCore,
    InstrumentCoreList,
    InstrumentEarnings,
    InstrumentQuote,
    InstrumentSecurityID,
    ListingType,
    OptionsContract,
    OptionsContractList,
    InstrumentGetInstrumentByIDResponse,
    InstrumentGetInstrumentsResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}">client.active.v1.instruments.<a href="./src/clear_street/resources/active/v1/instruments/instruments.py">get_instrument_by_id</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instrument_get_instrument_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instrument_get_instrument_by_id_response.py">InstrumentGetInstrumentByIDResponse</a></code>
- <code title="get /active/v1/instruments">client.active.v1.instruments.<a href="./src/clear_street/resources/active/v1/instruments/instruments.py">get_instruments</a>(\*\*<a href="src/clear_street/types/active/v1/instrument_get_instruments_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instrument_get_instruments_response.py">InstrumentGetInstrumentsResponse</a></code>

#### AnalystReporting

Types:

```python
from clear_street.types.active.v1.instruments import (
    AnalystDistribution,
    InstrumentAnalystConsensus,
    PriceTarget,
    AnalystReportingGetInstrumentAnalystConsensusResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}/analyst-reporting">client.active.v1.instruments.analyst_reporting.<a href="./src/clear_street/resources/active/v1/instruments/analyst_reporting.py">get_instrument_analyst_consensus</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instruments/analyst_reporting_get_instrument_analyst_consensus_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/analyst_reporting_get_instrument_analyst_consensus_response.py">AnalystReportingGetInstrumentAnalystConsensusResponse</a></code>

#### Events

Types:

```python
from clear_street.types.active.v1.instruments import (
    AllEventsEventType,
    InstrumentAllEventsData,
    InstrumentDividendEvent,
    InstrumentEventEnvelope,
    InstrumentEventIpoItem,
    InstrumentEventsByDate,
    InstrumentEventsData,
    InstrumentSplitEvent,
    EventGetAllInstrumentEventsResponse,
    EventGetInstrumentEventsResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/events">client.active.v1.instruments.events.<a href="./src/clear_street/resources/active/v1/instruments/events.py">get_all_instrument_events</a>(\*\*<a href="src/clear_street/types/active/v1/instruments/event_get_all_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/event_get_all_instrument_events_response.py">EventGetAllInstrumentEventsResponse</a></code>
- <code title="get /active/v1/instruments/{security_id_source}/{security_id}/events">client.active.v1.instruments.events.<a href="./src/clear_street/resources/active/v1/instruments/events.py">get_instrument_events</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instruments/event_get_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/event_get_instrument_events_response.py">EventGetInstrumentEventsResponse</a></code>

#### Options

##### Contracts

Types:

```python
from clear_street.types.active.v1.instruments.options import ContractGetOptionContractsResponse
```

Methods:

- <code title="get /active/v1/instruments/options/contracts">client.active.v1.instruments.options.contracts.<a href="./src/clear_street/resources/active/v1/instruments/options/contracts.py">get_option_contracts</a>(\*\*<a href="src/clear_street/types/active/v1/instruments/options/contract_get_option_contracts_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/options/contract_get_option_contracts_response.py">ContractGetOptionContractsResponse</a></code>

#### Reporting

Types:

```python
from clear_street.types.active.v1.instruments import ReportingGetInstrumentReportingResponse
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}/reporting">client.active.v1.instruments.reporting.<a href="./src/clear_street/resources/active/v1/instruments/reporting.py">get_instrument_reporting</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instruments/reporting_get_instrument_reporting_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/reporting_get_instrument_reporting_response.py">ReportingGetInstrumentReportingResponse</a></code>

#### Venues

Types:

```python
from clear_street.types.active.v1.instruments import (
    DisplayType,
    GtdAccepts,
    Venue,
    VenueList,
    VenueSession,
    VenueGetVenuesResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/venues">client.active.v1.instruments.venues.<a href="./src/clear_street/resources/active/v1/instruments/venues.py">get_venues</a>() -> <a href="./src/clear_street/types/active/v1/instruments/venue_get_venues_response.py">VenueGetVenuesResponse</a></code>

### MarketData

#### Snapshot

Types:

```python
from clear_street.types.active.v1.market_data import (
    MarketDataSnapshot,
    MarketDataSnapshotList,
    SnapshotLastTrade,
    SnapshotQuote,
    SnapshotSession,
    SnapshotGetSnapshotsResponse,
)
```

Methods:

- <code title="get /active/v1/market-data/snapshot">client.active.v1.market_data.snapshot.<a href="./src/clear_street/resources/active/v1/market_data/snapshot.py">get_snapshots</a>(\*\*<a href="src/clear_street/types/active/v1/market_data/snapshot_get_snapshots_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/market_data/snapshot_get_snapshots_response.py">SnapshotGetSnapshotsResponse</a></code>

### News

Types:

```python
from clear_street.types.active.v1 import (
    NewsInstrument,
    NewsItem,
    NewsItemList,
    NewsType,
    NewsGetNewsResponse,
)
```

Methods:

- <code title="get /active/v1/news">client.active.v1.news.<a href="./src/clear_street/resources/active/v1/news.py">get_news</a>(\*\*<a href="src/clear_street/types/active/v1/news_get_news_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/news_get_news_response.py">NewsGetNewsResponse</a></code>

### OmniAI

Types:

```python
from clear_street.types.active.v1 import (
    CancelResponsePayload,
    ContentPartChartPayload,
    ContentPartCustomPayload,
    ContentPartStructuredActionPayload,
    ContentPartSuggestedActionsPayload,
    ContentPartTextPayload,
    ContentPartThinkingPayload,
    CreateFeedbackResponse,
    CreateMessageResponse,
    CreateThreadResponse,
    ErrorStatus,
    Message,
    MessageContent,
    MessageContentPart,
    MessageList,
    MessageOutcome,
    MessageRole,
    OpenChartAction,
    OpenScreenerAction,
    OrderPayload,
    OrderStrategyType,
    PrefillOrderAction,
    Response,
    ResponseContent,
    ResponseContentPart,
    ResponseStatus,
    StructuredAction,
    Thread,
    ThreadList,
)
```

#### Messages

Types:

```python
from clear_street.types.active.v1.omni_ai import MessageGetMessageResponse
```

Methods:

- <code title="get /active/v1/omni-ai/messages/{message_id}">client.active.v1.omni_ai.messages.<a href="./src/clear_street/resources/active/v1/omni_ai/messages/messages.py">get_message</a>(message_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/message_get_message_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/message_get_message_response.py">MessageGetMessageResponse</a></code>

##### Feedback

Types:

```python
from clear_street.types.active.v1.omni_ai.messages import FeedbackCreateFeedbackResponse
```

Methods:

- <code title="post /active/v1/omni-ai/messages/{message_id}/feedback">client.active.v1.omni_ai.messages.feedback.<a href="./src/clear_street/resources/active/v1/omni_ai/messages/feedback.py">create_feedback</a>(message_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/messages/feedback_create_feedback_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/messages/feedback_create_feedback_response.py">FeedbackCreateFeedbackResponse</a></code>

#### Responses

Types:

```python
from clear_street.types.active.v1.omni_ai import (
    ResponseCancelResponseResponse,
    ResponseGetResponseResponse,
)
```

Methods:

- <code title="delete /active/v1/omni-ai/responses/{response_id}">client.active.v1.omni_ai.responses.<a href="./src/clear_street/resources/active/v1/omni_ai/responses.py">cancel_response</a>(response_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/response_cancel_response_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/response_cancel_response_response.py">ResponseCancelResponseResponse</a></code>
- <code title="get /active/v1/omni-ai/responses/{response_id}">client.active.v1.omni_ai.responses.<a href="./src/clear_street/resources/active/v1/omni_ai/responses.py">get_response</a>(response_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/response_get_response_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/response_get_response_response.py">ResponseGetResponseResponse</a></code>

#### Threads

Types:

```python
from clear_street.types.active.v1.omni_ai import (
    ThreadCreateThreadResponse,
    ThreadGetThreadResponse,
    ThreadListThreadsResponse,
)
```

Methods:

- <code title="post /active/v1/omni-ai/threads">client.active.v1.omni_ai.threads.<a href="./src/clear_street/resources/active/v1/omni_ai/threads/threads.py">create_thread</a>(\*\*<a href="src/clear_street/types/active/v1/omni_ai/thread_create_thread_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/thread_create_thread_response.py">ThreadCreateThreadResponse</a></code>
- <code title="get /active/v1/omni-ai/threads/{thread_id}">client.active.v1.omni_ai.threads.<a href="./src/clear_street/resources/active/v1/omni_ai/threads/threads.py">get_thread</a>(thread_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/thread_get_thread_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/thread_get_thread_response.py">ThreadGetThreadResponse</a></code>
- <code title="get /active/v1/omni-ai/threads">client.active.v1.omni_ai.threads.<a href="./src/clear_street/resources/active/v1/omni_ai/threads/threads.py">list_threads</a>(\*\*<a href="src/clear_street/types/active/v1/omni_ai/thread_list_threads_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/thread_list_threads_response.py">ThreadListThreadsResponse</a></code>

##### Messages

Types:

```python
from clear_street.types.active.v1.omni_ai.threads import (
    MessageCreateMessageResponse,
    MessageListMessagesResponse,
)
```

Methods:

- <code title="post /active/v1/omni-ai/threads/{thread_id}/messages">client.active.v1.omni_ai.threads.messages.<a href="./src/clear_street/resources/active/v1/omni_ai/threads/messages.py">create_message</a>(thread_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/threads/message_create_message_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/threads/message_create_message_response.py">MessageCreateMessageResponse</a></code>
- <code title="get /active/v1/omni-ai/threads/{thread_id}/messages">client.active.v1.omni_ai.threads.messages.<a href="./src/clear_street/resources/active/v1/omni_ai/threads/messages.py">list_messages</a>(thread_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/threads/message_list_messages_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/threads/message_list_messages_response.py">MessageListMessagesResponse</a></code>

##### Response

Types:

```python
from clear_street.types.active.v1.omni_ai.threads import ResponseGetThreadResponseResponse
```

Methods:

- <code title="get /active/v1/omni-ai/threads/{thread_id}/response">client.active.v1.omni_ai.threads.response.<a href="./src/clear_street/resources/active/v1/omni_ai/threads/response.py">get_thread_response</a>(thread_id, \*\*<a href="src/clear_street/types/active/v1/omni_ai/threads/response_get_thread_response_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/omni_ai/threads/response_get_thread_response_response.py">ResponseGetThreadResponseResponse</a></code>

### SavedScreeners

Types:

```python
from clear_street.types.active.v1 import (
    SavedScreenerFilter,
    ScreenerEntry,
    ScreenerEntryList,
    SavedScreenerCreateScreenerResponse,
    SavedScreenerGetScreenerByIDResponse,
    SavedScreenerGetScreenersResponse,
    SavedScreenerReplaceScreenerResponse,
)
```

Methods:

- <code title="post /active/v1/saved-screeners">client.active.v1.saved_screeners.<a href="./src/clear_street/resources/active/v1/saved_screeners.py">create_screener</a>(\*\*<a href="src/clear_street/types/active/v1/saved_screener_create_screener_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/saved_screener_create_screener_response.py">SavedScreenerCreateScreenerResponse</a></code>
- <code title="delete /active/v1/saved-screeners/{screener_id}">client.active.v1.saved_screeners.<a href="./src/clear_street/resources/active/v1/saved_screeners.py">delete_screener</a>(screener_id) -> None</code>
- <code title="get /active/v1/saved-screeners/{screener_id}">client.active.v1.saved_screeners.<a href="./src/clear_street/resources/active/v1/saved_screeners.py">get_screener_by_id</a>(screener_id) -> <a href="./src/clear_street/types/active/v1/saved_screener_get_screener_by_id_response.py">SavedScreenerGetScreenerByIDResponse</a></code>
- <code title="get /active/v1/saved-screeners">client.active.v1.saved_screeners.<a href="./src/clear_street/resources/active/v1/saved_screeners.py">get_screeners</a>() -> <a href="./src/clear_street/types/active/v1/saved_screener_get_screeners_response.py">SavedScreenerGetScreenersResponse</a></code>
- <code title="put /active/v1/saved-screeners/{screener_id}">client.active.v1.saved_screeners.<a href="./src/clear_street/resources/active/v1/saved_screeners.py">replace_screener</a>(screener_id, \*\*<a href="src/clear_street/types/active/v1/saved_screener_replace_screener_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/saved_screener_replace_screener_response.py">SavedScreenerReplaceScreenerResponse</a></code>

### Screener

Types:

```python
from clear_street.types.active.v1 import (
    FieldLookback,
    FieldPeriod,
    FieldRef,
    FieldType,
    ScreenerColumn,
    ScreenerFilter,
    ScreenerItem,
    ScreenerItemList,
    ScreenerRow,
    ScreenerRowList,
    ScreenerGetScreenerResponse,
    ScreenerSearchScreenerResponse,
)
```

Methods:

- <code title="get /active/v1/screener">client.active.v1.screener.<a href="./src/clear_street/resources/active/v1/screener.py">get_screener</a>(\*\*<a href="src/clear_street/types/active/v1/screener_get_screener_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/screener_get_screener_response.py">ScreenerGetScreenerResponse</a></code>
- <code title="post /active/v1/screener">client.active.v1.screener.<a href="./src/clear_street/resources/active/v1/screener.py">search_screener</a>(\*\*<a href="src/clear_street/types/active/v1/screener_search_screener_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/screener_search_screener_response.py">ScreenerSearchScreenerResponse</a></code>

### Version

Types:

```python
from clear_street.types.active.v1 import (
    Version,
    VersionGetVersionResponse,
    VersionUpdateVersionResponse,
)
```

Methods:

- <code title="get /active/v1/version">client.active.v1.version.<a href="./src/clear_street/resources/active/v1/version.py">get_version</a>() -> <a href="./src/clear_street/types/active/v1/version_get_version_response.py">VersionGetVersionResponse</a></code>
- <code title="patch /active/v1/version">client.active.v1.version.<a href="./src/clear_street/resources/active/v1/version.py">update_version</a>() -> <a href="./src/clear_street/types/active/v1/version_update_version_response.py">VersionUpdateVersionResponse</a></code>

### Watchlists

Types:

```python
from clear_street.types.active.v1 import (
    WatchlistDetail,
    WatchlistEntry,
    WatchlistEntryList,
    WatchlistItemEntry,
    WatchlistCreateWatchlistResponse,
    WatchlistGetWatchlistByIDResponse,
    WatchlistGetWatchlistsResponse,
)
```

Methods:

- <code title="post /active/v1/watchlists">client.active.v1.watchlists.<a href="./src/clear_street/resources/active/v1/watchlists/watchlists.py">create_watchlist</a>(\*\*<a href="src/clear_street/types/active/v1/watchlist_create_watchlist_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/watchlist_create_watchlist_response.py">WatchlistCreateWatchlistResponse</a></code>
- <code title="delete /active/v1/watchlists/{watchlist_id}">client.active.v1.watchlists.<a href="./src/clear_street/resources/active/v1/watchlists/watchlists.py">delete_watchlist</a>(watchlist_id) -> None</code>
- <code title="get /active/v1/watchlists/{watchlist_id}">client.active.v1.watchlists.<a href="./src/clear_street/resources/active/v1/watchlists/watchlists.py">get_watchlist_by_id</a>(watchlist_id) -> <a href="./src/clear_street/types/active/v1/watchlist_get_watchlist_by_id_response.py">WatchlistGetWatchlistByIDResponse</a></code>
- <code title="get /active/v1/watchlists">client.active.v1.watchlists.<a href="./src/clear_street/resources/active/v1/watchlists/watchlists.py">get_watchlists</a>() -> <a href="./src/clear_street/types/active/v1/watchlist_get_watchlists_response.py">WatchlistGetWatchlistsResponse</a></code>

#### Items

Types:

```python
from clear_street.types.active.v1.watchlists import (
    AddWatchlistItemData,
    ItemAddWatchlistItemResponse,
)
```

Methods:

- <code title="post /active/v1/watchlists/{watchlist_id}/items">client.active.v1.watchlists.items.<a href="./src/clear_street/resources/active/v1/watchlists/items.py">add_watchlist_item</a>(watchlist_id, \*\*<a href="src/clear_street/types/active/v1/watchlists/item_add_watchlist_item_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/watchlists/item_add_watchlist_item_response.py">ItemAddWatchlistItemResponse</a></code>
- <code title="delete /active/v1/watchlists/{watchlist_id}/items/{item_id}">client.active.v1.watchlists.items.<a href="./src/clear_street/resources/active/v1/watchlists/items.py">delete_watchlist_item</a>(item_id, \*, watchlist_id) -> None</code>

### Ws

Methods:

- <code title="get /active/v1/ws">client.active.v1.ws.<a href="./src/clear_street/resources/active/v1/ws.py">websocket_handler</a>() -> None</code>

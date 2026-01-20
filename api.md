# Shared Types

```python
from clear_street.types import APIError, BaseResponse, ResponseMetadata
```

# Active

## V1

Types:

```python
from clear_street.types.active import SecurityIDSource, SecurityType
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
    Order,
    OrderList,
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
    APITimestamp,
    MarginType,
    RegTBalance,
    BalanceGetAccountBalancesResponse,
)
```

Methods:

- <code title="get /active/v1/accounts/{account_id}/balances">client.active.v1.accounts.balances.<a href="./src/clear_street/resources/active/v1/accounts/balances.py">get_account_balances</a>(account_id) -> <a href="./src/clear_street/types/active/v1/accounts/balance_get_account_balances_response.py">BalanceGetAccountBalancesResponse</a></code>

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
    Destination,
    DmaStrategy,
    OrderStatus,
    OrderStrategy,
    OrderType,
    PovStrategy,
    Side,
    SorStrategy,
    TimeInForce,
    TwapStrategy,
    Urgency,
    VwapStrategy,
    OrderCancelAllOrdersResponse,
    OrderCancelOrderResponse,
    OrderGetOrderByIDResponse,
    OrderGetOrdersResponse,
    OrderReplaceOrderResponse,
    OrderSubmitOrdersResponse,
)
```

Methods:

- <code title="delete /active/v1/accounts/{account_id}/orders">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">cancel_all_orders</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_cancel_all_orders_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_cancel_all_orders_response.py">OrderCancelAllOrdersResponse</a></code>
- <code title="delete /active/v1/accounts/{account_id}/orders/{order_id}">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">cancel_order</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/active/v1/accounts/order_cancel_order_response.py">OrderCancelOrderResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/orders/{order_id}">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">get_order_by_id</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/active/v1/accounts/order_get_order_by_id_response.py">OrderGetOrderByIDResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/orders">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">get_orders</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_get_orders_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_get_orders_response.py">OrderGetOrdersResponse</a></code>
- <code title="patch /active/v1/accounts/{account_id}/orders/{order_id}">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">replace_order</a>(order_id, \*, account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_replace_order_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_replace_order_response.py">OrderReplaceOrderResponse</a></code>
- <code title="post /active/v1/accounts/{account_id}/orders">client.active.v1.accounts.orders.<a href="./src/clear_street/resources/active/v1/accounts/orders.py">submit_orders</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/order_submit_orders_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/order_submit_orders_response.py">OrderSubmitOrdersResponse</a></code>

#### Positions

Types:

```python
from clear_street.types.active.v1.accounts import (
    Position,
    PositionList,
    PositionClosePositionResponse,
    PositionGetPositionsResponse,
)
```

Methods:

- <code title="delete /active/v1/accounts/{account_id}/positions/{security_id_source}/{security_id}">client.active.v1.accounts.positions.<a href="./src/clear_street/resources/active/v1/accounts/positions.py">close_position</a>(security_id, \*, account_id, security_id_source, \*\*<a href="src/clear_street/types/active/v1/accounts/position_close_position_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/position_close_position_response.py">PositionClosePositionResponse</a></code>
- <code title="get /active/v1/accounts/{account_id}/positions">client.active.v1.accounts.positions.<a href="./src/clear_street/resources/active/v1/accounts/positions.py">get_positions</a>(account_id, \*\*<a href="src/clear_street/types/active/v1/accounts/position_get_positions_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/accounts/position_get_positions_response.py">PositionGetPositionsResponse</a></code>

### Assistant

#### Prompts

Types:

```python
from clear_street.types.active.v1.assistant import (
    PromptResult,
    PromptStatus,
    RunPromptResponse,
    PromptGetPromptResultResponse,
    PromptRunPromptResponse,
)
```

Methods:

- <code title="get /active/v1/assistant/prompts/{id}">client.active.v1.assistant.prompts.<a href="./src/clear_street/resources/active/v1/assistant/prompts.py">get_prompt_result</a>(id, \*\*<a href="src/clear_street/types/active/v1/assistant/prompt_get_prompt_result_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/assistant/prompt_get_prompt_result_response.py">PromptGetPromptResultResponse</a></code>
- <code title="post /active/v1/assistant/prompts">client.active.v1.assistant.prompts.<a href="./src/clear_street/resources/active/v1/assistant/prompts.py">run_prompt</a>(\*\*<a href="src/clear_street/types/active/v1/assistant/prompt_run_prompt_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/assistant/prompt_run_prompt_response.py">PromptRunPromptResponse</a></code>

### Calendars

#### Dividends

Types:

```python
from clear_street.types.active.v1.calendars import (
    DividendCalendarEvent,
    DividendCalendarEventList,
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
    EconomicGetEconomicCalendarResponse,
)
```

Methods:

- <code title="get /active/v1/calendars/economic">client.active.v1.calendars.economic.<a href="./src/clear_street/resources/active/v1/calendars/economic.py">get_economic_calendar</a>(\*\*<a href="src/clear_street/types/active/v1/calendars/economic_get_economic_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/calendars/economic_get_economic_calendar_response.py">EconomicGetEconomicCalendarResponse</a></code>

#### MarketHours

Types:

```python
from clear_street.types.active.v1.calendars import (
    MarketHours,
    MarketHoursList,
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

### Instruments

Types:

```python
from clear_street.types.active.v1 import (
    Instrument,
    InstrumentCore,
    InstrumentCoreList,
    InstrumentQuote,
    InstrumentGetInstrumentByIDResponse,
    InstrumentGetInstrumentsResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}">client.active.v1.instruments.<a href="./src/clear_street/resources/active/v1/instruments/instruments.py">get_instrument_by_id</a>(security_id, \*, security_id_source) -> <a href="./src/clear_street/types/active/v1/instrument_get_instrument_by_id_response.py">InstrumentGetInstrumentByIDResponse</a></code>
- <code title="get /active/v1/instruments">client.active.v1.instruments.<a href="./src/clear_street/resources/active/v1/instruments/instruments.py">get_instruments</a>(\*\*<a href="src/clear_street/types/active/v1/instrument_get_instruments_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instrument_get_instruments_response.py">InstrumentGetInstrumentsResponse</a></code>

#### AnalystReporting

Types:

```python
from clear_street.types.active.v1.instruments import (
    AnalystDistribution,
    AnalystRating,
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
    InstrumentEvent,
    InstrumentEventList,
    EventGetInstrumentEventsResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}/events">client.active.v1.instruments.events.<a href="./src/clear_street/resources/active/v1/instruments/events.py">get_instrument_events</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instruments/event_get_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/event_get_instrument_events_response.py">EventGetInstrumentEventsResponse</a></code>

#### News

Types:

```python
from clear_street.types.active.v1.instruments import (
    InstrumentNews,
    InstrumentNewsList,
    NewsGetInstrumentNewsResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}/news">client.active.v1.instruments.news.<a href="./src/clear_street/resources/active/v1/instruments/news.py">get_instrument_news</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instruments/news_get_instrument_news_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/news_get_instrument_news_response.py">NewsGetInstrumentNewsResponse</a></code>

#### Reporting

Types:

```python
from clear_street.types.active.v1.instruments import (
    FiscalPeriodType,
    InstrumentEarnings,
    ReportingGetInstrumentReportingResponse,
)
```

Methods:

- <code title="get /active/v1/instruments/{security_id_source}/{security_id}/reporting">client.active.v1.instruments.reporting.<a href="./src/clear_street/resources/active/v1/instruments/reporting.py">get_instrument_reporting</a>(security_id, \*, security_id_source, \*\*<a href="src/clear_street/types/active/v1/instruments/reporting_get_instrument_reporting_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/instruments/reporting_get_instrument_reporting_response.py">ReportingGetInstrumentReportingResponse</a></code>

#### Venues

Types:

```python
from clear_street.types.active.v1.instruments import Venue, VenueList, VenueGetVenuesResponse
```

Methods:

- <code title="get /active/v1/instruments/venues">client.active.v1.instruments.venues.<a href="./src/clear_street/resources/active/v1/instruments/venues.py">get_venues</a>() -> <a href="./src/clear_street/types/active/v1/instruments/venue_get_venues_response.py">VenueGetVenuesResponse</a></code>

### Screener

Types:

```python
from clear_street.types.active.v1 import ScreenerItem, ScreenerItemList, ScreenerGetScreenerResponse
```

Methods:

- <code title="get /active/v1/screener">client.active.v1.screener.<a href="./src/clear_street/resources/active/v1/screener.py">get_screener</a>(\*\*<a href="src/clear_street/types/active/v1/screener_get_screener_params.py">params</a>) -> <a href="./src/clear_street/types/active/v1/screener_get_screener_response.py">ScreenerGetScreenerResponse</a></code>

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

### Ws

Methods:

- <code title="get /active/v1/ws">client.active.v1.ws.<a href="./src/clear_street/resources/active/v1/ws.py">websocket_handler</a>() -> None</code>

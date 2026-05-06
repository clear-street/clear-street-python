# Shared Types

```python
from clear_street.types import APIError, BaseResponse, ResponseMetadata
```

# V1

Types:

```python
from clear_street.types import SecurityType
```

Methods:

- <code title="get /v1/ws">client.v1.<a href="./src/clear_street/resources/v1/v1.py">websocket_handler</a>() -> None</code>

## Accounts

Types:

```python
from clear_street.types.v1 import (
    Account,
    AccountList,
    AccountSettings,
    AccountStatus,
    AccountSubtype,
    AccountType,
    RiskSettings,
    AccountGetAccountByIDResponse,
    AccountGetAccountsResponse,
    AccountPatchAccountByIDResponse,
)
```

Methods:

- <code title="get /v1/accounts/{account_id}">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts/accounts.py">get_account_by_id</a>(account_id) -> <a href="./src/clear_street/types/v1/account_get_account_by_id_response.py">AccountGetAccountByIDResponse</a></code>
- <code title="get /v1/accounts">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts/accounts.py">get_accounts</a>(\*\*<a href="src/clear_street/types/v1/account_get_accounts_params.py">params</a>) -> <a href="./src/clear_street/types/v1/account_get_accounts_response.py">AccountGetAccountsResponse</a></code>
- <code title="patch /v1/accounts/{account_id}">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts/accounts.py">patch_account_by_id</a>(account_id, \*\*<a href="src/clear_street/types/v1/account_patch_account_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/account_patch_account_by_id_response.py">AccountPatchAccountByIDResponse</a></code>

### Balances

Types:

```python
from clear_street.types.v1.accounts import (
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

- <code title="get /v1/accounts/{account_id}/balances">client.v1.accounts.balances.<a href="./src/clear_street/resources/v1/accounts/balances.py">get_account_balances</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/balance_get_account_balances_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/balance_get_account_balances_response.py">BalanceGetAccountBalancesResponse</a></code>

### Orders

Types:

```python
from clear_street.types.v1.accounts import (
    CancelOrderRequest,
    InstrumentIDOrSymbol,
    NewOrderRequest,
    Order,
    OrderList,
    OrderStatus,
    OrderType,
    PositionEffect,
    QueueState,
    RequestOrderType,
    RequestTimeInForce,
    Side,
    TimeInForce,
    TrailingOffsetType,
    OrderCancelAllOpenOrdersResponse,
    OrderCancelOpenOrderResponse,
    OrderGetOrderByIDResponse,
    OrderGetOrdersResponse,
    OrderReplaceOrderResponse,
    OrderSubmitOrdersResponse,
)
```

Methods:

- <code title="delete /v1/accounts/{account_id}/orders">client.v1.accounts.orders.<a href="./src/clear_street/resources/v1/accounts/orders.py">cancel_all_open_orders</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/order_cancel_all_open_orders_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/order_cancel_all_open_orders_response.py">OrderCancelAllOpenOrdersResponse</a></code>
- <code title="delete /v1/accounts/{account_id}/orders/{order_id}">client.v1.accounts.orders.<a href="./src/clear_street/resources/v1/accounts/orders.py">cancel_open_order</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/v1/accounts/order_cancel_open_order_response.py">OrderCancelOpenOrderResponse</a></code>
- <code title="get /v1/accounts/{account_id}/orders/{order_id}">client.v1.accounts.orders.<a href="./src/clear_street/resources/v1/accounts/orders.py">get_order_by_id</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/v1/accounts/order_get_order_by_id_response.py">OrderGetOrderByIDResponse</a></code>
- <code title="get /v1/accounts/{account_id}/orders">client.v1.accounts.orders.<a href="./src/clear_street/resources/v1/accounts/orders.py">get_orders</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/order_get_orders_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/order_get_orders_response.py">OrderGetOrdersResponse</a></code>
- <code title="patch /v1/accounts/{account_id}/orders/{order_id}">client.v1.accounts.orders.<a href="./src/clear_street/resources/v1/accounts/orders.py">replace_order</a>(order_id, \*, account_id, \*\*<a href="src/clear_street/types/v1/accounts/order_replace_order_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/order_replace_order_response.py">OrderReplaceOrderResponse</a></code>
- <code title="post /v1/accounts/{account_id}/orders">client.v1.accounts.orders.<a href="./src/clear_street/resources/v1/accounts/orders.py">submit_orders</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/order_submit_orders_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/order_submit_orders_response.py">OrderSubmitOrdersResponse</a></code>

### PortfolioHistory

Types:

```python
from clear_street.types.v1.accounts import (
    PortfolioHistoryResponse,
    PortfolioHistorySegment,
    PortfolioHistoryGetPortfolioHistoryResponse,
)
```

Methods:

- <code title="get /v1/accounts/{account_id}/portfolio-history">client.v1.accounts.portfolio_history.<a href="./src/clear_street/resources/v1/accounts/portfolio_history.py">get_portfolio_history</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/portfolio_history_get_portfolio_history_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/portfolio_history_get_portfolio_history_response.py">PortfolioHistoryGetPortfolioHistoryResponse</a></code>

### Positions

Types:

```python
from clear_street.types.v1.accounts import (
    Position,
    PositionList,
    PositionType,
    PositionClosePositionResponse,
    PositionClosePositionsResponse,
    PositionGetPositionsResponse,
)
```

Methods:

- <code title="delete /v1/accounts/{account_id}/positions/{instrument_id}">client.v1.accounts.positions.<a href="./src/clear_street/resources/v1/accounts/positions.py">close_position</a>(instrument_id, \*, account_id, \*\*<a href="src/clear_street/types/v1/accounts/position_close_position_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/position_close_position_response.py">PositionClosePositionResponse</a></code>
- <code title="delete /v1/accounts/{account_id}/positions">client.v1.accounts.positions.<a href="./src/clear_street/resources/v1/accounts/positions.py">close_positions</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/position_close_positions_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/position_close_positions_response.py">PositionClosePositionsResponse</a></code>
- <code title="get /v1/accounts/{account_id}/positions">client.v1.accounts.positions.<a href="./src/clear_street/resources/v1/accounts/positions.py">get_positions</a>(account_id, \*\*<a href="src/clear_street/types/v1/accounts/position_get_positions_params.py">params</a>) -> <a href="./src/clear_street/types/v1/accounts/position_get_positions_response.py">PositionGetPositionsResponse</a></code>

## Calendars

### MarketHours

Types:

```python
from clear_street.types.v1.calendars import (
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

- <code title="get /v1/calendars/market-hours">client.v1.calendars.market_hours.<a href="./src/clear_street/resources/v1/calendars/market_hours.py">get_market_hours_calendar</a>(\*\*<a href="src/clear_street/types/v1/calendars/market_hour_get_market_hours_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/v1/calendars/market_hour_get_market_hours_calendar_response.py">MarketHourGetMarketHoursCalendarResponse</a></code>

## Clock

Types:

```python
from clear_street.types.v1 import ClockDetail, ClockGetClockResponse
```

Methods:

- <code title="get /v1/clock">client.v1.clock.<a href="./src/clear_street/resources/v1/clock.py">get_clock</a>() -> <a href="./src/clear_street/types/v1/clock_get_clock_response.py">ClockGetClockResponse</a></code>

## Instruments

Types:

```python
from clear_street.types.v1 import (
    AnalystRating,
    ContractType,
    ExerciseStyle,
    FiscalPeriodType,
    Instrument,
    InstrumentCore,
    InstrumentCoreList,
    InstrumentEarnings,
    ListingType,
    OptionsContract,
    OptionsContractList,
    InstrumentGetInstrumentByIDResponse,
    InstrumentGetInstrumentsResponse,
    InstrumentSearchInstrumentsResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments/instruments.py">get_instrument_by_id</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_get_instrument_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_get_instrument_by_id_response.py">InstrumentGetInstrumentByIDResponse</a></code>
- <code title="get /v1/instruments">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments/instruments.py">get_instruments</a>(\*\*<a href="src/clear_street/types/v1/instrument_get_instruments_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_get_instruments_response.py">InstrumentGetInstrumentsResponse</a></code>
- <code title="get /v1/instruments/search">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments/instruments.py">search_instruments</a>(\*\*<a href="src/clear_street/types/v1/instrument_search_instruments_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_search_instruments_response.py">InstrumentSearchInstrumentsResponse</a></code>

### AnalystReporting

Types:

```python
from clear_street.types.v1.instruments import (
    AnalystDistribution,
    InstrumentAnalystConsensus,
    PriceTarget,
    AnalystReportingGetInstrumentAnalystConsensusResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}/analyst-reporting">client.v1.instruments.analyst_reporting.<a href="./src/clear_street/resources/v1/instruments/analyst_reporting.py">get_instrument_analyst_consensus</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instruments/analyst_reporting_get_instrument_analyst_consensus_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/analyst_reporting_get_instrument_analyst_consensus_response.py">AnalystReportingGetInstrumentAnalystConsensusResponse</a></code>

### BalanceSheets

Types:

```python
from clear_street.types.v1.instruments import (
    InstrumentBalanceSheetStatement,
    InstrumentBalanceSheetStatementList,
    BalanceSheetGetInstrumentBalanceSheetStatementsResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}/balance-sheets">client.v1.instruments.balance_sheets.<a href="./src/clear_street/resources/v1/instruments/balance_sheets.py">get_instrument_balance_sheet_statements</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instruments/balance_sheet_get_instrument_balance_sheet_statements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/balance_sheet_get_instrument_balance_sheet_statements_response.py">BalanceSheetGetInstrumentBalanceSheetStatementsResponse</a></code>

### CashFlowStatements

Types:

```python
from clear_street.types.v1.instruments import (
    InstrumentCashFlowStatement,
    InstrumentCashFlowStatementList,
    CashFlowStatementGetInstrumentCashFlowStatementsResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}/cash-flow-statements">client.v1.instruments.cash_flow_statements.<a href="./src/clear_street/resources/v1/instruments/cash_flow_statements.py">get_instrument_cash_flow_statements</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instruments/cash_flow_statement_get_instrument_cash_flow_statements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/cash_flow_statement_get_instrument_cash_flow_statements_response.py">CashFlowStatementGetInstrumentCashFlowStatementsResponse</a></code>

### Events

Types:

```python
from clear_street.types.v1.instruments import (
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

- <code title="get /v1/instruments/events">client.v1.instruments.events.<a href="./src/clear_street/resources/v1/instruments/events.py">get_all_instrument_events</a>(\*\*<a href="src/clear_street/types/v1/instruments/event_get_all_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/event_get_all_instrument_events_response.py">EventGetAllInstrumentEventsResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/events">client.v1.instruments.events.<a href="./src/clear_street/resources/v1/instruments/events.py">get_instrument_events</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instruments/event_get_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/event_get_instrument_events_response.py">EventGetInstrumentEventsResponse</a></code>

### Fundamentals

Types:

```python
from clear_street.types.v1.instruments import (
    InstrumentFundamentals,
    FundamentalGetInstrumentFundamentalsResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}/fundamentals">client.v1.instruments.fundamentals.<a href="./src/clear_street/resources/v1/instruments/fundamentals.py">get_instrument_fundamentals</a>(instrument_id) -> <a href="./src/clear_street/types/v1/instruments/fundamental_get_instrument_fundamentals_response.py">FundamentalGetInstrumentFundamentalsResponse</a></code>

### IncomeStatements

Types:

```python
from clear_street.types.v1.instruments import (
    InstrumentIncomeStatement,
    InstrumentIncomeStatementList,
    IncomeStatementGetInstrumentIncomeStatementsResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}/income-statements">client.v1.instruments.income_statements.<a href="./src/clear_street/resources/v1/instruments/income_statements.py">get_instrument_income_statements</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instruments/income_statement_get_instrument_income_statements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/income_statement_get_instrument_income_statements_response.py">IncomeStatementGetInstrumentIncomeStatementsResponse</a></code>

### Options

Types:

```python
from clear_street.types.v1.instruments import OptionGetOptionContractsResponse
```

Methods:

- <code title="get /v1/instruments/options/contracts">client.v1.instruments.options.<a href="./src/clear_street/resources/v1/instruments/options.py">get_option_contracts</a>(\*\*<a href="src/clear_street/types/v1/instruments/option_get_option_contracts_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instruments/option_get_option_contracts_response.py">OptionGetOptionContractsResponse</a></code>

## MarketData

### DailySummary

Types:

```python
from clear_street.types.v1.market_data import (
    DailySummary,
    DailySummaryList,
    DailySummaryGetDailySummariesResponse,
)
```

Methods:

- <code title="get /v1/market-data/daily-summary">client.v1.market_data.daily_summary.<a href="./src/clear_street/resources/v1/market_data/daily_summary.py">get_daily_summaries</a>(\*\*<a href="src/clear_street/types/v1/market_data/daily_summary_get_daily_summaries_params.py">params</a>) -> <a href="./src/clear_street/types/v1/market_data/daily_summary_get_daily_summaries_response.py">DailySummaryGetDailySummariesResponse</a></code>

### Snapshot

Types:

```python
from clear_street.types.v1.market_data import (
    MarketDataSnapshot,
    MarketDataSnapshotList,
    SnapshotLastTrade,
    SnapshotQuote,
    SnapshotSession,
    SnapshotGetSnapshotsResponse,
)
```

Methods:

- <code title="get /v1/market-data/snapshot">client.v1.market_data.snapshot.<a href="./src/clear_street/resources/v1/market_data/snapshot.py">get_snapshots</a>(\*\*<a href="src/clear_street/types/v1/market_data/snapshot_get_snapshots_params.py">params</a>) -> <a href="./src/clear_street/types/v1/market_data/snapshot_get_snapshots_response.py">SnapshotGetSnapshotsResponse</a></code>

## News

Types:

```python
from clear_street.types.v1 import (
    NewsInstrument,
    NewsItem,
    NewsItemList,
    NewsType,
    NewsGetNewsResponse,
)
```

Methods:

- <code title="get /v1/news">client.v1.news.<a href="./src/clear_street/resources/v1/news.py">get_news</a>(\*\*<a href="src/clear_street/types/v1/news_get_news_params.py">params</a>) -> <a href="./src/clear_street/types/v1/news_get_news_response.py">NewsGetNewsResponse</a></code>

## OmniAI

Types:

```python
from clear_street.types.v1 import (
    ActionButton,
    CancelResponsePayload,
    ChartPayload,
    ChartPoint,
    ChartSeries,
    ContentPartChartPayload,
    ContentPartCustomPayload,
    ContentPartStructuredActionPayload,
    ContentPartSuggestedActionsPayload,
    ContentPartTextPayload,
    ContentPartThinkingPayload,
    CreateFeedbackResponse,
    CreateMessageResponse,
    CreateThreadResponse,
    DataChart,
    EntitlementAgreementKey,
    EntitlementCode,
    ErrorStatus,
    Message,
    MessageContent,
    MessageContentPart,
    MessageList,
    MessageOutcome,
    MessageRole,
    OpenChartAction,
    OpenEntitlementConsentAction,
    OpenScreenerAction,
    PrefillCancelOrderAction,
    PrefillNewOrderAction,
    PrefillOrderAction,
    PromptButtonAction,
    Response,
    ResponseContent,
    ResponseContentPart,
    ResponseStatus,
    StructuredAction,
    StructuredActionButtonAction,
    SuggestedActionsPayload,
    SymbolChart,
    Thread,
    ThreadList,
)
```

### EntitlementAgreements

Types:

```python
from clear_street.types.v1.omni_ai import (
    EntitlementAgreementResource,
    EntitlementAgreementResourceList,
    EntitlementAgreementGetEntitlementAgreementsResponse,
)
```

Methods:

- <code title="get /v1/omni-ai/entitlement-agreements">client.v1.omni_ai.entitlement_agreements.<a href="./src/clear_street/resources/v1/omni_ai/entitlement_agreements.py">get_entitlement_agreements</a>() -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_agreement_get_entitlement_agreements_response.py">EntitlementAgreementGetEntitlementAgreementsResponse</a></code>

### Entitlements

Types:

```python
from clear_street.types.v1.omni_ai import (
    DeleteEntitlementResponse,
    EntitlementResource,
    EntitlementResourceList,
    EntitlementCreateEntitlementsResponse,
    EntitlementDeleteEntitlementResponse,
    EntitlementGetEntitlementsResponse,
)
```

Methods:

- <code title="post /v1/omni-ai/entitlements">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">create_entitlements</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/entitlement_create_entitlements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_create_entitlements_response.py">EntitlementCreateEntitlementsResponse</a></code>
- <code title="delete /v1/omni-ai/entitlements/{entitlement_id}">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">delete_entitlement</a>(entitlement_id) -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_delete_entitlement_response.py">EntitlementDeleteEntitlementResponse</a></code>
- <code title="get /v1/omni-ai/entitlements">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">get_entitlements</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/entitlement_get_entitlements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_get_entitlements_response.py">EntitlementGetEntitlementsResponse</a></code>

### Messages

Types:

```python
from clear_street.types.v1.omni_ai import (
    MessageGetMessageByIDResponse,
    MessageSubmitFeedbackResponse,
)
```

Methods:

- <code title="get /v1/omni-ai/messages/{message_id}">client.v1.omni_ai.messages.<a href="./src/clear_street/resources/v1/omni_ai/messages.py">get_message_by_id</a>(message_id, \*\*<a href="src/clear_street/types/v1/omni_ai/message_get_message_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/message_get_message_by_id_response.py">MessageGetMessageByIDResponse</a></code>
- <code title="post /v1/omni-ai/messages/{message_id}/feedback">client.v1.omni_ai.messages.<a href="./src/clear_street/resources/v1/omni_ai/messages.py">submit_feedback</a>(message_id, \*\*<a href="src/clear_street/types/v1/omni_ai/message_submit_feedback_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/message_submit_feedback_response.py">MessageSubmitFeedbackResponse</a></code>

### Responses

Types:

```python
from clear_street.types.v1.omni_ai import (
    ResponseCancelResponseResponse,
    ResponseGetResponseByIDResponse,
)
```

Methods:

- <code title="delete /v1/omni-ai/responses/{response_id}">client.v1.omni_ai.responses.<a href="./src/clear_street/resources/v1/omni_ai/responses.py">cancel_response</a>(response_id, \*\*<a href="src/clear_street/types/v1/omni_ai/response_cancel_response_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/response_cancel_response_response.py">ResponseCancelResponseResponse</a></code>
- <code title="get /v1/omni-ai/responses/{response_id}">client.v1.omni_ai.responses.<a href="./src/clear_street/resources/v1/omni_ai/responses.py">get_response_by_id</a>(response_id, \*\*<a href="src/clear_street/types/v1/omni_ai/response_get_response_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/response_get_response_by_id_response.py">ResponseGetResponseByIDResponse</a></code>

### Threads

Types:

```python
from clear_street.types.v1.omni_ai import (
    ThreadCreateThreadResponse,
    ThreadGetThreadByIDResponse,
    ThreadGetThreadResponseResponse,
    ThreadGetThreadsResponse,
)
```

Methods:

- <code title="post /v1/omni-ai/threads">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads/threads.py">create_thread</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/thread_create_thread_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_create_thread_response.py">ThreadCreateThreadResponse</a></code>
- <code title="get /v1/omni-ai/threads/{thread_id}">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads/threads.py">get_thread_by_id</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_thread_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_thread_by_id_response.py">ThreadGetThreadByIDResponse</a></code>
- <code title="get /v1/omni-ai/threads/{thread_id}/response">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads/threads.py">get_thread_response</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_thread_response_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_thread_response_response.py">ThreadGetThreadResponseResponse</a></code>
- <code title="get /v1/omni-ai/threads">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads/threads.py">get_threads</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_threads_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_threads_response.py">ThreadGetThreadsResponse</a></code>

#### Messages

Types:

```python
from clear_street.types.v1.omni_ai.threads import (
    MessageCreateMessageResponse,
    MessageGetMessagesResponse,
)
```

Methods:

- <code title="post /v1/omni-ai/threads/{thread_id}/messages">client.v1.omni_ai.threads.messages.<a href="./src/clear_street/resources/v1/omni_ai/threads/messages.py">create_message</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/threads/message_create_message_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/threads/message_create_message_response.py">MessageCreateMessageResponse</a></code>
- <code title="get /v1/omni-ai/threads/{thread_id}/messages">client.v1.omni_ai.threads.messages.<a href="./src/clear_street/resources/v1/omni_ai/threads/messages.py">get_messages</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/threads/message_get_messages_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/threads/message_get_messages_response.py">MessageGetMessagesResponse</a></code>

## SavedScreeners

Types:

```python
from clear_street.types.v1 import (
    ScreenerEntry,
    ScreenerEntryList,
    SavedScreenerCreateScreenerResponse,
    SavedScreenerGetScreenerByIDResponse,
    SavedScreenerGetScreenersResponse,
    SavedScreenerReplaceScreenerResponse,
)
```

Methods:

- <code title="post /v1/saved-screeners">client.v1.saved_screeners.<a href="./src/clear_street/resources/v1/saved_screeners.py">create_screener</a>(\*\*<a href="src/clear_street/types/v1/saved_screener_create_screener_params.py">params</a>) -> <a href="./src/clear_street/types/v1/saved_screener_create_screener_response.py">SavedScreenerCreateScreenerResponse</a></code>
- <code title="delete /v1/saved-screeners/{screener_id}">client.v1.saved_screeners.<a href="./src/clear_street/resources/v1/saved_screeners.py">delete_screener</a>(screener_id) -> None</code>
- <code title="get /v1/saved-screeners/{screener_id}">client.v1.saved_screeners.<a href="./src/clear_street/resources/v1/saved_screeners.py">get_screener_by_id</a>(screener_id) -> <a href="./src/clear_street/types/v1/saved_screener_get_screener_by_id_response.py">SavedScreenerGetScreenerByIDResponse</a></code>
- <code title="get /v1/saved-screeners">client.v1.saved_screeners.<a href="./src/clear_street/resources/v1/saved_screeners.py">get_screeners</a>() -> <a href="./src/clear_street/types/v1/saved_screener_get_screeners_response.py">SavedScreenerGetScreenersResponse</a></code>
- <code title="put /v1/saved-screeners/{screener_id}">client.v1.saved_screeners.<a href="./src/clear_street/resources/v1/saved_screeners.py">replace_screener</a>(screener_id, \*\*<a href="src/clear_street/types/v1/saved_screener_replace_screener_params.py">params</a>) -> <a href="./src/clear_street/types/v1/saved_screener_replace_screener_response.py">SavedScreenerReplaceScreenerResponse</a></code>

## Screener

Types:

```python
from clear_street.types.v1 import (
    FieldLookback,
    FieldPeriod,
    FieldRef,
    FieldType,
    FilterOpSpec,
    FilterOperator,
    FilterValue,
    Modifier,
    ModifierOp,
    OperatorArg,
    ScreenerColumn,
    ScreenerFilter,
    ScreenerItem,
    ScreenerItemList,
    ScreenerRow,
    ScreenerRowList,
    SearchFilter,
    Variable,
    ScreenerGetScreenerResponse,
    ScreenerSearchScreenerResponse,
)
```

Methods:

- <code title="get /v1/screener">client.v1.screener.<a href="./src/clear_street/resources/v1/screener.py">get_screener</a>(\*\*<a href="src/clear_street/types/v1/screener_get_screener_params.py">params</a>) -> <a href="./src/clear_street/types/v1/screener_get_screener_response.py">ScreenerGetScreenerResponse</a></code>
- <code title="post /v1/screener">client.v1.screener.<a href="./src/clear_street/resources/v1/screener.py">search_screener</a>(\*\*<a href="src/clear_street/types/v1/screener_search_screener_params.py">params</a>) -> <a href="./src/clear_street/types/v1/screener_search_screener_response.py">ScreenerSearchScreenerResponse</a></code>

## Version

Types:

```python
from clear_street.types.v1 import Version, VersionGetVersionResponse
```

Methods:

- <code title="get /v1/version">client.v1.version.<a href="./src/clear_street/resources/v1/version.py">get_version</a>() -> <a href="./src/clear_street/types/v1/version_get_version_response.py">VersionGetVersionResponse</a></code>

## Watchlists

Types:

```python
from clear_street.types.v1 import (
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

- <code title="post /v1/watchlists">client.v1.watchlists.<a href="./src/clear_street/resources/v1/watchlists/watchlists.py">create_watchlist</a>(\*\*<a href="src/clear_street/types/v1/watchlist_create_watchlist_params.py">params</a>) -> <a href="./src/clear_street/types/v1/watchlist_create_watchlist_response.py">WatchlistCreateWatchlistResponse</a></code>
- <code title="delete /v1/watchlists/{watchlist_id}">client.v1.watchlists.<a href="./src/clear_street/resources/v1/watchlists/watchlists.py">delete_watchlist</a>(watchlist_id) -> object</code>
- <code title="get /v1/watchlists/{watchlist_id}">client.v1.watchlists.<a href="./src/clear_street/resources/v1/watchlists/watchlists.py">get_watchlist_by_id</a>(watchlist_id) -> <a href="./src/clear_street/types/v1/watchlist_get_watchlist_by_id_response.py">WatchlistGetWatchlistByIDResponse</a></code>
- <code title="get /v1/watchlists">client.v1.watchlists.<a href="./src/clear_street/resources/v1/watchlists/watchlists.py">get_watchlists</a>(\*\*<a href="src/clear_street/types/v1/watchlist_get_watchlists_params.py">params</a>) -> <a href="./src/clear_street/types/v1/watchlist_get_watchlists_response.py">WatchlistGetWatchlistsResponse</a></code>

### Items

Types:

```python
from clear_street.types.v1.watchlists import AddWatchlistItemData, ItemAddWatchlistItemResponse
```

Methods:

- <code title="post /v1/watchlists/{watchlist_id}/items">client.v1.watchlists.items.<a href="./src/clear_street/resources/v1/watchlists/items.py">add_watchlist_item</a>(watchlist_id, \*\*<a href="src/clear_street/types/v1/watchlists/item_add_watchlist_item_params.py">params</a>) -> <a href="./src/clear_street/types/v1/watchlists/item_add_watchlist_item_response.py">ItemAddWatchlistItemResponse</a></code>
- <code title="delete /v1/watchlists/{watchlist_id}/items/{item_id}">client.v1.watchlists.items.<a href="./src/clear_street/resources/v1/watchlists/items.py">delete_watchlist_item</a>(item_id, \*, watchlist_id) -> object</code>

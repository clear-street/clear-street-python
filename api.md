# Shared Types

```python
from clear_street.types import APIError, BaseResponse, ResponseMetadata
```

# V1

Types:

```python
from clear_street.types import SecurityType
```

## Accounts

Types:

```python
from clear_street.types.v1 import (
    Account,
    AccountBalances,
    AccountBalancesSod,
    AccountList,
    AccountSettings,
    AccountStatus,
    AccountSubtype,
    AccountType,
    MarginDetails,
    MarginDetailsUsage,
    MarginTopContributor,
    MarginType,
    PortfolioHistoryResponse,
    PortfolioHistorySegment,
    RiskSettings,
    AccountGetAccountBalancesResponse,
    AccountGetAccountByIDResponse,
    AccountGetAccountsResponse,
    AccountGetPortfolioHistoryResponse,
    AccountPatchAccountByIDResponse,
)
```

Methods:

- <code title="get /v1/accounts/{account_id}/balances">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts.py">get_account_balances</a>(account_id, \*\*<a href="src/clear_street/types/v1/account_get_account_balances_params.py">params</a>) -> <a href="./src/clear_street/types/v1/account_get_account_balances_response.py">AccountGetAccountBalancesResponse</a></code>
- <code title="get /v1/accounts/{account_id}">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts.py">get_account_by_id</a>(account_id) -> <a href="./src/clear_street/types/v1/account_get_account_by_id_response.py">AccountGetAccountByIDResponse</a></code>
- <code title="get /v1/accounts">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts.py">get_accounts</a>(\*\*<a href="src/clear_street/types/v1/account_get_accounts_params.py">params</a>) -> <a href="./src/clear_street/types/v1/account_get_accounts_response.py">AccountGetAccountsResponse</a></code>
- <code title="get /v1/accounts/{account_id}/portfolio-history">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts.py">get_portfolio_history</a>(account_id, \*\*<a href="src/clear_street/types/v1/account_get_portfolio_history_params.py">params</a>) -> <a href="./src/clear_street/types/v1/account_get_portfolio_history_response.py">AccountGetPortfolioHistoryResponse</a></code>
- <code title="patch /v1/accounts/{account_id}">client.v1.accounts.<a href="./src/clear_street/resources/v1/accounts.py">patch_account_by_id</a>(account_id, \*\*<a href="src/clear_street/types/v1/account_patch_account_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/account_patch_account_by_id_response.py">AccountPatchAccountByIDResponse</a></code>

## APIVersion

Types:

```python
from clear_street.types.v1 import Version, APIVersionGetVersionResponse
```

Methods:

- <code title="get /v1/version">client.v1.api_version.<a href="./src/clear_street/resources/v1/api_version.py">get_version</a>() -> <a href="./src/clear_street/types/v1/api_version_get_version_response.py">APIVersionGetVersionResponse</a></code>

## Calendar

Types:

```python
from clear_street.types.v1 import (
    ClockDetail,
    DayType,
    MarketHoursDetail,
    MarketHoursDetailList,
    MarketSessionType,
    MarketStatus,
    MarketType,
    SessionSchedule,
    TradingSessions,
    CalendarGetClockResponse,
    CalendarGetMarketHoursCalendarResponse,
)
```

Methods:

- <code title="get /v1/clock">client.v1.calendar.<a href="./src/clear_street/resources/v1/calendar.py">get_clock</a>() -> <a href="./src/clear_street/types/v1/calendar_get_clock_response.py">CalendarGetClockResponse</a></code>
- <code title="get /v1/calendars/market-hours">client.v1.calendar.<a href="./src/clear_street/resources/v1/calendar.py">get_market_hours_calendar</a>(\*\*<a href="src/clear_street/types/v1/calendar_get_market_hours_calendar_params.py">params</a>) -> <a href="./src/clear_street/types/v1/calendar_get_market_hours_calendar_response.py">CalendarGetMarketHoursCalendarResponse</a></code>

## InstrumentData

Types:

```python
from clear_street.types.v1 import (
    AllEventsEventType,
    AnalystDistribution,
    AnalystRating,
    FiscalPeriodType,
    InstrumentAllEventsData,
    InstrumentAnalystConsensus,
    InstrumentBalanceSheetStatement,
    InstrumentBalanceSheetStatementList,
    InstrumentCashFlowStatement,
    InstrumentCashFlowStatementList,
    InstrumentDividendEvent,
    InstrumentEarnings,
    InstrumentEventEnvelope,
    InstrumentEventIpoItem,
    InstrumentEventsByDate,
    InstrumentEventsData,
    InstrumentFundamentals,
    InstrumentIncomeStatement,
    InstrumentIncomeStatementList,
    InstrumentSplitEvent,
    PriceTarget,
    InstrumentDataGetAllInstrumentEventsResponse,
    InstrumentDataGetInstrumentAnalystConsensusResponse,
    InstrumentDataGetInstrumentBalanceSheetStatementsResponse,
    InstrumentDataGetInstrumentCashFlowStatementsResponse,
    InstrumentDataGetInstrumentEventsResponse,
    InstrumentDataGetInstrumentFundamentalsResponse,
    InstrumentDataGetInstrumentIncomeStatementsResponse,
)
```

Methods:

- <code title="get /v1/instruments/events">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_all_instrument_events</a>(\*\*<a href="src/clear_street/types/v1/instrument_data_get_all_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data_get_all_instrument_events_response.py">InstrumentDataGetAllInstrumentEventsResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/analyst-reporting">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_instrument_analyst_consensus</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_data_get_instrument_analyst_consensus_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data_get_instrument_analyst_consensus_response.py">InstrumentDataGetInstrumentAnalystConsensusResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/balance-sheets">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_instrument_balance_sheet_statements</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_data_get_instrument_balance_sheet_statements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data_get_instrument_balance_sheet_statements_response.py">InstrumentDataGetInstrumentBalanceSheetStatementsResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/cash-flow-statements">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_instrument_cash_flow_statements</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_data_get_instrument_cash_flow_statements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data_get_instrument_cash_flow_statements_response.py">InstrumentDataGetInstrumentCashFlowStatementsResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/events">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_instrument_events</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_data_get_instrument_events_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data_get_instrument_events_response.py">InstrumentDataGetInstrumentEventsResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/fundamentals">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_instrument_fundamentals</a>(instrument_id) -> <a href="./src/clear_street/types/v1/instrument_data_get_instrument_fundamentals_response.py">InstrumentDataGetInstrumentFundamentalsResponse</a></code>
- <code title="get /v1/instruments/{instrument_id}/income-statements">client.v1.instrument_data.<a href="./src/clear_street/resources/v1/instrument_data/instrument_data.py">get_instrument_income_statements</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_data_get_instrument_income_statements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data_get_instrument_income_statements_response.py">InstrumentDataGetInstrumentIncomeStatementsResponse</a></code>

### MarketData

Types:

```python
from clear_street.types.v1.instrument_data import (
    DailySummary,
    DailySummaryList,
    MarketDataSnapshot,
    MarketDataSnapshotList,
    SnapshotLastTrade,
    SnapshotQuote,
    SnapshotSession,
    MarketDataGetDailySummariesResponse,
    MarketDataGetSnapshotsResponse,
)
```

Methods:

- <code title="get /v1/market-data/daily-summary">client.v1.instrument_data.market_data.<a href="./src/clear_street/resources/v1/instrument_data/market_data.py">get_daily_summaries</a>(\*\*<a href="src/clear_street/types/v1/instrument_data/market_data_get_daily_summaries_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data/market_data_get_daily_summaries_response.py">MarketDataGetDailySummariesResponse</a></code>
- <code title="get /v1/market-data/snapshot">client.v1.instrument_data.market_data.<a href="./src/clear_street/resources/v1/instrument_data/market_data.py">get_snapshots</a>(\*\*<a href="src/clear_street/types/v1/instrument_data/market_data_get_snapshots_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data/market_data_get_snapshots_response.py">MarketDataGetSnapshotsResponse</a></code>

### News

Types:

```python
from clear_street.types.v1.instrument_data import (
    NewsInstrument,
    NewsItem,
    NewsItemList,
    NewsType,
    NewsGetNewsResponse,
)
```

Methods:

- <code title="get /v1/news">client.v1.instrument_data.news.<a href="./src/clear_street/resources/v1/instrument_data/news.py">get_news</a>(\*\*<a href="src/clear_street/types/v1/instrument_data/news_get_news_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_data/news_get_news_response.py">NewsGetNewsResponse</a></code>

## Instruments

Types:

```python
from clear_street.types.v1 import (
    ContractType,
    ExerciseStyle,
    Instrument,
    InstrumentCore,
    InstrumentCoreList,
    ListingType,
    OptionsContract,
    OptionsContractList,
    InstrumentGetInstrumentByIDResponse,
    InstrumentGetInstrumentsResponse,
    InstrumentGetOptionContractsResponse,
    InstrumentSearchInstrumentsResponse,
)
```

Methods:

- <code title="get /v1/instruments/{instrument_id}">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments.py">get_instrument_by_id</a>(instrument_id, \*\*<a href="src/clear_street/types/v1/instrument_get_instrument_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_get_instrument_by_id_response.py">InstrumentGetInstrumentByIDResponse</a></code>
- <code title="get /v1/instruments">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments.py">get_instruments</a>(\*\*<a href="src/clear_street/types/v1/instrument_get_instruments_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_get_instruments_response.py">InstrumentGetInstrumentsResponse</a></code>
- <code title="get /v1/instruments/options/contracts">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments.py">get_option_contracts</a>(\*\*<a href="src/clear_street/types/v1/instrument_get_option_contracts_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_get_option_contracts_response.py">InstrumentGetOptionContractsResponse</a></code>
- <code title="get /v1/instruments/search">client.v1.instruments.<a href="./src/clear_street/resources/v1/instruments.py">search_instruments</a>(\*\*<a href="src/clear_street/types/v1/instrument_search_instruments_params.py">params</a>) -> <a href="./src/clear_street/types/v1/instrument_search_instruments_response.py">InstrumentSearchInstrumentsResponse</a></code>

## OmniAI

Types:

```python
from clear_street.types.v1 import (
    ActionButton,
    ChartPayload,
    ChartPoint,
    ChartSeries,
    ContentPartChartPayload,
    ContentPartCustomPayload,
    ContentPartStructuredActionPayload,
    ContentPartSuggestedActionsPayload,
    ContentPartTextPayload,
    ContentPartThinkingPayload,
    DataChart,
    OpenChartAction,
    OpenEntitlementConsentAction,
    OpenScreenerAction,
    PrefillCancelOrderAction,
    PrefillNewOrderAction,
    PrefillOrderAction,
    PromptButtonAction,
    ScreenerFilter,
    StructuredAction,
    StructuredActionButtonAction,
    SuggestedActionsPayload,
)
```

### Entitlements

Types:

```python
from clear_street.types.v1.omni_ai import (
    DeleteEntitlementResponse,
    EntitlementAgreementKey,
    EntitlementAgreementResource,
    EntitlementAgreementResourceList,
    EntitlementCode,
    EntitlementResource,
    EntitlementResourceList,
    EntitlementCreateEntitlementsResponse,
    EntitlementDeleteEntitlementResponse,
    EntitlementGetEntitlementAgreementsResponse,
    EntitlementGetEntitlementsResponse,
)
```

Methods:

- <code title="post /v1/omni-ai/entitlements">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">create_entitlements</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/entitlement_create_entitlements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_create_entitlements_response.py">EntitlementCreateEntitlementsResponse</a></code>
- <code title="delete /v1/omni-ai/entitlements/{entitlement_id}">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">delete_entitlement</a>(entitlement_id) -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_delete_entitlement_response.py">EntitlementDeleteEntitlementResponse</a></code>
- <code title="get /v1/omni-ai/entitlement-agreements">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">get_entitlement_agreements</a>() -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_get_entitlement_agreements_response.py">EntitlementGetEntitlementAgreementsResponse</a></code>
- <code title="get /v1/omni-ai/entitlements">client.v1.omni_ai.entitlements.<a href="./src/clear_street/resources/v1/omni_ai/entitlements.py">get_entitlements</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/entitlement_get_entitlements_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/entitlement_get_entitlements_response.py">EntitlementGetEntitlementsResponse</a></code>

### Messages

Types:

```python
from clear_street.types.v1.omni_ai import (
    CreateFeedbackResponse,
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
    CancelResponsePayload,
    ErrorStatus,
    Response,
    ResponseContent,
    ResponseContentPart,
    ResponseStatus,
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
    CreateMessageResponse,
    CreateThreadResponse,
    Message,
    MessageContent,
    MessageContentPart,
    MessageList,
    MessageOutcome,
    MessageRole,
    Thread,
    ThreadList,
    ThreadCreateMessageResponse,
    ThreadCreateThreadResponse,
    ThreadGetMessagesResponse,
    ThreadGetThreadByIDResponse,
    ThreadGetThreadResponseResponse,
    ThreadGetThreadsResponse,
)
```

Methods:

- <code title="post /v1/omni-ai/threads/{thread_id}/messages">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads.py">create_message</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/thread_create_message_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_create_message_response.py">ThreadCreateMessageResponse</a></code>
- <code title="post /v1/omni-ai/threads">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads.py">create_thread</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/thread_create_thread_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_create_thread_response.py">ThreadCreateThreadResponse</a></code>
- <code title="get /v1/omni-ai/threads/{thread_id}/messages">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads.py">get_messages</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_messages_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_messages_response.py">ThreadGetMessagesResponse</a></code>
- <code title="get /v1/omni-ai/threads/{thread_id}">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads.py">get_thread_by_id</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_thread_by_id_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_thread_by_id_response.py">ThreadGetThreadByIDResponse</a></code>
- <code title="get /v1/omni-ai/threads/{thread_id}/response">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads.py">get_thread_response</a>(thread_id, \*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_thread_response_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_thread_response_response.py">ThreadGetThreadResponseResponse</a></code>
- <code title="get /v1/omni-ai/threads">client.v1.omni_ai.threads.<a href="./src/clear_street/resources/v1/omni_ai/threads.py">get_threads</a>(\*\*<a href="src/clear_street/types/v1/omni_ai/thread_get_threads_params.py">params</a>) -> <a href="./src/clear_street/types/v1/omni_ai/thread_get_threads_response.py">ThreadGetThreadsResponse</a></code>

## Orders

Types:

```python
from clear_street.types.v1 import (
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

- <code title="delete /v1/accounts/{account_id}/orders">client.v1.orders.<a href="./src/clear_street/resources/v1/orders.py">cancel_all_open_orders</a>(account_id, \*\*<a href="src/clear_street/types/v1/order_cancel_all_open_orders_params.py">params</a>) -> <a href="./src/clear_street/types/v1/order_cancel_all_open_orders_response.py">OrderCancelAllOpenOrdersResponse</a></code>
- <code title="delete /v1/accounts/{account_id}/orders/{order_id}">client.v1.orders.<a href="./src/clear_street/resources/v1/orders.py">cancel_open_order</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/v1/order_cancel_open_order_response.py">OrderCancelOpenOrderResponse</a></code>
- <code title="get /v1/accounts/{account_id}/orders/{order_id}">client.v1.orders.<a href="./src/clear_street/resources/v1/orders.py">get_order_by_id</a>(order_id, \*, account_id) -> <a href="./src/clear_street/types/v1/order_get_order_by_id_response.py">OrderGetOrderByIDResponse</a></code>
- <code title="get /v1/accounts/{account_id}/orders">client.v1.orders.<a href="./src/clear_street/resources/v1/orders.py">get_orders</a>(account_id, \*\*<a href="src/clear_street/types/v1/order_get_orders_params.py">params</a>) -> <a href="./src/clear_street/types/v1/order_get_orders_response.py">OrderGetOrdersResponse</a></code>
- <code title="patch /v1/accounts/{account_id}/orders/{order_id}">client.v1.orders.<a href="./src/clear_street/resources/v1/orders.py">replace_order</a>(order_id, \*, account_id, \*\*<a href="src/clear_street/types/v1/order_replace_order_params.py">params</a>) -> <a href="./src/clear_street/types/v1/order_replace_order_response.py">OrderReplaceOrderResponse</a></code>
- <code title="post /v1/accounts/{account_id}/orders">client.v1.orders.<a href="./src/clear_street/resources/v1/orders.py">submit_orders</a>(account_id, \*\*<a href="src/clear_street/types/v1/order_submit_orders_params.py">params</a>) -> <a href="./src/clear_street/types/v1/order_submit_orders_response.py">OrderSubmitOrdersResponse</a></code>

## Positions

Types:

```python
from clear_street.types.v1 import (
    Position,
    PositionInstruction,
    PositionInstructionList,
    PositionInstructionStatus,
    PositionInstructionType,
    PositionList,
    PositionType,
    PositionCancelPositionInstructionResponse,
    PositionClosePositionResponse,
    PositionClosePositionsResponse,
    PositionGetPositionInstructionsResponse,
    PositionGetPositionsResponse,
    PositionSubmitPositionInstructionsResponse,
)
```

Methods:

- <code title="delete /v1/accounts/{account_id}/positions/instructions/{instruction_id}">client.v1.positions.<a href="./src/clear_street/resources/v1/positions.py">cancel_position_instruction</a>(instruction_id, \*, account_id) -> <a href="./src/clear_street/types/v1/position_cancel_position_instruction_response.py">PositionCancelPositionInstructionResponse</a></code>
- <code title="delete /v1/accounts/{account_id}/positions/{instrument_id}">client.v1.positions.<a href="./src/clear_street/resources/v1/positions.py">close_position</a>(instrument_id, \*, account_id, \*\*<a href="src/clear_street/types/v1/position_close_position_params.py">params</a>) -> <a href="./src/clear_street/types/v1/position_close_position_response.py">PositionClosePositionResponse</a></code>
- <code title="delete /v1/accounts/{account_id}/positions">client.v1.positions.<a href="./src/clear_street/resources/v1/positions.py">close_positions</a>(account_id, \*\*<a href="src/clear_street/types/v1/position_close_positions_params.py">params</a>) -> <a href="./src/clear_street/types/v1/position_close_positions_response.py">PositionClosePositionsResponse</a></code>
- <code title="get /v1/accounts/{account_id}/positions/instructions">client.v1.positions.<a href="./src/clear_street/resources/v1/positions.py">get_position_instructions</a>(account_id, \*\*<a href="src/clear_street/types/v1/position_get_position_instructions_params.py">params</a>) -> <a href="./src/clear_street/types/v1/position_get_position_instructions_response.py">PositionGetPositionInstructionsResponse</a></code>
- <code title="get /v1/accounts/{account_id}/positions">client.v1.positions.<a href="./src/clear_street/resources/v1/positions.py">get_positions</a>(account_id, \*\*<a href="src/clear_street/types/v1/position_get_positions_params.py">params</a>) -> <a href="./src/clear_street/types/v1/position_get_positions_response.py">PositionGetPositionsResponse</a></code>
- <code title="post /v1/accounts/{account_id}/positions/instructions">client.v1.positions.<a href="./src/clear_street/resources/v1/positions.py">submit_position_instructions</a>(account_id, \*\*<a href="src/clear_street/types/v1/position_submit_position_instructions_params.py">params</a>) -> <a href="./src/clear_street/types/v1/position_submit_position_instructions_response.py">PositionSubmitPositionInstructionsResponse</a></code>

## Watchlist

Types:

```python
from clear_street.types.v1 import (
    AddWatchlistItemData,
    WatchlistDetail,
    WatchlistEntry,
    WatchlistEntryList,
    WatchlistItemEntry,
    WatchlistAddWatchlistItemResponse,
    WatchlistCreateWatchlistResponse,
    WatchlistGetWatchlistByIDResponse,
    WatchlistGetWatchlistsResponse,
)
```

Methods:

- <code title="post /v1/watchlists/{watchlist_id}/items">client.v1.watchlist.<a href="./src/clear_street/resources/v1/watchlist.py">add_watchlist_item</a>(watchlist_id, \*\*<a href="src/clear_street/types/v1/watchlist_add_watchlist_item_params.py">params</a>) -> <a href="./src/clear_street/types/v1/watchlist_add_watchlist_item_response.py">WatchlistAddWatchlistItemResponse</a></code>
- <code title="post /v1/watchlists">client.v1.watchlist.<a href="./src/clear_street/resources/v1/watchlist.py">create_watchlist</a>(\*\*<a href="src/clear_street/types/v1/watchlist_create_watchlist_params.py">params</a>) -> <a href="./src/clear_street/types/v1/watchlist_create_watchlist_response.py">WatchlistCreateWatchlistResponse</a></code>
- <code title="delete /v1/watchlists/{watchlist_id}">client.v1.watchlist.<a href="./src/clear_street/resources/v1/watchlist.py">delete_watchlist</a>(watchlist_id) -> object</code>
- <code title="delete /v1/watchlists/{watchlist_id}/items/{item_id}">client.v1.watchlist.<a href="./src/clear_street/resources/v1/watchlist.py">delete_watchlist_item</a>(item_id, \*, watchlist_id) -> object</code>
- <code title="get /v1/watchlists/{watchlist_id}">client.v1.watchlist.<a href="./src/clear_street/resources/v1/watchlist.py">get_watchlist_by_id</a>(watchlist_id) -> <a href="./src/clear_street/types/v1/watchlist_get_watchlist_by_id_response.py">WatchlistGetWatchlistByIDResponse</a></code>
- <code title="get /v1/watchlists">client.v1.watchlist.<a href="./src/clear_street/resources/v1/watchlist.py">get_watchlists</a>(\*\*<a href="src/clear_street/types/v1/watchlist_get_watchlists_params.py">params</a>) -> <a href="./src/clear_street/types/v1/watchlist_get_watchlists_response.py">WatchlistGetWatchlistsResponse</a></code>

## Websocket

Methods:

- <code title="get /v1/ws">client.v1.websocket.<a href="./src/clear_street/resources/v1/websocket.py">websocket_handler</a>() -> None</code>

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    Base64FileInput,
    omit,
    not_given,
)
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    RequestTimeInForce,
    order_get_orders_params,
    order_replace_order_params,
    order_get_executions_params,
    order_cancel_all_open_orders_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.request_time_in_force import RequestTimeInForce
from ...types.v1.instrument_id_or_symbol import InstrumentIDOrSymbol
from ...types.v1.new_order_request_param import NewOrderRequestParam
from ...types.v1.order_get_orders_response import OrderGetOrdersResponse
from ...types.v1.order_replace_order_response import OrderReplaceOrderResponse
from ...types.v1.order_submit_orders_response import OrderSubmitOrdersResponse
from ...types.v1.order_get_executions_response import OrderGetExecutionsResponse
from ...types.v1.order_get_order_by_id_response import OrderGetOrderByIDResponse
from ...types.v1.order_cancel_open_order_response import OrderCancelOpenOrderResponse
from ...types.v1.order_cancel_all_open_orders_response import OrderCancelAllOpenOrdersResponse

__all__ = ["OrdersResource", "AsyncOrdersResource"]


class OrdersResource(SyncAPIResource):
    """Place, monitor, and manage trading orders."""

    @cached_property
    def with_raw_response(self) -> OrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return OrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return OrdersResourceWithStreamingResponse(self)

    def cancel_all_open_orders(
        self,
        account_id: int,
        *,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"] | Omit = omit,
        side: Literal["BUY", "SELL", "SELL_SHORT", "OTHER"] | Omit = omit,
        type: Literal["MARKET", "LIMIT", "STOP", "STOP_LIMIT", "TRAILING_STOP", "TRAILING_STOP_LIMIT", "OTHER"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCancelAllOpenOrdersResponse:
        """
        Cancel all orders for an account

        Args:
          instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols).

          instrument_type: Filter by instrument type (e.g., COMMON_STOCK, OPTION)

          side: Filter by order side (BUY or SELL)

          type: Filter by order type (e.g., MARKET, LIMIT)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/v1/accounts/{account_id}/orders", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "instrument_ids": instrument_ids,
                        "instrument_type": instrument_type,
                        "side": side,
                        "type": type,
                    },
                    order_cancel_all_open_orders_params.OrderCancelAllOpenOrdersParams,
                ),
            ),
            cast_to=OrderCancelAllOpenOrdersResponse,
        )

    def cancel_open_order(
        self,
        order_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCancelOpenOrderResponse:
        """
        Cancel a specific order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._delete(
            path_template("/v1/accounts/{account_id}/orders/{order_id}", account_id=account_id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCancelOpenOrderResponse,
        )

    def get_executions(
        self,
        account_id: int,
        *,
        from_: Union[str, datetime] | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderGetExecutionsResponse:
        """
        Retrieves filled and partially-filled execution reports for the specified
        trading account, ordered by transaction time (nanosecond precision) descending.

        Args:
          from_: The start date and time for the query range, inclusive (ISO 8601 format)

          instrument_ids: Comma-separated instrument identifiers (UUIDs) or symbols (e.g. `AAPL`) to
              filter by. When provided, only executions for any of the listed instruments are
              returned.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to: The end date and time for the query range, inclusive (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/executions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "instrument_ids": instrument_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to": to,
                    },
                    order_get_executions_params.OrderGetExecutionsParams,
                ),
            ),
            cast_to=OrderGetExecutionsResponse,
        )

    def get_order_by_id(
        self,
        order_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderGetOrderByIDResponse:
        """
        Get Order By ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._get(
            path_template("/v1/accounts/{account_id}/orders/{order_id}", account_id=account_id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderGetOrderByIDResponse,
        )

    def get_orders(
        self,
        account_id: int,
        *,
        from_: Union[str, datetime] | Omit = omit,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"] | Omit = omit,
        order_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        status: List[
            Literal[
                "PENDING_NEW",
                "NEW",
                "PARTIALLY_FILLED",
                "FILLED",
                "CANCELED",
                "REJECTED",
                "EXPIRED",
                "PENDING_CANCEL",
                "PENDING_REPLACE",
                "REPLACED",
                "DONE_FOR_DAY",
                "STOPPED",
                "SUSPENDED",
                "CALCULATED",
                "OTHER",
            ]
        ]
        | Omit = omit,
        symbol: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        underlying_instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderGetOrdersResponse:
        """
        List orders for an account with optional filtering

        Args:
          from_: The start date and time for the query range, inclusive (ISO 8601 format)

          instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols).

          instrument_type: Instrument type filter (e.g., COMMON_STOCK, OPTION)

          order_ids: Comma-separated order IDs to filter by. When provided, only orders whose order
              ID is in this set are returned.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          status: Comma-separated order statuses to filter by

          symbol: Filter by symbol

          to: The end date and time for the query range, inclusive (ISO 8601 format)

          underlying_instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols). Matches options orders whose resolved underlier is any of the given
              instruments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v1/accounts/{account_id}/orders", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "instrument_ids": instrument_ids,
                        "instrument_type": instrument_type,
                        "order_ids": order_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "status": status,
                        "symbol": symbol,
                        "to": to,
                        "underlying_instrument_ids": underlying_instrument_ids,
                    },
                    order_get_orders_params.OrderGetOrdersParams,
                ),
            ),
            cast_to=OrderGetOrdersResponse,
        )

    def replace_order(
        self,
        order_id: str,
        *,
        account_id: int,
        limit_price: Optional[str] | Omit = omit,
        quantity: Optional[str] | Omit = omit,
        stop_price: Optional[str] | Omit = omit,
        time_in_force: RequestTimeInForce | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderReplaceOrderResponse:
        """
        Replace an order with new parameters

        Args:
          limit_price: New limit price for the order

          quantity: New quantity for the order

          stop_price: New stop price for the order

          time_in_force: New time in force for the order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._patch(
            path_template("/v1/accounts/{account_id}/orders/{order_id}", account_id=account_id, order_id=order_id),
            body=maybe_transform(
                {
                    "limit_price": limit_price,
                    "quantity": quantity,
                    "stop_price": stop_price,
                    "time_in_force": time_in_force,
                },
                order_replace_order_params.OrderReplaceOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderReplaceOrderResponse,
        )

    def submit_orders(
        self,
        account_id: int,
        *,
        orders: Iterable[NewOrderRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderSubmitOrdersResponse:
        """
        Submit new orders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/v1/accounts/{account_id}/orders", account_id=account_id),
            body=maybe_transform(orders, Iterable[NewOrderRequestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderSubmitOrdersResponse,
        )


class AsyncOrdersResource(AsyncAPIResource):
    """Place, monitor, and manage trading orders."""

    @cached_property
    def with_raw_response(self) -> AsyncOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/clear-street-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/clear-street-python#with_streaming_response
        """
        return AsyncOrdersResourceWithStreamingResponse(self)

    async def cancel_all_open_orders(
        self,
        account_id: int,
        *,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"] | Omit = omit,
        side: Literal["BUY", "SELL", "SELL_SHORT", "OTHER"] | Omit = omit,
        type: Literal["MARKET", "LIMIT", "STOP", "STOP_LIMIT", "TRAILING_STOP", "TRAILING_STOP_LIMIT", "OTHER"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCancelAllOpenOrdersResponse:
        """
        Cancel all orders for an account

        Args:
          instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols).

          instrument_type: Filter by instrument type (e.g., COMMON_STOCK, OPTION)

          side: Filter by order side (BUY or SELL)

          type: Filter by order type (e.g., MARKET, LIMIT)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/v1/accounts/{account_id}/orders", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "instrument_ids": instrument_ids,
                        "instrument_type": instrument_type,
                        "side": side,
                        "type": type,
                    },
                    order_cancel_all_open_orders_params.OrderCancelAllOpenOrdersParams,
                ),
            ),
            cast_to=OrderCancelAllOpenOrdersResponse,
        )

    async def cancel_open_order(
        self,
        order_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCancelOpenOrderResponse:
        """
        Cancel a specific order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._delete(
            path_template("/v1/accounts/{account_id}/orders/{order_id}", account_id=account_id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCancelOpenOrderResponse,
        )

    async def get_executions(
        self,
        account_id: int,
        *,
        from_: Union[str, datetime] | Omit = omit,
        instrument_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderGetExecutionsResponse:
        """
        Retrieves filled and partially-filled execution reports for the specified
        trading account, ordered by transaction time (nanosecond precision) descending.

        Args:
          from_: The start date and time for the query range, inclusive (ISO 8601 format)

          instrument_ids: Comma-separated instrument identifiers (UUIDs) or symbols (e.g. `AAPL`) to
              filter by. When provided, only executions for any of the listed instruments are
              returned.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          to: The end date and time for the query range, inclusive (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/executions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "instrument_ids": instrument_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to": to,
                    },
                    order_get_executions_params.OrderGetExecutionsParams,
                ),
            ),
            cast_to=OrderGetExecutionsResponse,
        )

    async def get_order_by_id(
        self,
        order_id: str,
        *,
        account_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderGetOrderByIDResponse:
        """
        Get Order By ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._get(
            path_template("/v1/accounts/{account_id}/orders/{order_id}", account_id=account_id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderGetOrderByIDResponse,
        )

    async def get_orders(
        self,
        account_id: int,
        *,
        from_: Union[str, datetime] | Omit = omit,
        instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        instrument_type: Literal["COMMON_STOCK", "OPTION", "CASH"] | Omit = omit,
        order_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        status: List[
            Literal[
                "PENDING_NEW",
                "NEW",
                "PARTIALLY_FILLED",
                "FILLED",
                "CANCELED",
                "REJECTED",
                "EXPIRED",
                "PENDING_CANCEL",
                "PENDING_REPLACE",
                "REPLACED",
                "DONE_FOR_DAY",
                "STOPPED",
                "SUSPENDED",
                "CALCULATED",
                "OTHER",
            ]
        ]
        | Omit = omit,
        symbol: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        underlying_instrument_ids: SequenceNotStr[InstrumentIDOrSymbol] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderGetOrdersResponse:
        """
        List orders for an account with optional filtering

        Args:
          from_: The start date and time for the query range, inclusive (ISO 8601 format)

          instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols).

          instrument_type: Instrument type filter (e.g., COMMON_STOCK, OPTION)

          order_ids: Comma-separated order IDs to filter by. When provided, only orders whose order
              ID is in this set are returned.

          page_size: The number of items to return per page. Only used when page_token is not
              provided.

          page_token: Token for retrieving the next or previous page of results. Contains encoded
              pagination state; when provided, page_size is ignored.

          status: Comma-separated order statuses to filter by

          symbol: Filter by symbol

          to: The end date and time for the query range, inclusive (ISO 8601 format)

          underlying_instrument_ids: Comma-separated instrument IDs (UUID) or symbols (equity tickers or OSI option
              symbols). Matches options orders whose resolved underlier is any of the given
              instruments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v1/accounts/{account_id}/orders", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "instrument_ids": instrument_ids,
                        "instrument_type": instrument_type,
                        "order_ids": order_ids,
                        "page_size": page_size,
                        "page_token": page_token,
                        "status": status,
                        "symbol": symbol,
                        "to": to,
                        "underlying_instrument_ids": underlying_instrument_ids,
                    },
                    order_get_orders_params.OrderGetOrdersParams,
                ),
            ),
            cast_to=OrderGetOrdersResponse,
        )

    async def replace_order(
        self,
        order_id: str,
        *,
        account_id: int,
        limit_price: Optional[str] | Omit = omit,
        quantity: Optional[str] | Omit = omit,
        stop_price: Optional[str] | Omit = omit,
        time_in_force: RequestTimeInForce | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderReplaceOrderResponse:
        """
        Replace an order with new parameters

        Args:
          limit_price: New limit price for the order

          quantity: New quantity for the order

          stop_price: New stop price for the order

          time_in_force: New time in force for the order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._patch(
            path_template("/v1/accounts/{account_id}/orders/{order_id}", account_id=account_id, order_id=order_id),
            body=await async_maybe_transform(
                {
                    "limit_price": limit_price,
                    "quantity": quantity,
                    "stop_price": stop_price,
                    "time_in_force": time_in_force,
                },
                order_replace_order_params.OrderReplaceOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderReplaceOrderResponse,
        )

    async def submit_orders(
        self,
        account_id: int,
        *,
        orders: Iterable[NewOrderRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderSubmitOrdersResponse:
        """
        Submit new orders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/v1/accounts/{account_id}/orders", account_id=account_id),
            body=await async_maybe_transform(orders, Iterable[NewOrderRequestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderSubmitOrdersResponse,
        )


class OrdersResourceWithRawResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.cancel_all_open_orders = to_raw_response_wrapper(
            orders.cancel_all_open_orders,
        )
        self.cancel_open_order = to_raw_response_wrapper(
            orders.cancel_open_order,
        )
        self.get_executions = to_raw_response_wrapper(
            orders.get_executions,
        )
        self.get_order_by_id = to_raw_response_wrapper(
            orders.get_order_by_id,
        )
        self.get_orders = to_raw_response_wrapper(
            orders.get_orders,
        )
        self.replace_order = to_raw_response_wrapper(
            orders.replace_order,
        )
        self.submit_orders = to_raw_response_wrapper(
            orders.submit_orders,
        )


class AsyncOrdersResourceWithRawResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.cancel_all_open_orders = async_to_raw_response_wrapper(
            orders.cancel_all_open_orders,
        )
        self.cancel_open_order = async_to_raw_response_wrapper(
            orders.cancel_open_order,
        )
        self.get_executions = async_to_raw_response_wrapper(
            orders.get_executions,
        )
        self.get_order_by_id = async_to_raw_response_wrapper(
            orders.get_order_by_id,
        )
        self.get_orders = async_to_raw_response_wrapper(
            orders.get_orders,
        )
        self.replace_order = async_to_raw_response_wrapper(
            orders.replace_order,
        )
        self.submit_orders = async_to_raw_response_wrapper(
            orders.submit_orders,
        )


class OrdersResourceWithStreamingResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.cancel_all_open_orders = to_streamed_response_wrapper(
            orders.cancel_all_open_orders,
        )
        self.cancel_open_order = to_streamed_response_wrapper(
            orders.cancel_open_order,
        )
        self.get_executions = to_streamed_response_wrapper(
            orders.get_executions,
        )
        self.get_order_by_id = to_streamed_response_wrapper(
            orders.get_order_by_id,
        )
        self.get_orders = to_streamed_response_wrapper(
            orders.get_orders,
        )
        self.replace_order = to_streamed_response_wrapper(
            orders.replace_order,
        )
        self.submit_orders = to_streamed_response_wrapper(
            orders.submit_orders,
        )


class AsyncOrdersResourceWithStreamingResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.cancel_all_open_orders = async_to_streamed_response_wrapper(
            orders.cancel_all_open_orders,
        )
        self.cancel_open_order = async_to_streamed_response_wrapper(
            orders.cancel_open_order,
        )
        self.get_executions = async_to_streamed_response_wrapper(
            orders.get_executions,
        )
        self.get_order_by_id = async_to_streamed_response_wrapper(
            orders.get_order_by_id,
        )
        self.get_orders = async_to_streamed_response_wrapper(
            orders.get_orders,
        )
        self.replace_order = async_to_streamed_response_wrapper(
            orders.replace_order,
        )
        self.submit_orders = async_to_streamed_response_wrapper(
            orders.submit_orders,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet._utils import parse_datetime
from clearstreet.types.v1 import (
    OrderGetOrdersResponse,
    OrderGetOrderByIDResponse,
    OrderReplaceOrderResponse,
    OrderSubmitOrdersResponse,
    OrderGetExecutionsResponse,
    OrderCancelOpenOrderResponse,
    OrderCancelAllOpenOrdersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel_all_open_orders(self, client: ClearStreet) -> None:
        order = client.v1.orders.cancel_all_open_orders(
            account_id=0,
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @parametrize
    def test_method_cancel_all_open_orders_with_all_params(self, client: ClearStreet) -> None:
        order = client.v1.orders.cancel_all_open_orders(
            account_id=0,
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            instrument_type="COMMON_STOCK",
            side="BUY",
            type="MARKET",
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @parametrize
    def test_raw_response_cancel_all_open_orders(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.cancel_all_open_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_cancel_all_open_orders(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.cancel_all_open_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel_open_order(self, client: ClearStreet) -> None:
        order = client.v1.orders.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @parametrize
    def test_raw_response_cancel_open_order(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_cancel_open_order(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel_open_order(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.v1.orders.with_raw_response.cancel_open_order(
                order_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_executions(self, client: ClearStreet) -> None:
        order = client.v1.orders.get_executions(
            account_id=0,
        )
        assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

    @parametrize
    def test_method_get_executions_with_all_params(self, client: ClearStreet) -> None:
        order = client.v1.orders.get_executions(
            account_id=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

    @parametrize
    def test_raw_response_get_executions(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.get_executions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_get_executions(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.get_executions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_order_by_id(self, client: ClearStreet) -> None:
        order = client.v1.orders.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @parametrize
    def test_raw_response_get_order_by_id(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_get_order_by_id(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_order_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.v1.orders.with_raw_response.get_order_by_id(
                order_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_orders(self, client: ClearStreet) -> None:
        order = client.v1.orders.get_orders(
            account_id=0,
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @parametrize
    def test_method_get_orders_with_all_params(self, client: ClearStreet) -> None:
        order = client.v1.orders.get_orders(
            account_id=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            instrument_type="COMMON_STOCK",
            order_ids=["string"],
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            status=["PENDING_NEW"],
            symbol="symbol",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            underlying_instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @parametrize
    def test_raw_response_get_orders(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.get_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_get_orders(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.get_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace_order(self, client: ClearStreet) -> None:
        order = client.v1.orders.replace_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @parametrize
    def test_method_replace_order_with_all_params(self, client: ClearStreet) -> None:
        order = client.v1.orders.replace_order(
            order_id="order_id",
            account_id=0,
            limit_price="49.00",
            quantity="1",
            stop_price="52.00",
            time_in_force="DAY",
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @parametrize
    def test_raw_response_replace_order(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.replace_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_replace_order(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.replace_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace_order(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.v1.orders.with_raw_response.replace_order(
                order_id="",
                account_id=0,
            )

    @parametrize
    def test_method_submit_orders(self, client: ClearStreet) -> None:
        order = client.v1.orders.submit_orders(
            account_id=0,
            orders=[
                {
                    "order_type": "LIMIT",
                    "quantity": "1",
                    "side": "BUY",
                    "time_in_force": "DAY",
                }
            ],
        )
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @parametrize
    def test_raw_response_submit_orders(self, client: ClearStreet) -> None:
        response = client.v1.orders.with_raw_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "order_type": "LIMIT",
                    "quantity": "1",
                    "side": "BUY",
                    "time_in_force": "DAY",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_submit_orders(self, client: ClearStreet) -> None:
        with client.v1.orders.with_streaming_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "order_type": "LIMIT",
                    "quantity": "1",
                    "side": "BUY",
                    "time_in_force": "DAY",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_cancel_all_open_orders(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.cancel_all_open_orders(
            account_id=0,
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @parametrize
    async def test_method_cancel_all_open_orders_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.cancel_all_open_orders(
            account_id=0,
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            instrument_type="COMMON_STOCK",
            side="BUY",
            type="MARKET",
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_cancel_all_open_orders(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.cancel_all_open_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_all_open_orders(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.cancel_all_open_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.v1.orders.with_raw_response.cancel_open_order(
                order_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_executions(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.get_executions(
            account_id=0,
        )
        assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

    @parametrize
    async def test_method_get_executions_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.get_executions(
            account_id=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_get_executions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.get_executions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_get_executions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.get_executions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderGetExecutionsResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.v1.orders.with_raw_response.get_order_by_id(
                order_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_orders(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.get_orders(
            account_id=0,
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @parametrize
    async def test_method_get_orders_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.get_orders(
            account_id=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            instrument_type="COMMON_STOCK",
            order_ids=["string"],
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            status=["PENDING_NEW"],
            symbol="symbol",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            underlying_instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_get_orders(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.get_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_get_orders(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.get_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace_order(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.replace_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @parametrize
    async def test_method_replace_order_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.replace_order(
            order_id="order_id",
            account_id=0,
            limit_price="49.00",
            quantity="1",
            stop_price="52.00",
            time_in_force="DAY",
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_replace_order(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.replace_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_replace_order(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.replace_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace_order(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.v1.orders.with_raw_response.replace_order(
                order_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_submit_orders(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.v1.orders.submit_orders(
            account_id=0,
            orders=[
                {
                    "order_type": "LIMIT",
                    "quantity": "1",
                    "side": "BUY",
                    "time_in_force": "DAY",
                }
            ],
        )
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_submit_orders(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.orders.with_raw_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "order_type": "LIMIT",
                    "quantity": "1",
                    "side": "BUY",
                    "time_in_force": "DAY",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_submit_orders(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.orders.with_streaming_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "order_type": "LIMIT",
                    "quantity": "1",
                    "side": "BUY",
                    "time_in_force": "DAY",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

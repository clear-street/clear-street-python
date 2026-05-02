# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street._utils import parse_datetime
from clear_street.types.active.v1.accounts import (
    OrderGetOrdersResponse,
    OrderGetOrderByIDResponse,
    OrderReplaceOrderResponse,
    OrderSubmitOrdersResponse,
    OrderCancelOpenOrderResponse,
    OrderCancelAllOpenOrdersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_all_open_orders(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.cancel_all_open_orders(
            account_id=0,
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_all_open_orders_with_all_params(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.cancel_all_open_orders(
            account_id=0,
            instrument_type="COMMON_STOCK",
            security_id=["string"],
            security_id_source=["string"],
            side="BUY",
            type="MARKET",
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_all_open_orders(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.orders.with_raw_response.cancel_all_open_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_all_open_orders(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.orders.with_streaming_response.cancel_all_open_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_open_order(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_open_order(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.orders.with_raw_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_open_order(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.orders.with_streaming_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_open_order(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.active.v1.accounts.orders.with_raw_response.cancel_open_order(
                order_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_order_by_id(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_order_by_id(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.orders.with_raw_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_order_by_id(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.orders.with_streaming_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_order_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.active.v1.accounts.orders.with_raw_response.get_order_by_id(
                order_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_orders(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.get_orders(
            account_id=0,
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_orders_with_all_params(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.get_orders(
            account_id=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            instrument_type="COMMON_STOCK",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            security_id=["string"],
            security_id_source=["string"],
            status=["PENDING_NEW"],
            symbol="symbol",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            underlying_instrument_ids="underlying_instrument_ids",
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_orders(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.orders.with_raw_response.get_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_orders(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.orders.with_streaming_response.get_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_order(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.replace_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_order_with_all_params(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.replace_order(
            order_id="order_id",
            account_id=0,
            limit_price="150.50",
            quantity="125",
            stop_price="148.00",
            time_in_force="DAY",
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace_order(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.orders.with_raw_response.replace_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace_order(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.orders.with_streaming_response.replace_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace_order(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.active.v1.accounts.orders.with_raw_response.replace_order(
                order_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_orders(self, client: ClearStreet) -> None:
        order = client.active.v1.accounts.orders.submit_orders(
            account_id=0,
            orders=[
                {
                    "legs": [
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-447a-706f-996f-097254663f02",
                            "side": "BUY",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-4db4-78ec-b4fd-cba8be61cf8a",
                            "side": "SELL",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-5264-7f20-8fd3-35df82cd6ef0",
                            "side": "BUY",
                        },
                    ],
                    "order_type": "LIMIT",
                    "time_in_force": "DAY",
                }
            ],
        )
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_orders(self, client: ClearStreet) -> None:
        response = client.active.v1.accounts.orders.with_raw_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "legs": [
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-447a-706f-996f-097254663f02",
                            "side": "BUY",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-4db4-78ec-b4fd-cba8be61cf8a",
                            "side": "SELL",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-5264-7f20-8fd3-35df82cd6ef0",
                            "side": "BUY",
                        },
                    ],
                    "order_type": "LIMIT",
                    "time_in_force": "DAY",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_orders(self, client: ClearStreet) -> None:
        with client.active.v1.accounts.orders.with_streaming_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "legs": [
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-447a-706f-996f-097254663f02",
                            "side": "BUY",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-4db4-78ec-b4fd-cba8be61cf8a",
                            "side": "SELL",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-5264-7f20-8fd3-35df82cd6ef0",
                            "side": "BUY",
                        },
                    ],
                    "order_type": "LIMIT",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_all_open_orders(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.cancel_all_open_orders(
            account_id=0,
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_all_open_orders_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.cancel_all_open_orders(
            account_id=0,
            instrument_type="COMMON_STOCK",
            security_id=["string"],
            security_id_source=["string"],
            side="BUY",
            type="MARKET",
        )
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_all_open_orders(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.orders.with_raw_response.cancel_all_open_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_all_open_orders(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.orders.with_streaming_response.cancel_all_open_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderCancelAllOpenOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.orders.with_raw_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.orders.with_streaming_response.cancel_open_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderCancelOpenOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_open_order(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.active.v1.accounts.orders.with_raw_response.cancel_open_order(
                order_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.orders.with_raw_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.orders.with_streaming_response.get_order_by_id(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderGetOrderByIDResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_order_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.active.v1.accounts.orders.with_raw_response.get_order_by_id(
                order_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_orders(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.get_orders(
            account_id=0,
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_orders_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.get_orders(
            account_id=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            instrument_type="COMMON_STOCK",
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            security_id=["string"],
            security_id_source=["string"],
            status=["PENDING_NEW"],
            symbol="symbol",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            underlying_instrument_ids="underlying_instrument_ids",
        )
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_orders(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.orders.with_raw_response.get_orders(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_orders(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.orders.with_streaming_response.get_orders(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderGetOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_order(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.replace_order(
            order_id="order_id",
            account_id=0,
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_order_with_all_params(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.replace_order(
            order_id="order_id",
            account_id=0,
            limit_price="150.50",
            quantity="125",
            stop_price="148.00",
            time_in_force="DAY",
        )
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace_order(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.orders.with_raw_response.replace_order(
            order_id="order_id",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace_order(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.orders.with_streaming_response.replace_order(
            order_id="order_id",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderReplaceOrderResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace_order(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.active.v1.accounts.orders.with_raw_response.replace_order(
                order_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_orders(self, async_client: AsyncClearStreet) -> None:
        order = await async_client.active.v1.accounts.orders.submit_orders(
            account_id=0,
            orders=[
                {
                    "legs": [
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-447a-706f-996f-097254663f02",
                            "side": "BUY",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-4db4-78ec-b4fd-cba8be61cf8a",
                            "side": "SELL",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-5264-7f20-8fd3-35df82cd6ef0",
                            "side": "BUY",
                        },
                    ],
                    "order_type": "LIMIT",
                    "time_in_force": "DAY",
                }
            ],
        )
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_orders(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.active.v1.accounts.orders.with_raw_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "legs": [
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-447a-706f-996f-097254663f02",
                            "side": "BUY",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-4db4-78ec-b4fd-cba8be61cf8a",
                            "side": "SELL",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-5264-7f20-8fd3-35df82cd6ef0",
                            "side": "BUY",
                        },
                    ],
                    "order_type": "LIMIT",
                    "time_in_force": "DAY",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_orders(self, async_client: AsyncClearStreet) -> None:
        async with async_client.active.v1.accounts.orders.with_streaming_response.submit_orders(
            account_id=0,
            orders=[
                {
                    "legs": [
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-447a-706f-996f-097254663f02",
                            "side": "BUY",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-4db4-78ec-b4fd-cba8be61cf8a",
                            "side": "SELL",
                        },
                        {
                            "instrument_type": "OPTION",
                            "ratio": "ratio",
                            "security": "0193bb84-5264-7f20-8fd3-35df82cd6ef0",
                            "side": "BUY",
                        },
                    ],
                    "order_type": "LIMIT",
                    "time_in_force": "DAY",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderSubmitOrdersResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

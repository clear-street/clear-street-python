# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1.omni_ai import (
    ResponseCancelResponseResponse,
    ResponseGetResponseByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel_response(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.responses.cancel_response(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ResponseCancelResponseResponse, response, path=["response"])

    @parametrize
    def test_raw_response_cancel_response(self, client: ClearStreet) -> None:
        http_response = client.v1.omni_ai.responses.with_raw_response.cancel_response(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseCancelResponseResponse, response, path=["response"])

    @parametrize
    def test_streaming_response_cancel_response(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.responses.with_streaming_response.cancel_response(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseCancelResponseResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_cancel_response(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.v1.omni_ai.responses.with_raw_response.cancel_response(
                response_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get_response_by_id(self, client: ClearStreet) -> None:
        response = client.v1.omni_ai.responses.get_response_by_id(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ResponseGetResponseByIDResponse, response, path=["response"])

    @parametrize
    def test_raw_response_get_response_by_id(self, client: ClearStreet) -> None:
        http_response = client.v1.omni_ai.responses.with_raw_response.get_response_by_id(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseGetResponseByIDResponse, response, path=["response"])

    @parametrize
    def test_streaming_response_get_response_by_id(self, client: ClearStreet) -> None:
        with client.v1.omni_ai.responses.with_streaming_response.get_response_by_id(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseGetResponseByIDResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_path_params_get_response_by_id(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.v1.omni_ai.responses.with_raw_response.get_response_by_id(
                response_id="",
                account_id=0,
            )


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_cancel_response(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.responses.cancel_response(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ResponseCancelResponseResponse, response, path=["response"])

    @parametrize
    async def test_raw_response_cancel_response(self, async_client: AsyncClearStreet) -> None:
        http_response = await async_client.v1.omni_ai.responses.with_raw_response.cancel_response(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseCancelResponseResponse, response, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_response(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.responses.with_streaming_response.cancel_response(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseCancelResponseResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_response(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.v1.omni_ai.responses.with_raw_response.cancel_response(
                response_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get_response_by_id(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.omni_ai.responses.get_response_by_id(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(ResponseGetResponseByIDResponse, response, path=["response"])

    @parametrize
    async def test_raw_response_get_response_by_id(self, async_client: AsyncClearStreet) -> None:
        http_response = await async_client.v1.omni_ai.responses.with_raw_response.get_response_by_id(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseGetResponseByIDResponse, response, path=["response"])

    @parametrize
    async def test_streaming_response_get_response_by_id(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.omni_ai.responses.with_streaming_response.get_response_by_id(
            response_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseGetResponseByIDResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_path_params_get_response_by_id(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.v1.omni_ai.responses.with_raw_response.get_response_by_id(
                response_id="",
                account_id=0,
            )

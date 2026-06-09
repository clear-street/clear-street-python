# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from clearstreet import ClearStreet, AsyncClearStreet
from tests.utils import assert_matches_type
from clearstreet.types.v1 import (
    PositionGetPositionsResponse,
    PositionClosePositionResponse,
    PositionClosePositionsResponse,
    PositionGetPositionInstructionsResponse,
    PositionCancelPositionInstructionResponse,
    PositionSubmitPositionInstructionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPositions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel_position_instruction(self, client: ClearStreet) -> None:
        position = client.v1.positions.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(PositionCancelPositionInstructionResponse, position, path=["response"])

    @parametrize
    def test_raw_response_cancel_position_instruction(self, client: ClearStreet) -> None:
        response = client.v1.positions.with_raw_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(PositionCancelPositionInstructionResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_cancel_position_instruction(self, client: ClearStreet) -> None:
        with client.v1.positions.with_streaming_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(PositionCancelPositionInstructionResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel_position_instruction(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instruction_id` but received ''"):
            client.v1.positions.with_raw_response.cancel_position_instruction(
                instruction_id="",
                account_id=0,
            )

    @parametrize
    def test_method_close_position(self, client: ClearStreet) -> None:
        position = client.v1.positions.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(PositionClosePositionResponse, position, path=["response"])

    @parametrize
    def test_method_close_position_with_all_params(self, client: ClearStreet) -> None:
        position = client.v1.positions.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
            cancel_orders=False,
        )
        assert_matches_type(PositionClosePositionResponse, position, path=["response"])

    @parametrize
    def test_raw_response_close_position(self, client: ClearStreet) -> None:
        response = client.v1.positions.with_raw_response.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(PositionClosePositionResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_close_position(self, client: ClearStreet) -> None:
        with client.v1.positions.with_streaming_response.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(PositionClosePositionResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close_position(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            client.v1.positions.with_raw_response.close_position(
                instrument_id="",
                account_id=0,
            )

    @parametrize
    def test_method_close_positions(self, client: ClearStreet) -> None:
        position = client.v1.positions.close_positions(
            account_id=0,
        )
        assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

    @parametrize
    def test_method_close_positions_with_all_params(self, client: ClearStreet) -> None:
        position = client.v1.positions.close_positions(
            account_id=0,
            cancel_orders=False,
        )
        assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

    @parametrize
    def test_raw_response_close_positions(self, client: ClearStreet) -> None:
        response = client.v1.positions.with_raw_response.close_positions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_close_positions(self, client: ClearStreet) -> None:
        with client.v1.positions.with_streaming_response.close_positions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_position_instructions(self, client: ClearStreet) -> None:
        position = client.v1.positions.get_position_instructions(
            account_id=0,
        )
        assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

    @parametrize
    def test_method_get_position_instructions_with_all_params(self, client: ClearStreet) -> None:
        position = client.v1.positions.get_position_instructions(
            account_id=0,
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

    @parametrize
    def test_raw_response_get_position_instructions(self, client: ClearStreet) -> None:
        response = client.v1.positions.with_raw_response.get_position_instructions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_get_position_instructions(self, client: ClearStreet) -> None:
        with client.v1.positions.with_streaming_response.get_position_instructions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_positions(self, client: ClearStreet) -> None:
        position = client.v1.positions.get_positions(
            account_id=0,
        )
        assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

    @parametrize
    def test_method_get_positions_with_all_params(self, client: ClearStreet) -> None:
        position = client.v1.positions.get_positions(
            account_id=0,
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            sort_by="SYMBOL",
            sort_direction="ASC",
        )
        assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

    @parametrize
    def test_raw_response_get_positions(self, client: ClearStreet) -> None:
        response = client.v1.positions.with_raw_response.get_positions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_get_positions(self, client: ClearStreet) -> None:
        with client.v1.positions.with_streaming_response.get_positions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit_position_instructions(self, client: ClearStreet) -> None:
        position = client.v1.positions.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )
        assert_matches_type(PositionSubmitPositionInstructionsResponse, position, path=["response"])

    @parametrize
    def test_raw_response_submit_position_instructions(self, client: ClearStreet) -> None:
        response = client.v1.positions.with_raw_response.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = response.parse()
        assert_matches_type(PositionSubmitPositionInstructionsResponse, position, path=["response"])

    @parametrize
    def test_streaming_response_submit_position_instructions(self, client: ClearStreet) -> None:
        with client.v1.positions.with_streaming_response.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = response.parse()
            assert_matches_type(PositionSubmitPositionInstructionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPositions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(PositionCancelPositionInstructionResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.positions.with_raw_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(PositionCancelPositionInstructionResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.positions.with_streaming_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(PositionCancelPositionInstructionResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instruction_id` but received ''"):
            await async_client.v1.positions.with_raw_response.cancel_position_instruction(
                instruction_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_close_position(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(PositionClosePositionResponse, position, path=["response"])

    @parametrize
    async def test_method_close_position_with_all_params(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
            cancel_orders=False,
        )
        assert_matches_type(PositionClosePositionResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_close_position(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.positions.with_raw_response.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(PositionClosePositionResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_close_position(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.positions.with_streaming_response.close_position(
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(PositionClosePositionResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close_position(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instrument_id` but received ''"):
            await async_client.v1.positions.with_raw_response.close_position(
                instrument_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_close_positions(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.close_positions(
            account_id=0,
        )
        assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

    @parametrize
    async def test_method_close_positions_with_all_params(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.close_positions(
            account_id=0,
            cancel_orders=False,
        )
        assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_close_positions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.positions.with_raw_response.close_positions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_close_positions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.positions.with_streaming_response.close_positions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(PositionClosePositionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_position_instructions(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.get_position_instructions(
            account_id=0,
        )
        assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

    @parametrize
    async def test_method_get_position_instructions_with_all_params(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.get_position_instructions(
            account_id=0,
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_get_position_instructions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.positions.with_raw_response.get_position_instructions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_get_position_instructions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.positions.with_streaming_response.get_position_instructions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(PositionGetPositionInstructionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_positions(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.get_positions(
            account_id=0,
        )
        assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

    @parametrize
    async def test_method_get_positions_with_all_params(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.get_positions(
            account_id=0,
            instrument_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            page_size=1,
            page_token="U3RhaW5sZXNzIHJvY2tz",
            sort_by="SYMBOL",
            sort_direction="ASC",
        )
        assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_get_positions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.positions.with_raw_response.get_positions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_get_positions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.positions.with_streaming_response.get_positions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(PositionGetPositionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit_position_instructions(self, async_client: AsyncClearStreet) -> None:
        position = await async_client.v1.positions.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )
        assert_matches_type(PositionSubmitPositionInstructionsResponse, position, path=["response"])

    @parametrize
    async def test_raw_response_submit_position_instructions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.positions.with_raw_response.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        position = await response.parse()
        assert_matches_type(PositionSubmitPositionInstructionsResponse, position, path=["response"])

    @parametrize
    async def test_streaming_response_submit_position_instructions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.positions.with_streaming_response.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            position = await response.parse()
            assert_matches_type(PositionSubmitPositionInstructionsResponse, position, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from clear_street import ClearStreet, AsyncClearStreet
from clear_street.types.v1.accounts.positions import (
    InstructionGetPositionInstructionsResponse,
    InstructionCancelPositionInstructionResponse,
    InstructionSubmitPositionInstructionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstructions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_position_instruction(self, client: ClearStreet) -> None:
        instruction = client.v1.accounts.positions.instructions.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(InstructionCancelPositionInstructionResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_position_instruction(self, client: ClearStreet) -> None:
        response = client.v1.accounts.positions.instructions.with_raw_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionCancelPositionInstructionResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_position_instruction(self, client: ClearStreet) -> None:
        with client.v1.accounts.positions.instructions.with_streaming_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instruction = response.parse()
            assert_matches_type(InstructionCancelPositionInstructionResponse, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_position_instruction(self, client: ClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instruction_id` but received ''"):
            client.v1.accounts.positions.instructions.with_raw_response.cancel_position_instruction(
                instruction_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_position_instructions(self, client: ClearStreet) -> None:
        instruction = client.v1.accounts.positions.instructions.get_position_instructions(
            account_id=0,
        )
        assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_position_instructions_with_all_params(self, client: ClearStreet) -> None:
        instruction = client.v1.accounts.positions.instructions.get_position_instructions(
            account_id=0,
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_position_instructions(self, client: ClearStreet) -> None:
        response = client.v1.accounts.positions.instructions.with_raw_response.get_position_instructions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = response.parse()
        assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_position_instructions(self, client: ClearStreet) -> None:
        with client.v1.accounts.positions.instructions.with_streaming_response.get_position_instructions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instruction = response.parse()
            assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_position_instructions(self, client: ClearStreet) -> None:
        instruction = client.v1.accounts.positions.instructions.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )
        assert_matches_type(InstructionSubmitPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_position_instructions(self, client: ClearStreet) -> None:
        response = client.v1.accounts.positions.instructions.with_raw_response.submit_position_instructions(
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
        instruction = response.parse()
        assert_matches_type(InstructionSubmitPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_position_instructions(self, client: ClearStreet) -> None:
        with client.v1.accounts.positions.instructions.with_streaming_response.submit_position_instructions(
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

            instruction = response.parse()
            assert_matches_type(InstructionSubmitPositionInstructionsResponse, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstructions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        instruction = await async_client.v1.accounts.positions.instructions.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )
        assert_matches_type(InstructionCancelPositionInstructionResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.positions.instructions.with_raw_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = await response.parse()
        assert_matches_type(InstructionCancelPositionInstructionResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.positions.instructions.with_streaming_response.cancel_position_instruction(
            instruction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instruction = await response.parse()
            assert_matches_type(InstructionCancelPositionInstructionResponse, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_position_instruction(self, async_client: AsyncClearStreet) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instruction_id` but received ''"):
            await async_client.v1.accounts.positions.instructions.with_raw_response.cancel_position_instruction(
                instruction_id="",
                account_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_position_instructions(self, async_client: AsyncClearStreet) -> None:
        instruction = await async_client.v1.accounts.positions.instructions.get_position_instructions(
            account_id=0,
        )
        assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_position_instructions_with_all_params(self, async_client: AsyncClearStreet) -> None:
        instruction = await async_client.v1.accounts.positions.instructions.get_position_instructions(
            account_id=0,
            instrument_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_position_instructions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.positions.instructions.with_raw_response.get_position_instructions(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instruction = await response.parse()
        assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_position_instructions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.positions.instructions.with_streaming_response.get_position_instructions(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instruction = await response.parse()
            assert_matches_type(InstructionGetPositionInstructionsResponse, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_position_instructions(self, async_client: AsyncClearStreet) -> None:
        instruction = await async_client.v1.accounts.positions.instructions.submit_position_instructions(
            account_id=0,
            instructions=[
                {
                    "instruction_type": "EXERCISE",
                    "instrument_id": "0195f6d0-a1b2-7c3d-8e4f-5a6b7c8d9e02",
                    "quantity": "1",
                }
            ],
        )
        assert_matches_type(InstructionSubmitPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_position_instructions(self, async_client: AsyncClearStreet) -> None:
        response = await async_client.v1.accounts.positions.instructions.with_raw_response.submit_position_instructions(
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
        instruction = await response.parse()
        assert_matches_type(InstructionSubmitPositionInstructionsResponse, instruction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_position_instructions(self, async_client: AsyncClearStreet) -> None:
        async with async_client.v1.accounts.positions.instructions.with_streaming_response.submit_position_instructions(
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

            instruction = await response.parse()
            assert_matches_type(InstructionSubmitPositionInstructionsResponse, instruction, path=["response"])

        assert cast(Any, response.is_closed) is True

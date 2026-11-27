from __future__ import annotations

import os
from typing import Dict, List, Type, NoReturn, Optional, cast
from typing_extensions import assert_type

import httpx
import pytest
from respx import MockRouter

from clearstreet import (
    ClearStreet,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    BadRequestError,
    AsyncClearStreet,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
)
from clearstreet.types.v1 import NewOrderRequestParam
from clearstreet.lib.errors import ErrorDetail, ErrorObject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ORDERS: List[NewOrderRequestParam] = [
    {"symbol": "AAPL", "side": "BUY", "order_type": "MARKET", "quantity": "10", "time_in_force": "DAY"}
]

# Shortened from the live response in issue #11.
RISK_CHECK_FAILED: Dict[str, object] = {
    "error": {
        "code": 422,
        "message": "Risk check failed",
        "details": [
            {"description": "Order quantity exceeds account limit", "subject": "order:my-client-id", "type": "MAX_QTY"},
            {"description": "Insufficient buying power", "subject": "order:my-client-id", "type": "BUYING_POWER"},
            {
                "domain": "com.clearstreet.oems.risk",
                "metadata": {"account_id": "100001", "available": "816.88", "required_total": "99999.9999"},
                "reason": "BUYING_POWER",
            },
        ],
    },
    "metadata": {"request_id": "req_123"},
}


def make_error(body: object, status_code: int = 400) -> APIStatusError:
    response = httpx.Response(status_code, request=httpx.Request("GET", base_url))
    return APIStatusError(f"Error code: {status_code}", response=response, body=body)


def assert_risk_check_failed(error: Optional[ErrorObject]) -> None:
    assert isinstance(error, ErrorObject)
    assert error.code == 422
    assert error.message == "Risk check failed"
    assert error.details is not None
    assert all(isinstance(detail, ErrorDetail) for detail in error.details)

    violation, _, context = error.details
    assert_type(violation.type, Optional[str])
    assert violation.type == "MAX_QTY"
    assert violation.subject == "order:my-client-id"
    assert violation.description == "Order quantity exceeds account limit"
    assert violation.reason is None
    assert violation.metadata is None

    assert context.type is None
    assert context.reason == "BUYING_POWER"
    assert context.domain == "com.clearstreet.oems.risk"
    assert context.metadata == {"account_id": "100001", "available": "816.88", "required_total": "99999.9999"}


class TestErrorObject:
    @pytest.mark.respx(base_url=base_url)
    def test_risk_check_rejection(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/accounts/100001/orders").mock(return_value=httpx.Response(422, json=RISK_CHECK_FAILED))

        with pytest.raises(UnprocessableEntityError) as exc_info:
            client.v1.orders.submit_orders(account_id=100001, orders=ORDERS)

        assert_type(exc_info.value.error, Optional[ErrorObject])
        assert_risk_check_failed(exc_info.value.error)
        assert exc_info.value.body == RISK_CHECK_FAILED

    @pytest.mark.respx(base_url=base_url)
    def test_raw_and_streaming_responses(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/accounts/100001/orders").mock(return_value=httpx.Response(422, json=RISK_CHECK_FAILED))

        with pytest.raises(UnprocessableEntityError) as exc_info:
            client.v1.orders.with_raw_response.submit_orders(account_id=100001, orders=ORDERS)
        assert_risk_check_failed(exc_info.value.error)

        with pytest.raises(UnprocessableEntityError) as exc_info:
            with client.v1.orders.with_streaming_response.submit_orders(account_id=100001, orders=ORDERS):
                pass
        assert_risk_check_failed(exc_info.value.error)

    @pytest.mark.respx(base_url=base_url)
    async def test_risk_check_rejection_async(self, async_client: AsyncClearStreet, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/accounts/100001/orders").mock(return_value=httpx.Response(422, json=RISK_CHECK_FAILED))

        with pytest.raises(UnprocessableEntityError) as exc_info:
            await async_client.v1.orders.submit_orders(account_id=100001, orders=ORDERS)

        assert_risk_check_failed(exc_info.value.error)
        assert exc_info.value.body == RISK_CHECK_FAILED

    @pytest.mark.parametrize(
        "status_code, error_class",
        [
            (400, BadRequestError),
            (401, AuthenticationError),
            (403, PermissionDeniedError),
            (404, NotFoundError),
            (409, ConflictError),
            (422, UnprocessableEntityError),
            (429, RateLimitError),
            (500, InternalServerError),
            (503, InternalServerError),
        ],
    )
    @pytest.mark.respx(base_url=base_url)
    def test_every_status_code(
        self, client: ClearStreet, respx_mock: MockRouter, status_code: int, error_class: Type[APIStatusError]
    ) -> None:
        body = {"error": {"code": status_code, "message": "Request failed"}, "metadata": {"request_id": "req_123"}}
        respx_mock.get("/v1/accounts").mock(return_value=httpx.Response(status_code, json=body))

        with pytest.raises(error_class) as exc_info:
            client.with_options(max_retries=0).v1.accounts.get_accounts()

        error = exc_info.value.error
        assert isinstance(error, ErrorObject)
        assert error.code == status_code
        assert error.message == "Request failed"
        assert error.details is None

    @pytest.mark.respx(base_url=base_url)
    def test_body_that_is_not_json(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/accounts").mock(return_value=httpx.Response(502, text="<html>Bad Gateway</html>"))

        with pytest.raises(InternalServerError) as exc_info:
            client.with_options(max_retries=0).v1.accounts.get_accounts()

        assert exc_info.value.error is None
        assert exc_info.value.body == "<html>Bad Gateway</html>"

    @pytest.mark.respx(base_url=base_url)
    def test_parsing_never_raises(
        self, client: ClearStreet, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def fail(**_: object) -> NoReturn:
            raise RuntimeError("parsing failed")

        monkeypatch.setattr("clearstreet.lib.errors.construct_type_unchecked", fail)
        respx_mock.post("/v1/accounts/100001/orders").mock(return_value=httpx.Response(422, json=RISK_CHECK_FAILED))

        with pytest.raises(UnprocessableEntityError) as exc_info:
            client.v1.orders.submit_orders(account_id=100001, orders=ORDERS)

        assert exc_info.value.error is None
        assert exc_info.value.body == RISK_CHECK_FAILED

    @pytest.mark.parametrize(
        "body",
        [
            None,
            "",
            "Not Found",
            [],
            {},
            {"message": "Not found"},
            {"error": None},
            {"error": "Not found"},
            {"error": []},
        ],
        ids=[
            "none",
            "empty",
            "text",
            "list",
            "empty-object",
            "no-error-key",
            "null-error",
            "string-error",
            "list-error",
        ],
    )
    def test_no_error_object(self, body: object) -> None:
        error = make_error(body)

        assert error.error is None
        assert error.body == body

    def test_detail_shapes(self) -> None:
        details: List[object] = [
            {"instrument_id": "a1a2a3a4-b1b2-c1c2-d1d2-e1e2e3e4e5e6"},
            {"field": "quantity", "description": "must be positive"},
        ]
        error = make_error({"error": {"code": 404, "message": "Not found", "details": details}}, 404).error

        assert error is not None
        assert error.details is not None
        not_found, unknown = error.details
        assert not_found.instrument_id == "a1a2a3a4-b1b2-c1c2-d1d2-e1e2e3e4e5e6"
        assert not_found.type is None
        assert unknown.description == "must be positive"
        assert unknown.type is None
        assert unknown.to_dict() == {"field": "quantity", "description": "must be positive"}

    def test_values_of_unexpected_types_are_kept(self) -> None:
        details: List[object] = [
            {"type": "MAX_QTY", "subject": "order:my-client-id", "description": "Order quantity exceeds account limit"},
            {"reason": "BUYING_POWER", "metadata": {"available": 816.88, "limit": None}},
        ]
        error = make_error({"error": {"code": 422, "message": "Risk check failed", "details": details}}, 422).error

        assert isinstance(error, ErrorObject)
        assert error.details is not None
        assert all(isinstance(detail, ErrorDetail) for detail in error.details)
        violation, context = error.details
        assert violation.type == "MAX_QTY"
        assert context.reason == "BUYING_POWER"
        assert cast(object, context.metadata) == {"available": 816.88, "limit": None}

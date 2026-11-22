from __future__ import annotations

import os
import json
from typing import Any, Dict, List, Tuple, Iterator, Optional, cast
from typing_extensions import assert_type

import httpx
import pytest
from respx import MockRouter

from clearstreet import ClearStreet, AsyncClearStreet
from clearstreet.types.v1 import (
    InstrumentCore,
    ScreenerColumn,
    FilterValueParam,
    SearchFilterParam,
    OrderGetOrdersResponse,
)
from clearstreet.lib.pagination import paginate, async_paginate

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

TOKEN_1 = "AAAAAAAAAAIAAAAAAAAAAg"
TOKEN_2 = "AAAAAAAAAAQAAAAAAAAAAg-_"

Pages = Dict[Optional[str], Tuple[object, Optional[str]]]

# Most tests use loose validation, so mocked items only need the fields a test reads. Tests whose pages
# have no items also run with strict validation.
loose = pytest.mark.parametrize("client", [False], indirect=True, ids=["loose"])
loose_and_strict = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])
async_loose = pytest.mark.parametrize("async_client", [False], indirect=True, ids=["loose"])
async_loose_and_strict = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])


class FakeAPI:
    """Serves `pages[page_token] = (data, next_page_token)` and records every request.

    Unknown tokens, and requests beyond `max_requests`, get a 400, which the client does not retry,
    so a pagination bug fails the test instead of looping.
    """

    def __init__(self, pages: Pages, max_requests: int = 5) -> None:
        self.pages = pages
        self.max_requests = max_requests
        self.requests: List[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if request.method == "GET":
            token = request.url.params.get("page_token")
        else:
            token = json.loads(request.content).get("page_token")
        if token not in self.pages or len(self.requests) > self.max_requests:
            return httpx.Response(400, json={"message": "unexpected request"})
        data, next_page_token = self.pages[token]
        metadata = {"request_id": f"req_{len(self.requests)}", "next_page_token": next_page_token}
        return httpx.Response(200, json={"data": data, "metadata": metadata})

    @property
    def params(self) -> List[Dict[str, str]]:
        return [dict(request.url.params) for request in self.requests]

    @property
    def bodies(self) -> List[Any]:
        return [json.loads(request.content) for request in self.requests]


def market_cap_values() -> Iterator[FilterValueParam]:
    yield {"value": 1e9}


def market_cap_filters() -> Iterator[SearchFilterParam]:
    yield {"left": {"name": "market_cap"}, "op": {"name": "GREATER_OR_EQUAL"}, "right": market_cap_values()}


MARKET_CAP_FILTERS = [{"left": {"name": "market_cap"}, "op": {"name": "GREATER_OR_EQUAL"}, "right": [{"value": 1e9}]}]

# A first iteration stopped after one item, then two full iterations over two pages.
RESTARTED_PARAMS = [
    {"instrument_type": "COMMON_STOCK", "page_size": "1"},
    {"instrument_type": "COMMON_STOCK", "page_size": "1"},
    {"instrument_type": "COMMON_STOCK", "page_token": TOKEN_1},
    {"instrument_type": "COMMON_STOCK", "page_size": "1"},
    {"instrument_type": "COMMON_STOCK", "page_token": TOKEN_1},
]

REPEATED_TOKENS: List[Tuple[Pages, Dict[str, Any], int]] = [
    ({None: ([], TOKEN_1), TOKEN_1: ([], TOKEN_1)}, {}, 2),
    ({None: ([], TOKEN_1), TOKEN_1: ([], TOKEN_2), TOKEN_2: ([], TOKEN_1)}, {}, 3),
    ({TOKEN_1: ([], TOKEN_2)}, {"extra_query": {"page_token": TOKEN_1}}, 2),
    ({TOKEN_1: ([], TOKEN_1)}, {"page_token": TOKEN_1}, 1),
]
repeated_tokens = pytest.mark.parametrize(
    "pages, kwargs, expected_requests",
    REPEATED_TOKENS,
    ids=["server-repeats-token", "token-cycle", "page-token-in-extra-query", "server-repeats-resume-token"],
)


class TestPaginate:
    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_iterates_items_across_pages(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI(
            {
                None: ([{"symbol": "A"}, {"symbol": "B"}], TOKEN_1),
                TOKEN_1: ([{"symbol": "C"}], TOKEN_2),
                TOKEN_2: ([{"symbol": "D"}], None),
            }
        )
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        pager = paginate(client.v1.instruments.get_instruments, instrument_type="COMMON_STOCK", page_size=2)
        assert api.requests == []

        instruments = list(pager)

        assert_type(instruments, List[InstrumentCore])
        assert all(isinstance(instrument, InstrumentCore) for instrument in instruments)
        assert [instrument.symbol for instrument in instruments] == ["A", "B", "C", "D"]
        assert api.params == [
            {"instrument_type": "COMMON_STOCK", "page_size": "2"},
            {"instrument_type": "COMMON_STOCK", "page_token": TOKEN_1},
            {"instrument_type": "COMMON_STOCK", "page_token": TOKEN_2},
        ]

    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_iter_pages_resends_arguments_and_follows_empty_pages(
        self, client: ClearStreet, respx_mock: MockRouter
    ) -> None:
        api = FakeAPI({None: ([{"id": "o1"}], TOKEN_1), TOKEN_1: ([], TOKEN_2), TOKEN_2: ([{"id": "o2"}], None)})
        respx_mock.get("/v1/accounts/123/orders").mock(side_effect=api)

        pager = paginate(client.v1.orders.get_orders, 123, status=["NEW", "FILLED"], extra_headers={"X-Test": "1"})
        pages = list(pager.iter_pages())

        assert_type(pages, List[OrderGetOrdersResponse])
        assert [[order.id for order in page.data] for page in pages] == [["o1"], [], ["o2"]]
        assert [page.metadata.next_page_token for page in pages] == [TOKEN_1, TOKEN_2, None]
        assert api.params == [
            {"status": "NEW,FILLED"},
            {"status": "NEW,FILLED", "page_token": TOKEN_1},
            {"status": "NEW,FILLED", "page_token": TOKEN_2},
        ]
        assert [request.headers["X-Test"] for request in api.requests] == ["1", "1", "1"]

    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_sends_page_token_in_the_json_body(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: ([[{"name": "AAPL"}]], TOKEN_1), TOKEN_1: ([[{"name": "MSFT"}]], None)})
        respx_mock.post("/v1/screener").mock(side_effect=api)

        rows = list(paginate(client.v1.screener.search_screener, columns=[{"name": "symbol"}], page_size=1))

        assert_type(rows, List[List[ScreenerColumn]])
        assert [row[0].name for row in rows] == ["AAPL", "MSFT"]
        assert api.bodies == [
            {"columns": [{"name": "symbol"}], "page_size": 1},
            {"columns": [{"name": "symbol"}], "page_token": TOKEN_1},
        ]
        assert api.params == [{}, {}]

    @loose_and_strict
    @pytest.mark.respx(base_url=base_url)
    def test_reads_iterator_arguments_once(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: ([], TOKEN_1), TOKEN_1: ([], None)})
        respx_mock.post("/v1/screener").mock(side_effect=api)

        pager = paginate(client.v1.screener.search_screener, filters=market_cap_filters())
        list(pager)
        list(pager)

        assert [body["filters"] for body in api.bodies] == [MARKET_CAP_FILTERS] * 4

    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_nested_data_is_read_from_pages(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: ({"events": [{"code": "E1"}]}, TOKEN_1), TOKEN_1: ({"events": [{"code": "E2"}]}, None)})
        respx_mock.get("/v1/instruments/predictions/events").mock(side_effect=api)

        pager = paginate(client.v1.instruments.get_prediction_events)

        assert [event.code for page in pager.iter_pages() for event in page.data.events] == ["E1", "E2"]
        with pytest.raises(TypeError, match="iter_pages"):
            list(cast(Any, pager))

    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_null_data_is_an_empty_page(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: (None, TOKEN_1), TOKEN_1: ([{"symbol": "A"}], None)})
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        assert [instrument.symbol for instrument in paginate(client.v1.instruments.get_instruments)] == ["A"]
        assert len(api.requests) == 2

    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_resumes_from_page_token(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({TOKEN_1: ([{"symbol": "B"}], TOKEN_2), TOKEN_2: ([{"symbol": "C"}], None)})
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        pager = paginate(client.v1.instruments.get_instruments, page_token=TOKEN_1, page_size=1)

        assert [instrument.symbol for instrument in pager] == ["B", "C"]
        assert api.params == [{"page_size": "1", "page_token": TOKEN_1}, {"page_token": TOKEN_2}]

    @loose_and_strict
    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.parametrize("next_page_token", [None, ""])
    def test_stops_without_next_page_token(
        self, client: ClearStreet, respx_mock: MockRouter, next_page_token: Optional[str]
    ) -> None:
        api = FakeAPI({None: ([], next_page_token)})
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        assert list(paginate(client.v1.instruments.get_instruments)) == []
        assert len(api.requests) == 1

    @loose_and_strict
    @pytest.mark.respx(base_url=base_url)
    @repeated_tokens
    def test_raises_instead_of_repeating_a_page_token(
        self, client: ClearStreet, respx_mock: MockRouter, pages: Pages, kwargs: Dict[str, Any], expected_requests: int
    ) -> None:
        api = FakeAPI(pages)
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        received: List[object] = []
        with pytest.raises(RuntimeError, match="already sent"):
            for page in paginate(client.v1.instruments.get_instruments, **kwargs).iter_pages():
                received.append(page)
        assert len(received) == len(api.requests) == expected_requests

    @loose
    @pytest.mark.respx(base_url=base_url)
    def test_fetches_lazily_and_restarts_on_each_iteration(self, client: ClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: ([{"symbol": "A"}], TOKEN_1), TOKEN_1: ([{"symbol": "B"}], None)})
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        pager = paginate(client.v1.instruments.get_instruments, instrument_type="COMMON_STOCK", page_size=1)
        assert len(api.requests) == 0

        assert next(iter(pager)).symbol == "A"
        assert len(api.requests) == 1

        assert [instrument.symbol for instrument in pager] == ["A", "B"]
        assert [instrument.symbol for instrument in pager] == ["A", "B"]
        assert api.params == RESTARTED_PARAMS


class TestAsyncPaginate:
    @async_loose
    @pytest.mark.respx(base_url=base_url)
    async def test_iterates_items_across_pages(self, async_client: AsyncClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: ([{"symbol": "A"}, {"symbol": "B"}], TOKEN_1), TOKEN_1: ([{"symbol": "C"}], None)})
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        pager = async_paginate(async_client.v1.instruments.get_instruments, instrument_type="COMMON_STOCK", page_size=2)
        instruments = [instrument async for instrument in pager]

        assert_type(instruments, List[InstrumentCore])
        assert [instrument.symbol for instrument in instruments] == ["A", "B", "C"]
        assert api.params == [
            {"instrument_type": "COMMON_STOCK", "page_size": "2"},
            {"instrument_type": "COMMON_STOCK", "page_token": TOKEN_1},
        ]

    @async_loose
    @pytest.mark.respx(base_url=base_url)
    async def test_iter_pages_resends_arguments_and_follows_empty_pages(
        self, async_client: AsyncClearStreet, respx_mock: MockRouter
    ) -> None:
        api = FakeAPI({None: ([{"id": "o1"}], TOKEN_1), TOKEN_1: ([], TOKEN_2), TOKEN_2: ([{"id": "o2"}], None)})
        respx_mock.get("/v1/accounts/123/orders").mock(side_effect=api)

        pager = async_paginate(
            async_client.v1.orders.get_orders, 123, status=["NEW", "FILLED"], extra_headers={"X-Test": "1"}
        )
        pages = [page async for page in pager.iter_pages()]

        assert_type(pages, List[OrderGetOrdersResponse])
        assert [[order.id for order in page.data] for page in pages] == [["o1"], [], ["o2"]]
        assert api.params == [
            {"status": "NEW,FILLED"},
            {"status": "NEW,FILLED", "page_token": TOKEN_1},
            {"status": "NEW,FILLED", "page_token": TOKEN_2},
        ]
        assert [request.headers["X-Test"] for request in api.requests] == ["1", "1", "1"]

    @async_loose
    @pytest.mark.respx(base_url=base_url)
    async def test_sends_page_token_in_the_json_body(
        self, async_client: AsyncClearStreet, respx_mock: MockRouter
    ) -> None:
        api = FakeAPI({None: ([[{"name": "AAPL"}]], TOKEN_1), TOKEN_1: ([[{"name": "MSFT"}]], None)})
        respx_mock.post("/v1/screener").mock(side_effect=api)

        pager = async_paginate(async_client.v1.screener.search_screener, filters=market_cap_filters(), page_size=1)
        rows = [row async for row in pager]

        assert_type(rows, List[List[ScreenerColumn]])
        assert [row[0].name for row in rows] == ["AAPL", "MSFT"]
        assert api.bodies == [
            {"filters": MARKET_CAP_FILTERS, "page_size": 1},
            {"filters": MARKET_CAP_FILTERS, "page_token": TOKEN_1},
        ]

    @async_loose
    @pytest.mark.respx(base_url=base_url)
    async def test_nested_data_is_read_from_pages(self, async_client: AsyncClearStreet, respx_mock: MockRouter) -> None:
        api = FakeAPI({None: ({"events": [{"code": "E1"}]}, TOKEN_1), TOKEN_1: ({"events": [{"code": "E2"}]}, None)})
        respx_mock.get("/v1/instruments/predictions/events").mock(side_effect=api)

        pager = async_paginate(async_client.v1.instruments.get_prediction_events)

        assert [event.code async for page in pager.iter_pages() for event in page.data.events] == ["E1", "E2"]
        with pytest.raises(TypeError, match="iter_pages"):
            [event async for event in cast(Any, pager)]

    @async_loose_and_strict
    @pytest.mark.respx(base_url=base_url)
    @repeated_tokens
    async def test_raises_instead_of_repeating_a_page_token(
        self,
        async_client: AsyncClearStreet,
        respx_mock: MockRouter,
        pages: Pages,
        kwargs: Dict[str, Any],
        expected_requests: int,
    ) -> None:
        api = FakeAPI(pages)
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        received: List[object] = []
        with pytest.raises(RuntimeError, match="already sent"):
            async for page in async_paginate(async_client.v1.instruments.get_instruments, **kwargs).iter_pages():
                received.append(page)
        assert len(received) == len(api.requests) == expected_requests

    @async_loose
    @pytest.mark.respx(base_url=base_url)
    async def test_fetches_lazily_and_restarts_on_each_iteration(
        self, async_client: AsyncClearStreet, respx_mock: MockRouter
    ) -> None:
        api = FakeAPI({None: ([{"symbol": "A"}], TOKEN_1), TOKEN_1: ([{"symbol": "B"}], None)})
        respx_mock.get("/v1/instruments").mock(side_effect=api)

        pager = async_paginate(async_client.v1.instruments.get_instruments, instrument_type="COMMON_STOCK", page_size=1)
        assert len(api.requests) == 0

        async for instrument in pager:
            assert instrument.symbol == "A"
            break
        assert len(api.requests) == 1

        assert [instrument.symbol async for instrument in pager] == ["A", "B"]
        assert [instrument.symbol async for instrument in pager] == ["A", "B"]
        assert api.params == RESTARTED_PARAMS

"""Auto-pagination for list methods that page with `page_size` and `page_token`.

```py
from clearstreet import ClearStreet
from clearstreet.lib.pagination import paginate

client = ClearStreet()

for instrument in paginate(client.v1.instruments.get_instruments, instrument_type="COMMON_STOCK"):
    print(instrument.symbol)
```
"""

from __future__ import annotations

import io
from typing import (
    Set,
    Dict,
    Tuple,
    Generic,
    TypeVar,
    Callable,
    Iterable,
    Iterator,
    Optional,
    Sequence,
    Awaitable,
    AsyncIterator,
    cast,
)
from typing_extensions import Protocol, ParamSpec

__all__ = ["paginate", "async_paginate", "SyncPager", "AsyncPager"]

_P = ParamSpec("_P")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

_Args = Tuple[object, ...]
_Kwargs = Dict[str, object]


class _PageMetadata(Protocol):
    @property
    def next_page_token(self) -> Optional[str]: ...


class _Page(Protocol):
    @property
    def metadata(self) -> _PageMetadata: ...


class _PageWithListData(_Page, Protocol[_T_co]):
    @property
    def data(self) -> Sequence[_T_co]: ...


_PageT = TypeVar("_PageT", bound=_Page)
_PageT_co = TypeVar("_PageT_co", bound=_Page, covariant=True)


def paginate(method: Callable[_P, _PageT], /, *args: _P.args, **kwargs: _P.kwargs) -> SyncPager[_PageT]:
    """Iterate over the items of a `ClearStreet` list method across all of its pages.

    `args` and `kwargs` are type-checked against `method` and sent with every request, except
    `page_size`, which is only sent with the first request: each later request sends the previous
    page's `metadata.next_page_token` as `page_token`, until a page has no `next_page_token`.
    Pass `page_token` to resume from a token you saved earlier. No request is made until you
    iterate, and each iteration starts again from the first page. Iterator arguments, such as
    generators, are read into lists here, so that every request can send them.

    ```py
    for instrument in paginate(client.v1.instruments.get_instruments, page_size=1000):
        print(instrument.symbol)

    # whole pages, e.g. for `metadata` or for methods whose `data` wraps the list
    for page in paginate(client.v1.instruments.get_prediction_events).iter_pages():
        for event in page.data.events:
            print(event.code)
    ```
    """
    return SyncPager(method, _snapshot_args(args), _snapshot_kwargs(kwargs))


def async_paginate(
    method: Callable[_P, Awaitable[_PageT]], /, *args: _P.args, **kwargs: _P.kwargs
) -> AsyncPager[_PageT]:
    """Iterate over the items of an `AsyncClearStreet` list method with `async for`; see `paginate()`.

    ```py
    async for instrument in async_paginate(client.v1.instruments.get_instruments, page_size=1000):
        print(instrument.symbol)
    ```
    """
    return AsyncPager(method, _snapshot_args(args), _snapshot_kwargs(kwargs))


class SyncPager(Generic[_PageT_co]):
    """Requests the pages of a list method lazily, following `metadata.next_page_token`.

    Iterating yields the items of each page's `data` list, and `iter_pages()` yields the pages
    themselves. Use `iter_pages()` to read `metadata` or `error`, and for methods whose `data`
    is an object that wraps the list: for those, iterating the pager is a type error. Raises
    `RuntimeError` instead of sending a `page_token` that was already sent. Create pagers with
    `paginate()`.
    """

    def __init__(self, method: Callable[..., _PageT_co], args: _Args, kwargs: _Kwargs) -> None:
        self._method = method
        self._args = args
        self._kwargs = kwargs

    def __iter__(self: SyncPager[_PageWithListData[_T]]) -> Iterator[_T]:
        for page in self.iter_pages():
            yield from _page_items(page)

    def iter_pages(self) -> Iterator[_PageT_co]:
        kwargs: Optional[_Kwargs] = self._kwargs
        sent_tokens: Set[str] = set()
        while kwargs is not None:
            page = self._method(*self._args, **kwargs)
            yield page
            kwargs = _next_page_kwargs(kwargs, page, sent_tokens)


class AsyncPager(Generic[_PageT_co]):
    """The async version of `SyncPager`, for `async for`. Create pagers with `async_paginate()`."""

    def __init__(self, method: Callable[..., Awaitable[_PageT_co]], args: _Args, kwargs: _Kwargs) -> None:
        self._method = method
        self._args = args
        self._kwargs = kwargs

    async def __aiter__(self: AsyncPager[_PageWithListData[_T]]) -> AsyncIterator[_T]:
        async for page in self.iter_pages():
            for item in _page_items(page):
                yield item

    async def iter_pages(self) -> AsyncIterator[_PageT_co]:
        kwargs: Optional[_Kwargs] = self._kwargs
        sent_tokens: Set[str] = set()
        while kwargs is not None:
            page = await self._method(*self._args, **kwargs)
            yield page
            kwargs = _next_page_kwargs(kwargs, page, sent_tokens)


def _next_page_kwargs(kwargs: _Kwargs, page: _Page, sent_tokens: Set[str]) -> Optional[_Kwargs]:
    sent = kwargs.get("page_token")
    if isinstance(sent, str):
        sent_tokens.add(sent)

    token = page.metadata.next_page_token
    if not token:
        return None
    if token in sent_tokens:
        raise RuntimeError(
            f"The API returned a `next_page_token` that was already sent ({token!r}), so the next page would repeat"
            " an earlier one. If you set `page_token` through `extra_query` or `extra_body`, pass it as `page_token`."
        )

    # The token carries the page size, and the API ignores `page_size` whenever `page_token` is sent.
    next_kwargs = {key: value for key, value in kwargs.items() if key != "page_size"}
    next_kwargs["page_token"] = token
    return next_kwargs


def _page_items(page: _PageWithListData[_T]) -> Sequence[_T]:
    data = page.data
    if not data:
        return []
    if not isinstance(data, list):
        raise TypeError(
            f"`{type(page).__name__}.data` is not a list; use `.iter_pages()` and read the items from each page"
        )
    return data


def _snapshot(value: object) -> object:
    # One-shot iterators (generators, `map()`, `iter()`) would be empty by the second request.
    if isinstance(value, io.IOBase):
        return value
    if isinstance(value, dict):
        return {key: _snapshot(item) for key, item in cast("Dict[object, object]", value).items()}
    if isinstance(value, tuple):
        return tuple(_snapshot(item) for item in cast("Tuple[object, ...]", value))
    if isinstance(value, (list, Iterator)):
        return [_snapshot(item) for item in cast("Iterable[object]", value)]
    return value


def _snapshot_args(args: _Args) -> _Args:
    return tuple(_snapshot(arg) for arg in args)


def _snapshot_kwargs(kwargs: _Kwargs) -> _Kwargs:
    return {key: _snapshot(value) for key, value in kwargs.items()}

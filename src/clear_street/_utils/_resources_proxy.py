from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `clear_street.resources` module.

    This is used so that we can lazily import `clear_street.resources` only when
    needed *and* so that users can just import `clear_street` and reference `clear_street.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("clear_street.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()

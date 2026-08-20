# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .catalog import Catalog
from ..shared.base_response import BaseResponse

__all__ = ["ScreenerGetScreenerCatalogResponse"]


class ScreenerGetScreenerCatalogResponse(BaseResponse):
    data: Catalog
    """
    The complete screener field catalog, serialized as the `data` payload of
    `GET /screener/catalog`.
    """

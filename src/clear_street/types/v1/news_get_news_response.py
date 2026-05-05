# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .news_item_list import NewsItemList
from ..shared.base_response import BaseResponse

__all__ = ["NewsGetNewsResponse"]


class NewsGetNewsResponse(BaseResponse):
    data: NewsItemList

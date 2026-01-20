# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .instrument_news_list import InstrumentNewsList
from ....shared.base_response import BaseResponse

__all__ = ["NewsGetInstrumentNewsResponse"]


class NewsGetInstrumentNewsResponse(BaseResponse):
    data: InstrumentNewsList

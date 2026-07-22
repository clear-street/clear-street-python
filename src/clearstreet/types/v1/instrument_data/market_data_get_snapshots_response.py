# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...shared.base_response import BaseResponse
from .market_data_snapshot_list import MarketDataSnapshotList

__all__ = ["MarketDataGetSnapshotsResponse"]


class MarketDataGetSnapshotsResponse(BaseResponse):
    data: MarketDataSnapshotList

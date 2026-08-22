# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .ioi_resource import IoiResource
from .ioi_company_resource import IoiCompanyResource
from .ioi_offering_resource import IoiOfferingResource

__all__ = ["IoiListingResource"]


class IoiListingResource(IoiResource):
    """IOI list item with the campaign identity needed to render it."""

    company: IoiCompanyResource
    """Company identity embedded in an IOI list item."""

    offering: IoiOfferingResource
    """Offering identity embedded in an IOI list item."""

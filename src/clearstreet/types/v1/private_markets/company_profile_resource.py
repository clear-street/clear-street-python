# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .company_person import CompanyPerson
from .company_category import CompanyCategory
from .company_citation import CompanyCitation
from .company_customer import CompanyCustomer
from .company_social_link import CompanySocialLink
from .company_headquarters import CompanyHeadquarters
from .company_legal_entity import CompanyLegalEntity
from .company_metric_series import CompanyMetricSeries
from .company_document_resource import CompanyDocumentResource
from .company_narrative_section import CompanyNarrativeSection

__all__ = ["CompanyProfileResource"]


class CompanyProfileResource(BaseModel):
    """The complete versioned company profile (schema version one)."""

    categories: Optional[List[CompanyCategory]] = None
    """Company categories."""

    citations: Optional[List[CompanyCitation]] = None
    """Sources referenced by narrative sections and metrics."""

    customers: Optional[List[CompanyCustomer]] = None
    """Named customers evidenced by the source material."""

    documents: Optional[List[CompanyDocumentResource]] = None
    """Company-level research and source documents."""

    headquarters: Optional[CompanyHeadquarters] = None
    """Company headquarters, when known."""

    legal_entities: Optional[List[CompanyLegalEntity]] = None
    """Known legal entities associated with the company."""

    metric_series: Optional[List[CompanyMetricSeries]] = None
    """Historical and estimated metric series."""

    narrative_sections: Optional[List[CompanyNarrativeSection]] = None
    """Ordered durable company fact and thesis blocks."""

    overview: Optional[str] = None
    """Long company overview."""

    people: Optional[List[CompanyPerson]] = None
    """Key people and their roles."""

    social: Optional[List[CompanySocialLink]] = None
    """Social/profile links."""

    tagline: Optional[str] = None
    """Short durable positioning line used with the company name."""

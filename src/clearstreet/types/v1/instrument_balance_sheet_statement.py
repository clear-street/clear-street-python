# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ..._models import BaseModel
from .fiscal_period_type import FiscalPeriodType

__all__ = ["InstrumentBalanceSheetStatement"]


class InstrumentBalanceSheetStatement(BaseModel):
    """A quarterly balance sheet statement for an instrument."""

    accepted_date: datetime
    """The date and time when the filing was accepted by the SEC"""

    filing_date: date
    """The date the financial statement was filed"""

    period: str
    """The fiscal period identifier (e.g., "Q1", "Q2", "Q3", "Q4")"""

    period_type: FiscalPeriodType
    """The type of fiscal period"""

    reported_currency: str
    """The currency in which the statement is reported (ISO 4217)"""

    year: int
    """The fiscal year of the statement"""

    account_payables: Optional[str] = None
    """Account payables"""

    accounts_receivables: Optional[str] = None
    """Accounts receivables"""

    accrued_expenses: Optional[str] = None
    """Accrued expenses"""

    accumulated_other_comprehensive_income_loss: Optional[str] = None
    """Accumulated other comprehensive income/loss"""

    additional_paid_in_capital: Optional[str] = None
    """Additional paid-in capital"""

    capital_lease_obligations: Optional[str] = None
    """Capital lease obligations (total)"""

    capital_lease_obligations_current: Optional[str] = None
    """Capital lease obligations (current portion)"""

    cash_and_cash_equivalents: Optional[str] = None
    """Cash and cash equivalents"""

    cash_and_short_term_investments: Optional[str] = None
    """Cash and short-term investments combined"""

    common_stock: Optional[str] = None
    """Common stock"""

    deferred_revenue: Optional[str] = None
    """Deferred revenue"""

    deferred_revenue_non_current: Optional[str] = None
    """Deferred revenue (non-current)"""

    deferred_tax_liabilities_non_current: Optional[str] = None
    """Deferred tax liabilities (non-current)"""

    goodwill: Optional[str] = None
    """Goodwill"""

    goodwill_and_intangible_assets: Optional[str] = None
    """Goodwill and intangible assets combined"""

    intangible_assets: Optional[str] = None
    """Intangible assets"""

    inventory: Optional[str] = None
    """Inventory"""

    long_term_debt: Optional[str] = None
    """Long-term debt"""

    long_term_investments: Optional[str] = None
    """Long-term investments"""

    minority_interest: Optional[str] = None
    """Minority interest"""

    net_debt: Optional[str] = None
    """Net debt (total debt minus cash)"""

    net_receivables: Optional[str] = None
    """Net receivables"""

    other_assets: Optional[str] = None
    """Other assets"""

    other_current_assets: Optional[str] = None
    """Other current assets"""

    other_current_liabilities: Optional[str] = None
    """Other current liabilities"""

    other_liabilities: Optional[str] = None
    """Other liabilities"""

    other_non_current_assets: Optional[str] = None
    """Other non-current assets"""

    other_non_current_liabilities: Optional[str] = None
    """Other non-current liabilities"""

    other_payables: Optional[str] = None
    """Other payables"""

    other_receivables: Optional[str] = None
    """Other receivables"""

    other_total_stockholders_equity: Optional[str] = None
    """Other total stockholders equity"""

    preferred_stock: Optional[str] = None
    """Preferred stock"""

    prepaids: Optional[str] = None
    """Prepaids"""

    property_plant_and_equipment_net: Optional[str] = None
    """Property, plant and equipment net of depreciation"""

    retained_earnings: Optional[str] = None
    """Retained earnings"""

    short_term_debt: Optional[str] = None
    """Short-term debt"""

    short_term_investments: Optional[str] = None
    """Short-term investments"""

    tax_assets: Optional[str] = None
    """Tax assets"""

    tax_payables: Optional[str] = None
    """Tax payables"""

    total_assets: Optional[str] = None
    """Total assets"""

    total_current_assets: Optional[str] = None
    """Total current assets"""

    total_current_liabilities: Optional[str] = None
    """Total current liabilities"""

    total_debt: Optional[str] = None
    """Total debt"""

    total_equity: Optional[str] = None
    """Total equity"""

    total_investments: Optional[str] = None
    """Total investments"""

    total_liabilities: Optional[str] = None
    """Total liabilities"""

    total_liabilities_and_total_equity: Optional[str] = None
    """Total liabilities and total equity"""

    total_non_current_assets: Optional[str] = None
    """Total non-current assets"""

    total_non_current_liabilities: Optional[str] = None
    """Total non-current liabilities"""

    total_payables: Optional[str] = None
    """Total payables"""

    total_stockholders_equity: Optional[str] = None
    """Total stockholders equity"""

    treasury_stock: Optional[str] = None
    """Treasury stock"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ....._models import BaseModel
from ..fiscal_period_type import FiscalPeriodType

__all__ = ["InstrumentCashFlowStatement"]


class InstrumentCashFlowStatement(BaseModel):
    """A quarterly cash flow statement for an instrument."""

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

    accounts_payables: Optional[str] = None
    """Change in accounts payables"""

    accounts_receivables: Optional[str] = None
    """Change in accounts receivables"""

    acquisitions_net: Optional[str] = None
    """Net acquisitions"""

    capital_expenditure: Optional[str] = None
    """Capital expenditure"""

    cash_at_beginning_of_period: Optional[str] = None
    """Cash and cash equivalents at beginning of period"""

    cash_at_end_of_period: Optional[str] = None
    """Cash and cash equivalents at end of period"""

    change_in_working_capital: Optional[str] = None
    """Change in working capital"""

    common_dividends_paid: Optional[str] = None
    """Common dividends paid"""

    common_stock_issuance: Optional[str] = None
    """Common stock issuance"""

    common_stock_repurchased: Optional[str] = None
    """Common stock repurchased (buybacks)"""

    deferred_income_tax: Optional[str] = None
    """Deferred income tax expense"""

    depreciation_and_amortization: Optional[str] = None
    """Depreciation and amortization expense"""

    effect_of_forex_changes_on_cash: Optional[str] = None
    """Effect of foreign exchange changes on cash"""

    free_cash_flow: Optional[str] = None
    """Free cash flow (operating cash flow minus capital expenditure)"""

    income_taxes_paid: Optional[str] = None
    """Income taxes paid"""

    interest_paid: Optional[str] = None
    """Interest paid"""

    inventory: Optional[str] = None
    """Change in inventory"""

    investments_in_property_plant_and_equipment: Optional[str] = None
    """Investments in property, plant, and equipment"""

    long_term_net_debt_issuance: Optional[str] = None
    """Long-term net debt issuance"""

    net_cash_provided_by_financing_activities: Optional[str] = None
    """Net cash provided by financing activities"""

    net_cash_provided_by_investing_activities: Optional[str] = None
    """Net cash provided by investing activities"""

    net_cash_provided_by_operating_activities: Optional[str] = None
    """Net cash provided by operating activities"""

    net_change_in_cash: Optional[str] = None
    """Net change in cash during the period"""

    net_common_stock_issuance: Optional[str] = None
    """Net common stock issuance"""

    net_debt_issuance: Optional[str] = None
    """Net debt issuance (long-term + short-term)"""

    net_dividends_paid: Optional[str] = None
    """Net dividends paid (common + preferred)"""

    net_income: Optional[str] = None
    """Net income for the period"""

    net_preferred_stock_issuance: Optional[str] = None
    """Net preferred stock issuance"""

    net_stock_issuance: Optional[str] = None
    """Net stock issuance (common + preferred)"""

    operating_cash_flow: Optional[str] = None
    """Operating cash flow (alternative calculation)"""

    other_financing_activities: Optional[str] = None
    """Other financing activities"""

    other_investing_activities: Optional[str] = None
    """Other investing activities"""

    other_non_cash_items: Optional[str] = None
    """Other non-cash items"""

    other_working_capital: Optional[str] = None
    """Change in other working capital"""

    preferred_dividends_paid: Optional[str] = None
    """Preferred dividends paid"""

    purchases_of_investments: Optional[str] = None
    """Purchases of investments"""

    sales_maturities_of_investments: Optional[str] = None
    """Sales and maturities of investments"""

    short_term_net_debt_issuance: Optional[str] = None
    """Short-term net debt issuance"""

    stock_based_compensation: Optional[str] = None
    """Stock-based compensation expense"""

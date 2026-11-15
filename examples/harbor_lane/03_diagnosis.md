# Diagnosis: Harbor Lane Supply Co. (FICTIONAL)

Every figure below is copied from 03a_metrics.md. No figure is computed in this step.

## Applicability

| method | level | paper | ratio | inputs required | available in 03a? | applicable? | reason |
|---|---|---|---|---|---|---|---|
| M1: Firm-level interest coverage ratio (simple threshold) | firm | fed_icr_vulnerabilities_2020.pdf | ebit_interest_coverage | ebit, interest_expense | yes | yes | all inputs available |
| M2: Free cash flow relative to total assets | firm | fed_icr_vulnerabilities_2020.pdf | free_cash_flow_to_assets | operating_income, depreciation, interest_expense, taxes, capital_expenditures, total_assets | yes | yes | all inputs available |
| M3: Leverage (total debt over assets) | firm | fed_icr_vulnerabilities_2020.pdf | total_debt_to_assets | total_debt, total_assets | yes | yes | all inputs available |
| M4: Credit line availability (undrawn lines of credit over assets) | firm | fed_icr_vulnerabilities_2020.pdf | undrawn_credit_lines_to_assets | undrawn_credit_lines, total_assets | yes | yes | all inputs available |
| M5: Share of debt maturing within a year | firm | fed_icr_vulnerabilities_2020.pdf | debt_maturing_within_one_year_share | debt_maturing_within_one_year, total_debt | no | no | missing line item(s): debt_maturing_within_one_year |
| M6: Debt composition (bonds relative to total debt) | firm | fed_icr_vulnerabilities_2020.pdf | bonds_to_total_debt | total_bonds, total_debt | no | no | missing line item(s): total_bonds |
| M7: Firm interest coverage below 2 (debt-at-risk criterion) | firm | fed_icr_stress_test_2024.pdf | ebit_interest_coverage | ebit, interest_expense | yes | yes | all inputs available |
| M8: Aggregate interest coverage and scenario projection | aggregate | fed_icr_stress_test_2024.pdf | aggregate_ebit_interest_coverage | aggregate_ebit, aggregate_interest_expense | no | no | aggregate-level method: it needs many firms or sector data, and this data is one company; missing line item(s): aggregate_ebit, aggregate_interest_expense |

## Findings

### M1: Firm-level interest coverage ratio (simple threshold)
- **What it measures:** whether earnings are enough to cover interest expenses
- **Evidence:** `ebit_interest_coverage`, from 03a_metrics.md: FY2023 7.2500; FY2024 5.6364; FY2025 3.7500
- **Threshold used:** `ebit_interest_coverage` < 1 (quoted from the paper on the M1 card)
- **Against the threshold (below 1?):** FY2023 7.2500: no; FY2024 5.6364: no; FY2025 3.7500: no
- **Threshold status:** not breached
- **Trend over 3 period(s):** the ratio fell in every period
- **Direction of this method:** lower is worse (basis: stated in the paper)
- **Verdict:** worsening
- **Result:** The ratio moved from 7.2500 (FY2023) to 3.7500 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: whether earnings are enough to cover interest expenses. It did not meet the threshold condition in any period.
- **Confidence:** high, because the paper states a threshold and the ratio is available in every period.

### M2: Free cash flow relative to total assets
- **What it measures:** how much cash the business generates after interest, taxes and investment, relative to its size
- **Evidence:** `free_cash_flow_to_assets`, from 03a_metrics.md: FY2023 0.0500; FY2024 0.0262; FY2025 0.0056
- **Threshold used:** none stated
- **Threshold status:** none stated
- **Trend over 3 period(s):** the ratio fell in every period
- **Direction of this method:** lower is worse (basis: inferred from the paper, not stated)
- **Verdict:** worsening
- **Result:** The ratio moved from 0.0500 (FY2023) to 0.0056 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: how much cash the business generates after interest, taxes and investment, relative to its size.
- **Confidence:** medium, because the paper states no threshold, so only the direction of change is judged.

### M3: Leverage (total debt over assets)
- **What it measures:** how much of the company's assets is financed by debt
- **Evidence:** `total_debt_to_assets`, from 03a_metrics.md: FY2023 0.2692; FY2024 0.3115; FY2025 0.3652
- **Threshold used:** none stated
- **Threshold status:** none stated
- **Trend over 3 period(s):** the ratio rose in every period
- **Direction of this method:** higher is worse (basis: inferred from the paper, not stated)
- **Verdict:** worsening
- **Result:** The ratio moved from 0.2692 (FY2023) to 0.3652 (FY2025) and rose in every period. Under this method that is the worse direction, which indicates a weakening in: how much of the company's assets is financed by debt.
- **Confidence:** medium, because the paper states no threshold, so only the direction of change is judged.

### M4: Credit line availability (undrawn lines of credit over assets)
- **What it measures:** how much unused borrowing capacity the company has as a buffer
- **Evidence:** `undrawn_credit_lines_to_assets`, from 03a_metrics.md: FY2023 0.1154; FY2024 0.0656; FY2025 0.0225
- **Threshold used:** none stated
- **Threshold status:** none stated
- **Trend over 3 period(s):** the ratio fell in every period
- **Direction of this method:** lower is worse (basis: inferred from the paper, not stated)
- **Verdict:** worsening
- **Result:** The ratio moved from 0.1154 (FY2023) to 0.0225 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: how much unused borrowing capacity the company has as a buffer.
- **Confidence:** medium, because the paper states no threshold, so only the direction of change is judged.

### M7: Firm interest coverage below 2 (debt-at-risk criterion)
- **What it measures:** whether the company would count as a firm whose debt is at risk
- **Evidence:** `ebit_interest_coverage`, from 03a_metrics.md: FY2023 7.2500; FY2024 5.6364; FY2025 3.7500
- **Threshold used:** `ebit_interest_coverage` < 2 (quoted from the paper on the M7 card)
- **Against the threshold (below 2?):** FY2023 7.2500: no; FY2024 5.6364: no; FY2025 3.7500: no
- **Threshold status:** not breached
- **Trend over 3 period(s):** the ratio fell in every period
- **Direction of this method:** lower is worse (basis: stated in the paper)
- **Verdict:** worsening
- **Result:** The ratio moved from 7.2500 (FY2023) to 3.7500 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: whether the company would count as a firm whose debt is at risk. It did not meet the threshold condition in any period.
- **Confidence:** high, because the paper states a threshold and the ratio is available in every period.

## Where methods disagree

All applicable methods (M1, M2, M3, M4, M7) point the same way: worsening.

## What the data cannot tell us

- operating_cash_flow fell every period (FY2023 240.0; FY2024 90.0; FY2025 -60.0) while net_income stayed positive (FY2023 180.0; FY2024 190.0; FY2025 175.0). What explains the gap between reported profit and cash from operations (for example slower customer payments, inventory purchases, or one-off items)?
- receivables rose every period (FY2023 520.0; FY2024 790.0; FY2025 1,080.0), and dso_days also rose (FY2023 45.2; FY2024 59.7; FY2025 72.9). Did customer payment terms change, is a small number of customers behind the increase, or are collections slower?
- inventory rose every period (FY2023 610.0; FY2024 860.0; FY2025 1,120.0), and dio_days also rose (FY2023 70.7; FY2024 85.8; FY2025 98.3). Was the build-up planned, and is any of the stock slow-moving?
- capital_expenditures rose every period (FY2023 120.0; FY2024 180.0; FY2025 220.0) while free_cash_flow fell (FY2023 130.0; FY2024 80.0; FY2025 20.0). What was the money spent on, and how was it funded?
- undrawn_credit_lines fell every period (FY2023 300.0; FY2024 200.0; FY2025 80.0). Were credit lines drawn, reduced or cancelled, and what are their terms, maturity dates and renewal plans?
- total_debt (FY2023 700.0; FY2024 950.0; FY2025 1,300.0) and interest_expense (FY2023 40.0; FY2024 55.0; FY2025 80.0) both rose every period. Which part of the debt carries a floating rate, and when do fixed rates reset?
- M5: Share of debt maturing within a year could not be applied because the data has no debt_maturing_within_one_year. Can the company supply it for FY2023 to FY2025?
- M6: Debt composition (bonds relative to total debt) could not be applied because the data has no total_bonds. Can the company supply it for FY2023 to FY2025?
- M8: Aggregate interest coverage and scenario projection is a sector-wide method. Is comparable sector or peer data available to put this company's figures in context?

# Method cards

Cards read from: fed_icr_stress_test_2024.json, fed_icr_vulnerabilities_2020.json. Each quotation was searched for in the paper's extracted method text (line breaks and repeated spaces ignored, nothing else).

## Verification summary

| card | paper file | checked against | lines | result |
|---|---|---|---|---|
| M1 | fed_icr_vulnerabilities_2020.pdf | 01_extracted/fed_icr_vulnerabilities_2020.methods.txt | 370-371 | FOUND |
| M2 | fed_icr_vulnerabilities_2020.pdf | 01_extracted/fed_icr_vulnerabilities_2020.methods.txt | 446-447 | FOUND |
| M3 | fed_icr_vulnerabilities_2020.pdf | 01_extracted/fed_icr_vulnerabilities_2020.methods.txt | 99-99 | FOUND |
| M4 | fed_icr_vulnerabilities_2020.pdf | 01_extracted/fed_icr_vulnerabilities_2020.methods.txt | 99-100 | FOUND |
| M5 | fed_icr_vulnerabilities_2020.pdf | 01_extracted/fed_icr_vulnerabilities_2020.methods.txt | 103-103 | FOUND |
| M6 | fed_icr_vulnerabilities_2020.pdf | 01_extracted/fed_icr_vulnerabilities_2020.methods.txt | 104-104 | FOUND |
| M7 | fed_icr_stress_test_2024.pdf | 01_extracted/fed_icr_stress_test_2024.methods.txt | 204-204 | FOUND |
| M8 | fed_icr_stress_test_2024.pdf | 01_extracted/fed_icr_stress_test_2024.methods.txt | 39-41 | FOUND |

## M1: Firm-level interest coverage ratio (simple threshold)

- **Source:** fed_icr_vulnerabilities_2020.pdf ("Interest Coverage Ratios: Assessing Vulnerabilities in Nonfinancial Corporate Credit")
- **Level:** firm
- **What it diagnoses:** whether earnings are enough to cover interest expenses
- **Ratio used:** `ebit_interest_coverage`
- **Inputs required:** ebit, interest_expense
- **Formula:** `ebit / interest_expense`
- **Threshold:** `ebit_interest_coverage` < 1
- **Bad direction:** lower is worse (basis: stated in the paper)
- **Notes:** The paper smooths seasonality with four-quarter sums; the annual figures in the data are used instead.
- **Quotation:**
  > First, a simple threshold of 1, below which a firm cannot completely cover its interest expenses using earnings.
- **Verification:** FOUND in `01_extracted/fed_icr_vulnerabilities_2020.methods.txt`, lines 370-371
- **Matching lines:**
  ```text
  fraction of debt below two meaningful interest coverage ratio thresholds. First, a simple
  threshold of 1, below which a firm cannot completely cover its interest expenses using earnings.
  ```

## M2: Free cash flow relative to total assets

- **Source:** fed_icr_vulnerabilities_2020.pdf ("Interest Coverage Ratios: Assessing Vulnerabilities in Nonfinancial Corporate Credit")
- **Level:** firm
- **What it diagnoses:** how much cash the business generates after interest, taxes and investment, relative to its size
- **Ratio used:** `free_cash_flow_to_assets`
- **Inputs required:** operating_income, depreciation, interest_expense, taxes, capital_expenditures, total_assets
- **Formula:** `(operating_income + depreciation - interest_expense - taxes - capital_expenditures) / total_assets`
- **Threshold:** None stated in the paper.
- **Bad direction:** lower is worse (basis: inferred from the paper, not stated)
- **Notes:** Operating income before depreciation is taken as operating_income plus depreciation.
- **Quotation:**
  > Free cash flow is computed as operating income before depreciation minus interest expenses minus taxes minus capital expenditures.
- **Verification:** FOUND in `01_extracted/fed_icr_vulnerabilities_2020.methods.txt`, lines 446-447
- **Matching lines:**
  ```text
  6. Free cash flow is computed as operating income before depreciation minus interest expenses minus taxes minus
  capital expenditures. Return to text
  ```

## M3: Leverage (total debt over assets)

- **Source:** fed_icr_vulnerabilities_2020.pdf ("Interest Coverage Ratios: Assessing Vulnerabilities in Nonfinancial Corporate Credit")
- **Level:** firm
- **What it diagnoses:** how much of the company's assets is financed by debt
- **Ratio used:** `total_debt_to_assets`
- **Inputs required:** total_debt, total_assets
- **Formula:** `total_debt / total_assets`
- **Threshold:** None stated in the paper.
- **Bad direction:** higher is worse (basis: inferred from the paper, not stated)
- **Quotation:**
  > leverage, expressed as total debt over assets
- **Verification:** FOUND in `01_extracted/fed_icr_vulnerabilities_2020.methods.txt`, lines 99-99
- **Matching lines:**
  ```text
  values for leverage, expressed as total debt over assets, and credit line availability, expressed
  ```

## M4: Credit line availability (undrawn lines of credit over assets)

- **Source:** fed_icr_vulnerabilities_2020.pdf ("Interest Coverage Ratios: Assessing Vulnerabilities in Nonfinancial Corporate Credit")
- **Level:** firm
- **What it diagnoses:** how much unused borrowing capacity the company has as a buffer
- **Ratio used:** `undrawn_credit_lines_to_assets`
- **Inputs required:** undrawn_credit_lines, total_assets
- **Formula:** `undrawn_credit_lines / total_assets`
- **Threshold:** None stated in the paper.
- **Bad direction:** lower is worse (basis: inferred from the paper, not stated)
- **Quotation:**
  > credit line availability, expressed as total undrawn lines of credit over assets
- **Verification:** FOUND in `01_extracted/fed_icr_vulnerabilities_2020.methods.txt`, lines 99-100
- **Matching lines:**
  ```text
  values for leverage, expressed as total debt over assets, and credit line availability, expressed
  as total undrawn lines of credit over assets, stand at 0.29 and 0.10, respectively. The interest
  ```

## M5: Share of debt maturing within a year

- **Source:** fed_icr_vulnerabilities_2020.pdf ("Interest Coverage Ratios: Assessing Vulnerabilities in Nonfinancial Corporate Credit")
- **Level:** firm
- **What it diagnoses:** how much of the debt has to be repaid or refinanced within a year
- **Ratio used:** `debt_maturing_within_one_year_share`
- **Inputs required:** debt_maturing_within_one_year, total_debt
- **Formula:** `debt_maturing_within_one_year / total_debt`
- **Threshold:** None stated in the paper.
- **Bad direction:** higher is worse (basis: inferred from the paper, not stated)
- **Quotation:**
  > only around 4 percent of debt matures within a year
- **Verification:** FOUND in `01_extracted/fed_icr_vulnerabilities_2020.methods.txt`, lines 103-103
- **Matching lines:**
  ```text
  percentile) of 5.78. For the median firm, only around 4 percent of debt matures within a year,
  ```

## M6: Debt composition (bonds relative to total debt)

- **Source:** fed_icr_vulnerabilities_2020.pdf ("Interest Coverage Ratios: Assessing Vulnerabilities in Nonfinancial Corporate Credit")
- **Level:** firm
- **What it diagnoses:** the mix of bonds and loans in the company's debt
- **Ratio used:** `bonds_to_total_debt`
- **Inputs required:** total_bonds, total_debt
- **Formula:** `total_bonds / total_debt`
- **Threshold:** None stated in the paper.
- **Bad direction:** not stated in the paper (basis: not stated)
- **Quotation:**
  > the median share of bonds relative to total debt
- **Verification:** FOUND in `01_extracted/fed_icr_vulnerabilities_2020.methods.txt`, lines 104-104
- **Matching lines:**
  ```text
  and the median share of bonds relative to total debt is about 69 percent.
  ```

## M7: Firm interest coverage below 2 (debt-at-risk criterion)

- **Source:** fed_icr_stress_test_2024.pdf ("Stress Testing the Corporate Debt Servicing Capacity: A Scenario Analysis")
- **Level:** firm
- **What it diagnoses:** whether the company would count as a firm whose debt is at risk
- **Ratio used:** `ebit_interest_coverage`
- **Inputs required:** ebit, interest_expense
- **Formula:** `ebit / interest_expense`
- **Threshold:** `ebit_interest_coverage` < 2
- **Bad direction:** lower is worse (basis: stated in the paper)
- **Notes:** The paper reports the share of sector debt held by firms below this value; for one company only its own ratio is compared with the threshold.
- **Quotation:**
  > the percent of debt held by firms with ICRs below 2
- **Verification:** FOUND in `01_extracted/fed_icr_stress_test_2024.methods.txt`, lines 204-204
- **Matching lines:**
  ```text
  across firms show that the percent of debt held by firms with ICRs below 2 (share of debt-atrisk) would expand in all three Moody's scenarios (Figure 6).
  ```

## M8: Aggregate interest coverage and scenario projection

- **Source:** fed_icr_stress_test_2024.pdf ("Stress Testing the Corporate Debt Servicing Capacity: A Scenario Analysis")
- **Level:** aggregate
- **What it diagnoses:** the debt-servicing capacity of a whole group of firms under macroeconomic scenarios
- **Ratio used:** `aggregate_ebit_interest_coverage`
- **Inputs required:** aggregate_ebit, aggregate_interest_expense
- **Formula:** `aggregate_ebit / aggregate_interest_expense`
- **Threshold:** None stated in the paper.
- **Bad direction:** lower is worse (basis: inferred from the paper, not stated)
- **Quotation:**
  > We compute the projected aggregate ICR for the chosen group of firms as the ratio of the projected combined earnings to the projected combined interest expense of all firms in the group.
- **Verification:** FOUND in `01_extracted/fed_icr_stress_test_2024.methods.txt`, lines 39-41
- **Matching lines:**
  ```text
  nonfinancial firms and over the subset of non-IG firms. We compute the projected aggregate
  ICR for the chosen group of firms as the ratio of the projected combined earnings to the
  projected combined interest expense of all firms in the group. As in McCoy et al. (2020), we
  ```

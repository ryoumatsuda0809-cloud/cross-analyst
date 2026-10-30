TASK: Apply each method card to the company's financial data.

Attachments:
- 02_methods.md: the method cards (M1, M2, ...), extracted from research papers
- 03a_metrics.md: the company's line items and ratios, already computed by a program

Write the diagnosis in this structure:

# Diagnosis

## Applicability
A table: | method | inputs required | available in 03a? | applicable? |
If an input is missing, the method is "not applicable" and you say which input is missing.

## Findings
For each applicable method, one subsection:

### M<n>: <method name>
- **Evidence:** the metric names, periods and values, copied exactly from 03a_metrics.md
- **Threshold used:** copied from the method card
- **Result:** what the method indicates for each period
- **Confidence:** high / medium / low, and one sentence on why

## Where methods disagree
If two methods point in different directions, describe both. Do not decide which one is right.

## What the data cannot tell us
Things the numbers cannot explain (causes, intentions, one-off events), written as questions
to ask the company's management or staff.

Rules:
1. Use ONLY numbers that appear in 03a_metrics.md. Do not calculate new numbers.
   If a method needs a value that is not in 03a, mark the method "not applicable"; do not compute it yourself.
2. Every finding must name its method ID (M1, M2, ...).
3. Write findings as hypotheses ("indicates", "is consistent with"), never as verdicts.

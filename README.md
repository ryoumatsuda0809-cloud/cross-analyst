# cross-analyst: from research papers to a financial diagnostic report

A small Python pipeline that

1. reads research papers (PDF) from a local folder,
2. extracts their text and finds the sections that describe their **methods**,
3. checks the prepared **method cards** against that text and applies them to a company's financial data
   with plain rule-based Python,
4. writes a **Markdown diagnostic report**, and checks that every number in it can be traced back to the data.

It runs completely offline. There is no account, no key and no network access anywhere in the code.
The same inputs always produce byte-identical outputs.

Everything in `data/financials/` is **fictional**: the company "Harbor Lane Supply Co." does not exist.

---

## Design in one paragraph

Each step reads files and writes files, so every result can be opened and read before the next step runs.

| Guarantee | How |
|---|---|
| Methods are not invented | each method card carries a quotation from the paper; the `methods` step searches the extracted text for it and stops if it is missing |
| No arithmetic outside one file | all ratios are computed in `pipeline/financials.py`, with their formulas shown in `03a_metrics.md` |
| The diagnosis only compares | values are copied from `03a_metrics.md` as written; the rules only compare (below a threshold? rising or falling?) |
| Numbers in the outputs are not made up | `pipeline/check.py` matches every number and method ID against the computed data and the method cards |

```
data/papers/*.pdf
   |  [extract]
   v
01_extracted/*.methods.txt
   |                                data/method_cards/*.json
   |  [methods]  <------------------------+
   v
02_methods.md ---------------------------+
                                         |  [apply]
data/financials/*.csv                    +----------------> 03_diagnosis.md
   |  [metrics]                          |                        |  [report]
   v                                     |                        v
03a_metrics.md --------------------------+               diagnostic_report.md
                                                                  |  [check]
                                                                  v
                                                          check_result.txt
```

| Step | Command | Output |
|---|---|---|
| 1-2 Read PDFs, split sections | `extract` | `01_extracted/` |
| 3a Compute ratios | `metrics` | `03a_metrics.md` |
| 2 Verify method cards against the papers | `methods` | `02_methods.md` |
| 3 Apply methods to the data | `apply` | `03_diagnosis.md` |
| 4 Assemble the report | `report` | `diagnostic_report.md` |
| 4 Verify numbers and method IDs | `check` | `check_result.txt` |

`run` does all six in order.

---

## Setup (once)

Requires Python 3.9 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python diagnose.py run --run outputs/final
python -m pytest -q
```

or one step at a time, reading each output before moving on:

```bash
python diagnose.py extract --run outputs/final     # then read 01_extracted/_extraction_summary.md
python diagnose.py metrics --run outputs/final     # then read 03a_metrics.md
python diagnose.py methods --run outputs/final     # then read 02_methods.md
python diagnose.py apply   --run outputs/final     # then read 03_diagnosis.md
python diagnose.py report  --run outputs/final     # then read diagnostic_report.md
python diagnose.py check   --run outputs/final
```

Options: `--papers DIR`, `--financials CSV`, `--cards DIR`, `--run DIR`.

### Using your own papers and data

```bash
python diagnose.py run --papers path/to/pdfs --financials path/to/company.csv --cards path/to/cards --run outputs/mycase
```

The CSV has one row per line item and one column per period. Lines starting with `#` are comments;
`# company: <name>` sets the company name. See `data/financials/harbor_lane_supply.csv`.
Missing items are reported as `n/a`.

Only use PDFs you have the right to use.

---

## Method cards

One JSON file per paper in `data/method_cards/`, each holding a list of cards:

| field | meaning |
|---|---|
| `id` | `M1`, `M2`, ... (unique across all files) |
| `name`, `diagnoses` | short name; one sentence on what the measure shows |
| `paper` | `file` (the PDF name) and `title` |
| `level` | `firm` (one company's statements are enough) or `aggregate` (needs many firms or sector data) |
| `ratio` | the ratio name used in `03a_metrics.md` (must match `pipeline/financials.py`) |
| `inputs` | the line items the ratio needs |
| `formula` | the formula, in line item names |
| `threshold` | `null`, or `{"operator": "<", "value": 1}` |
| `bad_direction` | `lower_is_worse`, `higher_is_worse`, or `null` when the paper gives none |
| `direction_basis` | `paper` (stated), `inferred` (the card's reading), or `not_stated` |
| `quote` | a sentence or phrase copied from the paper's extracted text |
| `notes` | optional |

The `methods` step looks for each `quote` in `01_extracted/<paper>.methods.txt`. Line breaks and repeated
spaces are ignored; nothing else is. A card whose quotation is not found stops the run and is marked
`NOT FOUND` in `02_methods.md`.

## Rules used by `apply`

- **Applicability.** A card is not applied when its level is `aggregate` (the data is one company), when its
  ratio is not in `03a_metrics.md` because a line item is missing, or when its quotation was not found.
  The reason is written next to each method.
- **Threshold.** Compared period by period, only when the card has one.
- **Trend.** `rising`, `falling`, `flat` or `mixed`, from comparing consecutive periods.
- **Verdict.** The trend read against the card's `bad_direction`: `worsening`, `improving`, `unchanged`,
  `mixed`, or `no verdict`.
- **Agreement.** Whether the applicable methods give the same verdict. A disagreement is described, not resolved.
- **Confidence.** `high`: a threshold is stated and every period is available. `medium`: no threshold, so only the
  direction is judged. `low`: a period is missing.
- **Open questions.** Fixed rules on the series in `03a_metrics.md` (for example operating cash flow falling while
  net income stays positive) plus one question for each method that could not be applied.

---

## What to look at after a run (review checklist)

1. **`01_extracted/_extraction_summary.md`**: did each paper's method text come from a real Methods section,
   or from `FALLBACK`? Any "no text layer" warning means the PDF is a scanned image.
2. **`02_methods.md`**: is every card `FOUND`, and do the matching lines say what the card claims?
3. **`03_diagnosis.md`**: is each non-applicable method marked as such, with its reason?
4. **`check`**: any number flagged here was not in the data. Treat it as an error.

`check` can tell you whether numbers are traceable. It cannot tell you whether the reasoning is good.
That part is the reviewer's job.

---

## Troubleshooting

| Message | Meaning / fix |
|---|---|
| `Quotation not found for card(s): ...` | the quotation is not in the extracted text; fix the card or check the PDF text |
| `No text layer` | the PDF is scanned; run OCR on it first |
| `No Methods/Model heading found` | the whole paper is used instead; check `02_methods.md` carefully |
| `... does not exist. Run the ... step first.` | run the earlier steps first (or use `run`) |

## Repository layout

```
diagnose.py              command-line entry point
pipeline/pdf_extract.py  PDF -> text -> sections
pipeline/financials.py   CSV -> ratios (all arithmetic lives here)
pipeline/cards.py        method cards: load, validate, quotation check
pipeline/stages.py       methods, apply and report steps
pipeline/check.py        traceability check for numbers and method IDs
data/papers/             the research PDFs
data/method_cards/       one JSON file of method cards per paper
data/financials/         fictional company data
scripts/                 regenerates synthetic sample PDFs
tests/                   pytest, fully offline
```

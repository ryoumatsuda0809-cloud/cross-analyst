"""Method cards: load them, validate them, and check each card's quotation against the paper text.

A card is a small JSON object describing one measure from one paper (see data/method_cards/).
The quotation on a card must appear word for word in the text extracted from that paper
(01_extracted/<paper>.methods.txt). Line breaks and runs of spaces are ignored when matching,
because PDF text is wrapped; nothing else is relaxed.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

REQUIRED = ("id", "name", "paper", "level", "ratio", "inputs", "formula", "threshold",
            "bad_direction", "direction_basis", "diagnoses", "quote")
LEVELS = ("firm", "aggregate")
DIRECTIONS = ("lower_is_worse", "higher_is_worse", None)
DIRECTION_BASES = ("paper", "inferred", "not_stated")
OPERATORS = ("<", "<=", ">", ">=")


def load(folder: Path) -> list[dict]:
    """Read every *.json file in the folder (each holds a list of cards), validate, sort by card number."""
    files = sorted(folder.glob("*.json"))
    if not files:
        raise SystemExit(f"No method cards (*.json) in {folder}")
    cards: list[dict] = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise SystemExit(f"{f.name}: not valid JSON ({e})")
        if not isinstance(data, list):
            raise SystemExit(f"{f.name}: expected a JSON list of cards")
        for card in data:
            _validate(card, f.name)
            cards.append(card)
    ids = [c["id"] for c in cards]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise SystemExit(f"Duplicate card id(s): {', '.join(dupes)}")
    return sorted(cards, key=lambda c: int(c["id"][1:]))


def _validate(card: dict, source: str) -> None:
    where = f"{source}: card {card.get('id', '?')}"
    missing = [k for k in REQUIRED if k not in card]
    if missing:
        raise SystemExit(f"{where}: missing field(s) {', '.join(missing)}")
    if not re.fullmatch(r"M\d+", card["id"]):
        raise SystemExit(f"{where}: id must look like M1, M2, ...")
    if card["level"] not in LEVELS:
        raise SystemExit(f"{where}: level must be one of {LEVELS}")
    if card["bad_direction"] not in DIRECTIONS:
        raise SystemExit(f"{where}: bad_direction must be lower_is_worse, higher_is_worse or null")
    if card["direction_basis"] not in DIRECTION_BASES:
        raise SystemExit(f"{where}: direction_basis must be one of {DIRECTION_BASES}")
    if not isinstance(card["inputs"], list) or not card["inputs"]:
        raise SystemExit(f"{where}: inputs must be a non-empty list of line item names")
    if not isinstance(card["paper"], dict) or not {"file", "title"} <= set(card["paper"]):
        raise SystemExit(f"{where}: paper must have 'file' and 'title'")
    th = card["threshold"]
    if th is not None and (not isinstance(th, dict) or th.get("operator") not in OPERATORS
                           or not isinstance(th.get("value"), (int, float))):
        raise SystemExit(f"{where}: threshold must be null or {{\"operator\": one of {OPERATORS}, \"value\": number}}")
    if not card["quote"].strip():
        raise SystemExit(f"{where}: quote is empty")


@dataclass
class Verification:
    card_id: str
    found: bool
    checked_file: str                      # path relative to the run folder, e.g. 01_extracted/x.methods.txt
    first_line: int = 0
    last_line: int = 0
    lines: list[str] = field(default_factory=list)
    note: str = ""


def _pattern(quote: str) -> re.Pattern:
    return re.compile(r"\s+".join(re.escape(word) for word in quote.split()))


def verify(card: dict, extracted: Path) -> Verification:
    """Look for the card's quotation in the paper's method text (the full text if there is no method text)."""
    stem = Path(card["paper"]["file"]).stem
    for kind in ("methods", "full"):
        path = extracted / f"{stem}.{kind}.txt"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        rel = f"{extracted.name}/{path.name}"
        m = _pattern(card["quote"]).search(text)
        if not m:
            return Verification(card["id"], False, rel, note="quotation not found in the extracted text")
        first = text.count("\n", 0, m.start()) + 1
        last = text.count("\n", 0, m.end()) + 1
        return Verification(card["id"], True, rel, first, last, text.splitlines()[first - 1:last])
    return Verification(card["id"], False, f"{extracted.name}/{stem}.methods.txt",
                        note="no extracted text for this paper (run extract first, or check the file name on the card)")

"""Step 1-2: read research PDFs and split them into sections.

No LLM is used here. Everything in this file is plain Python, so you can
inspect exactly what text the model will (and will not) receive later.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from pypdf import PdfReader

# A heading is a short line such as "3. Methods", "2 Methodology", "METHOD".
HEADING = re.compile(
    r"^\s*(?:(?:\d+|[IVX]+)(?:\.\d+)*\.?\s+)?"           # optional "3." / "2.1" / "III."
    r"(abstract|introduction|background|literature review|related work|data|"
    r"data and sample|sample|method|methods|methodology|model|the model|approach|"
    r"framework|empirical strategy|research design|results|findings|discussion|"
    r"conclusion|conclusions|limitations|references|bibliography|appendix)\s*$",
    re.I,
)
METHOD_NAMES = {"method", "methods", "methodology", "model", "the model", "approach",
                "framework", "empirical strategy", "research design"}
MIN_CHARS_PER_PAGE = 200   # below this a page is probably a scanned image (no text layer)


@dataclass
class Paper:
    path: Path
    title: str
    pages: int
    text: str
    sections: dict[str, str] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

    @property
    def method_text(self) -> str:
        """The part of the paper that describes its method(s)."""
        picked = [body for name, body in self.sections.items() if _base(name) in METHOD_NAMES]
        if picked:
            return "\n\n".join(picked)
        # Fallback: no "Methods" heading was found. Send everything except references.
        return "\n\n".join(b for n, b in self.sections.items()
                           if _base(n) not in {"references", "bibliography"}) or self.text

    @property
    def method_source(self) -> str:
        found = [n for n in self.sections if _base(n) in METHOD_NAMES]
        return ", ".join(found) if found else "FALLBACK: no method heading found, whole paper used"


def clean(text: str) -> str:
    text = text.replace("\u00ad", "")                    # soft hyphen
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)          # join words broken across lines
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {"_front": []}
    current = "_front"
    for line in text.splitlines():
        m = HEADING.match(line)
        if m and len(line) < 60:
            current = m.group(1).lower()
            # A paper can have two "Model" sections etc. Keep them all.
            base, n = current, 2
            while current in sections:
                current, n = f"{base} ({n})", n + 1
            sections[current] = []
            continue
        sections[current].append(line)
    out = {k: "\n".join(v).strip() for k, v in sections.items()}
    return {k: v for k, v in out.items() if v}


def _base(name: str) -> str:
    return re.sub(r" \(\d+\)$", "", name)


def read_paper(path: Path) -> Paper:
    reader = PdfReader(str(path))
    raw_pages = [(p.extract_text() or "") for p in reader.pages]
    text = clean("\n".join(raw_pages))
    meta_title = (reader.metadata.title if reader.metadata else None) or ""
    first_line = next((ln.strip() for ln in text.splitlines() if ln.strip()), path.stem)
    paper = Paper(path=path, title=meta_title.strip() or first_line, pages=len(raw_pages), text=text)

    empty = [i + 1 for i, t in enumerate(raw_pages) if len(t.strip()) < MIN_CHARS_PER_PAGE]
    if len(empty) == len(raw_pages):
        paper.warnings.append("No text layer. This PDF is probably a scanned image; OCR it first.")
    elif empty:
        paper.warnings.append(f"Pages with almost no text: {empty} (figures, or scanned pages).")

    paper.sections = split_sections(text)
    if not any(_base(n) in METHOD_NAMES for n in paper.sections):
        paper.warnings.append("No Methods/Model heading found. The whole paper is sent instead.")
    return paper


def read_folder(folder: Path) -> list[Paper]:
    pdfs = sorted(folder.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDF files in {folder}")
    return [read_paper(p) for p in pdfs]

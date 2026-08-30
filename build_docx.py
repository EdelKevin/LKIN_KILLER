#!/usr/bin/env python3
"""md → .docx via python-docx. Single-page resume formatting matching build_pdf.py.

Usage: python3 build_docx.py <path.md>

Supports the base_resume.md markdown subset:
  # H1     → centered name
  ## H2    → uppercase section header w/ bottom border
  ### H3   → role / project title
  *text*   → italic
  **text** → bold
  - item   → bullet
  plain paragraphs (e.g. contact line right after H1)
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, Inches, RGBColor


META_RE = re.compile(r'<span class="meta">(.+?)</span>', re.DOTALL)

# ── inline parser ────────────────────────────────────────────────────────────

INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\))")


def emit_runs(paragraph, text: str, *, base_bold=False, base_italic=False, base_size=Pt(10.5)):
    """Emit text into paragraph honoring **bold**, *italic*, and [label](url)."""
    pos = 0
    for m in INLINE_RE.finditer(text):
        if m.start() > pos:
            r = paragraph.add_run(text[pos:m.start()])
            r.bold = base_bold
            r.italic = base_italic
            r.font.size = base_size
        token = m.group(0)
        if token.startswith("**"):
            r = paragraph.add_run(token[2:-2])
            r.bold = True
            r.italic = base_italic
            r.font.size = base_size
        elif token.startswith("*"):
            r = paragraph.add_run(token[1:-1])
            r.italic = True
            r.bold = base_bold
            r.font.size = base_size
        else:  # link
            label = re.match(r"\[([^\]]+)\]", token).group(1)
            r = paragraph.add_run(label)
            r.bold = base_bold
            r.italic = base_italic
            r.font.size = base_size
            r.font.color.rgb = RGBColor(0x1A, 0x4E, 0xA0)
        pos = m.end()
    if pos < len(text):
        r = paragraph.add_run(text[pos:])
        r.bold = base_bold
        r.italic = base_italic
        r.font.size = base_size


# ── styling helpers ──────────────────────────────────────────────────────────

def set_bottom_border(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "333333")
    pBdr.append(bottom)
    pPr.append(pBdr)


def tight(p, *, space_before=0, space_after=1, line_spacing=1.15):
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing


def split_meta(text: str):
    """Return (main_text, meta_text_or_None)."""
    m = META_RE.search(text)
    if not m:
        return text, None
    return (text[:m.start()] + text[m.end():]).rstrip(), m.group(1).strip()


def emit_with_meta(p, text, *, base_bold=False, base_size=Pt(10.5),
                   meta_italic=True, meta_size=Pt(9.5),
                   right_tab_inches=7.4):
    """Emit text into paragraph; if `<span class="meta">…</span>` is present,
    add a right-aligned tab stop and put the meta text after the tab in italic."""
    main, meta = split_meta(text)
    emit_runs(p, main, base_bold=base_bold, base_size=base_size)
    if meta:
        # add right-aligned tab stop
        tab_stops = p.paragraph_format.tab_stops
        tab_stops.add_tab_stop(Inches(right_tab_inches), WD_TAB_ALIGNMENT.RIGHT)
        p.add_run("\t")
        r = p.add_run(meta)
        r.italic = meta_italic
        r.font.size = meta_size
        r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)


# ── markdown line walker ─────────────────────────────────────────────────────

def render(md_path: Path) -> Path:
    doc = Document()

    # Letter, narrow margins to match PDF
    section = doc.sections[0]
    section.top_margin = Inches(0.4)
    section.bottom_margin = Inches(0.4)
    section.left_margin = Inches(0.55)
    section.right_margin = Inches(0.55)
    section.page_height = Inches(11)
    section.page_width = Inches(8.5)

    style = doc.styles["Normal"]
    style.font.name = "Helvetica Neue"
    style.font.size = Pt(9.8)

    lines = md_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line:
            i += 1
            continue

        # H1 — centered name
        if line.startswith("# "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            tight(p, space_before=0, space_after=1)
            emit_runs(p, line[2:].strip(), base_bold=True, base_size=Pt(16))
            # Contact line
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and not lines[j].lstrip().startswith(("#", "-")):
                cp = doc.add_paragraph()
                cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                tight(cp, space_before=0, space_after=3)
                emit_runs(cp, lines[j].strip(), base_size=Pt(9))
                i = j + 1
                continue
            i += 1
            continue

        # H2 — section header (title-case, NOT uppercase — checklist rule "Education NOT EDUCATION")
        if line.startswith("## "):
            p = doc.add_paragraph()
            tight(p, space_before=3, space_after=1)
            r = p.add_run(line[3:].strip().title())
            r.bold = True
            r.font.size = Pt(10.5)
            set_bottom_border(p)
            i += 1
            continue

        # H3 — role/project title (optionally with right-aligned <span class="meta"> date/location)
        if line.startswith("### "):
            p = doc.add_paragraph()
            tight(p, space_before=2, space_after=0)
            emit_with_meta(p, line[4:].strip(), base_bold=True, base_size=Pt(10))
            i += 1
            continue

        # Bullet
        if line.lstrip().startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            tight(p, space_before=0, space_after=0, line_spacing=1.18)
            p.paragraph_format.left_indent = Inches(0.22)
            emit_runs(p, line.lstrip()[2:].strip())
            i += 1
            continue

        # Plain paragraph (may also carry <span class="meta"> — e.g. Education lines)
        p = doc.add_paragraph()
        tight(p, space_before=0, space_after=0)
        emit_with_meta(p, line.strip(), base_size=Pt(9.8))
        i += 1

    out = md_path.with_suffix(".docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 build_docx.py <path.md>")
    print(render(Path(sys.argv[1])))

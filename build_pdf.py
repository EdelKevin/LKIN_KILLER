#!/usr/bin/env python3
"""md → single-page PDF via Chrome headless. Usage: python3 build_pdf.py <path.md>"""

import os
import shutil
import sys
import subprocess
from pathlib import Path
from markdown_it import MarkdownIt


def _find_chrome() -> str:
    env = os.environ.get("CHROME_BIN")
    if env and os.path.exists(env):
        return env
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe",
        "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe",
        "/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chrome"),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    raise SystemExit("No Chrome/Edge binary found. Set CHROME_BIN env var.")


def _to_chrome_path(p: Path) -> str:
    """Translate a POSIX path for the Chrome binary in use.
    Windows-side Chrome under /mnt/c needs Windows-style paths."""
    if CHROME.endswith(".exe"):
        result = subprocess.run(["wslpath", "-w", str(p.resolve())],
                                capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    return str(p.resolve())


CHROME = _find_chrome()

CSS = """
@page { size: Letter; margin: 0.4in 0.55in; }
* { box-sizing: border-box; }
body {
    font-family: "Helvetica Neue", "Helvetica", "Arial", "PingFang SC", sans-serif;
    color: #111;
    font-size: 10pt;
    line-height: 1.22;
    margin: 0; padding: 0;
}
h1 {
    font-size: 17pt; font-weight: 700;
    margin: 0 0 1px;
    text-align: center;
    letter-spacing: 0.3px;
}
h1 + p {
    text-align: center;
    font-size: 9.4pt;
    margin: 0 0 4px;
    color: #333;
}
h2 {
    font-size: 11pt; font-weight: 700;
    border-bottom: 1px solid #333;
    padding-bottom: 0;
    margin: 4px 0 1px;
}
h3 {
    font-size: 10.5pt; font-weight: 700;
    margin: 2px 0 0;
    overflow: hidden;
}
h3 .meta, p .meta {
    float: right;
    font-weight: 400;
    font-style: italic;
    font-size: 9.9pt;
    color: #333;
}
p { overflow: hidden; }
p { margin: 0 0 1px; }
em { font-style: italic; }
strong { font-weight: 700; }
ul { margin: 0 0 1px; padding-left: 15px; }
li { margin: 0; line-height: 1.25; }
a { color: #1a4ea0; text-decoration: none; }
hr { display: none; }
li, h3, h2 { page-break-inside: avoid; }
"""


def md_to_html(md_path: Path) -> str:
    parser = MarkdownIt("commonmark", {"html": True, "linkify": True, "breaks": True})
    body = parser.render(md_path.read_text(encoding="utf-8"))
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><title>{md_path.stem}</title>
<style>{CSS}</style></head><body>
{body}
</body></html>"""


def build(md_path: Path) -> Path:
    if not md_path.exists():
        raise SystemExit(f"Input not found: {md_path}")
    html_path = md_path.with_suffix(".html")
    pdf_path = md_path.with_suffix(".pdf")
    html_path.write_text(md_to_html(md_path), encoding="utf-8")
    html_for_chrome = _to_chrome_path(html_path)
    pdf_for_chrome = _to_chrome_path(pdf_path)
    file_url = ("file:///" + html_for_chrome.replace("\\", "/")
                if CHROME.endswith(".exe")
                else f"file://{html_for_chrome}")
    cmd = [
        CHROME, "--headless=new", "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_for_chrome}",
        file_url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    try:
        html_path.unlink()
    except OSError:
        pass
    if result.returncode != 0:
        raise SystemExit(f"Chrome PDF failed:\n{result.stderr}")
    if not pdf_path.exists():
        raise SystemExit(f"PDF not produced at {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 build_pdf.py <path.md>")
    print(build(Path(sys.argv[1])))

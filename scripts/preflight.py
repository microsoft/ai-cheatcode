#!/usr/bin/env python3
"""
Pre-Flight Checker — validate an issue before publication.

Runs the PRODUCTION_PLAYBOOK pre-send checklist against a single issue
number (or "all"). Exits non-zero if any check fails, so it's safe to
wire into CI or a pre-push hook.

Usage:
    python3 scripts/preflight.py 005
    python3 scripts/preflight.py all
    python3 scripts/preflight.py 005 --strict   # fail on warnings too

Checks:
  Newsletter HTML
    - file exists, no placeholder text (TBD, TODO, {{, <placeholder>)
    - correct issue number in <title>
    - unique Konami glyphs (not reused from another issue)
    - 'ABS Tech Strategy' in footer
    - 'aka.ms/the-cheat-code' archive link present
    - type badge emoji (🧠 or 🔧) when issue >= 007
    - reasonable file size (10-40KB)
  PDF
    - file exists, non-trivial size
  Diagram
    - at least one PNG in diagrams/ matching issue number
  Interactive walkthrough
    - docs/interactive/issue-NNN/index.html exists
    - every data-context element has a matching data-tooltip
    - NAV_ISSUES in interactive.js references this issue
  Portal consistency
    - docs/index.html references this issue (if published)
    - no .html extensions in nav links
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ISSUES_DIR = REPO_ROOT / "issues"
DIAGRAMS_DIR = REPO_ROOT / "diagrams"
DOCS_DIR = REPO_ROOT / "docs"
DOCS_INDEX = DOCS_DIR / "index.html"
ARCHIVE_INDEX = REPO_ROOT / "index.html"
SHARED_JS = DOCS_DIR / "interactive" / "shared" / "interactive.js"

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
RESET = "\033[0m"

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b",
    r"\bTODO\b",
    r"\{\{[^}]+\}\}",
    r"<placeholder>",
    r"\blorem ipsum\b",
]

# Issues 7+ use the alternating 🧠/🔧 cadence badge.
CADENCE_START = 7


class Report:
    def __init__(self, issue_num: str):
        self.issue = issue_num
        self.rows: list[tuple[str, str, str]] = []  # (status, check, detail)

    def passed(self, check: str, detail: str = "") -> None:
        self.rows.append(("pass", check, detail))

    def warn(self, check: str, detail: str) -> None:
        self.rows.append(("warn", check, detail))

    def fail(self, check: str, detail: str) -> None:
        self.rows.append(("fail", check, detail))

    def print(self) -> None:
        print(f"\n── Issue #{self.issue} " + "─" * (60 - len(self.issue)))
        for status, check, detail in self.rows:
            if status == "pass":
                icon = f"{GREEN}✓{RESET}"
            elif status == "warn":
                icon = f"{YELLOW}!{RESET}"
            else:
                icon = f"{RED}✗{RESET}"
            line = f"  {icon} {check}"
            if detail:
                line += f"  {DIM}{detail}{RESET}"
            print(line)

    @property
    def failed(self) -> bool:
        return any(r[0] == "fail" for r in self.rows)

    @property
    def warned(self) -> bool:
        return any(r[0] == "warn" for r in self.rows)


# --- Individual checks --------------------------------------------------------

def _extract_konami(text: str) -> str | None:
    """Pull the issue's Konami glyph sequence out of the HTML."""
    m = re.search(r'class="konami"[^>]*>([^<]+)<', text)
    if m:
        return re.sub(r"\s+", "", m.group(1))
    return None


def check_newsletter(num: str, report: Report, all_konami: dict[str, str]) -> None:
    path = ISSUES_DIR / f"the_cheat_code_issue_{num}.html"
    if not path.exists():
        report.fail("Newsletter HTML", f"missing: {path.relative_to(REPO_ROOT)}")
        return
    size_kb = path.stat().st_size / 1024
    text = path.read_text(encoding="utf-8", errors="replace")

    report.passed("Newsletter HTML", f"{size_kb:.1f} KB")

    if size_kb < 10 or size_kb > 40:
        report.warn("Newsletter file size", f"{size_kb:.1f} KB (typical 10-40 KB)")

    # Placeholder scan
    hits = []
    for pat in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            hits.append(m.group(0))
    if hits:
        report.fail("No placeholder text", f"found: {', '.join(sorted(set(hits))[:5])}")
    else:
        report.passed("No placeholder text")

    # Title check
    title_match = re.search(r"<title>([^<]+)</title>", text)
    if title_match and f"#{num}" in title_match.group(1):
        report.passed("Issue number in title")
    else:
        found = title_match.group(1) if title_match else "(none)"
        report.fail("Issue number in title", f"title: {found!r}")

    # Footer strings
    if "ABS Tech Strategy" in text:
        report.passed("ABS Tech Strategy footer")
    else:
        report.fail("ABS Tech Strategy footer", "string not found")

    if "aka.ms/the-cheat-code" in text:
        report.passed("Archive link (aka.ms/the-cheat-code)")
    else:
        report.fail("Archive link (aka.ms/the-cheat-code)", "string not found")

    # Type badge for post-cadence issues
    if int(num) >= CADENCE_START:
        if "🧠" in text or "🔧" in text:
            report.passed("Type badge (🧠/🔧)")
        else:
            report.fail("Type badge (🧠/🔧)", "neither emoji found in body")

    # Konami uniqueness
    glyphs = _extract_konami(text)
    if glyphs:
        duplicates = [n for n, g in all_konami.items() if g == glyphs and n != num]
        if duplicates:
            report.fail("Unique Konami glyphs", f"duplicated with #{', #'.join(duplicates)}")
        else:
            report.passed("Unique Konami glyphs", glyphs[:20])
    else:
        report.warn("Konami glyphs", "no .konami element found")


def check_pdf(num: str, report: Report) -> None:
    path = ISSUES_DIR / f"the_cheat_code_issue_{num}.pdf"
    if not path.exists():
        report.fail("PDF", f"missing: {path.relative_to(REPO_ROOT)}")
        return
    size_kb = path.stat().st_size / 1024
    if size_kb < 50:
        report.warn("PDF", f"suspiciously small ({size_kb:.1f} KB)")
    else:
        report.passed("PDF", f"{size_kb:.1f} KB")


def check_diagram(num: str, report: Report) -> None:
    matches = list(DIAGRAMS_DIR.glob(f"issue_{num}_*.png"))
    if matches:
        report.passed("Diagram PNG", f"{len(matches)} file(s)")
    else:
        report.warn("Diagram PNG", f"no diagrams/issue_{num}_*.png found")


def check_interactive(num: str, report: Report) -> None:
    path = DOCS_DIR / "interactive" / f"issue-{num}" / "index.html"
    if not path.exists():
        report.warn("Interactive walkthrough", f"missing: {path.relative_to(REPO_ROOT)}")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    report.passed("Interactive walkthrough", f"{path.stat().st_size // 1024} KB")

    # Tooltip coverage — every data-context element should also have data-tooltip.
    # Match either delimiter style.
    context_tags = re.findall(r"<[a-zA-Z][^>]*?data-context=[\"'][^\"']*[\"'][^>]*>", text, re.DOTALL)
    missing = [t for t in context_tags if "data-tooltip" not in t]
    if context_tags:
        if missing:
            report.fail("Tooltip coverage", f"{len(missing)}/{len(context_tags)} elements missing data-tooltip")
        else:
            report.passed("Tooltip coverage", f"{len(context_tags)}/{len(context_tags)} elements")
    else:
        report.warn("Tooltip coverage", "no data-context elements found")

    # NAV_ISSUES
    if SHARED_JS.exists():
        nav_text = SHARED_JS.read_text(encoding="utf-8")
        if f"num: '{num}'" in nav_text:
            report.passed("NAV_ISSUES entry")
        else:
            report.fail("NAV_ISSUES entry", f"#{num} not in NAV_ISSUES array")


def check_portal(num: str, report: Report) -> None:
    if not DOCS_INDEX.exists():
        report.warn("Portal (docs/index.html)", "file not found")
        return
    text = DOCS_INDEX.read_text(encoding="utf-8", errors="replace")
    if f"#{num}" in text or f"issue-{num}" in text:
        report.passed("Portal mentions issue")
    else:
        report.warn("Portal mentions issue", f"#{num} not referenced in docs/index.html")

    # Nav links must be clean-URL (no .html in <a href> for interactive/)
    dirty = re.findall(r'href="[^"]*interactive/[^"]*\.html"', text)
    if dirty:
        report.fail("Clean-URL nav links", f"{len(dirty)} link(s) contain .html")
    else:
        report.passed("Clean-URL nav links")


# --- Runner -------------------------------------------------------------------

def _collect_all_konami() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in ISSUES_DIR.glob("the_cheat_code_issue_*.html"):
        m = re.search(r"issue_(\d{3})", p.name)
        if not m:
            continue
        glyphs = _extract_konami(p.read_text(encoding="utf-8", errors="replace"))
        if glyphs:
            out[m.group(1)] = glyphs
    return out


def _all_issue_numbers() -> list[str]:
    nums = []
    for p in ISSUES_DIR.glob("the_cheat_code_issue_*.html"):
        m = re.search(r"issue_(\d{3})", p.name)
        if m:
            nums.append(m.group(1))
    return sorted(set(nums))


def run_one(num: str, all_konami: dict[str, str]) -> Report:
    report = Report(num)
    check_newsletter(num, report, all_konami)
    check_pdf(num, report)
    check_diagram(num, report)
    check_interactive(num, report)
    check_portal(num, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("targets", nargs="+", help="Issue number(s) (e.g. 005) or 'all'")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    if "all" in args.targets:
        nums = _all_issue_numbers()
    else:
        nums = [t.zfill(3) for t in args.targets]

    all_konami = _collect_all_konami()
    reports = [run_one(n, all_konami) for n in nums]
    for r in reports:
        r.print()

    total_pass = sum(1 for r in reports for row in r.rows if row[0] == "pass")
    total_warn = sum(1 for r in reports for row in r.rows if row[0] == "warn")
    total_fail = sum(1 for r in reports for row in r.rows if row[0] == "fail")

    print()
    print(f"Summary: {GREEN}{total_pass} pass{RESET}  {YELLOW}{total_warn} warn{RESET}  {RED}{total_fail} fail{RESET}")

    if total_fail > 0:
        return 1
    if args.strict and total_warn > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

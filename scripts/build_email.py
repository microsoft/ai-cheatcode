#!/usr/bin/env python3
"""
Build email-ready newsletter HTML with embedded diagram images.

Reads the archive HTML, finds <img> tags referencing ../diagrams/,
base64-encodes the PNG inline, and adds a fallback archive link.
Outputs to issues/email/.

Usage:
    python scripts/build_email.py 001          # Single issue
    python scripts/build_email.py all          # All issues
    python scripts/build_email.py 001 002 003  # Multiple issues
"""

import base64
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ISSUES_DIR = REPO_ROOT / "issues"
EMAIL_DIR = ISSUES_DIR / "email"
DIAGRAMS_DIR = REPO_ROOT / "diagrams"

ARCHIVE_URL = "https://aka.ms/the-cheat-code"

FALLBACK_HTML = (
    '<p style="margin:4px 0 0 0;font-family:\'Segoe UI\',Tahoma,Geneva,Verdana,'
    'sans-serif;font-size:11px;color:#999999;text-align:center;">'
    'Image not loading? '
    f'<a href="{ARCHIVE_URL}" style="color:#6B2FA0;text-decoration:underline;">'
    'View this issue in the archive &rarr;</a></p>'
)

# Matches <img src="../diagrams/FILENAME"> with any attributes
IMG_PATTERN = re.compile(
    r'(<img\s[^>]*?)src=["\'](\.\./diagrams/([^"\']+))["\']([^>]*?>)',
    re.IGNORECASE | re.DOTALL
)


def embed_image(match: re.Match) -> str:
    """Replace a diagram <img> src with base64-encoded data URI + add fallback link."""
    prefix = match.group(1)
    rel_path = match.group(2)
    filename = match.group(3)
    suffix = match.group(4)

    png_path = DIAGRAMS_DIR / filename
    if not png_path.exists():
        print(f"  ⚠  Diagram not found: {png_path} — keeping original src")
        return match.group(0)

    # Determine MIME type
    ext = png_path.suffix.lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "gif": "image/gif", "svg": "image/svg+xml"}.get(ext.lstrip("."), "image/png")

    data = png_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    size_kb = len(data) / 1024

    print(f"  ✓  Embedded {filename} ({size_kb:.0f} KB)")

    embedded_img = f'{prefix}src="data:{mime};base64,{b64}"{suffix}'
    return embedded_img + "\n" + FALLBACK_HTML


def build_email(issue_num: str) -> bool:
    """Generate email-ready HTML for a single issue number (e.g., '001')."""
    padded = issue_num.zfill(3)
    source = ISSUES_DIR / f"the_cheat_code_issue_{padded}.html"

    if not source.exists():
        print(f"  ✗  Source not found: {source}")
        return False

    html = source.read_text(encoding="utf-8")

    # Count diagrams before replacement
    matches = IMG_PATTERN.findall(html)
    if not matches:
        print(f"  ℹ  No diagram <img> tags found — copying as-is")

    # Replace diagram references with base64
    result = IMG_PATTERN.sub(embed_image, html)

    # Write output
    EMAIL_DIR.mkdir(parents=True, exist_ok=True)
    output = EMAIL_DIR / f"the_cheat_code_issue_{padded}_email.html"
    output.write_text(result, encoding="utf-8")

    source_kb = len(html.encode()) / 1024
    output_kb = len(result.encode()) / 1024
    print(f"  📧 {output.name}  ({source_kb:.0f} KB → {output_kb:.0f} KB)")
    return True


def find_all_issues() -> list[str]:
    """Find all issue numbers in the issues/ directory."""
    nums = []
    for f in sorted(ISSUES_DIR.glob("the_cheat_code_issue_*.html")):
        if "_email" not in f.name:
            m = re.search(r"issue_(\d{3})", f.name)
            if m:
                nums.append(m.group(1))
    return nums


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    args = sys.argv[1:]

    if "all" in args:
        issues = find_all_issues()
        print(f"Building email versions for {len(issues)} issues...\n")
    else:
        issues = [a.zfill(3) for a in args]

    success = 0
    for num in issues:
        print(f"Issue #{num}:")
        if build_email(num):
            success += 1
        print()

    print(f"Done: {success}/{len(issues)} issues processed.")
    if success < len(issues):
        sys.exit(1)


if __name__ == "__main__":
    main()

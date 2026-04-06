#!/usr/bin/env python3
"""
Build email-ready newsletter files with embedded diagram images.

Produces two outputs per issue:
  1. issues/email/the_cheat_code_issue_NNN_email.html  — base64-encoded diagrams (browser preview)
  2. issues/email/the_cheat_code_issue_NNN.eml          — CID-embedded diagrams (open in Outlook)

Usage:
    python scripts/build_email.py 001          # Single issue
    python scripts/build_email.py all          # All issues
    python scripts/build_email.py 001 002 003  # Multiple issues
"""

import base64
import mimetypes
import re
import sys
from email.message import EmailMessage
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
    re.IGNORECASE | re.DOTALL,
)

TITLE_PATTERN = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def _make_cid(filename: str) -> str:
    """Derive a stable Content-ID from a filename."""
    return filename.replace(".", "_").replace(" ", "_")


# ── HTML (base64) output ─────────────────────────────────────────────

def _embed_b64(match: re.Match) -> str:
    prefix, _, filename, suffix = match.group(1), match.group(2), match.group(3), match.group(4)
    png_path = DIAGRAMS_DIR / filename
    if not png_path.exists():
        return match.group(0)
    ext = png_path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "gif": "image/gif", "svg": "image/svg+xml"}.get(ext, "image/png")
    b64 = base64.b64encode(png_path.read_bytes()).decode("ascii")
    size_kb = png_path.stat().st_size / 1024
    print(f"  ✓  Embedded {filename} ({size_kb:.0f} KB) [base64]")
    return f'{prefix}src="data:{mime};base64,{b64}"{suffix}\n{FALLBACK_HTML}'


def build_html_email(padded: str, html: str) -> Path:
    """Write a base64-embedded HTML email file (for browser preview)."""
    result = IMG_PATTERN.sub(_embed_b64, html)
    EMAIL_DIR.mkdir(parents=True, exist_ok=True)
    output = EMAIL_DIR / f"the_cheat_code_issue_{padded}_email.html"
    output.write_text(result, encoding="utf-8")
    size_kb = len(result.encode()) / 1024
    print(f"  📄 {output.name}  ({size_kb:.0f} KB)")
    return output


# ── EML (CID) output ─────────────────────────────────────────────────

def build_eml(padded: str, html: str) -> Path:
    """Write a .eml file with CID-embedded inline images (for Outlook)."""
    # Collect diagram references
    diagrams: list[tuple[str, Path]] = []
    for m in IMG_PATTERN.finditer(html):
        filename = m.group(3)
        png_path = DIAGRAMS_DIR / filename
        if png_path.exists():
            diagrams.append((filename, png_path))

    # Replace img srcs with cid: references
    def _cid_replacer(match: re.Match) -> str:
        prefix, _, filename, suffix = match.group(1), match.group(2), match.group(3), match.group(4)
        png_path = DIAGRAMS_DIR / filename
        if not png_path.exists():
            return match.group(0)
        cid = _make_cid(filename)
        size_kb = png_path.stat().st_size / 1024
        print(f"  ✓  Attached {filename} ({size_kb:.0f} KB) [cid:{cid}]")
        return f'{prefix}src="cid:{cid}"{suffix}\n{FALLBACK_HTML}'

    cid_html = IMG_PATTERN.sub(_cid_replacer, html)

    # Extract subject from <title>
    title_match = TITLE_PATTERN.search(html)
    subject = title_match.group(1).strip() if title_match else f"The Ch(e)at Code — Issue #{padded}"

    # Build MIME message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = ""
    msg["To"] = ""
    msg.make_alternative()
    msg.add_alternative(cid_html, subtype="html")

    # Attach inline images
    html_part = msg.get_payload()[-1]
    for filename, png_path in diagrams:
        cid = _make_cid(filename)
        maintype, subtype = (mimetypes.guess_type(str(png_path))[0] or "image/png").split("/")
        html_part.add_related(
            png_path.read_bytes(),
            maintype=maintype,
            subtype=subtype,
            cid=f"<{cid}>",
            filename=filename,
        )

    # Write .eml
    EMAIL_DIR.mkdir(parents=True, exist_ok=True)
    output = EMAIL_DIR / f"the_cheat_code_issue_{padded}.eml"
    output.write_text(msg.as_string(), encoding="utf-8")
    size_kb = output.stat().st_size / 1024
    print(f"  📧 {output.name}  ({size_kb:.0f} KB)")
    return output


# ── Main ──────────────────────────────────────────────────────────────

def build_email(issue_num: str) -> bool:
    padded = issue_num.zfill(3)
    source = ISSUES_DIR / f"the_cheat_code_issue_{padded}.html"
    if not source.exists():
        print(f"  ✗  Source not found: {source}")
        return False

    html = source.read_text(encoding="utf-8")
    matches = IMG_PATTERN.findall(html)
    if not matches:
        print(f"  ℹ  No diagram <img> tags found — copying as-is")

    build_html_email(padded, html)
    build_eml(padded, html)
    return True


def find_all_issues() -> list[str]:
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

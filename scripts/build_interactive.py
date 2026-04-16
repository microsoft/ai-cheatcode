#!/usr/bin/env python3
"""
Interactive Walkthrough Builder — scaffold docs/interactive/issue-NNN/.

Reads a YAML spec describing an issue's zones and components and emits a
fully working interactive walkthrough page that matches the Bento design
system (Sora/Outfit/JetBrains Mono, glassmorphism, StepEngine context
panels with matching hover tooltips).

Generates the "vertical pipeline of layers" layout used by issues #005
and #006 — the most common shape. Editors can hand-adjust afterward for
bespoke layouts.

Also:
  - Appends an entry to NAV_ISSUES in docs/interactive/shared/interactive.js
    (idempotent — skips if the issue number is already present).

Usage:
    python3 scripts/build_interactive.py path/to/issue-007.yaml
    python3 scripts/build_interactive.py path/to/issue-007.yaml --no-nav
    python3 scripts/build_interactive.py --init-template issue-007.yaml

Spec format (YAML-ish — actually parsed with a strict minimal parser; see
--init-template for the exact shape. For complex specs, use the JSON
variant by naming the file *.json).
"""

import argparse
import json
import html
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_INTERACTIVE = REPO_ROOT / "docs" / "interactive"
SHARED_JS = DOCS_INTERACTIVE / "shared" / "interactive.js"

LAYER_PALETTE = {
    "purple": ("#F5F0FA, #EDE5F5", "#6B2FA0"),
    "blue":   ("#EBF3FD, #D6E8FA", "#0078D4"),
    "green":  ("#E8F5E9, #D6EDD8", "#107C10"),
    "orange": ("#FFF8E1, #FFF0CC", "#CA5010"),
    "teal":   ("#E0F2F1, #CDE8E5", "#008272"),
}

ICON_PALETTE = {
    "purple": "#6B2FA0",
    "blue":   "#0078D4",
    "green":  "#107C10",
    "orange": "#D83B01",
    "amber":  "#CA5010",
    "teal":   "#008272",
}

TEMPLATE_HEAD = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive: {title} — The Cheat Code #{num}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Outfit:wght@400;500;600&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../shared/interactive.css">
<style>
  .layer-label {{ font-family: 'Sora', 'Segoe UI', sans-serif; }}
  .comp-name   {{ font-family: 'Outfit', 'Segoe UI', sans-serif; }}
  .comp-desc   {{ font-family: 'Outfit', 'Segoe UI', sans-serif; }}

  .pipeline {{ display: flex; flex-direction: column; gap: 12px; }}

  .layer {{
    border-radius: 14px;
    padding: 16px 18px;
    position: relative;
    transition: all 0.4s ease;
  }}
  .layer.dimmed       {{ opacity: 0.25; transform: scale(0.98); }}
  .layer.highlighted  {{ opacity: 1; transform: scale(1); box-shadow: 0 0 0 3px rgba(107,47,160,0.3); }}

  .layer-label {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 10px;
    display: flex; align-items: center; gap: 6px;
  }}

{layer_css}

  .component-row {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 12px;
  }}

  .component {{
    background: white;
    border-radius: 10px;
    padding: 12px 14px;
    border: 1px solid rgba(0,0,0,0.08);
    cursor: pointer;
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
  }}
  .component:hover {{
    box-shadow: 0 4px 16px rgba(107, 47, 160, 0.14);
    border-color: rgba(107, 47, 160, 0.25);
  }}

  .comp-name {{
    display: flex; align-items: center; gap: 8px;
    font-weight: 600; font-size: 14px; color: #1B1B3A;
    margin-bottom: 4px;
  }}
  .comp-desc {{ font-size: 12px; line-height: 1.45; color: #5F5F7A; }}

  .icon {{
    width: 28px; height: 28px; border-radius: 7px;
    display: flex; align-items: center; justify-content: center;
    color: white; font-size: 14px; flex-shrink: 0;
  }}
{icon_css}

  .flow-arrow {{ display: flex; justify-content: center; margin: 4px 0; }}
  .varrow .shaft {{
    width: 2px; height: 18px; background: #6B2FA0; margin: 0 auto;
  }}
  .varrow .head {{
    width: 0; height: 0; margin: 0 auto;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 7px solid #6B2FA0;
  }}
  .varrow .label {{
    font-size: 10px; font-family: 'JetBrains Mono', monospace;
    color: #6B2FA0; text-align: center; padding: 2px 0;
  }}
</style>
</head>
<body>

<div class="interactive-page">
  <div class="page-header">
    <a href="../../" class="back-link">← Back to patterns</a>
    <span class="issue-badge">Issue #{num} · {type_label}</span>
    <h1>{title}</h1>
    <p class="page-subtitle">{subtitle}</p>
  </div>

  <div class="diagram-canvas" id="diagram">
    <div class="pipeline">
"""

TEMPLATE_TAIL = """\
    </div>
  </div>
</div>

<script src="../shared/interactive.js"></script>
<script>
  window.interactiveConfig = {
    contextMode: 'lightweight',
    steps: []
  };
</script>
</body>
</html>
"""


# --- Minimal YAML reader (subset sufficient for our spec) ---------------------

def _read_spec(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text)
    except ImportError:
        print("error: PyYAML not installed. Install with `pip install pyyaml`, or use a .json spec.", file=sys.stderr)
        sys.exit(1)


# --- Rendering -----------------------------------------------------------------

def _first_sentence(text: str, max_len: int = 180) -> str:
    text = (text or "").strip()
    m = re.search(r"([^.!?]+[.!?])(?:\s|$)", text)
    s = m.group(1).strip() if m else text
    if len(s) > max_len:
        s = s[:max_len].rsplit(" ", 1)[0] + "…"
    return s


def _layer_css(zones: list) -> str:
    blocks = []
    for z in zones:
        color = z.get("color", "purple")
        if color not in LAYER_PALETTE:
            color = "purple"
        grad, border = LAYER_PALETTE[color]
        slug = z["slug"]
        blocks.append(
            f"  .layer-{slug} {{\n"
            f"    background: linear-gradient(135deg, {grad});\n"
            f"    border: 1.5px solid {border};\n"
            f"  }}\n"
            f"  .layer-{slug} .layer-label {{ color: {border}; }}"
        )
    return "\n".join(blocks)


def _icon_css() -> str:
    return "\n".join(f"  .icon-{name} {{ background: {color}; }}" for name, color in ICON_PALETTE.items())


def _esc_attr_single(text: str) -> str:
    """Escape for inclusion inside single-quoted HTML attributes."""
    # We'll write JSON that contains single quotes etc; encode them as HTML entities.
    return (text.replace("&", "&amp;")
                .replace("'", "&#39;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))


def _render_component(comp: dict) -> str:
    ctx = {
        "title":         comp.get("title") or comp.get("name", ""),
        "what":          comp.get("what") or comp.get("desc", ""),
        "requires":      comp.get("requires", []),
        "prerequisites": comp.get("prerequisites", []),
        "links":         comp.get("links", []),
        "code":          comp.get("code", ""),
    }
    ctx_json = json.dumps(ctx, ensure_ascii=False)
    ctx_attr = _esc_attr_single(ctx_json)
    tooltip = _first_sentence(ctx["what"] or ctx["title"])
    tooltip_attr = html.escape(tooltip, quote=True)

    icon_color = comp.get("icon_color", "purple")
    icon_emoji = comp.get("icon", "🔹")
    name = html.escape(comp["name"])
    desc = html.escape(comp.get("desc", ""))

    return (
        "          <div class=\"component\"\n"
        f"               data-tooltip=\"{tooltip_attr}\"\n"
        f"               data-context='{ctx_attr}'>\n"
        f"            <div class=\"comp-name\"><div class=\"icon icon-{icon_color}\">{icon_emoji}</div> {name}</div>\n"
        f"            <div class=\"comp-desc\">{desc}</div>\n"
        "          </div>"
    )


def _render_zone(zone: dict) -> str:
    slug = zone["slug"]
    label = html.escape(zone["label"])
    ctx = {
        "title":         zone.get("title", zone["label"]),
        "what":          zone.get("what", ""),
        "requires":      zone.get("requires", []),
        "prerequisites": zone.get("prerequisites", []),
        "links":         zone.get("links", []),
        "code":          zone.get("code", ""),
    }
    ctx_attr = _esc_attr_single(json.dumps(ctx, ensure_ascii=False))
    tooltip_attr = html.escape(_first_sentence(ctx["what"] or ctx["title"]), quote=True)
    components = "\n".join(_render_component(c) for c in zone.get("components", []))
    arrow = ""
    if zone.get("arrow_to_next"):
        label_text = html.escape(zone["arrow_to_next"])
        arrow = (
            f'      <div class="flow-arrow"><div class="varrow"><div class="shaft"></div>'
            f'<div class="label">{label_text}</div><div class="head"></div></div></div>\n'
        )
    return (
        f'      <div class="layer layer-{slug}" data-layer="{slug}"\n'
        f'           data-tooltip="{tooltip_attr}"\n'
        f"           data-context='{ctx_attr}'>\n"
        f'        <div class="layer-label">{label}</div>\n'
        f'        <div class="component-row">\n{components}\n        </div>\n'
        f"      </div>\n"
        f"{arrow}"
    )


def render(spec: dict) -> str:
    num = f"{int(spec['issue']):03d}"
    title = spec["title"]
    subtitle = spec.get("subtitle", "")
    type_label = "Conceptual" if spec.get("type", "conceptual").lower().startswith("c") else "Practical"
    zones = spec["zones"]

    head = TEMPLATE_HEAD.format(
        title=html.escape(title),
        num=num,
        subtitle=html.escape(subtitle),
        type_label=type_label,
        layer_css=_layer_css(zones),
        icon_css=_icon_css(),
    )
    body = "".join(_render_zone(z) for z in zones)
    return head + body + TEMPLATE_TAIL


# --- NAV_ISSUES patch ---------------------------------------------------------

def update_nav(num: str, title: str, type_label: str) -> bool:
    if not SHARED_JS.exists():
        print(f"warning: {SHARED_JS} not found, skipping nav update")
        return False
    text = SHARED_JS.read_text(encoding="utf-8")
    if f"num: '{num}'" in text:
        print(f"NAV_ISSUES already contains #{num} — skipping")
        return False
    entry = (
        f"    {{ num: '{num}', short: '#{num}', title: '{title}',"
        f" path: '../issue-{num}/', type: '{type_label.lower()}' }},"
    )
    new_text, n = re.subn(
        r"(\n  const NAV_ISSUES = \[\n(?:.*\n)*?)(  \];)",
        lambda m: m.group(1) + entry + "\n" + m.group(2),
        text,
        count=1,
    )
    if n == 0:
        print("warning: could not locate NAV_ISSUES array — nav not patched")
        return False
    SHARED_JS.write_text(new_text, encoding="utf-8")
    print(f"Patched NAV_ISSUES with #{num}")
    return True


# --- Template scaffold --------------------------------------------------------

TEMPLATE_YAML = """\
# Interactive walkthrough spec
issue: 7
title: "Your Pattern Name"
subtitle: "One-sentence pattern description shown under the page title"
type: conceptual   # conceptual | practical

zones:
  - slug: input
    color: purple
    label: "🟣 Input Zone"
    title: "Input Zone"
    what: "Short description of the zone for the hover tooltip and context panel."
    requires: ["Dependency A", "Dependency B"]
    prerequisites: ["Setup step A", "Setup step B"]
    links:
      - label: "Docs"
        url: "https://learn.microsoft.com/"
    code: "// optional code snippet"
    arrow_to_next: "Label for arrow"
    components:
      - name: "Component Name"
        icon: "🤖"
        icon_color: purple
        desc: "Short card description."
        title: "Full Context Panel Title"
        what: "Longer explanation for the context panel."
        requires: ["A"]
        prerequisites: ["B"]
        links:
          - label: "More"
            url: "https://example.com"
        code: "// snippet"
  - slug: output
    color: green
    label: "🟢 Output Zone"
    what: "..."
    components:
      - name: "Output"
        icon: "📤"
        icon_color: green
        desc: "..."
        what: "..."
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("spec", nargs="?", help="Path to spec file (*.yaml or *.json)")
    parser.add_argument("--no-nav", action="store_true", help="Skip NAV_ISSUES patch")
    parser.add_argument("--init-template", type=Path, help="Write a starter YAML spec to this path and exit")
    parser.add_argument("--stdout", action="store_true", help="Print generated HTML to stdout instead of writing")
    args = parser.parse_args()

    if args.init_template:
        args.init_template.parent.mkdir(parents=True, exist_ok=True)
        args.init_template.write_text(TEMPLATE_YAML, encoding="utf-8")
        print(f"Wrote starter spec: {args.init_template}")
        return 0

    if not args.spec:
        parser.print_help()
        return 2

    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"error: spec not found: {spec_path}", file=sys.stderr)
        return 1

    spec = _read_spec(spec_path)
    try:
        html_out = render(spec)
    except KeyError as e:
        print(f"error: spec is missing required key: {e}", file=sys.stderr)
        return 1

    if args.stdout:
        print(html_out)
        return 0

    num = f"{int(spec['issue']):03d}"
    out_dir = DOCS_INTERACTIVE / f"issue-{num}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(html_out, encoding="utf-8")
    print(f"Wrote {out_path}")

    if not args.no_nav:
        type_label = "Conceptual" if spec.get("type", "conceptual").lower().startswith("c") else "Practical"
        # NAV_ISSUES stores short title — use the provided title, caller can edit
        update_nav(num, spec["title"].replace("'", "\\'"), type_label)

    print()
    print("Next steps:")
    print(f"  1. Open {out_path} and review layout")
    print("  2. Add data-step indices if using StepEngine walkthrough")
    print("  3. Add a card to docs/index.html Bento grid")
    print(f"  4. Run: python3 scripts/preflight.py {num}")
    print(f"  (generated {date.today().isoformat()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

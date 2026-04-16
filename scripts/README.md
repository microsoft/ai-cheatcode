# Production scripts

Automation for the weekly Cheat Code pipeline. Each script is standalone
Python 3, stdlib-only where possible (PyYAML is optional, JSON specs work
equivalently).

---

## `pattern_scout.py`

Turns raw transcripts into an LLM-ready pattern extraction prompt.

```bash
# Produce a prompt artifact + blank candidate YAML from a transcript
python3 scripts/pattern_scout.py notes/tyson-1on1.md

# Custom output path
python3 scripts/pattern_scout.py notes/tyson-1on1.md --out candidates/tyson.md

# Just scaffold a blank candidates YAML
python3 scripts/pattern_scout.py --init-template candidates/new.yaml
```

Output goes to `candidates/` by default. Paste the generated `*__scout.md`
into Copilot Chat / any LLM, capture approved candidates in the
companion `*__spec.yaml`, then promote them into `series_plan/`.

The prompt bundles: the source text, the editorial rubric, the full
published-issue titles map (dedupe), and the current series roadmap
(so candidates can be mapped to open arcs).

---

## `build_interactive.py`

Scaffolds `docs/interactive/issue-NNN/index.html` from a YAML or JSON
spec. Generates the "vertical pipeline of layers" layout used by issues
#005 and #006 — the most common shape. Editors hand-tune afterward for
bespoke layouts.

```bash
# Generate a starter spec
python3 scripts/build_interactive.py --init-template specs/issue-009.yaml

# Build the page (also patches NAV_ISSUES)
python3 scripts/build_interactive.py specs/issue-009.yaml

# Skip the NAV_ISSUES update
python3 scripts/build_interactive.py specs/issue-009.yaml --no-nav

# Print to stdout for preview
python3 scripts/build_interactive.py specs/issue-009.yaml --stdout
```

Every generated component gets both a rich `data-context` JSON payload
(for click-to-open context panels) and a matching `data-tooltip`
(derived from the first sentence of `what`), so tooltip coverage is
100% by construction.

**Spec keys**

| Key | Required | Notes |
|-----|----------|-------|
| `issue` | yes | integer, zero-padded on output |
| `title` | yes | page H1 and `<title>` |
| `subtitle` | no | shown under the H1 |
| `type` | yes | `conceptual` or `practical` |
| `zones[]` | yes | list of zones top-to-bottom |
| `zones[].slug` | yes | CSS slug (letters/digits/hyphens) |
| `zones[].color` | no | `purple\|blue\|green\|orange\|teal` |
| `zones[].label` | yes | zone heading with emoji |
| `zones[].what` | yes | tooltip + context panel copy |
| `zones[].arrow_to_next` | no | arrow label to following zone |
| `zones[].components[]` | yes | list of component cards |

Component keys mirror zone keys, plus `name`, `icon`, `icon_color`,
`desc`.

JSON specs work identically — just name the file `*.json`.

---

## `preflight.py`

Pre-publish checklist automation. Validates newsletter HTML, PDF,
diagram, interactive page, NAV_ISSUES entry, Konami glyph uniqueness,
placeholder text, and portal consistency.

```bash
# Single issue
python3 scripts/preflight.py 005

# Multiple issues
python3 scripts/preflight.py 005 006 007

# All published + drafted issues
python3 scripts/preflight.py all

# Fail on warnings too (for CI)
python3 scripts/preflight.py 005 --strict
```

Exits non-zero when any check fails — safe to wire into a pre-push hook
or CI step. Warnings don't fail the run unless `--strict` is set.

Checks performed (per issue):

| Category | Checks |
|----------|--------|
| Newsletter HTML | exists, size sane, no placeholder text (TBD/TODO/`{{…}}`), issue number in title, ABS Tech Strategy footer, `aka.ms/the-cheat-code` link, type badge emoji (🧠/🔧) for issues ≥ 007 |
| PDF | exists, non-trivial size |
| Diagram | at least one `diagrams/issue_NNN_*.png` |
| Interactive walkthrough | page exists, every `data-context` has a matching `data-tooltip`, NAV_ISSUES contains the issue |
| Konami | glyphs not duplicated with any other issue |
| Portal | `docs/index.html` references the issue; no `.html` extensions in interactive nav links |

---

## `build_email.py`

(Existing) Produces the CID-embedded `.eml` and base64 `*_email.html`
from the archive HTML.

```bash
python3 scripts/build_email.py 005
python3 scripts/build_email.py all
```

---

## `test_navigation.js`

(Existing) Playwright smoke test. Requires a local static server:

```bash
npx serve docs -p 8787
node scripts/test_navigation.js
```

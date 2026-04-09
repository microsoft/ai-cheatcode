# Copilot Instructions — The Cheat Code

## What This Is

"The Cheat Code" is an internal Microsoft newsletter distributed weekly to the ABS Tech Strategy team (AI Business Solutions). Each issue features a reusable agentic pattern for Copilot Chat, extracted from real customer engagements. The name is a play on "chat" (Copilot Chat) and "cheat" (cheat codes) — the Konami code motif appears subtly in every issue.

## Architecture

Each issue exists in **four parallel formats**, all produced from the same source content:

1. **HTML email** (`issues/the_cheat_code_issue_NNN.html`) — primary format, 600px max-width, inline CSS, Outlook-compatible
2. **PDF** (`issues/the_cheat_code_issue_NNN.pdf`) — rendered from HTML via Chrome headless, attached to Engage posts
3. **Viva Amplify content** (`viva_amplify/issue_NNN_amplify.md`) — section-by-section content mapped to Amplify web parts
4. **Architecture diagram** (`diagrams/issue_NNN_*_rich.png`) — rendered from companion HTML/CSS files in `diagrams/`

The **PRODUCTION_PLAYBOOK.md** is the authoritative reference for all production processes. Read it first when working on anything.

## Hosting & Distribution

- **GitHub Pages archive:** https://aka.ms/the-cheat-code (resolves to `microsoft.github.io/ai-cheatcode`)
- **Repo:** `microsoft/the-cheat-code` (private, GitHub Enterprise)
- **Pages source:** `main` branch, root `/`
- **Workflow:** Edit files → `git push` → GitHub Pages auto-deploys
- Only the `index.html` and `issues/` folder are reader-facing via Pages. Everything else (playbook, series plan, templates) lives in the repo but isn't linked from the page.
- The `index.html` should only show **published** issues + a "Coming Next" teaser for the next one. Update it as each issue is sent.

## Alternating Cadence: Conceptual → Practical

Starting with Issue #007, the series follows a two-issue arc model:

- **Odd issues (🧠 Conceptual Pattern)**: Names the pattern, explains *why* it exists, frames the architecture, identifies design decisions. Sections: Intro → Pattern Breakdown → Where This Pattern Lands → Quick Tips. No Agent Spotlight.
- **Even issues (🔧 Practical Build)**: Shows *how* to build it in Copilot Studio, step-by-step with components. Sections: Intro (links back to conceptual pair) → Agent Spotlight (the build) → Pattern Breakdown (components in build order) → Try This Now.

The issue info bar carries a type tag: `🧠 CONCEPTUAL PATTERN` or `🔧 PRACTICAL BUILD`.

Issues #001–006 predate this cadence and stand as-is — no rebranding.

## Content Model

Each issue follows a fixed structure defined in `the_cheat_code_template.html`:

- **Header**: Dark navy (#1B1B3A), unique Konami code glyphs per issue (see Symbol Registry in playbook)
- **Intro**: Customer problem → pattern name (2 paragraphs max)
- **Agent Spotlight** (when featuring a specific agent): Attribution, scenario, solution
- **Pattern Breakdown** (always): The core reusable pattern with numbered design decisions
- **Rotating sections**: Quick Tips, Try This Now, Where This Pattern Lands (not all appear in every issue)

### Key Editorial Rules

- Lead with the customer scenario, never write a demo recap
- One agent demo often yields 2–4 standalone patterns — disaggregate them into separate issues
- Every section must answer: "How does this make me faster as a CSA?"
- Full name attribution for the builder in every issue
- Cross-reference related issues when patterns connect — all cross-refs are hyperlinked to the Pages archive

## Current Issue Map (20 issues)

| # | Title | Type | Builder | Date |
|---|-------|------|---------|------|
| 001 | Code-First Agent Delivery | 🔧 | Cristiano Almeida Gonçalves | Mar 23 |
| 002 | Scoped Multi-Source Search | 🧠 | Raghav BN | Mar 31 |
| 003 | Prompt-Chained Triage + Playbooks | 🔧 | Raghav BN | Apr 7 |
| 004 | Secure In-Boundary Processing | 🧠 | Raghav BN | Apr 14 |
| 005 | Human-in-the-Loop Approval Gates | 🧠 | Pete Puustinen | Apr 21 |
| 006 | Meeting-to-Knowledge Pipeline | 🔧 | Pete Puustinen | Apr 28 |
| 007 | Holographic Memory | 🧠 | Tyson Dowd | May 5 |
| 008 | Cross-Project Knowledge Agent | 🔧 | Tyson Dowd | May 12 |
| 009 | Adaptive Guardrails | 🧠 | TBD | May 19 |
| 010 | Building Adaptive Guardrails | 🔧 | TBD | May 26 |
| 011 | Multi-Agent Handoff | 🧠 | TBD | Jun 2 |
| 012 | Building Multi-Agent Handoff | 🔧 | TBD | Jun 9 |
| 013 | Persistent Agent Memory | 🧠 | TBD | Jun 16 |
| 014 | Building Persistent Memory | 🔧 | TBD | Jun 23 |
| 015 | Proactive Agent Triggers | 🧠 | TBD | Jun 30 |
| 016 | Building Proactive Agents | 🔧 | TBD | Jul 7 |
| 017 | Agent Evaluation & Trust Signals | 🧠 | TBD | Jul 14 |
| 018 | Building Agent Analytics | 🔧 | TBD | Jul 21 |
| 019 | Custom Connector Patterns | 🧠 | TBD | Jul 28 |
| 020 | Building Custom Connectors | 🔧 | TBD | Aug 4 |

Only Issue #001 is published. Issues #002–006 are written and ready from prior work. Issues #007–020 are drafted.

## Series Plan

Detailed arc briefs with full content outlines are in `series_plan/`:
- `SERIES_ROADMAP.md` — master roadmap, editorial calendar, Konami code assignments
- `arc_1_adaptive_guardrails.md` through `arc_6_custom_connectors.md` — per-arc content briefs

## Diagram Production

Diagrams use **HTML/CSS rendered via Chrome headless** (not Mermaid, not Paper Banana).

### Render commands

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Render diagram PNG (1680px wide, height varies per diagram)
"$CHROME" --headless --disable-gpu --no-sandbox \
  --screenshot="diagrams/issue_NNN_name_rich.png" \
  --window-size=1680,HEIGHT \
  "file://$PWD/diagrams/issue_NNN_name.html"

# Render newsletter PDF
"$CHROME" --headless --disable-gpu --no-sandbox \
  --print-to-pdf="issues/the_cheat_code_issue_NNN.pdf" \
  --print-to-pdf-no-header "file://$PWD/issues/the_cheat_code_issue_NNN.html"
```

**Critical**: Chrome `--screenshot` silently clips content taller than `--window-size` height. Always match the `min-height` in body CSS to the `--window-size` height. When in doubt, add 100–200px.

### Diagram Design System

- **Zone containers**: 16px border-radius, 2px solid colored border, linear gradient background, drop shadow
- **Component cards**: White `#FFFFFF`, 12px rounded corners, inside zones
- **Icon badges**: 30px rounded squares with emoji
- **Color palette**: Purple `#6B2FA0` (agents), Blue `#0078D4` (Azure), Green `#107C10` (output/trust), Orange `#D83B01` (external/warnings), Amber `#CA5010` (decisions/gates)

Copy an existing diagram HTML file from `diagrams/` as your starting point for new diagrams.

## Newsletter Styling

- Max width: 600px, font: Segoe UI family, body 15px `#444444` on white
- Top accent bar: 6px `#6B2FA0`
- Color-coded 4px left borders per section: Purple (Spotlight), Blue (Pattern), Green (Tips), Orange (Try This), Amber (Positioning)
- Callout boxes: Warning (`#FFF8E1`/`#FFE082`), Insight (`#F0ECF5`), Flow diagram (`#F0F6FF`), Positioning (`#FFF3E0`/`#FFCC80`)
- All CSS must be inline for email compatibility; use `<!--[if mso]>` conditionals for Outlook
- Footer includes: "ABS Tech Strategy • AI Business Solutions" and "Browse all issues at aka.ms/the-cheat-code"

## Repo Structure

```
├── index.html                    # GitHub Pages landing page
├── README.md                     # Repo overview
├── PRODUCTION_PLAYBOOK.md        # Authoritative production reference
├── the_cheat_code_template.html  # Issue HTML template
├── viva_engage_posts.txt         # Companion Viva Engage posts (all issues)
├── teams_launch_post.txt         # Teams launch announcement
├── issues/                       # All 20 newsletter HTML + PDF files
├── diagrams/                     # Architecture diagram HTML sources + rendered PNGs
├── series_plan/                  # Series roadmap + 6 per-arc content briefs
└── viva_amplify/                 # Amplify setup guide + per-issue Amplify content
```

## File Naming Conventions

- Newsletter HTML: `issues/the_cheat_code_issue_NNN.html`
- Newsletter PDF: `issues/the_cheat_code_issue_NNN.pdf`
- Diagram source: `diagrams/issue_NNN_shortname.html`
- Diagram render: `diagrams/issue_NNN_shortname_rich.png`
- Amplify content: `viva_amplify/issue_NNN_amplify.md`

## Publishing Workflow

1. Finalize the issue HTML in `issues/`
2. Render PDF via Chrome headless
3. Create/render the diagram in `diagrams/`
4. Move the issue from "Coming Next" to "Published" in `index.html`
5. Update the "Coming Next" teaser to the following issue
6. `git add -A && git commit && git push` — Pages auto-deploys
7. Send the HTML email (Monday AM)
8. Post the Viva Engage teaser from `viva_engage_posts.txt` (Monday PM)

## Pre-Send Checklist

Before publishing any issue, verify: no placeholder text remaining, correct issue number and date, unique Konami glyphs (check Symbol Registry in playbook), full builder attribution, accurate cross-references with working hyperlinks, type badge (🧠/🔧) in info bar, "ABS Tech Strategy" in footer, `aka.ms/the-cheat-code` archive link, and reasonable file size (18–28KB typical for HTML).

## Decision Log (Key Decisions)

- **"ABS Tech Strategy"** not "AIWF Team" — represents the broader org
- **No rebranding of #001–006** — published, in inboxes, cadence starts at #007
- **Copilot Studio as default practical stack** — widest CSA audience, immediately actionable
- **aka.ms/the-cheat-code** — vanity URL pointing to GitHub Pages archive
- **Private repo, public-facing Pages** — repo holds all working files, only index + issues are reader-facing
- **Alternating cadence** — inspired by Issue #007 producing two equally strong versions (conceptual + practical)

# The Cheat Code

<div align="center">

```
  ╔══════════════════════════════════════════════╗
  ║                                              ║
  ║          T H E   C H ( E ) A T   C O D E    ║
  ║                                              ║
  ║       ▲ ▲ ▼ ▼ ◄ ► ◄ ► B A START            ║
  ║                                              ║
  ║       Agent Patterns for Copilot Chat        ║
  ║                                              ║
  ╚══════════════════════════════════════════════╝
```

**Agent Patterns for Copilot Chat** — A weekly newsletter by ABS Tech Strategy

*Each issue: one reusable pattern, extracted from a real customer engagement, ready to land.*

[**Browse the Archive →**](https://aka.ms/the-cheat-code)

</div>

---

## What Is This?

The Cheat Code is a weekly internal newsletter that extracts **reusable agentic patterns** from real Microsoft customer engagements. The name is a play on "chat" (Copilot Chat) and "cheat" (cheat codes) — every issue is a cheat code for building AI agents faster.

The Konami code (↑ ↑ ↓ ↓ ← → ← → B A START) appears as a subtle easter egg in every issue, rendered in near-invisible 8px monospace — a nod to the original cheat codes that gave you an unfair advantage.

Starting with Issue #008, the series alternates between:

- **🧠 Conceptual Patterns** — names the pattern, explains *why* it exists, frames the architecture
- **🔧 Practical Builds** — shows *how* to build it in Copilot Studio, step by step

## Brand Identity

| Element | Value |
|---------|-------|
| **Name** | The Cheat Code — parentheses around the "e" are part of the mark |
| **Tagline** | Agent Patterns for Copilot Chat |
| **Primary color** | Purple `#6B2FA0` — represents AI agents throughout |
| **Header color** | Dark navy `#1B1B3A` |
| **Section accents** | Blue `#0078D4` (patterns), Green `#107C10` (tips), Orange `#D83B01` (try this), Amber `#CA5010` (positioning) |
| **Typography** | Segoe UI (body), Consolas (code/Konami glyphs) |
| **Signature element** | Konami code sequence — unique arrow glyphs per issue (see Symbol Registry in playbook) |
| **Tone** | Professional with a wink — enterprise-grade content, gaming-inspired identity |

### Logo Concept

The logo is a **chat bubble containing the Konami directional arrows** — a speech bubble (representing Copilot Chat) with ▲ ▼ ◄ ► inside it (representing the cheat code). Rendered in brand purple (`#6B2FA0`) on a dark navy (`#1B1B3A`) background.

> **Why this works:** It's the literal visual intersection of the two words in the name — "chat" (the bubble) and "cheat" (the code arrows). Recognizable at any size, from a favicon to a slide deck. Anyone who's ever entered a cheat code recognizes those arrows instantly.

## Browse the Archive

👉 **[aka.ms/the-cheat-code](https://aka.ms/the-cheat-code)**

### Interactive Portal

The interactive portal at [aka.ms/the-cheat-code](https://aka.ms/the-cheat-code) provides step-through architectural walkthroughs for each pattern. Click any component in a diagram to see implementation requirements, prerequisites, platform links, and code snippets. Issues #001–004 have interactive walkthroughs; more are being added.

## Repo Structure

```
├── index.html                    # GitHub Pages landing page (archive)
├── docs/                         # GitHub Pages portal (Bento design)
│   ├── index.html                # Landing page with Bento grid layout
│   └── interactive/              # Step-through diagram walkthroughs
│       ├── shared/               # Shared CSS/JS framework
│       └── issue-NNN/            # Per-issue interactive pages
├── PRODUCTION_PLAYBOOK.md        # Authoritative production reference
├── the_cheat_code_template.html  # Issue template
├── viva_engage_posts.txt         # Viva Engage companion posts
├── teams_launch_post.txt         # Teams launch announcement
│
├── issues/                       # All newsletter HTML + PDFs
│   ├── the_cheat_code_issue_001.html
│   ├── the_cheat_code_issue_001.pdf
│   └── ...
│
├── samples/                      # Working code samples per issue
│   ├── ENVIRONMENT_GUIDE.md           # CDX + Azure setup reference
│   ├── VALIDATION_CHECKLIST.md        # 10-item readiness check
│   ├── PROVENANCE.md                  # Who built what, from which engagement
│   ├── issue-001/                     # Tier 3: azd deployable template (Python + Bicep)
│   ├── issue-003/                     # Tier 2: Copilot Studio starter kit
│   └── ...
│
├── diagrams/                     # Architecture diagram sources + renders
│   ├── issue_001_deployment.html       # HTML/CSS source
│   ├── issue_001_deployment_rich.png   # Chrome headless render
│   └── ...
│
├── series_plan/                  # Series roadmap + per-arc briefs
│   ├── SERIES_ROADMAP.md
│   ├── arc_1_adaptive_guardrails.md
│   └── ...
│
└── viva_amplify/                 # Amplify setup guide + per-issue content
    ├── AMPLIFY_SETUP_GUIDE.md
    └── ...
```

## Published Issues

| # | Pattern | Type | Builder | Code Sample | Interactive |
|---|---------|------|---------|-------------|-------------|
| 001 | Code-First Agent Delivery | 🔧 | Cristiano Almeida Gonçalves | [Deployable Template](samples/issue-001/) | [Walkthrough](docs/interactive/issue-001/) |
| 002 | Scoped Multi-Source Search | 🧠 | Raghav BN | [Prompt Pack](samples/issue-002/) | [Walkthrough](docs/interactive/issue-002/) |
| 003 | Prompt-Chained Triage + Playbooks | 🔧 | Raghav BN | [Starter Kit](samples/issue-003/) | [Walkthrough](docs/interactive/issue-003/) |
| 004 | Secure In-Boundary Processing | 🧠 | Raghav BN | [Prompt Pack](samples/issue-004/) | [Walkthrough](docs/interactive/issue-004/) |
| 005 | Human-in-the-Loop Approval Gates | 🧠 | Pete Puustinen | [Prompt Pack](samples/issue-005/) | — |
| 006 | Meeting-to-Knowledge Pipeline | 🔧 | Pete Puustinen | [Starter Kit](samples/issue-006/) | — |
| 007 | Holographic Memory | 🧠 | Tyson Dowd | [Prompt Pack](samples/issue-007/) | — |
| 008 | Cross-Project Knowledge Agent | 🔧 | Tyson Dowd | [Deployable Template](samples/issue-008/) | — |

## Code Samples

Every issue has a companion code sample in [`samples/`](samples/):

| Tier | What You Get | Setup Time |
|------|-------------|------------|
| **Prompt Pack** | Tested prompts + expected outputs | ~5 min |
| **Starter Kit** | Importable Copilot Studio solution + flows | ~30 min |
| **Deployable Template** | `azd up` from zero to working demo | ~15 min |

See [`samples/PROVENANCE.md`](samples/PROVENANCE.md) for who built each pattern and which customer engagement it came from.

## How to Publish a New Issue

1. Create the issue HTML from `the_cheat_code_template.html` (see `PRODUCTION_PLAYBOOK.md`)
2. Render the PDF: `"$CHROME" --headless --print-to-pdf="issues/issue_NNN.pdf" --print-to-pdf-no-header "file://$PWD/issues/issue_NNN.html"`
3. Create the diagram in `diagrams/` and render the PNG
4. Create the interactive walkthrough page in `docs/interactive/issue-NNN/` and update the portal landing page (`docs/index.html`)
5. Update `index.html` to add the new issue to the Published section
6. `git add -A && git commit && git push` — GitHub Pages deploys automatically
7. Send the HTML email, post the Viva Engage teaser (see `viva_engage_posts.txt`)

## Distribution Channels

- **Outlook Newsletter** — HTML email, Monday AM
- **Viva Engage** — Teaser post + PDF attachment, Monday PM
- **GitHub Pages** — [aka.ms/the-cheat-code](https://aka.ms/the-cheat-code) — browsable archive

## Internal Only

Microsoft Internal — Not for external distribution.

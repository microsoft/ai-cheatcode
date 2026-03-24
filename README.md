# The Ch(e)at Code

**Agent Patterns for Copilot Chat** — A weekly newsletter by ABS Tech Strategy

↑ ↑ ↓ ↓ ← → ← → B A START

---

## What Is This?

Each issue extracts one reusable agentic pattern from a real customer engagement and packages it so any CSA can land it with their own customers. The name is a play on "chat" (Copilot Chat) and "cheat" (cheat codes).

Starting with Issue #008, the series alternates between:

- **🧠 Conceptual Patterns** — names the pattern, explains *why* it exists, frames the architecture
- **🔧 Practical Builds** — shows *how* to build it in Copilot Studio, step by step

## Browse the Archive

👉 **[aka.ms/the-cheat-code](https://aka.ms/the-cheat-code)**

## Repo Structure

```
├── index.html                    # GitHub Pages landing page (archive)
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

| # | Pattern | Type | Builder |
|---|---------|------|---------|
| 001 | Code-First Agent Delivery | 🔧 | Cristiano Almeida Gonçalves |
| 002 | Scoped Multi-Source Search | 🧠 | Raghav BN |
| 003 | Prompt-Chained Triage + Playbooks | 🔧 | Raghav BN |
| 004 | Secure In-Boundary Processing | 🧠 | Raghav BN |
| 005 | Human-in-the-Loop Approval Gates | 🧠 | Pete Puustinen |
| 006 | Meeting-to-Knowledge Pipeline | 🔧 | Pete Puustinen |
| 007 | Holographic Memory | 🧠 | Tyson Dowd |

## How to Publish a New Issue

1. Create the issue HTML from `the_cheat_code_template.html` (see `PRODUCTION_PLAYBOOK.md`)
2. Render the PDF: `"$CHROME" --headless --print-to-pdf="issues/issue_NNN.pdf" --print-to-pdf-no-header "file://$PWD/issues/issue_NNN.html"`
3. Create the diagram in `diagrams/` and render the PNG
4. Update `index.html` to add the new issue to the Published section
5. `git add -A && git commit && git push` — GitHub Pages deploys automatically
6. Send the HTML email, post the Viva Engage teaser (see `viva_engage_posts.txt`)

## Distribution Channels

- **Outlook Newsletter** — HTML email, Monday AM
- **Viva Engage** — Teaser post + PDF attachment, Monday PM
- **GitHub Pages** — [aka.ms/the-cheat-code](https://aka.ms/the-cheat-code) — browsable archive

## Internal Only

Microsoft Internal — Not for external distribution.

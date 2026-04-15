# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

"The Cheat Code" is an internal Microsoft newsletter (ABS Tech Strategy) publishing weekly reusable agentic patterns for Copilot Chat. Each issue exists in parallel formats: HTML email, PDF, Viva Amplify content, architecture diagram, and interactive portal page. The `PRODUCTION_PLAYBOOK.md` is the authoritative reference for all production processes — read it first.

## Key Commands

```bash
# Chrome path (macOS)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Render newsletter PDF from HTML
"$CHROME" --headless --disable-gpu --no-sandbox \
  --print-to-pdf="issues/the_cheat_code_issue_NNN.pdf" \
  --print-to-pdf-no-header "file://$PWD/issues/the_cheat_code_issue_NNN.html"

# Render architecture diagram PNG
"$CHROME" --headless --disable-gpu --no-sandbox \
  --screenshot="diagrams/issue_NNN_name_rich.png" \
  --window-size=1680,HEIGHT \
  "file://$PWD/diagrams/issue_NNN_name.html"

# Build email-ready files (base64 + .eml with CID-embedded diagrams)
python scripts/build_email.py NNN        # single issue
python scripts/build_email.py all        # all issues

# Run navigation tests (requires local server on :8787)
npx playwright install chromium          # one-time setup
node scripts/test_navigation.js          # needs: npx serve docs -p 8787
```

## Architecture

### Content Pipeline
1. Source content from meeting transcripts (WorkIQ) or 1:1 sessions
2. Extract reusable patterns (disaggregate — one demo often yields 2-4 issues)
3. Write issue HTML from `the_cheat_code_template.html`
4. Render PDF + diagram PNG via Chrome headless
5. Build interactive walkthrough page in `docs/interactive/issue-NNN/`
6. Update portal (`docs/index.html`) and archive (`index.html`)
7. `git push` — GitHub Pages auto-deploys from `docs/` on `main`

### Two Design Systems
- **Email newsletter**: Segoe UI, 600px max-width, all inline CSS, Outlook-compatible. Template: `the_cheat_code_template.html`.
- **Interactive portal** (`docs/`): Dark theme with Outfit/Sora/JetBrains Mono (Google Fonts), glassmorphism cards, Bento grid layout. Full design system in `DESIGN.md`.

### Alternating Cadence (starting Issue #007)
- **Odd issues** = Conceptual Pattern: names the pattern, explains *why*, frames architecture
- **Even issues** = Practical Build: shows *how* to build it in Copilot Studio step-by-step
- Issues #001-006 predate this cadence and stand as-is

### Interactive Walkthroughs (`docs/interactive/`)
- Shared framework: `docs/interactive/shared/interactive.css` + `interactive.js`
- **StepEngine** drives step-through walkthroughs with narrative panels
- **Context panels** show implementation details via `data-context` JSON attributes on diagram elements
- Use `contextMode: 'lightweight'` in `window.interactiveConfig`
- Copy an existing issue page as starting point for new ones

## File Naming Conventions

- Newsletter: `issues/the_cheat_code_issue_NNN.html` / `.pdf`
- Diagram source: `diagrams/issue_NNN_shortname.html`
- Diagram render: `diagrams/issue_NNN_shortname_rich.png`
- Amplify content: `viva_amplify/issue_NNN_amplify.md`
- Interactive pages: `docs/interactive/issue-NNN/index.html`
- Code samples: `samples/issue-NNN/`

## Critical Gotchas

- Chrome `--screenshot` silently clips content taller than `--window-size` height. Always match `min-height` in body CSS to `--window-size` height, plus 100-200px buffer.
- All newsletter CSS must be inline for email compatibility. Use `<!--[if mso]>` conditionals for Outlook.
- Portal uses clean directory URLs — never link to `.html` files.
- The Konami code easter egg (near-invisible 8px monospace glyphs) appears on every page. Each issue gets unique glyphs from the Symbol Registry in the playbook.
- `docs/index.html` should only show published issues plus a "Coming Next" teaser for the next one.
- Only `docs/` is reader-facing via GitHub Pages. Everything else stays repo-only.

## Brand Colors

| Role | Color |
|------|-------|
| Primary / Agents | Purple `#6B2FA0` |
| Azure / Conceptual | Blue `#0078D4` |
| Output / Trust | Green `#107C10` |
| External / Practical | Orange `#D83B01` |
| Decisions / Gates | Amber `#CA5010` |
| Header / Surfaces | Navy `#1B1B3A` |
| Portal background | Deep Navy `#0E0E1F` |

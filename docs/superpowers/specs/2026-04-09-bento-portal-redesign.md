# Bento Portal Redesign — Design Spec

**Date:** 2026-04-09  
**Scope:** Portal index + shared framework + issue-001 (two variants)

## Goal

Redesign the interactive pattern library portal using the Bento grid concept (Option D), update the shared interactive framework to match, and create two variants of issue-001 to A/B test implementation context depth.

## Mission Context

Help Microsoft field teams move from conceptual understanding to practical implementation of AI agent patterns. Each diagram should connect architecture to platforms, requirements, and code samples.

## Deliverables

### 1. Portal — `docs/index.html`
- Bento grid layout (12-col CSS Grid, mixed card sizes)
- All 8 issues with metadata (type, builder, tags, arc pairing)
- Issues 001-004: interactive links; 005-008: "coming soon" state
- Utility cards: Subscribe, Sample Code (`#sample-repo` placeholder), About
- Typography: Outfit (body), Sora (display), JetBrains Mono (code)
- Dark theme, glassmorphism, warm/cool gradients for practical/conceptual
- Clean directory URLs throughout
- Fully responsive (12-col → 8-col → 2-col → 1-col)
- Konami code easter egg

### 2. Shared Framework — `docs/interactive/shared/`

**interactive.css updates:**
- Bento design language: Outfit/Sora/JetBrains Mono fonts
- Updated nav bar matching portal aesthetic
- New implementation context panel (right slide-out, richer than current expand panel)
- Progress indicators for visited steps
- Warm/cool color theming for practical vs conceptual issues
- Updated mobile breakpoints

**interactive.js updates:**
- Enhanced StepEngine with implementation context panel
- Two rendering modes for the context panel: `lightweight` and `detailed`
- Mode selected via `window.interactiveConfig.contextMode`
- Progress tracking UI (visited dots get filled state)
- Keyboard shortcut for toggling context panel (Tab or `i` key)
- Updated global nav to match Bento portal design

### 3. Issue 001 — Two Variants

**Variant A — Lightweight Pointers** (`docs/interactive/issue-001/index.html`)
- `contextMode: 'lightweight'`
- Component context panels show: brief description + "Requires: [service]" + "See: [link to sample-repo]" + "Docs: [link to platform docs placeholder]"
- Minimal, scannable, gets field teams to the right resource fast

**Variant B — Detailed Specs** (`docs/interactive/issue-001-detailed/index.html`)
- `contextMode: 'detailed'`
- Component context panels show: full description + Azure service tier + estimated cost + licensing requirements + prerequisites + step-by-step setup pointers + sample code snippet preview
- Deep reference for teams doing hands-on implementation

Both variants share the same diagram HTML and step config; only the `data-context-*` attributes and `contextMode` differ.

### 4. What Stays the Same
- StepEngine core navigation (prev/next/dots/keyboard)
- `data-step` / `data-tooltip` / `data-expand-*` attribute system
- CSS-only diagram rendering (no external libraries)
- Konami code easter egg
- Zero external dependencies (static site)

## Framework Decision

**Keep vanilla JS StepEngine.** No framework change. Reasons:
- Zero dependencies = zero build step = instant deploy via GitHub Pages
- Custom HTML diagrams are the product's strength (hand-crafted, not generated)
- StepEngine's selector-based highlighting is flexible enough for all 4 current diagram topologies
- Enhancement is additive (new panel, new data attributes) not structural

## Non-Goals
- Updating issues 002-004 (follow-up after 001 is validated)
- Building a backend or adding build tooling
- Replacing diagram HTML with a rendering library
- Adding real sample code repo links (placeholder only)

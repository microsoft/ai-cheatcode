# Interactive Companion Pages

Each issue of The Cheat Code can have an interactive companion page that brings the architecture diagram to life with animated flows, hover tooltips, click-to-expand detail panels, and a step-through narrative walkthrough.

## Structure

```
interactive/
├── shared/
│   ├── interactive.css    # Bento design language: fonts, context panels, animations
│   └── interactive.js     # StepEngine, context panels, nav, Konami easter egg
├── issue-001/
│   └── index.html         # Code-First Agent Delivery
├── issue-002/
│   └── index.html         # Scoped Multi-Source Search
├── issue-003/
│   └── index.html         # Prompt-Chained Triage + Playbooks
└── issue-004/
    └── index.html         # Secure In-Boundary Processing
```

## Creating a New Interactive Page

### 1. Copy an existing issue page

```bash
mkdir interactive/issue-NNN
cp interactive/issue-001/index.html interactive/issue-NNN/index.html
```

Issue 001 is the reference implementation with the full Bento design system.

### 2. Adapt the HTML

Open the corresponding diagram source (`diagrams/issue_NNN_*.html`) and the new interactive page. Replace the diagram-specific HTML and CSS:

- **Google Fonts import**: Add import for Outfit, Sora, JetBrains Mono
- **Bento font overrides**: Map Sora to zone/section labels, Outfit to descriptions, JetBrains Mono to badges
- **`<style>` block**: Copy CSS from the diagram source file, then adjust `width: 1680px` to be responsive (`max-width: 100%`)
- **HTML structure**: Copy the diagram's `<body>` content into `<div class="diagram-canvas" id="diagram">`
- **Page header**: Include issue badge: `<span class="issue-badge">Issue #NNN · Type</span>`
- **Add `data-step="N"` attributes** to each zone/component that should be highlighted during walkthrough
- **Add `data-tooltip="..."` attributes** for hover explanations
- **Add `data-expand-title`, `data-expand-desc`, `data-expand-details`** for click-to-expand panels

### 3. Add implementation context data

Add `data-context` attributes to diagram elements. Each attribute contains a JSON object:

```json
{
  "what": "Brief description of this component's role",
  "requires": ["Service or tool needed", "Another requirement"],
  "prerequisites": ["Setup step 1", "Setup step 2"],
  "links": [
    {"label": "Display text", "url": "https://learn.microsoft.com/..."}
  ],
  "code": "# CLI command or code snippet\naz resource create ..."
}
```

The context panel renders these sections when a user clicks a component:
1. **What it is** — description
2. **What you need** — requirement pills
3. **Prerequisites** — checklist with green checkmarks
4. **Get started** — clickable links to docs
5. **Code** — terminal-style code block

Escape JSON properly in HTML attributes. Use `&#39;` for apostrophes, `&quot;` for quotes.

### 4. Define the step config

At the bottom of the page, define `window.interactiveConfig`:

```javascript
window.interactiveConfig = {
  container: '#diagram',
  contextMode: 'lightweight',
  steps: [
    {
      id: 'unique-step-id',
      title: 'Step Title',
      description: 'Narrative text explaining what happens at this step.',
      highlight: ['[data-step="1"]']
    },
    // ... more steps
  ]
};
```

### 5. Update the newsletter

Add the interactive CTA link after the diagram image in the newsletter HTML:

```html
<a href="../interactive/issue-NNN/" style="color:#6B2FA0;text-decoration:none;font-weight:600;">
  🔬 Explore this pattern interactively →
</a>
```

### 6. Update `index.html`

Add the interactive badge to the issue entry:

```html
<a class="issue-interactive" href="interactive/issue-NNN/">🔬 Interactive</a>
```

## Features

### Step-Through Walkthrough
- Bottom bar with Previous/Next buttons and step dots
- Keyboard navigation: Arrow keys, Escape to reset, Home for overview
- Narrative panel shows context for each step
- Non-highlighted zones dim to 25% opacity

### Hover Tooltips
- Add `data-tooltip="explanation text"` to any element
- Tooltip appears above the element on hover
- Max 280px wide, auto-positioned

### Click-to-Expand Detail Panel
- Add `data-expand-title`, `data-expand-desc`, `data-expand-details` attributes
- `data-expand-details` accepts JSON: `[{"heading":"Title","items":["Item 1","Item 2"]}]`
- Panel slides in from right on click
- Click overlay or × to close

### Implementation Context Panel (New)
- Set `contextMode: 'lightweight'` in the page config
- Add `data-context` JSON attributes to diagram elements
- Dark-themed slide-in panel (440px) with sections for requirements, prerequisites, links, and code
- Press `i` to toggle the panel for the last-selected component
- Falls back to legacy expand panel for elements without `data-context`

### Entrance Animations
- Elements with `data-step` attributes fade in on scroll
- Staggered timing based on step number

### Konami Code
- Type ↑↑↓↓←→←→BA on any interactive page 🎮

## Design System (Bento)

Interactive pages use the Bento design language, separate from the email newsletter's Segoe UI styling.

### Fonts (Google Fonts)
- **Sora** — zone labels, section headings, display text
- **Outfit** — component names, descriptions, body text
- **JetBrains Mono** — badges, code elements, step counters

### Page Header Pattern
```html
<a href="../../" class="back-link">← Back to patterns</a>
<span class="issue-badge">Issue #NNN · Practical</span>
<h1>Pattern Name</h1>
<p class="page-subtitle">Subtitle — Explore the pattern interactively</p>
```

### Color Coding
- Warm gradients (orange-tinted) for **Practical** issues
- Cool gradients (blue-tinted) for **Conceptual** issues
- Purple #6B2FA0 remains the primary brand accent

## Testing Locally

```bash
# Simple HTTP server from repo root
python3 -m http.server 8000
# Then open http://localhost:8000/interactive/issue-002/
```

## Technology

- **Vanilla JavaScript** — no frameworks, no npm, no build step
- **CSS animations** — `@keyframes`, transitions, zero external libraries
- **Progressive enhancement** — pages work without JS (shows static diagram)
- **Responsive** — works on desktop and mobile (unlike the 1680px static diagrams)

# Interactive Companion Pages

Each issue of The Cheat Code can have an interactive companion page that brings the architecture diagram to life with animated flows, hover tooltips, click-to-expand detail panels, and a step-through narrative walkthrough.

## Structure

```
interactive/
├── shared/
│   ├── interactive.css    # Shared styles: animations, tooltips, step bar, responsive layout
│   └── interactive.js     # Step-through engine, tooltips, expand panels, Konami easter egg
├── issue-001/
│   └── index.html         # Code-First Agent Delivery
├── issue-002/
│   └── index.html         # Scoped Multi-Source Search
└── issue-003/
    └── index.html         # Prompt-Chained Triage + Playbooks
```

## Creating a New Interactive Page

### 1. Copy an existing issue page

```bash
mkdir interactive/issue-NNN
cp interactive/issue-002/index.html interactive/issue-NNN/index.html
```

### 2. Adapt the HTML

Open the corresponding diagram source (`diagrams/issue_NNN_*.html`) and the new interactive page. Replace the diagram-specific HTML and CSS:

- **`<style>` block**: Copy CSS from the diagram source file, then adjust `width: 1680px` to be responsive (`max-width: 100%`)
- **HTML structure**: Copy the diagram's `<body>` content into `<div class="diagram-canvas" id="diagram">`
- **Add `data-step="N"` attributes** to each zone/component that should be highlighted during walkthrough
- **Add `data-tooltip="..."` attributes** for hover explanations
- **Add `data-expand-title`, `data-expand-desc`, `data-expand-details`** for click-to-expand panels

### 3. Define the step config

At the bottom of the page, define `window.interactiveConfig`:

```javascript
window.interactiveConfig = {
  container: '#diagram',
  steps: [
    {
      id: 'unique-step-id',
      title: 'Step Title',
      description: 'Narrative text explaining what happens at this step.',
      highlight: ['[data-step="1"]']  // CSS selectors for elements to highlight
    },
    // ... more steps
  ]
};
```

### 4. Update the newsletter

Add the interactive CTA link after the diagram image in the newsletter HTML:

```html
<p style="margin:8px 0 0 0;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;font-size:12px;">
  <a href="../interactive/issue-NNN/" style="color:#6B2FA0;text-decoration:none;font-weight:600;">
    🔬 Explore this pattern interactively →
  </a>
</p>
```

### 5. Update `index.html`

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

### Entrance Animations
- Elements with `data-step` attributes fade in on scroll
- Staggered timing based on step number

### Konami Code
- Type ↑↑↓↓←→←→BA on any interactive page 🎮

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

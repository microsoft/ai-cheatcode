# Portal Usability Audit Report

**Site:** https://microsoft.github.io/ai-cheatcode/  
**Date:** 2025-07-10  
**Viewports tested:** 1440×900, 1024×768, 768×1024, 480×800  
**Tool:** Playwright 1.59.1 (headless Chromium)

---

## Summary

| Category | Issues Found |
|---|---|
| JS Console Errors | 0 ✅ |
| Broken Links | 0 ✅ |
| Layout / Overflow | 3 issues |
| Contrast / Readability | 4 distinct issue classes |
| Accessibility | 0 focus-indicator issues ✅ |
| Interactive Elements | 0 ✅ |

**Overall:** The portal is structurally solid — no broken links, no JS errors, all
interactive elements have hover states, and keyboard focus indicators are present on
all tabbable elements. The issues found are **contrast/readability** and
**cosmetic overflow from decorative elements**.

---

## Issue 1: Low contrast on `.brand-sub` and footer text

**Severity:** Medium (WCAG AA failure)  
**Viewports affected:** All  
**Elements:**  
- `span.brand-sub` — "ABS Tech Strategy • AI Business Solutions"  
- Footer links (`a` — "Portal home", "Issue 001", "Issue 002", "Issue 003")  
- `p` — "Microsoft Internal • Not for external distribution"

**Measured:** color `rgb(107, 96, 128)` (`#6B6080`) on dark background → contrast ratio **3.61:1** (needs 4.5:1 for WCAG AA normal text)

**Root cause in source:**  
`docs/index.html` line 34 — `--text-muted: #6B6080;`  
Line 278 — `.brand-sub { color: var(--text-muted); }`  
Footer links and the confidentiality notice also use `var(--text-muted)`.

**Suggested fix:**  
Brighten `--text-muted` from `#6B6080` to `#9088A0` (ratio ≈ 5.1:1) or `#8A82A0` (≈ 4.7:1). This single CSS variable change fixes all affected elements at once.

```css
/* line 34 */
--text-muted: #8A82A0;  /* was #6B6080, now 4.7:1 on #0E0E1F */
```

---

## Issue 2: Low contrast on `.interactive-pill` text

**Severity:** Medium (WCAG AA failure)  
**Viewports affected:** All  
**Elements:** `span.interactive-pill` — "View interactive" pills on cards with interactive walkthroughs

**Measured:** color `rgb(155, 95, 208)` (`#9B5FD0`) on background `rgba(107, 47, 160, 0.3)` → contrast ratio **1.95:1** (needs 4.5:1)

**Root cause in source:**  
`docs/index.html` lines 520–534:
```css
.interactive-pill {
  background: rgba(107, 47, 160, 0.3);   /* line 529 */
  color: var(--purple-light);             /* line 531 — #9B5FD0 */
}
```

The semi-transparent purple background blends with the dark card behind it, creating near-same-hue foreground and background.

**Suggested fix:**  
Make the pill text brighter and increase background opacity for better contrast:

```css
.interactive-pill {
  background: rgba(107, 47, 160, 0.15);   /* reduce bg opacity */
  color: #C9A8E8;                          /* brighter purple, ~5.5:1 on dark */
}
```

---

## Issue 3: Low contrast on `.diagram-label`

**Severity:** Low (hidden by default, only visible on hover)  
**Viewports affected:** All  
**Elements:** `span.diagram-label` — "Flow", "Branch", "Pipeline", "Boundary" labels that appear on card hover

**Measured:** color `var(--text-muted)` (#6B6080) on `rgba(0, 0, 0, 0.5)` → ratio **3.61:1**

**Root cause in source:**  
`docs/index.html` lines 576–593:
```css
.diagram-label {
  background: rgba(0, 0, 0, 0.5);  /* line 588 */
  color: var(--text-muted);         /* line 590 — #6B6080 */
  opacity: 0;                       /* hidden until hover */
}
```

**Suggested fix:**  
Use a lighter color for the label text since it sits on a dark semi-transparent background:

```css
.diagram-label {
  color: var(--text-secondary);  /* #A89DC0, ratio ~5.8:1 on black overlay */
}
```

---

## Issue 4: Low contrast on `.cm` code comment text

**Severity:** Low (intentionally muted code comment styling)  
**Viewports affected:** All  
**Element:** `span.cm` — "# coming soon..." in the code sample card

**Measured:** color `#546E7A` on dark background → ratio **3.89:1** (needs 4.5:1)

**Root cause in source:**  
`docs/index.html` line 776:
```css
.code-line .cm  { color: #546E7A; }
```

**Suggested fix:**  
Brighten the comment color slightly:

```css
.code-line .cm  { color: #78909C; }  /* ratio ~5.5:1 */
```

---

## Issue 5: `.bg-mesh` decorative element extends beyond viewport

**Severity:** Low (cosmetic, no functional impact)  
**Viewports affected:** All  
**Element:** `div.bg-mesh` — the animated gradient mesh background

**Detail:** The element is intentionally sized at `200% × 200%` with `inset: -50%`, so it extends well beyond the viewport at every size. At 480px, it extends to 961px wide.

**Root cause in source:**  
`docs/index.html` lines 192–203:
```css
.bg-mesh {
  position: absolute;
  inset: -50%;
  width: 200%;
  height: 200%;
}
```

The parent `.bg-scene` (line 185) has `overflow: hidden` and `body` has `overflow-x: hidden`, so this **does not cause visible horizontal scroll**. The audit flagged it because the DOM bounding box exceeds the viewport, but it's clipped by ancestors.

**Verdict:** Not a bug — intentional design for the edge-bleed gradient effect. No fix needed.

---

## Issue 6: `.card-glow` elements extend beyond card bounds at 480px

**Severity:** Low (cosmetic, clipped by parent overflow)  
**Viewports affected:** 480×800 only  
**Elements:** `div.card-glow` — decorative blur orbs behind cards

**Detail:** Some glow orbs use negative positioning (`right: -10px`, `bottom: -30px`) and extend 5px past the viewport edge at 480px. They're clipped by the card's `overflow: hidden`.

**Root cause in source:**  
Inline styles on card glow elements, e.g. line 1307:
```html
<div class="card-glow" style="width:140px;height:120px;bottom:-30px;right:-10px;..."></div>
```

**Verdict:** No visible impact — the parent card has `overflow: hidden` (line 370). Not a functional bug.

---

## Issue 7: Hero section overlaps flagged between parent/child elements

**Severity:** None (false positive)  
**Viewports affected:** All  
**Elements:** `section.hero-section` overlapping `p.hero-kicker`, `h1.hero-headline`, `p.hero-desc`; cards overlapping `.hero-visual`

**Detail:** The overlap detector flagged parent-child and sibling relationships that are by design: the hero section is a container for its children, and `.hero-visual` is an absolutely-positioned background layer (`z-index: 0`) behind card content. These are intentional layout patterns, not bugs.

**Verdict:** Not a bug — normal CSS stacking context behavior.

---

## Issue 8: Element with `z-index: 9999` at `position: fixed`

**Severity:** None (by design)  
**Viewports affected:** All  
**Element:** `#konami-overlay` — the Konami code easter egg overlay

**Root cause in source:**  
`docs/index.html` lines 959–965:
```css
#konami-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: none;  /* hidden by default */
}
```

**Verdict:** Not a bug — this is a hidden full-screen overlay for the Konami code easter egg. The high z-index ensures it covers everything when activated. No fix needed.

---

## Positive Findings

- **✅ No JavaScript console errors** — clean execution
- **✅ All 4 links resolve successfully** — no 404s or network errors
- **✅ All interactive elements have hover states** — cards, links, pills all respond visually
- **✅ Keyboard focus indicators present** — all 10 tabbable elements show visible outline/box-shadow on focus
- **✅ No text clipping or vertical overflow** — all text content fits within containers
- **✅ No off-screen interactive elements** — all clickable items are reachable
- **✅ No horizontal scrollbar** — `overflow-x: hidden` on body works correctly
- **✅ Responsive grid adapts well** — Bento grid reorganizes cleanly across breakpoints

---

## Actionable Fixes Summary

| # | Fix | Effort | Impact |
|---|-----|--------|--------|
| 1 | Change `--text-muted` from `#6B6080` → `#8A82A0` | 1 line | Fixes contrast for brand-sub, footer links, diagram labels, confidentiality text |
| 2 | Change `.interactive-pill` color to `#C9A8E8` and reduce bg opacity | 2 lines | Fixes worst contrast violation (1.95:1 → ~5.5:1) |
| 3 | Change `.code-line .cm` from `#546E7A` → `#78909C` | 1 line | Fixes code comment contrast |

Total: **3 CSS changes, 4 lines modified** to achieve WCAG AA compliance.

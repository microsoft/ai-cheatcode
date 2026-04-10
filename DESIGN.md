# Design System — The Cheat Code (Bento)

## 1. Visual Theme & Atmosphere

The Cheat Code's interactive portal is built on a dark-mode-native canvas where content floats on near-black surfaces with glassmorphism depth. The overall impression is a sleek developer dashboard — think Linear meets Apple WWDC keynotes — where information-dense cards emerge from a deep navy void (`#0E0E1F`) through layered translucency. The name references gaming cheat codes, and the Konami code (↑↑↓↓←→←→BA) appears as a functional easter egg throughout.

The typography stack is deliberately non-generic: **Sora** for display headings (geometric, sharp), **Outfit** for body text (friendly, readable), and **JetBrains Mono** for code and technical labels (developer-native). This triple-font system creates clear visual hierarchy without weight gymnastics — each font carries its own personality.

The color system encodes meaning: **warm gradients** (orange-tinted) signal Practical/build issues, **cool gradients** (blue-tinted) signal Conceptual/architecture issues. Purple `#6B2FA0` is the brand accent, used for CTAs, active states, and the primary identity. Cards use glassmorphism — `backdrop-filter: blur(20px)` with semi-transparent white borders — creating depth through layered translucency rather than shadows.

**Key Characteristics:**
- Dark-mode-native: `#0E0E1F` deep background, `#1B1B3A` surfaces, `#252548` elevated panels
- Three-font system: Sora (display), Outfit (body), JetBrains Mono (code)
- Glassmorphism cards: `rgba(255,255,255,0.04)` background + `backdrop-filter: blur(20px)`
- Brand purple: `#6B2FA0` (primary) / `#9B5FD0` (light/interactive)
- Pattern type encoding: warm=Practical (orange `#D83B01`), cool=Conceptual (blue `#0078D4`)
- Animated gradient mesh background with grain texture overlay
- Scroll-reveal animations with staggered entrance timing
- Konami code easter egg on every page

## 2. Color Palette & Roles

### Background Surfaces
- **Navy Deep** (`#0E0E1F`): The deepest background — portal page canvas, context panel backgrounds. Near-black with a cool purple undertone.
- **Navy** (`#1B1B3A`): Navigation bar, step bar, panel surfaces. The primary dark surface.
- **Navy Light** (`#252548`): Context panels, elevated surfaces, card hover states.

### Text & Content
- **Text Primary** (`#F0EDF8`): Near-white with a lavender cast. Default text on dark surfaces.
- **Text Secondary** (`#A89DC0`): Muted lavender-gray for descriptions, metadata, body text on dark surfaces.
- **Text Muted** (`#6B6080`): Lowest contrast — timestamps, builder attributions, de-emphasized labels.
- **Muted** (`#6B6B8D`): Body text on light surfaces (diagram canvases).

### Brand & Accent
- **Purple** (`#6B2FA0`): Primary brand accent — CTAs, active nav states, step highlights, glow effects.
- **Purple Light** (`#9B5FD0`): Interactive hover states, links, badge text, gradient endpoints.
- **Purple Dark** (`#4A1F70`): Deep purple for brand card backgrounds, gradient anchors.
- **Purple Glow** (`rgba(107, 47, 160, 0.4)`): Box-shadow glow on highlighted elements.

### Semantic Colors
- **Blue** (`#0078D4`): Azure/cloud services, Conceptual issue gradients, zone borders.
- **Blue Light** (`#2899F5`): Brighter blue for Conceptual badges, gradient shimmer endpoints.
- **Green** (`#107C10`): Output/success, trust boundaries, prerequisite checkmarks, subscribe buttons.
- **Green Light** (`#13A113`): Brighter green for active states.
- **Orange** (`#D83B01`): Practical issue gradients, warning callouts, external service indicators.
- **Orange Light** (`#F25220`): Brighter orange for Practical badges.
- **Amber** (`#CA5010`): Decision gates, caution indicators.

### Glass & Border
- **Glass** (`rgba(255, 255, 255, 0.04)`): Default card background on dark surfaces.
- **Glass Hover** (`rgba(255, 255, 255, 0.07)`): Card background on hover.
- **Border** (`rgba(255, 255, 255, 0.08)`): Default card/component border on dark surfaces.
- **Border Bright** (`rgba(255, 255, 255, 0.14)`): Hover-state border, emphasized edges.

### Pattern Type Gradients
- **Practical Card** (`linear-gradient(145deg, rgba(216,59,1,0.12), rgba(107,47,160,0.08))`): Warm orange tint.
- **Conceptual Card** (`linear-gradient(145deg, rgba(0,120,212,0.12), rgba(107,47,160,0.10))`): Cool blue tint.

### Diagram Surfaces (Light Theme)
- **Background** (`#F8F8FC`): Light surface for diagram canvases (readability).
- **Card** (`#FFFFFF`): White component cards inside diagram zones.
- **Shadow** (`rgba(0,0,0,0.08)`): Subtle drop shadow on diagram elements.

## 3. Typography Rules

### Font Families
- **Display**: `'Sora', sans-serif` — geometric, sharp, used for headlines and card titles
- **Body**: `'Outfit', -apple-system, BlinkMacSystemFont, sans-serif` — friendly, readable, all body text and UI
- **Mono**: `'JetBrains Mono', monospace` — developer-native, used for badges, code, labels, counters
- **Google Fonts Import**: `Outfit:wght@300;400;500;600;700` + `Sora:wght@400;600;700;800` + `JetBrains Mono:wght@400;500;700`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Headline | Sora | clamp(38px, 5vw, 68px) | 800 | 1.05 | -2px | Portal hero, gradient shimmer text |
| Card Title (Hero) | Sora | clamp(20px, 2.5vw, 30px) | 700 | 1.2 | -0.8px | Large bento cards |
| Card Title (Large) | Sora | 18px | 700 | 1.2 | -0.4px | Medium bento cards |
| Card Title (Medium) | Sora | 15px | 700 | 1.2 | -0.3px | Standard bento cards |
| Card Title (Small) | Sora | 13px | 700 | 1.2 | -0.2px | Compact bento cards |
| Page Title | Sora | 32px | 700 | 1.2 | normal | Interactive page `h1` |
| Zone Label | Sora | 13px | 700 | 1.2 | 1.5px | Diagram zone headers, uppercase |
| Body | Outfit | 16px | 400 | 1.6 | normal | Default reading text |
| Body Large | Outfit | 16px | 400 | 1.7 | normal | Hero descriptions |
| Body Small | Outfit | 14px | 400 | 1.5 | normal | Component names |
| Body XS | Outfit | 13px | 400 | 1.6 | normal | Context panel body, narrative text |
| Body Tiny | Outfit | 12px | 400 | 1.55 | normal | Card descriptions, component descriptions |
| Caption | Outfit | 11px | 400–500 | 1.6 | normal | Builder attributions, subtitles |
| Issue Number | JetBrains Mono | 10px | 500 | 1.2 | normal | "Issue 001" labels |
| Badge | JetBrains Mono | 10px | 600 | 1.2 | 0.6px | Type badges (PRACTICAL/CONCEPTUAL) |
| Tag | JetBrains Mono | 9px | 500 | 1.2 | 0.3px | Technology tags |
| Label | JetBrains Mono | 10–11px | 500–600 | 1.2 | 0.8–1.2px | Section labels, kickers, uppercase |
| Context Label | JetBrains Mono | 10px | 600 | 1.2 | 1px | Context panel section headers, uppercase |
| Code | JetBrains Mono | 12px | 400 | 1.65 | normal | Code blocks in context panels |
| Nav Link | JetBrains Mono | 12px | 600 | 1.2 | normal | Issue navigation links |
| Step Counter | Outfit | 13px | 600 | 1.2 | normal | "Step 2 of 5" text |
| Button | Outfit | 14px | 600 | 1.2 | normal | Step bar buttons |

### Principles
- **Three fonts, three jobs**: Sora announces (display), Outfit explains (body), JetBrains Mono labels (code/badges). Never cross roles.
- **Weight restraint**: Sora uses 700–800 only. Outfit ranges 400–600. JetBrains Mono uses 400–700. No extremes.
- **Uppercase sparingly**: Only zone labels, section kickers, context panel headers, and type badges. Never body text.
- **Negative tracking at scale**: Sora headlines use -0.3px to -2px letter-spacing. Below 15px, spacing is normal.

## 4. Component Stylings

### Bento Cards (Portal)

**Base Card**
- Background: `var(--glass)` (`rgba(255,255,255,0.04)`)
- Border: `1px solid var(--border)` (`rgba(255,255,255,0.08)`)
- Radius: `var(--radius-lg)` (24px)
- Backdrop-filter: `blur(20px)`
- Transition: `transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease, border-color 0.25s ease`
- Hover: `translateY(-3px) scale(1.008)`, shadow `0 20px 60px rgba(0,0,0,0.5)`, border brightens to `var(--border-bright)`

**Practical Card** (warm gradient overlay)
- Background: `linear-gradient(145deg, rgba(216,59,1,0.12), rgba(107,47,160,0.08))`

**Conceptual Card** (cool gradient overlay)
- Background: `linear-gradient(145deg, rgba(0,120,212,0.12), rgba(107,47,160,0.10))`

**Card Glow Orb** (ambient color behind content)
- Position: absolute, border-radius 50%, filter `blur(40px)`, opacity 0.35
- Color matches card type (purple, blue, or orange tint)

### Type Badges

**Practical Badge**
- Background: `rgba(216,59,1,0.2)`, Border: `1px solid rgba(216,59,1,0.35)`, Color: `#F77050`
- Font: JetBrains Mono 10px weight 600, letter-spacing 0.6px

**Conceptual Badge**
- Background: `rgba(0,120,212,0.2)`, Border: `1px solid rgba(0,120,212,0.35)`, Color: `#5BB5FF`

### Interactive Pill (link to walkthrough)
- Background: `rgba(107,47,160,0.3)`, Border: `1px solid rgba(155,95,208,0.4)`, Color: `var(--purple-light)`
- Font: 10px weight 600, letter-spacing 0.4px, radius 100px
- Hover: background `rgba(107,47,160,0.5)`, border `rgba(155,95,208,0.7)`

### Coming Soon Chip
- Background: `rgba(255,255,255,0.07)`, Border: `1px solid rgba(255,255,255,0.1)`, Color: `var(--text-muted)`
- Includes 5px dot prefix via `::before` pseudo-element

### Technology Tags
- Font: JetBrains Mono 9px weight 500
- Background: `rgba(255,255,255,0.07)`, Border: `1px solid rgba(255,255,255,0.1)`, Color: `var(--text-secondary)`
- Radius: 4px, Padding: 2px 7px

### Navigation Bar
- Background: `linear-gradient(180deg, var(--navy), var(--navy-deep))`
- Height: 52px, position sticky, z-index 300
- Brand: Sora 17px weight 700
- Links: JetBrains Mono 12px weight 600, color `rgba(255,255,255,0.5)`
- Active link: `var(--purple)` background, white text
- Issue type badges inline: `.type-practical` (orange), `.type-conceptual` (blue)

### Step Bar (bottom walkthrough controls)
- Background: `linear-gradient(180deg, var(--navy), var(--navy-deep))`
- Height: 64px, fixed bottom, z-index 200
- Buttons: Outfit 14px weight 600, `rgba(255,255,255,0.12)` background, 8px radius
- Primary button: `var(--purple)` background, `box-shadow: 0 0 20px rgba(107,47,160,0.3)`
- Step dots: 10px circles, `rgba(255,255,255,0.2)` default, `var(--purple)` active with 1.3x scale

### Context Panel (implementation details)
- Width: 440px, slides from right, `var(--navy-light)` background
- Close button: `var(--text-muted)`, 28px
- Section label: JetBrains Mono 10px weight 600, uppercase, `var(--purple-light)`
- Body: Outfit 13px, `var(--text-secondary)`
- Requirement pills: JetBrains Mono 11px, glass background, radius 20px
- Prerequisite items: Outfit 12px, glass background + border, radius 8px, green checkmark prefix
- Links: `var(--purple-light)`, flex with arrow icon
- Code block: `var(--navy-deep)` background, traffic-light title bar (red/amber/green dots), JetBrains Mono 12px

### Diagram Components (light surface)
- Zone containers: 16px radius, 2px solid colored border, linear gradient background, `0 4px 20px` shadow
- Component cards: White `#FFFFFF`, 12px radius, `0 2px 8px rgba(0,0,0,0.06)` shadow
- Icon badges: 30px rounded squares (8px radius) with emoji, colored backgrounds
- Connection rows: `#F8F8FC` background, 10px radius, `1px solid #E8E8F0` border

## 5. Layout Principles

### Portal — Bento Grid
- Container: 1400px max-width, 24px horizontal padding
- Grid: `display: grid; grid-template-columns: repeat(12, 1fr); grid-auto-rows: 100px; gap: 14px`
- Card sizes: Hero (`span-6 row-4`), Large (`span-5 row-3`), Medium (`span-4 row-3`), Small (`span-3 row-2`), Full-width (`span-12 row-2`)
- Every row must sum to 12 columns
- Utility cards (subscribe, sample code, stats, about, brand) fill remaining grid cells

### Interactive Pages
- Content: 1200px max-width, 24px padding, 120px bottom padding (above step bar)
- Diagram canvas: white background, 16px radius, 32px internal padding, `0 4px 24px` shadow
- Narrative panel: 600px max-width, fixed above step bar, 16px radius, 4px purple top border

### Spacing Scale
- Base: 4px
- Scale: 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 40, 48, 56, 80px
- Card internal padding: 22–28px
- Grid gap: 14px
- Section vertical spacing: 32–40px

### Border Radius Scale
- Tiny (4px): Tags, small badges
- Small (8px): Buttons, icon badges, step bar buttons, component cards
- Standard (12px): Input fields, context panel sections, diagram component cards
- Medium (18px): Featured elements
- Large (24px): Bento cards, diagram canvas
- XL (32px): Large panel elements
- Pill (100px): Interactive pills, badges, subscribe buttons
- Circle (50%): Step dots, glow orbs

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Void (Level 0) | `#0E0E1F` solid | Portal page background, deepest canvas |
| Surface (Level 1) | `#1B1B3A` solid | Nav bar, step bar, panel backgrounds |
| Elevated (Level 2) | `#252548` solid or `rgba(255,255,255,0.04)` glass | Context panels, card surfaces |
| Glass (Level 2b) | `rgba(255,255,255,0.04)` + `backdrop-filter: blur(20px)` | Bento cards — translucent, layered |
| Glass Hover (Level 3) | `rgba(255,255,255,0.07)` + `blur(20px)` | Card hover state |
| Glow (Level 4) | `box-shadow: 0 0 0 4px rgba(107,47,160,0.2), 0 8px 32px rgba(107,47,160,0.15)` | Step-highlighted diagram elements |
| Float (Level 5) | `box-shadow: 0 20px 60px rgba(0,0,0,0.5)` + border brighten | Hovered bento cards |
| Ambient (Background) | Radial gradient orbs + grain SVG filter | Animated mesh behind portal content |

**Depth Philosophy**: On the dark Bento canvas, depth is communicated through opacity stepping rather than shadows. Each elevation level slightly increases the white opacity of its surface (`0.00` → `0.04` → `0.07`). Glow effects (purple `box-shadow`) replace traditional drop shadows for highlighting. The animated gradient mesh background creates atmospheric depth, while the grain texture overlay adds tactile materiality. On diagram pages, the canvas uses a contrasting light surface (`#F8F8FC` / white) for readability, with traditional shadows returning.

## 7. Do's and Don'ts

### Do
- Use Sora for all display text and card titles — it's the brand's typographic voice
- Use Outfit for all body text, descriptions, and UI labels — it's readable and friendly
- Use JetBrains Mono for all code, badges, tags, and monospace elements — it signals "developer"
- Encode pattern type in color: warm (orange-tinted) for Practical, cool (blue-tinted) for Conceptual
- Use glassmorphism (`backdrop-filter: blur(20px)` + translucent background) for cards on dark surfaces
- Keep card backgrounds translucent: `rgba(255,255,255,0.04)` — never solid colors on dark
- Use `#F0EDF8` for primary text on dark — not pure white, which is too harsh
- Apply the spring easing for card hovers: `cubic-bezier(0.34, 1.56, 0.64, 1)`
- Use glow (`box-shadow`) instead of drop shadows for highlighting on dark surfaces
- Keep diagram canvases on light backgrounds (`#F8F8FC`) for readability
- Add `data-context` JSON attributes to all interactive diagram components
- Include the Konami code easter egg on every page

### Don't
- Don't use Inter, Roboto, Arial, or system fonts — they're the generic AI aesthetic we're avoiding
- Don't use flat white cards on the dark portal — everything should be translucent glass
- Don't mix pattern type colors — a Practical card should never have blue gradient tinting
- Don't use solid colored borders on dark backgrounds — borders are semi-transparent white only
- Don't put body text in Sora or display text in Outfit — each font has one job
- Don't use uppercase on body text — only zone labels, kickers, badges, and context panel headers
- Don't skip the Google Fonts import — without it, the page falls back to system fonts and loses identity
- Don't use shadows for depth on the dark portal — use opacity stepping and glow instead
- Don't create components without hover states — every interactive element needs a visible transition
- Don't link to `.html` files — all URLs use clean directory paths

## 8. Responsive Behavior

### Breakpoints

| Name | Width | Grid | Key Changes |
|------|-------|------|-------------|
| Desktop | >1100px | 12-column | Full bento grid, all card sizes active |
| Tablet | 720–1100px | 8-column | Hero cards halve to `span-4`, medium cards `span-4` |
| Mobile | 480–720px | 2-column | All cards `span-2 row-3`, stacked layout |
| Mobile Small | <480px | 1-column | Single column, auto row heights, 180px min-height |

### Touch Targets
- Step bar buttons: 8px 20px padding minimum, 14px font
- Step dots: 10px diameter with adequate spacing (8px gap)
- Nav links: 6px 12px padding, 12px font
- Cards: full-surface clickable area
- Context panel close: 28px target area

### Collapsing Strategy
- Portal hero: `clamp(38px, 5vw, 68px)` headline scales fluidly
- Bento grid: 12-col → 8-col → 2-col → 1-col via breakpoints
- Diagram canvas: horizontal flex → vertical column at 900px
- Step dots: hidden below 600px (buttons + counter remain)
- Context panel: 440px on desktop → full-width on mobile
- Narrative panel: `max-width: 600px` → `calc(100% - 24px)` on mobile

### Image Behavior
- SVG diagram previews in cards: `opacity: 0.25` rest → `0.38` hover, `pointer-events: none`
- Card glow orbs: `filter: blur(40px)`, positioned absolutely, never clip
- Animated background mesh: fixed position, `200%` width/height, drifts via `@keyframes meshDrift`
- Grain texture: SVG filter, `opacity: 0.028`, `background-size: 200px 200px`

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: `#0E0E1F`
- Nav / Step Bar: `#1B1B3A` → `#0E0E1F` gradient
- Card Surface: `rgba(255,255,255,0.04)` with `backdrop-filter: blur(20px)`
- Card Border: `rgba(255,255,255,0.08)`
- Primary Accent: `#6B2FA0`
- Interactive Accent: `#9B5FD0`
- Heading Text: `#F0EDF8`
- Body Text: `#A89DC0`
- Muted Text: `#6B6080`
- Practical Badge: `#F77050` on `rgba(216,59,1,0.2)`
- Conceptual Badge: `#5BB5FF` on `rgba(0,120,212,0.2)`
- Success / Checkmark: `#107C10`
- Diagram Background: `#F8F8FC` (light surface)

### Example Component Prompts
- "Create a Bento card for Issue #009 (Conceptual: Adaptive Guardrails). Use `rgba(0,120,212,0.12)` → `rgba(107,47,160,0.10)` gradient, `backdrop-filter: blur(20px)`, 24px radius, `rgba(255,255,255,0.08)` border. Title in Sora 15px weight 700, `#F0EDF8`. Badge: JetBrains Mono 10px 'CONCEPTUAL' in `#5BB5FF` on `rgba(0,120,212,0.2)`. Description in Outfit 12px `#A89DC0`. Tags in JetBrains Mono 9px glass pills. Hover: `translateY(-3px) scale(1.008)` with spring easing."
- "Create a context panel section for an Azure OpenAI component. Dark panel (`#252548`), section label in JetBrains Mono 10px uppercase `#9B5FD0`. Body in Outfit 13px `#A89DC0`. Requirements as glass pills (JetBrains Mono 11px, `rgba(255,255,255,0.04)` bg, 20px radius). Prerequisites as checklist items (Outfit 12px, glass bg, 8px radius, green `#107C10` checkmark prefix). Code block: `#0E0E1F` bg, traffic-light dots, JetBrains Mono 12px."
- "Design a step bar: fixed bottom, 64px height, `#1B1B3A` → `#0E0E1F` gradient. Prev/Next buttons in Outfit 14px weight 600, `rgba(255,255,255,0.12)` bg, 8px radius. Primary button: `#6B2FA0` bg with `0 0 20px rgba(107,47,160,0.3)` glow. Step dots: 10px, `rgba(255,255,255,0.2)` default, `#6B2FA0` active at 1.3x scale. Counter in Outfit 13px weight 600."
- "Build a portal hero: `#0E0E1F` background with animated gradient mesh (radial gradients of `rgba(107,47,160,0.18)` and `rgba(0,120,212,0.12)`, drifting at 30s). Kicker: JetBrains Mono 11px uppercase `#9B5FD0` with 20px line prefix. Headline: Sora weight 800, clamp(38px,5vw,68px), -2px tracking, with gradient shimmer on accent words. Body: Outfit 16px `#A89DC0`, 560px max-width."

### Iteration Guide
1. Always load Google Fonts: Outfit (300–700), Sora (400–800), JetBrains Mono (400–700)
2. Three fonts, three jobs: Sora announces, Outfit explains, JetBrains Mono labels
3. Pattern type is color-coded: warm gradients = Practical, cool gradients = Conceptual
4. Cards are glass: translucent `rgba(255,255,255,0.04)` + `backdrop-filter: blur(20px)`, never solid
5. Depth via opacity stepping: `0.00` (void) → `0.04` (glass) → `0.07` (hover) → `0.14` (bright border)
6. Glow replaces shadow on dark: `box-shadow` with purple rgba, not black rgba
7. Spring easing for micro-interactions: `cubic-bezier(0.34, 1.56, 0.64, 1)` on card hovers
8. Diagram canvases stay light (`#F8F8FC`) for readability — dark theme applies to chrome only
9. Every interactive element needs a hover state with visible transition
10. Clean directory URLs only — never link to `.html` files

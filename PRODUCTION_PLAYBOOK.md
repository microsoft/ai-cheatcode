# The Cheat Code — Production Playbook

## How to Produce a New Issue

This is the complete process for creating new issues of The Cheat Code newsletter. Follow this playbook so you don't have to reinvent anything.

---

## Step 1: Source the Content

### Option A: Team Meeting Demo
1. Use WorkIQ to pull the transcript from the relevant **AIWF Team Meeting** (that's the meeting name in Teams)
2. Ask for the full detailed walkthrough of the demo: customer scenario, architecture, technical details, team reactions, Q&A
3. Meeting transcripts are the richest source — they capture what was actually said, not a cleaned-up summary

### Option B: 1:1 Meeting Discussion
1. Use WorkIQ to pull the transcript from a 1:1 meeting where a team member walked through their solution
2. Same approach: get customer scenario, architecture, technical details, design decisions, known issues

### What to Extract
- **Customer scenario**: What's the pain point? Who has this problem?
- **Architecture**: What was built? What services/tools were used?
- **Design decisions**: Why was it built this way? What alternatives were considered?
- **Known issues/bugs**: What didn't work? What workarounds exist?
- **Build time/delivery model**: How long did it take? Hackathon? Sprint?
- **Team reactions**: Did anyone say "I'll reuse this"? What questions came up?

---

## Step 2: Identify the Patterns

This is the most important step. **Don't just write up the agent — extract the reusable patterns.**

### The Key Question
> "If I took away the specific customer and the specific agent, what architectural or design decision here would help any CSA build faster?"

### Disaggregation Rules (learned through iteration)
- **One rich agent demo often contains 2–4 standalone patterns.** Don't jam them into one issue.
- Ask: "Does this pattern stand on its own? Can a CSA apply it to a completely different scenario?"
- If yes → it's its own issue
- If two patterns are tightly coupled (one depends on the other) → pair them in one issue
- **Not every issue needs an agent frame.** Pattern-first issues (like #005: Approval Gates) work great on their own.
- **Agent-frame issues are for the full technical walkthrough** — architecture, flow diagrams, known bugs, delivery model.

### Pattern Types We've Used
| Type | Example | When to Use |
|------|---------|-------------|
| **Delivery pattern** | Code-First Agent Delivery (#001) | How to build/ship fast |
| **Architecture pattern** | Scoped Multi-Source Search (#002) | How to design a component |
| **Orchestration pattern** | Prompt-Chained Triage (#003) | How to structure agent reasoning |
| **Security/compliance pattern** | In-Boundary Processing (#004) | How to address enterprise blockers |
| **Trust pattern** | Approval Gates (#005) | How to make AI output enterprise-ready |
| **Agent frame** | Meeting-to-Knowledge (#006) | Full solution walkthrough |
| **Knowledge pattern** | Holographic Memory (#007) | How to design cross-domain recall |

### Alternating Cadence: Conceptual → Practical

Starting with Issue #007, the series follows a two-issue arc model:

| Week | Type | Editorial Focus | Reader Outcome |
|------|------|----------------|----------------|
| **Odd** | 🧠 **Conceptual Pattern** | Names the pattern, explains *why*, frames architecture, identifies design decisions | "I understand the problem and the shape of the solution" |
| **Even** | 🔧 **Practical Build** | Shows *how* to build it in Copilot Studio, step-by-step with components | "I can land this with a customer this week" |

**Rules for the cadence:**
- Conceptual issue always drops first. Practical issue references it and links back.
- Each pair is self-contained — either issue works standalone, but together they're a complete playbook.
- The issue info bar gets a type tag: `ISSUE #007 · MAY 5 · 🧠 CONCEPTUAL PATTERN` or `ISSUE #008 · MAY 12 · 🔧 PRACTICAL BUILD`
- Practical issues intro paragraph links to the conceptual pair: *"Last issue, we named the pattern. This issue, we build it."*
- Conceptual issues use sections: Pattern Breakdown + Where This Lands + Quick Tips
- Practical issues use sections: Agent Spotlight (the build) + Pattern Breakdown (components in build order) + Try This Now

**Series roadmap and per-arc briefs are in `series_plan/`.**

---

## Step 3: Write the Issue

### Use the Template
Copy `the_cheat_code_template.html` and fill in the sections. The template has comments marking each section.

### Section-by-Section Guide

**Header:**
- Update issue number and date
- Pick a new Konami code glyph set (see Symbol Registry below)

**Intro (always include):**
- 2 paragraphs max
- Para 1: The customer problem, stated as something the CSA has heard or will hear
- Para 2: "This issue's pattern:" — one sentence naming the pattern and what it does

**Agent Spotlight (include when there's a specific agent to feature):**
- Attribution line: "Built by [Full Name] • Validated with [Customer/Context]"
- "The scenario:" — customer pain point, NOT a demo recap
- "The solution:" — what was built, in practical terms
- Optional: build time, hackathon context
- Skip this section entirely for pattern-first issues (see #005)

**Pattern Breakdown (always include — this is the core):**
- Pattern name as H3 (this is what people will remember)
- Subtitle with the key components
- "Why this matters:" — why the pattern exists, stated as a CSA problem
- Numbered design decisions or components (3-4 max)
- Key insight callout (purple box)
- Warning callout (amber box) if there are gotchas

**Quick Tips (rotating — use when you have practical implementation tips):**
- Bite-sized, immediately actionable
- Known bugs, workarounds, configuration tips
- ✓ bullets, not numbered steps

**Try This Now (rotating — use when the pattern has a clear customer landing motion):**
- Title: action-oriented ("Land This with a Customer This Week", "Add an Approval Gate to Any Agent")
- 4 numbered steps with orange circles
- Each step: bold action + explanation
- End with "The line that opens doors:" — a one-liner the CSA can use verbatim

**Where This Pattern Lands (rotating — use when vertical positioning matters):**
- Bullet list of verticals with specific use cases
- Positioning tip in amber box
- Optional: "Next issue" teaser or "Series recap" if closing a multi-issue arc

### Copy Rules (hard-won through iteration)
1. **NEVER write a demo recap.** Always lead with the customer scenario.
2. **Every section must answer:** "How does this make me faster as a CSA?"
3. **Patterns are configurable assets**, not one-off builds. Frame them that way.
4. **"Try This Now" is "land this with a customer this week"**, not "build something in your spare time."
5. **"Where This Pattern Lands" needs specific verticals** with specific use cases, not vague industry names.
6. **Include cross-references** to related issues when patterns connect (e.g., "see Issue #002 for scoped search").
7. **Always give full name attribution** to the CSA who built the solution.

---

## Step 4: Style & Format

### Layout Specs (optimized for HTML email)
- Max width: 600px (email client standard)
- Font: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- Header font: 28px bold, white on #1B1B3A background
- Body font: 15px, #444444 on #FFFFFF
- Outer background: #f4f4f4
- Card: #FFFFFF with 8px border-radius, subtle box-shadow
- Top accent bar: 6px #6B2FA0

### Color-Coded Section Borders (4px left border)
| Section | Color | Hex |
|---------|-------|-----|
| Agent Spotlight | Purple | #6B2FA0 |
| Pattern Breakdown | Blue | #0078D4 |
| Quick Tips | Green | #107C10 |
| Try This Now | Orange | #D83B01 |
| Where This Pattern Lands | Amber | #CA5010 |

### Callout Boxes
| Type | Background | Border | Text Color |
|------|-----------|--------|------------|
| Warning/Bug | #FFF8E1 | #FFE082 | #795548 |
| Insight/Tip | #F0ECF5 | none | #444444 with #6B2FA0 bold |
| Flow diagram | #F0F6FF | none | #333333 monospace |
| Positioning tip | #FFF3E0 | #FFCC80 | #5D4037 |

### Konami Code Symbol Registry
Same sequence every issue (↑↑↓↓←→←→ B A START), different glyphs:
| Issue | Glyphs | HTML Entities |
|-------|--------|---------------|
| #001 | ▲▼◄► | `&#9650; &#9660; &#9664; &#9654;` |
| #002 | ↑↓←→ | `&#8593; &#8595; &#8592; &#8594;` |
| #003 | ⇑⇓⇐⇒ | `&#8657; &#8659; &#8656; &#8658;` |
| #004 | △▽◁▷ | `&#9651; &#9661; &#9665; &#9655;` |
| #005 | ^v<> | `^ v &lt; &gt;` |
| #006 | ▴▾◂▸ | `&#9652; &#9662; &#9666; &#9656;` |
| #007 | ⬆⬇⬅➡ | `&#11014; &#11015; &#11013; &#10145;` |
| #008 | ⏶⏷⏴⏵ | `&#9206; &#9207; &#9204; &#9205;` |

Future issues: pick new Unicode arrow/triangle variants. Plenty available: ◀▶, ꜛꜜ, 🔼🔽, ⮝⮟⮜⮞, etc.

### Email Compatibility
- All CSS must be inline (email clients strip `<head>` styles)
- Use `<!--[if mso]>` conditional comments for Outlook
- Tables with `role="presentation"` for layout (not semantic tables)
- `@media (max-width: 620px)` breakpoint for mobile
- Word Online connector for Word doc creation uses Segoe UI

---

## Step 5: Generate Email Version (Embedded Diagrams)

The archive HTML (`issues/the_cheat_code_issue_NNN.html`) uses relative paths for diagrams, which work on GitHub Pages but **break in Outlook email**. Use the build script to create email-ready outputs.

### Build the email files

```bash
# Single issue
python3 scripts/build_email.py 001

# All issues
python3 scripts/build_email.py all
```

Output goes to `issues/email/` with two files per issue:
- `the_cheat_code_issue_NNN_email.html` — base64-encoded diagram (browser preview)
- `the_cheat_code_issue_NNN.eml` — CID inline attachment (open in Outlook)

### Send from the .eml file (recommended)

1. Run `python3 scripts/build_email.py NNN`
2. Double-click `issues/email/the_cheat_code_issue_NNN.eml` to open in Outlook
3. Add recipients (To/CC) and your From address
4. Verify the diagram renders inline
5. Send

The `.eml` file uses CID (Content-ID) inline attachments, which Outlook handles natively — the diagram travels with the email without relying on external URLs or base64 paste behavior.

### Alternative: paste from HTML preview

1. Open `issues/email/the_cheat_code_issue_NNN_email.html` in Chrome
2. Verify the diagram renders
3. Select All → Copy → Paste into Outlook compose
4. **Note:** Outlook may strip base64 images on paste. If the diagram is missing, use the `.eml` method above.

**Always send from the `issues/email/` outputs, never the archive version.**

### Size reference

Email versions are 380–740 KB (vs 20–32 KB archive). This is well within internal Outlook limits. Each issue contains a single diagram (270–530 KB as PNG). The `.eml` file is similar in size to the base64 HTML version.

---

## Step 6: Validate Before Sending

### Checklist
- [ ] No `PLACEHOLDER`, `TODO`, or `TBD` text remaining
- [ ] Tagline reads "Agent Patterns for Copilot Chat" (not old version)
- [ ] Full name attribution for CSA builder
- [ ] Unique Konami code glyphs (not reused from prior issue)
- [ ] Issue number and date correct
- [ ] Cross-references to related issues are accurate
- [ ] All callout boxes have appropriate styling
- [ ] File size is reasonable (18–26K typical for archive; 380–740K for email version)
- [ ] **Email version generated** (`python3 scripts/build_email.py NNN`)
- [ ] **Diagram renders in .eml preview** (double-click `.eml` to verify in Outlook)
- [ ] **Interactive page created/updated** (see Interactive Portal Page section)
- [ ] **Portal card updated** in `docs/index.html`

---

## Issue History & Attribution

| Issue | Type | Pattern | Builder | Source |
|-------|------|---------|---------|--------|
| #001 | — | Code-First Agent Delivery | Cristiano Almeida Gonçalves | AIWF Team Meeting 3/18 |
| #002 | — | Scoped Multi-Source Search | Raghav BN | 1:1 with Justin |
| #003 | — | Prompt-Chained Triage + Playbooks | Raghav BN | 1:1 with Justin |
| #004 | — | Secure In-Boundary Processing | Raghav BN | 1:1 with Justin |
| #005 | — | Human-in-the-Loop Approval Gates | Pete Puustinen | AIWF Team Meeting 3/3 |
| #006 | — | Meeting-to-Knowledge Pipeline | Pete Puustinen | AIWF Team Meeting 3/3 |
| #007 | 🧠 | Holographic Memory | Tyson Dowd | 1:1 with Justin 3/24 |
| #008 | 🔧 | Cross-Project Knowledge Agent (Copilot Studio) | Tyson Dowd | 1:1 with Justin 3/24 |
| #009 | 🧠 | Adaptive Guardrails | TBD | Series Plan |
| #010 | 🔧 | Building Adaptive Guardrails (Copilot Studio) | TBD | Series Plan |
| #011 | 🧠 | Multi-Agent Handoff | TBD | Series Plan |
| #012 | 🔧 | Building Multi-Agent Handoff (Copilot Studio) | TBD | Series Plan |
| #013 | 🧠 | Persistent Agent Memory | TBD | Series Plan |
| #014 | 🔧 | Building Persistent Memory (Copilot Studio) | TBD | Series Plan |
| #015 | 🧠 | Proactive Agent Triggers | TBD | Series Plan |
| #016 | 🔧 | Building Proactive Agents (Copilot Studio) | TBD | Series Plan |
| #017 | 🧠 | Agent Evaluation & Trust Signals | TBD | Series Plan |
| #018 | 🔧 | Building Agent Analytics (Copilot Studio) | TBD | Series Plan |
| #019 | 🧠 | Custom Connector Patterns | TBD | Series Plan |
| #020 | 🔧 | Building Custom Connectors (Copilot Studio) | TBD | Series Plan |

---

## Decision Log

### Why "Agent Patterns for Copilot Chat" (not "Agentic Patterns for CSAs")
The name "The Cheat Code" is a play on both "chat" (Copilot Chat) and "cheat" (cheat codes). The subtitle should reinforce the Copilot Chat landing goal, not just generically reference CSAs.

### Why patterns over agents
The first draft of Issue #002 was a single "Special Edition: 4 Patterns" issue covering Raghav's entire triage agent. Justin's feedback: disaggregate. The patterns are what CSAs reuse — the agent is just one implementation. This led to the 3-issue split and established the principle that one agent demo often yields multiple standalone issues.

### Why professional corporate (not retro arcade)
V1 had dark backgrounds, neon colors, pixel fonts, and full arcade theming. Justin's feedback: "This is for internal corporate communication. Needs to be professional, easy to read, easy to consume." Gaming nods were reduced to: the name, the Konami code in 8px near-invisible text, and purple as an accent color.

### Why HTML email format
The newsletter is distributed via email (Outlook). The 600px max-width, inline CSS, and mso conditionals are all email-client requirements, not style choices. If the distribution method changes (e.g., SharePoint, Teams), the layout constraints can be relaxed.

### Why human-in-the-loop got its own issue
Pete's meeting agent demo contained a universal pattern (approval gates) that applies far beyond meetings. Rather than burying it inside a meeting-specific issue, it was extracted as a standalone pattern-first issue (#005) with the meeting agent as just one example. The full agent walkthrough became #006.

### Why alternating Conceptual → Practical cadence
Starting with Issue #007, the series follows a two-issue arc model. Odd issues (🧠 Conceptual Pattern) name the pattern and explain the architecture; even issues (🔧 Practical Build) show how to build it step-by-step in Copilot Studio. This maps cleanly to Copilot Studio as the default implementation platform — giving the series a consistent landing zone for CSAs who want to act on what they learn immediately.

### Why not rebrand Issues #001–006
The alternating cadence starts at #007. Issues #001–006 are already published, distributed, and in recipients' inboxes. Retroactively adding "🧠 CONCEPTUAL" or "🔧 PRACTICAL" tags would break existing references, confuse readers, and imply a structure that wasn't there when they first read them. The retroactive classification in `series_plan/SERIES_ROADMAP.md` exists for internal planning only — it's not reader-facing. Issue #007's intro naturally introduces the cadence going forward.

### Why Issue #007 spawned the alternating cadence
Issue #007 (Holographic Memory) produced two equally strong versions from a single 1:1 with Tyson Dowd: an architectural pattern and a Copilot Studio implementation. The conceptual version became #007 (🧠 Holographic Memory), the practical version became #008 (🔧 Cross-Project Knowledge Agent). This revealed that the series naturally alternates between "why this pattern exists" and "how to build it." Formalizing this as a two-issue arc gives readers the strategic framing one week and the tactical build the next.

### Why Copilot Studio as the default practical stack
Copilot Studio + Power Automate + Azure AI Search covers the widest CSA audience. Most CSAs can build in this stack today without waiting for dev team engagement. Code-first patterns (Issue #001) remain valid but are positioned as the "advanced" path, not the default. This makes the practical issues immediately actionable for the broadest audience.

---

## Newsletter Archive

All issues are hosted on GitHub Pages for easy browsing and cross-reference linking.

- **Archive URL:** https://microsoft.github.io/ai-cheatcode/ (requires GitHub login — internal only)
- **Repo:** https://github.com/microsoft/the-cheat-code (private)
- **How to publish a new issue:** Copy the HTML + PDF to the repo, create/update the interactive page under `docs/interactive/issue-NNN/`, update the portal card in `docs/index.html`, then `git push`. GitHub Pages deploys automatically.
- **Cross-references:** All "Issue #NNN" mentions in newsletter HTML are hyperlinked to the archive. When creating new issues, link cross-references using: `<a href="https://microsoft.github.io/ai-cheatcode/the_cheat_code_issue_NNN.html" style="color:#6B2FA0;text-decoration:underline;">Issue #NNN</a>`
- **Portal landing page:** `docs/index.html` is the GitHub Pages landing page, using a Bento grid design with glassmorphism cards. Update it when adding new issues (see Interactive Portal Page section for grid layout details).
- **Interactive pages:** Each issue with an interactive companion lives at `docs/interactive/issue-NNN/index.html`. Cards on the portal link directly to these pages.

---

## Multi-Channel Distribution

The newsletter goes out through three channels each week. Here's the workflow.

### Channel 1: HTML Email (Primary)
- **When:** Monday AM
- **What:** Full HTML email with rich formatting, color-coded sections, diagrams embedded inline
- **How:** Open `issues/email/the_cheat_code_issue_NNN_email.html` in Chrome → Select All → Copy → Paste into Outlook → Send
- **Important:** Always use the `_email.html` version (diagrams embedded). The archive version uses relative paths that break in email.
- **Audience:** Direct distribution to CSA team

### Channel 2: Outlook Newsletter (Subscription + Analytics)
- **When:** Monday AM (same time as email, or replace email entirely once set up)
- **How:** Rebuild content in Outlook's Newsletter block editor (see adaptation guide below)
- **Audience:** Anyone in org who subscribes — provides discoverability and analytics

### Channel 3: Viva Engage (Discussion + Reach)
- **When:** Monday PM or Tuesday AM (after newsletter drops)
- **What:** Teaser post — NOT the full newsletter. Hook + pattern name + key insight + PDF attached + subscribe link
- **How:** Use the posts in `viva_engage_posts.txt` — one per issue, ready to paste
- **Audience:** AIWF Team community; optionally cross-post to broader CSA/AI communities

### Weekly Distribution Checklist
- [ ] Generate email version (`python3 scripts/build_email.py NNN`)
- [ ] Verify diagram renders (double-click `.eml` in Outlook)
- [ ] Create/update the interactive page (see Interactive Portal Page section)
- [ ] Update the portal card in `docs/index.html`
- [ ] Send `.eml` version via Outlook (Monday AM)
- [ ] Post Viva Engage teaser (Monday PM / Tuesday AM)
- [ ] Attach PDF to Engage post
- [ ] Tag the builder (@mention) in Engage post
- [ ] Reply to at least one comment on Engage by end of week

---

## Outlook Newsletter Production Workflow

Outlook Newsletters (New Outlook → Newsletters tab, or [outlook.office.com/newsletters](https://outlook.office.com/newsletters)) manages subscriptions, back-issue catalog, and analytics natively. Each edition is assembled from pre-rendered hi-def images plus a live footer added directly in the editor.

**Platform reference:** [learn.microsoft.com/en-us/microsoft-365-apps/outlook/manage/newsletters](https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/manage/newsletters)

### Approach: Image-First

Rather than rebuilding layout block-by-block in the section editor, we render the newsletter body as a high-definition image (1200px x 144 DPI) and insert it directly. The platform handles the header banner, subscription management, back-issue catalog, and unsubscribe footer natively.

**Assets per issue:**

| File | Description |
|---|---|
| `issues/the_cheat_code_issue_NNN_content.html` | Forked HTML — no nav, no header, no footer, interactive link removed |
| `issues/the_cheat_code_issue_NNN_content.png` | Hi-def body image (1200px @ 144 DPI) |
| `issues/the_cheat_code_issue_NNN_interactive_link.png` | Standalone interactive link button image |
| `viva_amplify/banner_header.png` | Series-level header banner (set once, reused every issue) |

### One-Time Setup

1. Open New Outlook → **Newsletters** (or [outlook.office.com/newsletters](https://outlook.office.com/newsletters))
2. Click **Create newsletter** (creates the series)
3. Title: **"The Cheat Code"**
4. Description: "Weekly agent patterns for landing agents in Copilot Chat. Built by ABS Tech Strategy."
5. Visibility: **My organization**
6. Upload `viva_amplify/banner_header.png` as the series header image
7. Enable **Subscriptions** toggle
8. Add co-owners (minimum 2 required)

### Generating Per-Issue Assets

**Step 1: Fork the HTML**

```bash
cp issues/the_cheat_code_issue_NNN.html issues/the_cheat_code_issue_NNN_content.html
```

**Step 2: Edit the fork — remove:**
- Global nav bar block
- Full header block (purple bar, title, Konami, info bar) — replace with a single 6px purple accent bar at top of main container
- Footer block
- The interactive link inline (render separately as `_interactive_link.png`)

Replace CTA copy with: *"Got an agent or pattern to share? Respond back and you may be featured in the next issue!"* (no issue-specific links)

Add a no-link team attribution footer (HR divider + "The Cheat Code" / "ABS Tech Strategy · AI Business Solutions" / "Microsoft Internal · Not for external distribution").

**Step 3: Render hi-def images**

> **Critical:** Use `--force-device-scale-factor=2` — not `--device-scale-factor`. Chrome 147+ ignores the latter in headless mode. This renders at 600px logical → 1200px physical (144 DPI).

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Main body
"$CHROME" --headless --disable-gpu --no-sandbox   --force-device-scale-factor=2   --screenshot="issues/the_cheat_code_issue_NNN_content.png"   --window-size=600,5000   "file://$PWD/issues/the_cheat_code_issue_NNN_content.html"

# Interactive link button
"$CHROME" --headless --disable-gpu --no-sandbox   --force-device-scale-factor=2   --screenshot="issues/the_cheat_code_issue_NNN_interactive_link.png"   --window-size=600,200   "file://$PWD/issues/the_cheat_code_issue_NNN_interactive_link.html"
```

Auto-crop both to content using Python (PIL) — scan from bottom for last non-background row, crop with ~40px padding, save at dpi=(144,144).

**Typical output:** body ~1200x7800-8200px, link button ~1200x128px.

### Per-Issue Assembly in Outlook Newsletters

1. Click **Create edition** under "The Cheat Code" series
2. Title: the pattern name (e.g., "Chat-First Agent Delivery")
3. **Section 1 — Body:** Insert `_content.png` as an **Images** component
4. **Section 2 — Interactive link:** Insert `_interactive_link.png` as an **Images** component → set image hyperlink to the interactive page or repo URL
5. **Section 3 — Footer** (type directly in editor, no images):
   - **The Cheat Code**
   - ABS Tech Strategy · AI Business Solutions
   - *Microsoft Internal · Not for external distribution*
   - Platform auto-appends unsubscribe and subscriber management links
6. Preview (light mode, dark mode, mobile)
7. **Send and Publish**

### What the Platform Handles Natively

- Back-issue catalog (all editions browsable by subscribers)
- Subscription management and sign-up
- Unsubscribe footer
- Delivery analytics (opens, clicks)
- Mobile-responsive layout
- Reply routing (readers reply directly to the newsletter)
---

## Viva Engage Post Guide

### Post Format
Each Engage post is a **teaser** — not the full newsletter. Structure:

```
🎮 The Cheat Code — Issue #[NNN]: [Pattern Name]

[One-sentence customer problem hook]

This week's pattern: [Pattern name] — [one-line description]
Built by: @[Full Name] · [Context]

🔑 "[Key insight quote from the issue]"

📎 Full issue attached as PDF
📬 Subscribe in Outlook Newsletters for weekly delivery

[Konami code glyphs for this issue]

💬 [Discussion question]
```

### Ready-to-Use Posts
Pre-written posts for all 6 issues are in `viva_engage_posts.txt`. Copy, paste, attach PDF, and post.

### Engage Best Practices
- **Tag the builder** — they can answer questions and share additional context
- **Ask a discussion question** — this is the whole point of the Engage cross-post
- **Reply to comments** — keep the thread alive for at least 2-3 days
- **Use Article format** for deeper posts if a teaser isn't enough
- **Schedule posts** up to 2 weeks in advance for batch planning

### Future: Viva Amplify
If Viva Amplify becomes available in your tenant, it can publish to Outlook, Teams, Viva Engage, and SharePoint simultaneously from one interface — replacing the manual cross-post workflow. Check with your admin on availability.

---

## Architecture Diagram Production Workflow

### Why HTML/CSS + Chrome Headless (Tool Decision History)
We evaluated three tools:
1. **Mermaid CLI** — Renders clean but sterile diagrams. Good for dev docs but too flat/boxy for customer-facing content. Lacks gradients, shadows, and branding flexibility. **Rejected by team lead.**
2. **Paper Banana** (paper-banana.org) — AI-powered text-to-figure. Promising quality but CLI requires a Google Gemini API key we don't have. Prompts saved in `diagrams/PAPER_BANANA_PROMPTS.md` for future web UI use.
3. **HTML/CSS + Chrome headless** ✅ — Full control over Microsoft Fluent Design branding. Editable source files, pixel-perfect renders, consistent output. **This is the production tool.**

### Overview
Each newsletter issue has a companion architecture diagram in `diagrams/`. These are rich, branded HTML/CSS renders aligned to Microsoft Fluent Design. They're embedded in the newsletter HTML and included in PDFs.

### Color System (matches newsletter)
| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Agent / Copilot zones | Purple | #6B2FA0 | Primary agent boundaries |
| Azure services | Blue | #0078D4 | Cloud services, APIs |
| Output / Trust zones | Green | #107C10 | Approved content, published outputs |
| External / Error zones | Orange | #D83B01 | External systems, warnings |
| Decision / Gate points | Amber | #CA5010 | Human approval, routing decisions |
| Component cards | White | #FFFFFF | Individual service/component boxes |
| Zone backgrounds | Linear gradients | varies | Light gradient fills inside zones |

### Visual Conventions
- **Zone containers**: Rounded 16px borders, 2px solid colored border, linear gradient background, drop shadow (0 4px 16px)
- **Component cards**: White background, 12px rounded corners, inside zone containers
- **Icon badges**: 32px rounded squares with emoji/icon, color-coded to zone
- **Flow arrows**: SVG arrows or CSS-drawn connectors between zones
- **Lock badges**: 🔒 overlay on security-scoped components
- **Typography**: Segoe UI, zone titles 18px bold, component labels 14px, captions 12px italic

### CSS Design System Reference

Use these CSS patterns when creating new diagrams. Copy from existing diagram HTML files as your starting point.

**Zone containers (colored groupings):**
```css
/* Pattern: linear-gradient background, 2px solid border, rounded corners, shadow */
.zone {
  border-radius: 16px;
  padding: 28px 24px;
  /* Per-color: */
  background: linear-gradient(135deg, #F5F0FA 0%, #EDE5F5 100%); /* purple */
  border: 2px solid #6B2FA0;
  box-shadow: 0 4px 20px rgba(107, 47, 160, 0.12);
}
/* For dashed trust/security boundaries, use: */
.zone-boundary { border: 3px dashed #107C10; }
```

**Component cards (white boxes inside zones):**
```css
.component {
  background: #FFFFFF;
  border-radius: 12px;
  padding: 16px 18px;
  margin-bottom: 14px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.08);
}
```

**Icon badges (32px colored squares with emoji):**
```css
.component-icon {
  width: 32px; height: 32px;
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px;
}
.icon-purple { background: #6B2FA0; color: white; }
.icon-blue { background: #0078D4; color: white; }
.icon-green { background: #107C10; color: white; }
```

**Connection rows (arrows between zones):**
```css
.conn-row {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 16px;
  background: #F8F8FC;
  border-radius: 10px;
  border: 1px solid #E8E8F0;
}
```

**Layout patterns used across diagrams:**
- Horizontal 3-zone (#001): Flexbox `.canvas { display: flex; gap: 48px; }`
- Vertical stacked (#002, #005): Column flow with arrow dividers
- Combined (#003): Top chain + bottom playbook architecture
- Nested boundary (#004): Dashed green outer boundary containing inner zones
- Pipeline (#006): Sequential stages with connecting arrows

### Creating a New Diagram

1. **Copy a similar existing HTML diagram** from `diagrams/` as your starting point
2. **Edit the HTML/CSS** — adjust zones, components, arrows, and labels
3. **Set the body `min-height`** to match your content (critical to avoid Chrome clipping)
4. **Test render** with Chrome headless:
   ```bash
   CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   "$CHROME" --headless --disable-gpu --no-sandbox \
     --screenshot="diagrams/issue_NNN_name_rich.png" \
     --window-size=1680,HEIGHT \
     "file://$PWD/diagrams/issue_NNN_name.html"
   ```
   Replace `HEIGHT` with your body `min-height` value.
5. **Verify the PNG** — open it, check nothing is clipped at the bottom
6. **Embed in newsletter HTML**:
   ```html
   <img src="diagrams/issue_NNN_name_rich.png" alt="[descriptive alt text]"
        style="width:100%;max-width:536px;height:auto;display:block;border-radius:6px;border:1px solid #E0E0E0;">
   ```
7. **Create/update the interactive page** using the diagram HTML (see Interactive Portal Page section)
8. **Re-render the PDF**:
   ```bash
   "$CHROME" --headless --disable-gpu --no-sandbox \
     --print-to-pdf="the_cheat_code_issue_NNN.pdf" \
     --print-to-pdf-no-header "file://$PWD/the_cheat_code_issue_NNN.html"
   ```

### Height Reference (existing diagrams)
| Issue | File | Window Height |
|-------|------|---------------|
| #001 | `issue_001_deployment.html` | 1060px |
| #002 | `issue_002_query_routing.html` | 1400px |
| #003 | `issue_003_chain_sequence.html` | 900px |
| #004 | `issue_004_trust_boundary.html` | 1500px |
| #005 | `issue_005_approval_flow.html` | 1300px |
| #006 | `issue_006_pipeline.html` | 920px |

All diagrams are 1680px wide.

### Critical Gotcha: Chrome Height Clipping
Chrome `--screenshot` captures exactly the `--window-size` height. If your HTML content is taller, the bottom gets silently clipped. **Always** set both:
- `min-height` in the body CSS
- `--window-size` height parameter

When in doubt, set it 100-200px taller than you think you need and trim later.

### Paper Banana (Alternative)
For even higher-fidelity renders, detailed prompts for all 7 diagrams are saved in `diagrams/PAPER_BANANA_PROMPTS.md`. These can be pasted into the Paper Banana web UI at paper-banana.org. The CLI version requires a Google Gemini API key (`GOOGLE_API_KEY` env var).

---

## Viva Amplify Distribution Workflow

### Overview
Viva Amplify enables one-click publishing to Outlook, SharePoint, Teams, and Viva Engage from a single authoring surface. Pre-adapted content for all 6 issues is in `viva_amplify/`.

### Files
| File | Purpose |
|---|---|
| `viva_amplify/AMPLIFY_SETUP_GUIDE.md` | Step-by-step campaign creation, channel config, template setup, scheduling, analytics |
| `viva_amplify/issue_001_amplify.md` through `issue_006_amplify.md` | Section-by-section content mapped to Amplify web parts, ready to paste into the editor |

### Quick Workflow for Each Issue
1. Open the Amplify campaign → **+ New publication** → Select custom template
2. Update **Title Area** (title, Konami glyphs in "text above title", date)
3. Paste section content from the companion `.md` file
4. Upload architecture diagram from `diagrams/` as an Image web part
5. **Preview** on all 4 channels (Outlook, SharePoint, Teams, Engage)
6. **Schedule** for Monday AM publish

### Key Constraints
- Images max 12MB (all architecture diagrams are well under this)
- Multi-column layouts collapse to single column in Outlook email
- Section backgrounds and dividers may not render in Outlook
- Always preview per channel before publishing

### Content Mapping
HTML newsletter sections → Amplify web parts:
- Agent Spotlight → Text web part (purple section background if available)
- Pattern Breakdown → Text + Image web parts
- Comparison tables → Formatted text pairs (tables break in email)
- Architecture diagrams → Image web part (full width)
- Quick Tips / Try This Now → Text web part (numbered lists)

See `AMPLIFY_SETUP_GUIDE.md` for the full setup and authoring guide.

## Interactive Portal Page

Each published issue should have an interactive companion page at `docs/interactive/issue-NNN/index.html`. These pages bring the architecture diagram to life with step-through walkthroughs and implementation context panels. The portal landing page at `docs/index.html` uses a Bento grid layout to showcase all issues.

### Design System

The portal uses the **Bento design language**, separate from the email newsletter's Segoe UI styling:

- **Fonts**: Outfit (body), Sora (display), JetBrains Mono (code) — loaded via Google Fonts
- **Theme**: Dark navy background (#0E0E1F), glassmorphism cards, purple (#6B2FA0) accents
- **Color coding**: Warm gradients for Practical issues, cool gradients for Conceptual issues

### Creating the Interactive Page

1. Copy `docs/interactive/issue-001/index.html` (reference implementation)
2. Replace diagram HTML with the new issue's architecture
3. Add Google Fonts import and Bento font overrides for diagram CSS classes
4. Add `data-context` JSON attributes to all major components with:
   - `what` — brief description
   - `requires` — array of requirements (rendered as pills)
   - `prerequisites` — array of setup steps (rendered as checklist)
   - `links` — array of `{label, url}` objects pointing to Microsoft Learn docs
   - `code` — CLI commands or code snippets
5. Set `contextMode: 'lightweight'` in `window.interactiveConfig`
6. Update page header with issue badge and back link
7. Test locally: `python3 -m http.server 8000 --directory docs`

### Article-Framing Sections (added April 2026)

Starting with Issue #005, the interactive page is wrapped with narrative sections derived from the newsletter so visitors get the *why* and *what to do next*, not just the *how*. Layout:

1. Page header (existing)
2. **`.pattern-why`** — customer hook + one-line lead + meta strip (type · builder · customer · paired build · date)
3. Interactive walkthrough (existing)
4. **`.pattern-applications`** — "Where else this lands" with a pill grid (4–5 scenarios)
5. **`.pattern-pitfall`** — one-line warning callout (amber)
6. **`.pattern-try-now`** — 4-step checklist + "line that opens doors" quote
7. **`.pattern-credits`** — attribution + links to full email write-up, related issue, paired practical issue
8. Footer (existing)

All layout primitives are defined in `docs/interactive/shared/interactive.css` under "Article-Framing Sections". See `docs/interactive/issue-005/index.html` as the reference implementation.

Required companion artifact: copy the email newsletter into `docs/issues/the_cheat_code_issue_NNN.html` and the diagram PNG into `docs/diagrams/` so the "Full email write-up" link resolves on GitHub Pages. The email file needs no edits — its relative path `../diagrams/...` resolves correctly from `docs/issues/`.

### Updating the Portal

After creating the interactive page, update `docs/index.html`:

1. Change the issue's card from `<div>` to `<a>` with `href="interactive/issue-NNN/"`
2. Add the `interactive-pill` element to the card
3. Remove the `coming-soon-chip` if present
4. If this is a new issue (not one of the existing 8), add a new card to the Bento grid with appropriate span classes

### Portal Grid Layout

The Bento grid uses 12 columns with `grid-auto-rows: 100px`. Card sizes:
- Hero (latest arc): `span-6 row-4`
- Large (with interactive): `span-5 row-3`
- Medium: `span-4 row-3`
- Small: `span-3 row-2`
- Full-width (about): `span-12 row-2`

Every row must sum to 12 columns. When adding a new card, adjust existing spans to maintain the grid.

### Pre-Publish Checklist (Interactive)

- [ ] Google Fonts import present (Outfit, Sora, JetBrains Mono)
- [ ] `contextMode: 'lightweight'` set in config
- [ ] All major components have `data-context` attributes with valid JSON
- [ ] Links use real Microsoft Learn URLs (not placeholders)
- [ ] Page header has issue badge with correct type (Practical/Conceptual)
- [ ] Footer links to `../../` (back to portal)
- [ ] Clean directory URLs (no .html extensions)
- [ ] Responsive layout works on mobile (test at 600px width)
- [ ] Portal card updated in `docs/index.html`
- [ ] Konami code works (up-up-down-down-left-right-left-right-B-A)

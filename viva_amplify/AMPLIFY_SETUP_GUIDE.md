# Viva Amplify Setup Guide — The Ch(e)at Code

> **Purpose:** Step-by-step instructions to create and manage "The Ch(e)at Code" as a Viva Amplify campaign, enabling one-click publishing to Outlook, SharePoint, Teams, and Viva Engage from a single authoring surface.

---

## Prerequisites

- Viva Amplify license enabled for your tenant
- Author permissions in Viva Amplify (Corporate Communicator role or higher)
- Access to the target distribution channels:
  - Outlook distribution list or M365 group for AIWF CSAs
  - SharePoint communication site for content archival
  - Teams channel (e.g., AIWF Team general or a dedicated channel)
  - Viva Engage community (e.g., AIWF or broader CSA community)
- Architecture diagram images uploaded to an accessible SharePoint library or ready for inline upload

---

## Step 1: Create the Campaign

1. Open **Viva Amplify** from the Microsoft 365 app launcher or navigate to `amplify.microsoft.com`
2. Click **+ New campaign**
3. Configure:
   - **Campaign name:** `The Ch(e)at Code — Agent Patterns for Copilot Chat`
   - **Description:** Weekly newsletter covering agentic patterns that CSAs can quickly land with customers. Each issue highlights a pattern, the agent behind it, and how to reuse it.
   - **Campaign goal:** Enable and inform (select the closest match from Amplify's options)
4. Click **Create**

---

## Step 2: Configure Distribution Channels

In the campaign settings, add all target channels:

### Outlook (Email)
- Click **Add channel** → **Outlook**
- Add recipients: Enter the AIWF CSA distribution list or M365 group
- Limit: Up to 200 individual addresses or groups per publication

### SharePoint
- Click **Add channel** → **SharePoint**
- Select the target communication site (e.g., AIWF Team Site or a dedicated "The Ch(e)at Code" site)
- The publication will appear as a news post on the site
- Limit: Up to 10 SharePoint sites

### Teams
- Click **Add channel** → **Teams**
- Select the AIWF Team and the target channel
- Publications appear as a card with preview text and a link
- Limit: Up to 5 Teams channels

### Viva Engage
- Click **Add channel** → **Viva Engage**
- Select the target community (or post to your Storyline)
- Limit: Up to 5 communities

---

## Step 3: Create the First Publication (Issue #001)

1. In the campaign, click **+ New publication**
2. Select the **Newsletter** template (built-in)
3. Configure the **Title Area:**
   - **Title:** `The Ch(e)at Code — Issue #001`
   - **Text above title:** `▲▲ ▼▼ ◄► ◄► B A START`
   - **Author:** Justin Preston (or the issue author)
   - **Show published date:** Yes
   - **Title image:** Upload or select a branded header image (dark navy #1B1B3A background with "The Ch(e)at Code" text and Konami code — create as a 1200×300px banner image)

> **Tip:** The header banner image should be pre-created as a 1200×300px PNG with the newsletter branding. This replaces the dark HTML header from the email version.

4. Build the publication body using the content from `issue_001_amplify.md` (see companion file)
5. Follow the section-by-section mapping below

---

## Step 4: Section-by-Section Authoring Pattern

Each issue follows this pattern in the Amplify editor:

### A. Issue Subtitle
- **Web part:** Text (Heading 2)
- **Content:** The issue subtitle (e.g., "Agent Patterns for Copilot Chat · Issue #001 · Week of March 23, 2026")
- **Formatting:** Gray text, smaller size

### B. Agent Spotlight Section
- **Web part:** Text
- **Section background:** Light purple tint (if available in your tenant's theme; otherwise, use a horizontal rule/divider above)
- **Structure:**
  1. Section header: "🎮 AGENT SPOTLIGHT" (Heading 3, bold, purple #6B2FA0)
  2. Agent title (Heading 2, bold)
  3. Builder attribution line (italic)
  4. Body paragraphs — paste directly from the companion `.md` file
  5. Bullet lists — use Amplify's native bullet formatting

### C. Pattern Breakdown Section
- **Web part:** Text + Image
- **Structure:**
  1. Section header: "🧩 PATTERN BREAKDOWN" (Heading 3, bold, blue #0078D4)
  2. Pattern title (Heading 2, bold)
  3. Pattern subtitle (gray, italic)
  4. Body paragraphs
  5. **Image web part:** Insert the architecture diagram from `diagrams/issue_NNN_xxx_rich.png`
     - Alt text: Use the descriptive alt text from the companion file
     - Size: Full width (Amplify will handle responsive scaling)
  6. Continuation text after the diagram

### D. Additional Sections (varies by issue)
- **Quick Tips** → Text web part, numbered list, green header
- **Try This Now** → Text web part, numbered steps, orange header
- **Where This Pattern Lands** → Text web part, vertical-specific positioning

### E. Dividers Between Sections
- Use the **Divider** web part between major sections
- Note: Dividers may not render in Outlook email — preview before publishing

### F. Footer
- **Web part:** Text
- **Content:** Series navigation (Previous / Next issue links), feedback link
- **Keep simple:** Plain text with hyperlinks

---

## Step 5: Save as Custom Template

After building Issue #001:

1. Click the **...** menu in the publication editor
2. Select **Save as template**
3. Name it: `The Ch(e)at Code — Weekly Issue`
4. This template will be available for all future issues, pre-loaded with:
   - The title area layout and branding
   - Section structure (Agent Spotlight → Pattern Breakdown → rotating sections → Footer)
   - Distribution channel configuration (inherited from the campaign)

For future issues: **+ New publication** → Select your custom template → Update content.

---

## Step 6: Scheduling and Workflow

### Weekly Publishing Schedule
- **Monday AM (9:00 AM local):** Publish the week's issue
- Use Amplify's **Schedule** feature: set the publish date/time when the publication is ready
- Publications can be prepared in advance and queued

### Approval Workflow (Optional)
- If your organization requires review before publishing:
  1. In campaign settings, enable **Approval workflow**
  2. Add approvers (e.g., Justin Preston or team leads)
  3. Publications go through Draft → Submitted → Approved → Scheduled/Published

### Batch Preparation
- Create all 6 issues in the campaign upfront
- Set scheduled publish dates: Mar 23, 30, Apr 6, 13, 20, 27
- Each publication auto-publishes to all configured channels at the scheduled time

---

## Step 7: Channel-Specific Preview

**Before publishing each issue, preview on every channel:**

1. Click **Preview** in the Amplify editor
2. Toggle between: Outlook / SharePoint / Teams / Viva Engage
3. Check for these known issues:

| Issue | Outlook (Email) | SharePoint | Teams | Viva Engage |
|---|---|---|---|---|
| Multi-column layouts | ❌ Collapses to single column | ✅ Full fidelity | ⚠️ Card only | ⚠️ Link only |
| Section backgrounds | ❌ Not rendered | ✅ Rendered | N/A | N/A |
| Collapsible sections | ❌ Expanded/flat | ✅ Interactive | N/A | N/A |
| Dividers | ❌ May not render | ✅ Rendered | N/A | N/A |
| Images | ✅ Inline (< 12MB) | ✅ Full size | ⚠️ Thumbnail | ⚠️ Thumbnail |
| Architecture diagrams | ✅ Inline, scaled | ✅ Full resolution | Link to view | Link to view |

---

## Step 8: Analytics and Engagement

After publishing, Amplify provides built-in analytics:

- **Reach:** How many people received/viewed the publication per channel
- **Engagement:** Clicks, time spent, reactions
- **Sentiment:** If sentiment analysis is enabled

### Recommended Tracking
- Review analytics 48 hours after each publication
- Track which issues get the most engagement to inform future content
- Use Viva Engage comments as qualitative feedback
- Share analytics summary in monthly team reviews

---

## Image Assets Needed

To fully brand the Amplify publications, prepare these images:

| Asset | Dimensions | Purpose | Status |
|---|---|---|---|
| Header banner | 1200×300px | Title area hero image (dark navy with branding) | **To create** |
| Architecture diagrams | 1680px wide (various heights) | Pattern Breakdown sections | ✅ Already in `diagrams/` |
| Section accent icons (optional) | 48×48px | Visual markers for Agent Spotlight, Pattern Breakdown, etc. | Optional |

> **Header banner tip:** Create a single reusable banner image with "The Ch(e)at Code" title and tagline on the dark navy (#1B1B3A) background. Update the Konami code glyphs per issue, or use a generic version with the series name only.

---

## Quick Reference: File Mapping

| Issue | HTML Source | Amplify Content | Architecture Diagram |
|---|---|---|---|
| #001 | `the_cheat_code_issue_001.html` | `viva_amplify/issue_001_amplify.md` | `diagrams/issue_001_deployment_rich.png` |
| #002 | `the_cheat_code_issue_002.html` | `viva_amplify/issue_002_amplify.md` | `diagrams/issue_002_query_routing_rich.png` |
| #003 | `the_cheat_code_issue_003.html` | `viva_amplify/issue_003_amplify.md` | `diagrams/issue_003_chain_sequence_rich.png` |
| #004 | `the_cheat_code_issue_004.html` | `viva_amplify/issue_004_amplify.md` | `diagrams/issue_004_trust_boundary_rich.png` |
| #005 | `the_cheat_code_issue_005.html` | `viva_amplify/issue_005_amplify.md` | `diagrams/issue_005_approval_flow_rich.png` |
| #006 | `the_cheat_code_issue_006.html` | `viva_amplify/issue_006_amplify.md` | `diagrams/issue_006_pipeline_rich.png` |

# The Cheat Code — Issue #006: Viva Amplify Version
## Meeting-to-Knowledge Pipeline

> **Publish date:** April 27, 2026
> **Konami glyphs:** ▴ ▴ ▾ ▾ ◂ ▸ ◂ ▸ B A START

---

## Title Area Configuration

| Field | Value |
|---|---|
| **Title** | The Cheat Code — Issue #006 |
| **Text above title** | ▴ ▴ ▾ ▾ ◂ ▸ ◂ ▸ B A START |
| **Author** | Justin Preston |
| **Show published date** | Yes |
| **Title image** | Branded header banner (reuse from campaign) |

---

## Section 1: Introduction

**Web part:** Text

**Content to paste:**

> **Agent Patterns for Copilot Chat · Issue #006 · Week of April 27, 2026**

Last issue, we covered the approval gate pattern. This issue, we show you the full agent that uses it. A pharma customer had 20 project managers running multiple meetings per day — and every single one required manual meeting minutes. Here's how Pete Puustinen turned that into a two-agent pipeline built in 2.5 days.

**This issue's pattern:** A meeting-to-knowledge pipeline that automatically captures transcripts, generates summaries, gates them through approval, and makes the entire history searchable for leadership.

---

## Section 2: 🎮 Agent Spotlight — The Meeting Scribe & Library Agents

**Web part:** Text
**Section background:** Light purple tint (if available)

**Content to paste:**

### 🎮 AGENT SPOTLIGHT

## The Meeting Scribe & Library Agents

*Built by Pete Puustinen · Validated with Eggis Pharma (Budapest Hackathon)*

**The scenario:** A pharmaceutical company in Budapest has 20 project managers running multiple product meetings daily. After each meeting, someone manually copies the Teams meeting minutes into a Word document, reviews it, fixes gaps, and saves it. Leadership wants to ask questions across all project meetings — but first, those minutes have to be created, verified, and stored somewhere searchable. Today, all of this is manual and inconsistent.

**The solution: Two agents, one pipeline.**

**Agent 1: The Scribe.** Connects to the meeting object, fetches the raw transcript via a custom connector, saves the transcript as an immutable backup to a SharePoint library, then generates structured meeting minutes as a Word document. The document is routed to the project owner for approval.

**Agent 2: The Library.** Once a summary is approved, a Power Automate flow copies it to Azure Blob Storage and indexes it in Azure AI Search. The Library Agent queries this index, giving leadership a natural-language interface to ask questions across all project meetings.

**Build time:** 2.5 days at a customer hackathon in Budapest, with a train-the-trainer session the day before. This was the most complex scenario across 10–11 customers at the hackathon — and it shipped working.

---

## Section 3: Divider

**Web part:** Divider

---

## Section 4: 🧩 Pattern Breakdown — Meeting-to-Knowledge Pipeline

**Web part:** Text + Image

**Content to paste:**

### 🧩 PATTERN BREAKDOWN

## Meeting-to-Knowledge Pipeline

*Copilot Studio + Power Automate + custom connector + Azure AI Search*

**End-to-End Flow:**

1. Meeting ends in Teams
2. Scribe Agent triggered → decodes base64 meeting chat ID
3. Custom connector → join URL → meeting ID → transcript ID
4. Raw transcript (WebVTT) saved to SharePoint Library A
5. AI generates meeting minutes → Word doc via Word Online connector
6. Doc saved to OneDrive → copied to SharePoint Library B
7. Project owner reviews & approves (Issue #005 pattern)
8. Approved doc → Azure Blob Storage → Azure AI Search index
9. Library Agent answers leadership questions over indexed docs

**⬇️ INSERT IMAGE WEB PART HERE ⬇️**

| Field | Value |
|---|---|
| **Image file** | `diagrams/issue_006_pipeline_rich.png` |
| **Alt text** | Meeting-to-Knowledge Pipeline: Scribe Agent fetches Teams transcript via Graph API, generates structured Word summary, routes for human approval; Library Agent indexes approved docs in Azure AI Search for leadership queries via Copilot Chat |
| **Size** | Full width |

*Caption: Full pipeline: Scribe Agent → approval gate → Library Agent with Azure AI Search*

**Key architecture decisions:**

**1. Custom connector for transcript access.** The customer doesn't have Frontier enabled, so the team built a custom connector that calls Graph API to retrieve the raw transcript. This involves decoding a base64 meeting chat ID, resolving the join URL, fetching the meeting ID, then the transcript ID, then the raw WebVTT content. It's the most complex part of the build — but once it exists, it's reusable for any meeting intelligence scenario.

**2. Save-then-reference (token limit workaround).** Raw transcripts from one-hour meetings exceed AI prompt token limits. The team initially tried passing transcripts directly but hit limits. The fix: save the transcript to SharePoint, then pass a *link* to the file instead of the file contents. The sub-agent reads from the link.

**3. Two SharePoint libraries, not one.** Raw transcripts go to Library A (immutable, archival). Generated summaries go to Library B (editable, approvable). Clean separation means originals can never be accidentally modified.

**4. The agent is simple; the flow is complex.** As Pete put it: "The agent itself is actually simple. All the magic happens in the agent flow." The intelligence is in the Power Automate orchestration — the Copilot Studio agent is a thin interface on top. This is an important design insight: keep the conversational layer lean and push business logic into deterministic flows.

> **Looking ahead:** Pete has already tested MCP servers that can retrieve transcripts directly — which would eliminate the need for the custom connector entirely. Once Frontier moves to GA, this simplifies significantly. Build with the connector today; plan for MCP tomorrow.

> ⚠️ **Known bug:** Text files (.txt, .vtt) currently can't be passed as attachments to AI prompts due to a parsing bug. Workaround: pass a link to the file instead. The sub-agent reads the content from the link. This is a known issue — flag it early with customers so it doesn't derail a demo.

---

## Section 5: Divider

**Web part:** Divider

---

## Section 6: 🛠 Try This Now — Pitch the Hackathon, Not Just the Agent

**Web part:** Text

**Content to paste:**

### 🛠 TRY THIS NOW

## Pitch the Hackathon, Not Just the Agent

1. **Find the meeting-heavy team.** Every customer has a group that runs 5–10+ recurring project meetings per week and drowns in documentation. Product management, R&D, clinical ops, and PMOs are the usual suspects. Ask: "How long after a meeting are searchable, approved minutes available to leadership?"

2. **Propose a 2–3 day hackathon.** This solution was built at a customer hackathon — not as a long consulting engagement. Position it as a joint build where the customer walks away with a working prototype and ownership of the solution. This shifts the dynamic from "vendor demo" to "we built this together."

3. **Day 0: Train-the-trainer.** Run a prep session the day before the hackathon. Brainstorm the customer's specific meeting types, what a good summary looks like for them, and who the approvers should be. This is where you tailor the pattern to their process.

4. **Layer on the patterns.** Start with the Scribe Agent (generation + approval gate from Issue #005). If time allows, add the Library Agent (Azure AI Search) on Day 2. The customer gets immediate value from the scribe alone — the library is the multiplier.

> 💡 **The line that opens doors:** "What if every meeting your team runs this week was automatically documented, approved by the project owner, and searchable by leadership by end of day — and we could build that together in two days?"

---

## Section 7: Divider

**Web part:** Divider

---

## Section 8: 🏆 Where This Pattern Lands

**Web part:** Text

**Content to paste:**

### 🏆 WHERE THIS PATTERN LANDS

- **Pharmaceuticals & life sciences** — product development meetings, clinical trial reviews, regulatory documentation
- **Professional services** — client engagement meetings, project status reviews, partner coordination
- **Manufacturing** — production planning, quality reviews, supplier coordination
- **Education** — faculty meetings, academic committee discussions, board records
- **Any organization** where leadership needs cross-project visibility without attending every meeting

**Positioning tip:** Lead with the PMO (Program Management Office) persona. They're drowning in meeting follow-ups and are often the internal champion for Teams adoption. They'll pull leadership into the conversation once they see the Library Agent in action.

---

## Section 9: Footer

**Web part:** Text

**Content to paste:**

---

**Got an agent or pattern to share?** Reply to this email and you might be featured in a future issue.

*The Cheat Code · AIWF Team · AI Business Solutions*
*Questions or ideas for the next issue? Reply to this email.*

*Microsoft Internal · Not for external distribution*

---

## Channel Preview Notes

| Channel | What to check |
|---|---|
| **Outlook** | This is the longest issue — the 4 architecture decisions section is substantial. Verify it doesn't get truncated in email clients with message size limits. The 9-step pipeline list should render cleanly as a numbered list. |
| **SharePoint** | Full fidelity. This is the most technical issue — excellent reference for CSAs preparing hackathons. |
| **Teams** | Card preview — "A pharma customer had 20 project managers" is a strong hook for preview text. |
| **Viva Engage** | Discussion question: "Have you pitched or run a customer hackathon? What worked, what would you do differently? Drop your experience below." |

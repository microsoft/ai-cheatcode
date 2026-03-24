# The Ch(e)at Code — Issue #004: Viva Amplify Version
## Secure In-Boundary Processing

> **Publish date:** April 13, 2026
> **Konami glyphs:** △ △ ▽ ▽ ◁ ▷ ◁ ▷ B A START

---

## Title Area Configuration

| Field | Value |
|---|---|
| **Title** | The Ch(e)at Code — Issue #004 |
| **Text above title** | △ △ ▽ ▽ ◁ ▷ ◁ ▷ B A START |
| **Author** | Justin Preston |
| **Show published date** | Yes |
| **Title image** | Branded header banner (reuse from campaign) |

---

## Section 1: Introduction

**Web part:** Text

**Content to paste:**

> **Agent Patterns for Copilot Chat · Issue #004 · Week of April 13, 2026**

You've heard this from a customer: "We can't use AI — our data can't leave our tenant." Legal, healthcare, financial services, government — the objection is real, and it kills deals.

**This issue's pattern:** How to build agents that process sensitive data without any of it leaving the Microsoft boundary. This is the architecture that turns "we can't" into "show me how."

---

## Section 2: 🎮 Agent Spotlight — The Work Item Triage Agent (continued)

**Web part:** Text
**Section background:** Light purple tint (if available)

**Content to paste:**

### 🎮 AGENT SPOTLIGHT

## The Work Item Triage Agent (continued)

*Built by Raghav BN · Part 3 of 3 from this agent*

**The scenario:** Work items often contain sensitive information — customer names, account details, PII from escalations, internal security incidents. The triage agent needs to read, search, and reason over this data. But it also can't export it to any external service, store it persistently outside authorized systems, or create new data exfiltration surfaces.

Raghav's agent solves this by using MCP (Model Context Protocol) connectors to access Azure DevOps and M365 data within the Microsoft boundary, processing everything in-memory, and using Work IQ as an in-boundary reasoning engine. No data leaves. No new storage surfaces. The agent reads, reasons, and recommends — all within the tenant.

---

## Section 3: Divider

**Web part:** Divider

---

## Section 4: 🧩 Pattern Breakdown — Secure In-Boundary Processing

**Web part:** Text + Image

**Content to paste:**

### 🧩 PATTERN BREAKDOWN

## Secure In-Boundary Processing

*MCP connectors + in-memory aggregation + tenant-scoped auth*

**Why this matters:** Most agent architectures involve moving data somewhere for processing — an external LLM, a vector database, a processing pipeline. For customers with sensitive data, each hop is a compliance risk. The question isn't "can AI help?" — it's "can AI help *without creating new risk?*"

**The architecture has four principles:**

1. **MCP over REST APIs.** Model Context Protocol provides structured, authenticated access to data sources like Azure DevOps. It's built for compliance — unlike raw REST calls that require custom auth and audit logic.

2. **In-memory aggregation.** The agent assembles context at runtime — it doesn't write sensitive data to new databases or file systems. When the task is complete, the aggregated context is gone.

3. **Tenant-scoped authentication.** The agent authenticates via Azure CLI within the customer's tenant. It can only access what the authenticated user can access — no privilege escalation.

4. **In-boundary reasoning.** Work IQ handles search and LLM reasoning within the Microsoft boundary. Data is processed in-context, not exported to third-party models.

> ⚠️ **Watch for this:** During development, local logging can inadvertently capture PII from work items or search results. Before any customer-facing deployment, audit logging practices to ensure sensitive data isn't being written to local files or dev consoles.

**⬇️ INSERT IMAGE WEB PART HERE ⬇️**

| Field | Value |
|---|---|
| **Image file** | `diagrams/issue_004_trust_boundary_rich.png` |
| **Alt text** | Secure In-Boundary Processing architecture: Customer tenant boundary containing Copilot Chat, Declarative Agent, MCP Connectors (ADO, Graph, SharePoint), In-Memory Aggregation, and Tenant-Scoped Azure OpenAI — data never leaves the boundary |
| **Size** | Full width |

*Caption: Secure In-Boundary Processing — every component stays within the customer tenant*

> **Key insight:** This isn't just about security — it's about removing the biggest objection to AI adoption in regulated industries. When you can demonstrate that zero data leaves the tenant, the conversation shifts from "can we?" to "where do we start?"

---

## Section 5: Divider

**Web part:** Divider

---

## Section 6: 🛠 Try This Now — Turn "We Can't Use AI" into a Deal

**Web part:** Text

**Content to paste:**

### 🛠 TRY THIS NOW

## Turn "We Can't Use AI" into a Deal

1. **Identify the blocked account.** Which customer has said "our data can't leave" or "we're not allowed to use AI for this"? Legal, healthcare, financial services, and government accounts almost always have this objection.

2. **Understand the specific concern.** Is it data residency? Third-party model access? Persistent storage of sensitive data? PII in logs? Each concern maps to a specific architecture principle above.

3. **Walk through the architecture.** Show them the four principles: MCP access, in-memory processing, tenant-scoped auth, in-boundary reasoning. For each one, explain how it addresses their specific concern.

4. **Combine with prior patterns.** Once the security objection is removed, you can layer on scoped search (Issue #002) and prompt-chained triage (Issue #003) to build a complete agent solution. The in-boundary architecture is the foundation that makes everything else possible for these customers.

> 💡 **The line that opens doors:** "What if I showed you an agent that can read your sensitive data, reason over it, and recommend actions — without any of that data ever leaving your Microsoft tenant? No third-party models. No new data stores. No exfiltration surface."

---

## Section 7: Divider

**Web part:** Divider

---

## Section 8: 🏆 Where This Pattern Lands

**Web part:** Text

**Content to paste:**

### 🏆 WHERE THIS PATTERN LANDS

- **Financial services** — trade surveillance, compliance monitoring, client communication review
- **Healthcare** — patient record analysis, clinical documentation, claims processing
- **Government** — citizen services, case management, benefits adjudication
- **Legal** — case data (including sensitive domestic/criminal matters), privileged communications
- **Any regulated industry** where "data can't leave" has been the blocker to AI adoption

**Series recap:** Over the last 3 issues, we've covered the full stack from Raghav's triage agent — scoped search for quality, prompt chaining + playbooks for process automation, and in-boundary architecture for compliance. Together, these patterns let you pitch: "An agent that triages your intake queue, finds the right context, follows your team's process, and keeps all data in your tenant."

---

## Section 9: Footer

**Web part:** Text

**Content to paste:**

---

**Got an agent or pattern to share?** Reply to this email and you might be featured in Issue #005.

*The Ch(e)at Code · AIWF Team · AI Business Solutions*
*Questions or ideas for the next issue? Reply to this email.*

*Microsoft Internal · Not for external distribution*

---

## Channel Preview Notes

| Channel | What to check |
|---|---|
| **Outlook** | The 4-principle numbered list is the core content — verify it renders cleanly as single-column. Warning callout box may lose its background styling. |
| **SharePoint** | Full fidelity. This is a high-value reference page for regulated industry CSAs. |
| **Teams** | Card preview — the "we can't use AI" hook should appear in the preview text. |
| **Viva Engage** | Discussion question: "Which accounts have you unblocked (or want to unblock) with an in-boundary architecture argument? Share the industry and the objection." |

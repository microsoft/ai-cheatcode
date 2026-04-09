# Issue #002 — Outlook Newsletter Edition
## Scoped Multi-Source Search

> **Edition title:** Scoped Multi-Source Search
> **Series:** The Cheat Code
> **Schedule date:** March 30, 2026

---

## Series Header Image

Upload the branded banner (704px wide, 16:9 ratio) with:
- Title: The Cheat Code
- Subtitle: Agent Patterns for Copilot Chat
- Konami glyphs: ↑ ↑ ↓ ↓ ← → ← → B A START

---

## Section 1: Introduction

### Component: Text & Image (text only)

**ISSUE #002 · MARCH 30, 2026 · WEEKLY**

If your customer has deployed Copilot or any RAG-based agent and the results feel shallow or noisy, this issue is for you. The problem isn't usually the model — it's that the search is too broad.

**This issue's pattern:** How to make agent search dramatically better by scoping it to specific, known-relevant sources instead of searching everything.

---

## Section 2: Agent Spotlight

### Component 1: People

| Field | Value |
|---|---|
| **Name** | Raghav BN |
| **Title/Role** | CSA · Validated on live ADO work items |

### Component 2: Text & Image (text only)

### 🎮 Agent Spotlight: The Work Item Triage Agent

**The scenario:** Your team receives work items that need to be classified, cross-referenced against historical context, and routed. The triage person spends most of their time not on the item itself but on searching for related information — digging through Teams channels, past tickets, office hours notes, field readiness threads. That search step is where scoped search changes everything.

Raghav built an agent that reads an ADO work item and automatically searches across M365 sources to surface related context. The critical design choice: the agent doesn't search broadly. It first analyzes the work item, then generates targeted queries aimed at specific, known-relevant sources. The result: 80+ precise historical matches on a live Excel Copilot issue — context that would have taken a human 30 minutes to find manually.

---

## Section 3: Pattern Breakdown

### Component 1: Text & Image

### 🧩 Pattern Breakdown: Scoped Multi-Source Search

*Stop searching everything. Search the right things.*

**Why broad search fails:** When an agent searches "everything for anything related," it returns hundreds of results, most irrelevant. The model wastes tokens processing noise, and the output quality drops. This is the #1 complaint CSAs hear about RAG implementations: "Copilot found the wrong stuff."

**The fix is a two-step process:** First, analyze the input to understand what you're looking for. Then generate targeted search queries aimed at specific, known-relevant sources. The search is narrow by design.

**❌ BROAD RAG:**
"Search all documents for anything about Excel Copilot accuracy"
→ Hundreds of results, most irrelevant

**✅ SCOPED SEARCH:**
"Search #copilot-feedback for Excel calculation errors after March 2026"
→ 12 highly relevant threads

**The two-step approach:**

1. Analyze the input → extract key entities + intent
2. Generate scoped queries → target specific sources
3. Search only those sources → high-relevance results

### Component 2: Images

Upload: `diagrams/issue_002_query_routing_rich.png`

| Field | Value |
|---|---|
| **Alt text** | Scoped Multi-Source Search architecture: Query Analyzer routes intent to ADO, Graph API, and SharePoint with targeted queries, then merges and ranks results for Copilot Chat |

### Component 3: Text & Image (text only)

**What "scoping" actually means:**

- **Source scoping** — search a specific Teams channel, not all of Teams
- **Time scoping** — search items from the last 90 days, not all time
- **Entity scoping** — search for the specific product, feature, or error type mentioned in the input
- **Role scoping** — search conversations from people who would know about this topic

### Component 4: Styled Quote

💜 **Key insight:** The first step in better search isn't improving the search engine. It's improving the *query*. When the agent analyzes the input before searching, the queries it generates are dramatically more precise than anything a human would type.

---

## Section 4: Try This Now

### Component 1: Text & Image (text only)

### 🔧 Try This Now: Fix a Customer's Noisy Search in One Conversation

1. **Identify the complaint.** "Copilot isn't finding the right information" or "search results aren't relevant" — these are scoped search problems in disguise.

2. **Map the sources.** Ask: "When your best person handles this task, where do they actually look?" Write down the 3–5 specific sources. Those are your scoping targets.

3. **Add the analysis step.** Before the agent searches, it should first read the input and extract key entities, time ranges, and context. This turns a vague user question into a precise, multi-faceted query.

4. **Test the difference.** Run the same question through broad search and scoped search side by side. The quality gap is immediately obvious — and it's the best demo you can give.

### Component 2: Styled Quote

💡 **Positioning:** "The model isn't the problem — the search is. Let me show you what happens when we point the agent at the right sources instead of everything."

---

## Section 5: Where This Pattern Lands

### Component: Text & Image (text only)

### 🏆 Where This Pattern Lands

- **Any Copilot deployment** where users say "it doesn't find the right stuff"
- **Customer support** — search known KB articles and past tickets, not the whole SharePoint
- **Sales intelligence** — search CRM notes for a specific account, not all accounts
- **Compliance** — search relevant policy docs for a specific regulation, not the entire library
- **Engineering** — search incident history for a specific service, not all incidents

**Bottom line:** This pattern applies to every RAG-based agent you'll encounter. If the customer is unhappy with search quality, this is your first move. It's also the foundation for the more advanced triage patterns we'll cover in Issue #003.

---

## Section 6: Footer / CTA

### Component: Text & Image (text only)

**Next issue:** Prompt-Chained Triage + Playbook Orchestration — How to automate any read-classify-route workflow with configurable YAML playbooks.

📦 Code sample: [github.com/microsoft/the-cheat-code/samples/issue-002](https://github.com/microsoft/the-cheat-code/tree/main/samples/issue-002)

Browse all issues: [aka.ms/the-cheat-code](https://aka.ms/the-cheat-code)

*ABS Tech Strategy · AI Business Solutions*

---

## Outlook Newsletter Editor Checklist

- [ ] Edition created under "The Cheat Code" series
- [ ] Edition title: "Scoped Multi-Source Search"
- [ ] Header image shows branded banner with Konami glyphs (↑↓←→)
- [ ] 6 sections added in order (Intro → Spotlight → Pattern → Try This → Lands → Footer)
- [ ] **People** component used for Raghav BN attribution
- [ ] Architecture diagram uploaded via Insert → Pictures
- [ ] **Styled Quote** components for key insight and positioning callouts
- [ ] Broad vs Scoped comparison reads well as sequential text (no side-by-side columns)
- [ ] All hyperlinks working (aka.ms/the-cheat-code, code sample link)
- [ ] Previewed in light mode, dark mode, and mobile
- [ ] Recipients/subscribers configured
- [ ] Scheduled for Monday AM, March 30

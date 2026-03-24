# The Ch(e)at Code — Series Roadmap

## Cadence: Conceptual → Practical (Alternating Weeks)

Each topic gets a two-issue arc:

- **Odd issues (🧠 Conceptual Pattern)**: Names the pattern, explains *why* it exists, frames the architecture, identifies the design decisions. Reader walks away thinking: "Now I understand the problem and the shape of the solution."
- **Even issues (🔧 Practical Build)**: Shows *how* to build it in Copilot Studio with specific components, step-by-step. Reader walks away thinking: "I can land this with a customer this week."

The conceptual issue always drops first. The practical issue references it and links back. Each pair is self-contained — you can read either one standalone, but together they're a complete playbook.

---

## Published Issues (Retroactive Classification)

| Issue | Title | Type | Pair |
|-------|-------|------|------|
| #001 | Code-First Agent Delivery | 🔧 Practical | Standalone (delivery pattern) |
| #002 | Scoped Multi-Source Search | 🧠 Conceptual | → #003 |
| #003 | Prompt-Chained Triage + Playbooks | 🔧 Practical | ← #002 |
| #004 | Secure In-Boundary Processing | 🧠 Conceptual | Standalone (foundational) |
| #005 | Human-in-the-Loop Approval Gates | 🧠 Conceptual | → #006 |
| #006 | Meeting-to-Knowledge Pipeline | 🔧 Practical | ← #005 |
| #007 | Holographic Memory | 🧠 Conceptual | → #007 Alt |
| #007 Alt | Cross-Project Knowledge Agent | 🔧 Practical | ← #007 |

---

## Planned Issues: Season 2

### Arc 1: Adaptive Guardrails (#008–#009)

**Customer pain:** Static prompt-based guardrails break when context changes. A rule that works for HR queries blocks legitimate finance queries. Customers need safety boundaries that adapt to the conversation, not hardcoded blocklists.

| Issue | Type | Title | Stack |
|-------|------|-------|-------|
| **#008** | 🧠 Conceptual | **Adaptive Guardrails** | Pattern theory |
| **#009** | 🔧 Practical | **Building Adaptive Guardrails in Copilot Studio** | Copilot Studio + AI Builder classifier + conditional topics + Power Automate escalation |

**#008 — Conceptual: Adaptive Guardrails**
- Why static prompt rules fail at scale
- Three types of guardrails: input filtering, output validation, contextual gates
- The "confidence threshold" pattern: let the agent assess its own uncertainty and escalate
- Design decision: guardrails as topics vs. guardrails as plugins vs. guardrails as external classifiers
- Cross-reference: Issue #005 (Approval Gates) as the human fallback when guardrails trigger

**#009 — Practical: Building Adaptive Guardrails in Copilot Studio**
- Component 1: AI Builder custom model trained on the customer's sensitive/non-sensitive query pairs
- Component 2: Copilot Studio topic that calls the classifier before routing to generative answers
- Component 3: Conditional branching — low-risk queries get instant answers, medium-risk get caveated answers, high-risk route to human via Power Automate approval (Issue #005 pattern)
- Component 4: Feedback loop — Power Automate logs every classification for model retraining
- Try This Now: Build a 3-tier topic router with a mock classifier in one afternoon

---

### Arc 2: Multi-Agent Handoff (#010–#011)

**Customer pain:** One agent can't do everything. The HR agent shouldn't answer IT questions. But when a user asks an HR agent about laptop provisioning for a new hire, the agent should seamlessly hand off to the IT agent — with full conversation context, not "please go talk to the other bot."

| Issue | Type | Title | Stack |
|-------|------|-------|-------|
| **#010** | 🧠 Conceptual | **Multi-Agent Handoff** | Pattern theory |
| **#011** | 🔧 Practical | **Building Multi-Agent Handoff in Copilot Studio** | Copilot Studio agent transfer + plugin actions + Dataverse shared context |

**#010 — Conceptual: Multi-Agent Handoff**
- When to split vs. when to keep one agent (the "cognitive load" test)
- The context transfer problem: what does Agent B need to know about Agent A's conversation?
- Three handoff patterns: cold transfer (restart), warm transfer (summary), hot transfer (full context)
- Trust boundaries: should Agent B trust Agent A's classification? What if Agent A was wrong?
- Design decision: shared memory (Dataverse) vs. inline context (conversation variable) vs. external orchestrator

**#011 — Practical: Building Multi-Agent Handoff in Copilot Studio**
- Component 1: Two Copilot Studio agents with distinct knowledge scopes (HR + IT)
- Component 2: Intent classifier topic in each agent — detects "this isn't my domain" and triggers handoff
- Component 3: Copilot Studio "Transfer to agent" action with conversation summary passed as context variable
- Component 4: Dataverse table for shared session state (user ID, conversation history, handoff reason)
- Component 5: Power Automate flow for handoff logging and analytics
- Try This Now: Build a two-agent HR/IT handoff demo with Dataverse context passing

---

### Arc 3: Persistent Agent Memory (#012–#013)

**Customer pain:** Every conversation starts from zero. The agent helped a user configure their project last Tuesday — but today it has no memory of that interaction. Users repeat themselves constantly. Agents can't learn from past interactions to improve future ones.

| Issue | Type | Title | Stack |
|-------|------|-------|-------|
| **#012** | 🧠 Conceptual | **Persistent Agent Memory** | Pattern theory |
| **#013** | 🔧 Practical | **Building Persistent Memory in Copilot Studio** | Copilot Studio + Dataverse + Power Automate + Azure OpenAI |

**#012 — Conceptual: Persistent Agent Memory**
- Three memory tiers: conversation (built-in), session (cross-turn), long-term (cross-session)
- The summarization trap: why naive "save the conversation" doesn't scale
- Structured memory: key-value facts vs. episodic memories vs. preference profiles
- Privacy and retention: what should agents remember vs. forget? Data lifecycle considerations
- Cross-reference: Issue #007 (Holographic Memory) as the knowledge-layer equivalent

**#013 — Practical: Building Persistent Memory in Copilot Studio**
- Component 1: Dataverse table — `AgentMemory` with fields: user_id, memory_type (fact/preference/episode), key, value, created_at, expires_at
- Component 2: "Remember this" plugin action — Power Automate flow that extracts key facts from conversation and writes to Dataverse
- Component 3: "Recall" topic — on conversation start, query Dataverse for user's stored facts and inject into system prompt as context
- Component 4: Memory hygiene — scheduled Power Automate flow that prunes expired memories, summarizes old episodes
- Try This Now: Build a "preferences" memory that remembers a user's project, role, and communication style across sessions

---

### Arc 4: Proactive Agent Triggers (#014–#015)

**Customer pain:** Every agent today is reactive — it waits for the user to ask. But the most valuable agent behavior is proactive: "Your compliance certification expires in 14 days," "Three open items from last week's meeting haven't been addressed," "This month's spend is tracking 20% over budget."

| Issue | Type | Title | Stack |
|-------|------|-------|-------|
| **#014** | 🧠 Conceptual | **Proactive Agent Triggers** | Pattern theory |
| **#015** | 🔧 Practical | **Building Proactive Agents with Copilot Studio** | Copilot Studio + Power Automate scheduled/event flows + Teams Adaptive Cards |

**#014 — Conceptual: Proactive Agent Triggers**
- Reactive vs. proactive: the value inversion (proactive agents save 10x the time because users don't have to remember to ask)
- Three trigger types: scheduled (daily/weekly checks), event-driven (data change), threshold (metric crosses boundary)
- The notification problem: how to be helpful without being annoying — frequency, severity, channel
- Design decision: push (Teams message) vs. pull (dashboard) vs. ambient (Viva Insights card)
- Cross-reference: Issue #006 (Meeting-to-Knowledge) as an event-driven trigger example

**#015 — Practical: Building Proactive Agents with Copilot Studio**
- Component 1: Power Automate scheduled flow — runs daily, queries Dataverse/SharePoint for actionable conditions
- Component 2: Azure OpenAI call — generates natural-language alert summary from raw data
- Component 3: Teams Adaptive Card — sent via Power Automate with action buttons (Acknowledge, Snooze, Open Agent)
- Component 4: Copilot Studio plugin action — "Show me my alerts" surfaces proactive findings in conversation
- Component 5: Severity routing — critical alerts → Teams chat, informational → digest email, low → agent memory for next conversation
- Try This Now: Build a "weekly project health check" that scans SharePoint for overdue items and sends a Teams card

---

### Arc 5: Agent Evaluation & Trust Signals (#016–#017)

**Customer pain:** "How do I know the agent is actually working?" Leadership approved the pilot, it's been running for three weeks, and nobody can answer whether it's helping or hallucinating. No metrics, no regression detection, no confidence visibility.

| Issue | Type | Title | Stack |
|-------|------|-------|-------|
| **#016** | 🧠 Conceptual | **Agent Evaluation & Trust Signals** | Pattern theory |
| **#017** | 🔧 Practical | **Building Agent Analytics in Copilot Studio** | Copilot Studio analytics + Application Insights + Power BI + Power Automate |

**#016 — Conceptual: Agent Evaluation & Trust Signals**
- Three evaluation layers: usage metrics (are people using it?), quality metrics (are answers good?), business metrics (is it saving time?)
- The hallucination detection problem: confidence scoring, source grounding, citation verification
- Regression detection: how to catch "the agent got worse after we added new knowledge"
- Trust signals for end users: showing confidence, citing sources, flagging uncertainty
- Cross-reference: Issue #005 (Approval Gates) as the human-in-the-loop quality check

**#017 — Practical: Building Agent Analytics in Copilot Studio**
- Component 1: Copilot Studio built-in analytics — session completion rate, topic triggering, escalation rate
- Component 2: Application Insights custom telemetry — log every generative answer with confidence score, sources used, response latency
- Component 3: Power BI dashboard — daily active users, satisfaction trends, top unanswered questions, regression alerts
- Component 4: Power Automate alert — "confidence score dropped below threshold for 3 consecutive days" → Teams notification to agent owner
- Component 5: User feedback loop — thumbs up/down in Adaptive Card, logged to Dataverse, surfaced in Power BI
- Try This Now: Add Application Insights to any existing Copilot Studio agent and build a 3-chart Power BI dashboard in one session

---

### Arc 6: Custom Connector Patterns (#018–#019)

**Customer pain:** The agent needs to call an internal API — a legacy ERP, a custom CRM, a proprietary compliance system. There's no pre-built connector. Graph API doesn't cover it. The customer is stuck.

| Issue | Type | Title | Stack |
|-------|------|-------|-------|
| **#018** | 🧠 Conceptual | **Custom Connector Patterns** | Pattern theory |
| **#019** | 🔧 Practical | **Building Custom Connectors for Copilot Studio** | Copilot Studio + Custom connectors + Power Automate + Azure API Management |

**#018 — Conceptual: Custom Connector Patterns**
- When you need a custom connector vs. when a plugin action with Power Automate is enough
- The OpenAPI specification: the contract between your agent and the API
- Authentication patterns: API key, OAuth 2.0, managed identity, certificate-based
- Error handling and resilience: what happens when the API is slow, down, or returns garbage?
- Cross-reference: Issue #006 (Meeting-to-Knowledge) used a custom connector for Teams transcript access

**#019 — Practical: Building Custom Connectors for Copilot Studio**
- Component 1: Write the OpenAPI spec — minimum viable definition with one GET and one POST operation
- Component 2: Create the custom connector in Power Platform — import OpenAPI, configure auth, test
- Component 3: Expose as a Copilot Studio plugin action — map input/output parameters, add natural-language descriptions
- Component 4: Azure API Management as a gateway — rate limiting, caching, retry policies, monitoring
- Component 5: Error handling topic — when the connector fails, the agent explains and offers alternatives instead of crashing
- Try This Now: Wrap any internal REST API in a custom connector and expose it as a Copilot Studio action in one afternoon

---

## Series-Level Cross-References

The arcs interconnect. Here's the dependency map:

```
#002 Scoped Search ────────────────────────────────────┐
#004 In-Boundary ──────────────────────┐               │
#005 Approval Gates ───┐               │               │
                       ↓               ↓               ↓
#006 Meeting Pipeline  #008 Guardrails #007 Holographic Memory
                       ↓                               ↓
                       #010 Multi-Agent Handoff         #012 Persistent Memory
                       ↓                               ↓
                       #014 Proactive Triggers          #016 Evaluation & Trust
                                                       ↓
                       #018 Custom Connectors ──────────┘
```

Every practical issue should reference at least one prior conceptual issue. Every conceptual issue should name at least one customer scenario where the pattern applies.

---

## Konami Code Assignments (Planned)

| Issue | Glyphs | HTML Entities |
|-------|--------|---------------|
| #008 | ⏶⏷⏴⏵ | `&#9206; &#9207; &#9204; &#9205;` |
| #009 | ◀▶▲▼ | `&#9664; &#9654; &#9650; &#9660;` (reversed sequence) |
| #010 | ⮝⮟⮜⮞ | `&#11165; &#11167; &#11164; &#11166;` |
| #011 | ↟↡↞↠ | `&#8607; &#8609; &#8606; &#8608;` |
| #012 | ⇧⇩⇦⇨ | `&#8679; &#8681; &#8678; &#8680;` |
| #013 | ⤊⤋⬱⇻ | `&#10378; &#10379; &#11185; &#8827;` |
| #014 | ⬆⬇⬅➡ | Reassign — #007 used these |
| #015 | ꜛꜜ‹› | `&#42779; &#42780; &#8249; &#8250;` |
| #016 | ▵▿◃▹ | `&#9653; &#9663; &#9667; &#9657;` |
| #017 | ⏫⏬⏪⏩ | `&#9195; &#9196; &#9194; &#9193;` |
| #018 | ↑↓←→ | Reassign — #002 used these |
| #019 | ⥣⥥⥢⥤ | `&#10595; &#10597; &#10594; &#10596;` |

Note: Verify uniqueness against Symbol Registry in PRODUCTION_PLAYBOOK.md before publishing.

---

## Editorial Calendar Template

| Week | Date | Issue | Type | Title | Builder | Status |
|------|------|-------|------|-------|---------|--------|
| 1 | Mar 23 | #001 | 🔧 | Code-First Agent Delivery | Cristiano | ✅ Published |
| 2 | Mar 31 | #002 | 🧠 | Scoped Multi-Source Search | Raghav | ✅ Published |
| 3 | Apr 7 | #003 | 🔧 | Prompt-Chained Triage | Raghav | ✅ Published |
| 4 | Apr 14 | #004 | 🧠 | Secure In-Boundary Processing | Raghav | ✅ Published |
| 5 | Apr 21 | #005 | 🧠 | Approval Gates | Pete | ✅ Published |
| 6 | Apr 28 | #006 | 🔧 | Meeting-to-Knowledge Pipeline | Pete | ✅ Published |
| 7 | May 5 | #007 | 🧠 | Holographic Memory | Tyson | 📝 Draft |
| 8 | May 12 | #007 Alt | 🔧 | Cross-Project Knowledge Agent | Tyson | 📝 Draft |
| 9 | May 19 | #008 | 🧠 | Adaptive Guardrails | TBD | 🔲 Planned |
| 10 | May 26 | #009 | 🔧 | Building Adaptive Guardrails | TBD | 🔲 Planned |
| 11 | Jun 2 | #010 | 🧠 | Multi-Agent Handoff | TBD | 🔲 Planned |
| 12 | Jun 9 | #011 | 🔧 | Building Multi-Agent Handoff | TBD | 🔲 Planned |
| 13 | Jun 16 | #012 | 🧠 | Persistent Agent Memory | TBD | 🔲 Planned |
| 14 | Jun 23 | #013 | 🔧 | Building Persistent Memory | TBD | 🔲 Planned |
| 15 | Jun 30 | #014 | 🧠 | Proactive Agent Triggers | TBD | 🔲 Planned |
| 16 | Jul 7 | #015 | 🔧 | Building Proactive Agents | TBD | 🔲 Planned |
| 17 | Jul 14 | #016 | 🧠 | Agent Evaluation & Trust | TBD | 🔲 Planned |
| 18 | Jul 21 | #017 | 🔧 | Building Agent Analytics | TBD | 🔲 Planned |
| 19 | Jul 28 | #018 | 🧠 | Custom Connector Patterns | TBD | 🔲 Planned |
| 20 | Aug 4 | #019 | 🔧 | Building Custom Connectors | TBD | 🔲 Planned |

Builder assignments are TBD — source from team meetings and 1:1s as demos surface.

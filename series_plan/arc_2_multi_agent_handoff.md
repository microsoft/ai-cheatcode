# Arc 2: Multi-Agent Handoff (#010–#011)

## Customer Pain
One agent can't do everything. The HR agent shouldn't answer IT questions. But when a user asks the HR agent about laptop provisioning for a new hire, the agent should hand off seamlessly — with context, not "please go talk to the other bot."

## Why This Matters for CSAs
Customers start with one agent, prove value, then want five more. The moment they have two agents, they hit the handoff problem. This is the #1 blocker to multi-agent deployment at enterprise scale. CSAs who can solve this own the expansion conversation.

---

## Issue #010 — 🧠 Conceptual: Multi-Agent Handoff

### Key Sections

**The Cognitive Load Test**
- When to split: agent scope exceeds ~3 knowledge domains or the system prompt exceeds ~2000 tokens of instruction
- When to keep one: domains overlap significantly, users can't predict which agent to ask
- The "receptionist" pattern: one front-door agent that routes to specialists

**Three Handoff Patterns**
1. **Cold transfer** — restart conversation with new agent. User repeats context. Simple but terrible UX.
2. **Warm transfer** — Agent A generates a conversation summary, passes it to Agent B as context. Agent B picks up mid-stride. Good UX, moderate complexity.
3. **Hot transfer** — shared memory store. Both agents read/write to the same session state. Seamless but architecturally complex.

**Trust Boundaries**
- Should Agent B trust Agent A's intent classification?
- What if Agent A misrouted? How does Agent B detect and recover?
- Authentication context: does the user need to re-authenticate with Agent B?

**Design Decision: Where to Store Shared Context**
- Conversation variables (lightweight, ephemeral)
- Dataverse session table (persistent, queryable)
- External orchestrator (Azure Bot Framework Composer, API-based)

---

## Issue #011 — 🔧 Practical: Building Multi-Agent Handoff in Copilot Studio

### Build Components

**Component 1: Two Agents with Distinct Scopes**
- Agent A: HR Knowledge Agent (PTO, benefits, onboarding)
- Agent B: IT Support Agent (devices, access, software)
- Each has its own knowledge sources, topics, and system prompt
- Key: each agent's system prompt includes "If the user asks about [other domain], do not attempt to answer — trigger the handoff topic"

**Component 2: Out-of-Scope Detection Topic**
- In each agent: a fallback topic that fires when generative answers return low confidence
- Uses a Power Automate flow to classify: "Is this query about HR or IT?"
- If the query belongs to the other agent → trigger handoff

**Component 3: Copilot Studio Agent Transfer**
- Use the "Transfer to agent" system topic
- Before transfer: generate a conversation summary via Azure OpenAI ("Summarize this conversation in 3 sentences, including the user's original question and what's been discussed so far")
- Pass summary as a context variable to the receiving agent

**Component 4: Dataverse Session State**
- Table: `AgentSession` — session_id, user_id, source_agent, target_agent, summary, handoff_reason, timestamp
- On handoff: write session record
- On receive: receiving agent's greeting topic queries Dataverse for the session and injects context
- Enables analytics: which handoffs happen most? Which are misroutes?

**Component 5: Handoff Analytics**
- Power Automate logs every transfer
- Power BI dashboard: handoff volume, round-trip (user bounced back), resolution rate per agent
- Alert: "HR→IT handoff rate spiked 40% this week" → might indicate a knowledge gap in HR agent

### Try This Now
- Title: "Build a Two-Agent Handoff in One Session"
- Step 1: Clone an existing agent, split the knowledge sources between two agents
- Step 2: Add a fallback topic to each that detects out-of-scope queries
- Step 3: Configure agent transfer with conversation summary passing
- Step 4: Test by asking Agent A a question that belongs to Agent B — verify context carries over
- The line: "What if your employees could ask any agent any question and always get routed to the right one — without restarting the conversation?"

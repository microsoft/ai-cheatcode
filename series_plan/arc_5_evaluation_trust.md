# Arc 5: Agent Evaluation & Trust Signals (#016–#017)

## Customer Pain
"How do I know the agent is actually working?" The pilot shipped three weeks ago. Leadership wants ROI numbers. The agent owner wants quality metrics. Users want confidence signals. Nobody has any of these.

## Why This Matters for CSAs
Every pilot has a "prove it" moment at 30 days. Without evaluation infrastructure, the conversation becomes anecdotal: "Some people like it, some don't." This pattern gives CSAs the toolkit to turn anecdotes into dashboards — and dashboards into expansion funding.

---

## Issue #016 — 🧠 Conceptual: Agent Evaluation & Trust Signals

### Key Sections

**Three Evaluation Layers**
1. **Usage metrics** — Are people using it? Sessions/day, returning users, topic trigger rates, drop-off points. Answers: "Is the agent being adopted?"
2. **Quality metrics** — Are the answers good? Confidence scores, source grounding rates, hallucination detection, user thumbs-up/down. Answers: "Is the agent trustworthy?"
3. **Business metrics** — Is it saving time/money? Tasks automated, escalations avoided, time-to-resolution compared to pre-agent baseline. Answers: "Is the agent worth the investment?"

**The Hallucination Detection Problem**
- Confidence scoring: agent self-reports certainty (unreliable alone, useful as a signal)
- Source grounding: did the answer cite a real document? Is the citation accurate?
- Citation verification: automated check that the cited passage actually supports the claim
- Human spot-check: random sample of responses reviewed by SME (Issue #005 pattern applied to evaluation)

**Regression Detection**
- The "new knowledge" trap: adding documents to the knowledge source can degrade existing answers
- Pattern: golden test set — 20 known-good question-answer pairs, run weekly, alert on drift
- Metrics: answer similarity score vs. baseline, confidence score trends, topic mismatch rate

**Trust Signals for End Users**
- Show confidence: "I'm 85% confident based on 3 sources"
- Cite sources: link to the actual document, not just name it
- Flag uncertainty: "I found partial information but couldn't fully answer — here's what I know and what's missing"
- These aren't just nice-to-have — they're the difference between users trusting the agent and users Googling instead

---

## Issue #017 — 🔧 Practical: Building Agent Analytics in Copilot Studio

### Build Components

**Component 1: Copilot Studio Built-In Analytics**
- Session completion rate, engagement rate, topic triggering heatmap, escalation rate
- Available out-of-the-box — just enable and review
- Key metric to watch: "Resolution rate" — sessions that ended without escalation

**Component 2: Application Insights Custom Telemetry**
- Connect Copilot Studio to Application Insights (built-in integration)
- Add custom events via Power Automate:
  - On every generative answer: log `confidence_score`, `sources_used[]`, `response_length`, `topic_triggered`
  - On every user feedback: log `feedback_type` (thumbs up/down), `session_id`, `query_text`
  - On every escalation: log `escalation_reason`, `last_agent_response`
- KQL queries for: average confidence over time, low-confidence query patterns, feedback trends

**Component 3: Power BI Dashboard (3 Charts)**
- Chart 1: Daily active users + sessions (line chart, 30-day trend)
- Chart 2: Confidence score distribution (histogram, bucketed by topic)
- Chart 3: User satisfaction (thumbs up/down ratio, rolling 7-day average)
- Data source: Application Insights via KQL connector
- Refresh: daily automatic

**Component 4: Regression Alert Flow**
- Golden test set: 20 question-answer pairs stored in a SharePoint list
- Weekly Power Automate flow: sends each question to the agent via HTTP, compares response to expected answer using Azure OpenAI similarity scoring
- If similarity drops below threshold → Teams alert to agent owner: "3 of 20 golden test answers degraded this week — review recent knowledge changes"

**Component 5: User Feedback Capture**
- Adaptive Card at end of agent response: "Was this helpful? 👍 👎"
- Power Automate logs to Dataverse: `UserFeedback` table
- Weekly digest: Top 5 negative-feedback queries → review and improve
- Optional: "Tell me more" follow-up on 👎 → captures qualitative feedback

### Try This Now
- Title: "Add Analytics to Any Agent in One Session"
- Step 1: Enable Application Insights in your Copilot Studio agent (Settings → Advanced)
- Step 2: Add a thumbs-up/down Adaptive Card after generative answers
- Step 3: Build 3 KQL queries in Application Insights: sessions/day, avg confidence, feedback ratio
- Step 4: Pin them to a Power BI dashboard and share with the agent owner
- The line: "Right now, can you tell me how many people used your agent yesterday and whether the answers were good? This dashboard answers both in real-time."

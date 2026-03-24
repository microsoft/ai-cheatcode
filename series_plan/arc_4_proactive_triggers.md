# Arc 4: Proactive Agent Triggers (#014–#015)

## Customer Pain
Every agent waits for the user to ask. The most valuable agent behavior is proactive: alerting users to deadlines, surfacing anomalies, and nudging action before problems escalate. Today, users have to remember to ask — and they don't.

## Why This Matters for CSAs
Proactive agents are the strongest expansion play. The customer already has a reactive agent. This pattern turns it into an always-on assistant that delivers value even when no one is in the chat window. It's the difference between a search bar and a co-worker.

---

## Issue #014 — 🧠 Conceptual: Proactive Agent Triggers

### Key Sections

**The Value Inversion**
- Reactive agents save time when users ask. Proactive agents save time because users *don't have to ask*.
- Proactive value is 10x reactive: catching a missed deadline before it's missed, flagging a budget overrun before month-end, surfacing a compliance gap before the auditor finds it.

**Three Trigger Types**
1. **Scheduled** — runs on a cadence (daily standup summary, weekly project health check, monthly compliance scan)
2. **Event-driven** — fires when data changes (new document uploaded, status field changed, approval completed)
3. **Threshold** — activates when a metric crosses a boundary (spend > 80% of budget, overdue items > 5, SLA response time > 24 hours)

**The Notification Problem**
- Too many alerts → notification fatigue → users ignore everything
- Too few → users don't see value → agent gets turned off
- Design principle: severity-based routing, user-controlled frequency, snooze/dismiss capability

**Channel Strategy**
- Push (Teams message): high-urgency, needs immediate attention
- Digest (email summary): informational, weekly cadence
- Ambient (Viva Insights card): awareness, no action required
- Conversational (surfaced in next chat): low-priority, mentioned when the user next engages

---

## Issue #015 — 🔧 Practical: Building Proactive Agents with Copilot Studio

### Build Components

**Component 1: Scheduled Scan Flow (Power Automate)**
- Recurrence trigger: daily at 8 AM user's local time
- Queries: SharePoint for overdue tasks, Dataverse for stale records, Planner for upcoming deadlines
- Collects all actionable items into a JSON array
- Passes to Azure OpenAI for natural-language summary generation

**Component 2: Alert Classification**
- Azure OpenAI call classifies each finding by severity:
  - 🔴 Critical: "Compliance cert expires tomorrow" → immediate Teams message
  - 🟡 Warning: "3 items overdue by 2+ days" → include in daily digest
  - 🟢 Info: "New document uploaded to Project X" → mention in next conversation
- Classification prompt: "Rate each item as critical, warning, or info based on time sensitivity and business impact."

**Component 3: Teams Adaptive Card Delivery**
- Power Automate sends Adaptive Cards to Teams
- Card includes: alert title, severity badge, one-sentence summary, action buttons
- Actions: "Open in SharePoint" / "Snooze 24h" / "Ask the Agent" (deep-links to Copilot Studio agent)
- Critical alerts: sent immediately. Warnings: batched into daily digest card at 8 AM.

**Component 4: "Show My Alerts" Plugin Action**
- Copilot Studio plugin that queries the alert log in Dataverse
- When user opens the agent: "You have 2 unacknowledged alerts from yesterday. Want me to walk through them?"
- Combines proactive findings with reactive conversation naturally

**Component 5: Snooze and Feedback Loop**
- Dataverse table: `ProactiveAlerts` — alert_id, user_id, severity, content, status (pending/acknowledged/snoozed/dismissed), created_at
- "Snooze" button writes back to Dataverse, reschedules a follow-up flow
- "Dismissed" items feed back into classification tuning: "User dismissed 5 'info' alerts this week → reduce info alert frequency"

### Try This Now
- Title: "Build a Weekly Health Check That Sends Itself"
- Step 1: Pick one SharePoint list with a due date column (tasks, issues, anything)
- Step 2: Build a Power Automate flow that runs weekly, finds overdue items, calls Azure OpenAI to summarize
- Step 3: Send an Adaptive Card to a Teams channel with the summary and action buttons
- Step 4: Add a "Show my alerts" topic in your existing Copilot Studio agent
- The line: "What if your team got a personalized project health check every Monday morning — without anyone having to ask for it?"

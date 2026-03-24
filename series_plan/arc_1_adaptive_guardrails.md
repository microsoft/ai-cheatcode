# Arc 1: Adaptive Guardrails (#008–#009)

## Customer Pain
Static prompt-based guardrails break when context changes. A rule that works for HR queries ("don't discuss salaries") blocks legitimate finance queries ("what's the salary budget for Q3?"). Customers need safety boundaries that understand context, not hardcoded blocklists.

## Why This Matters for CSAs
Every enterprise deployment hits this wall within the first month. The agent works great in demos, then gets deployed and either over-blocks (users complain it's useless) or under-blocks (security team shuts it down). This pattern gives CSAs a framework for building guardrails that scale.

---

## Issue #008 — 🧠 Conceptual: Adaptive Guardrails

### Core Argument
Guardrails aren't a single feature — they're a three-layer system that needs to adapt based on context, user role, and query intent.

### Key Sections

**Pattern Breakdown: Three Guardrail Layers**
1. **Input filtering** — Classify the incoming query before the agent processes it. Is it in-scope? Is it sensitive? Does it require elevated authorization?
2. **Output validation** — After the agent generates a response, check it before showing the user. Does it contain PII? Does it reference restricted documents? Does it exceed the agent's confidence threshold?
3. **Contextual gates** — Mid-conversation checks that adapt based on what's been discussed. If the user shifted from general questions to specific employee data, escalate the guardrail level dynamically.

**Design Decisions**
- Static rules vs. classifier-based vs. LLM-as-judge
- Where to put the guardrail: in the prompt, in a topic, in a plugin, or in an external service
- The confidence threshold pattern: agent self-assesses uncertainty and routes accordingly
- Graceful degradation: when a guardrail triggers, what does the user see? (Not "I can't help with that")

**Callout Boxes**
- Insight: "The best guardrail is invisible when it's not needed and unmissable when it is."
- Warning: "Don't build guardrails in the system prompt alone — prompt injection can bypass them. Use architectural guardrails (topic routing, external classifiers) as your primary defense."
- Cross-reference: Issue #005 (Approval Gates) as the human fallback layer

**Where This Lands**
- Financial services — investment advice boundaries, client data access control
- Healthcare — clinical vs. administrative query separation, HIPAA-sensitive content
- Government — classification-level-aware responses, FOIA boundary compliance
- HR/People — salary, performance review, disciplinary information boundaries

---

## Issue #009 — 🔧 Practical: Building Adaptive Guardrails in Copilot Studio

### Build Components (in order)

**Component 1: AI Builder Intent Classifier**
- Train a custom classification model on the customer's query categories
- Categories: `general` (no guardrails), `sensitive` (caveated response), `restricted` (human escalation)
- Training data: 50–100 example queries per category (use Copilot Chat to generate synthetic examples)
- Output: confidence score per category

**Component 2: Classifier Topic in Copilot Studio**
- Entry point for all user queries before generative answers
- Calls AI Builder model via Power Automate
- Branches based on classification:
  - `general` → route to generative answers (standard knowledge source)
  - `sensitive` → route to generative answers + append caveat message ("This response may require verification from [department]")
  - `restricted` → route to escalation topic (no AI answer, direct to human)

**Component 3: Output Validation Flow**
- Power Automate flow triggered after generative answer is produced
- Calls Azure OpenAI with validation prompt: "Does this response contain PII, salary information, or restricted content? Respond YES/NO with explanation."
- If YES → replace response with safe alternative + log the incident
- If NO → pass through

**Component 4: Feedback & Retraining Loop**
- Log every classification decision to Dataverse: query, classification, confidence, user feedback (thumbs up/down)
- Monthly Power Automate flow exports low-confidence classifications for model retraining
- Dashboard in Power BI shows guardrail trigger rates, false positive rates, escalation volume

### Try This Now
- Title: "Add a Safety Layer to Any Existing Agent"
- Step 1: Export 50 real user queries from your agent's analytics
- Step 2: Manually label them as general/sensitive/restricted
- Step 3: Train an AI Builder model (takes ~30 minutes)
- Step 4: Add a pre-routing topic that calls the model before generative answers
- The line: "What if your agent could tell the difference between 'What's the PTO policy?' and 'What's John's salary?' — and handle each one appropriately, automatically?"

### Known Limitations
- AI Builder custom models require Power Apps/Power Automate premium licenses
- Classification latency adds 1–2 seconds to response time
- Output validation doubles the Azure OpenAI cost (two calls per response)
- Workaround for cost: only validate `sensitive` classifications, skip validation for `general`

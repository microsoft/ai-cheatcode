# Arc 3: Persistent Agent Memory (#012–#013)

## Customer Pain
Every conversation starts from zero. The agent helped a user configure their project last Tuesday — but today it has no memory. Users repeat themselves constantly. The agent can't learn preferences, track ongoing issues, or build on past interactions.

## Why This Matters for CSAs
Memory is the gap between "chatbot" and "assistant." Without it, agents are stateless tools. With it, they become personal. This is the feature that makes users say "I can't go back." Land this and the agent becomes sticky.

---

## Issue #012 — 🧠 Conceptual: Persistent Agent Memory

### Key Sections

**Three Memory Tiers**
1. **Conversation memory** (built-in) — what was said in this session. Copilot Studio handles this natively.
2. **Session memory** (cross-turn) — facts established during a conversation that should persist until the task is done. Example: "The user is configuring Project Falcon."
3. **Long-term memory** (cross-session) — preferences, past decisions, recurring requests. Example: "This user always wants answers in bullet points and prefers PowerShell over CLI."

**The Summarization Trap**
- Naive approach: save the full conversation transcript → retrieve it next time
- Why it fails: transcripts are noisy, token-heavy, and full of irrelevant turns
- Better approach: extract structured facts, not raw text. Memory should be key-value pairs, not paragraphs.

**Memory Types**
- **Facts**: "User's project is Falcon" / "User prefers dark mode" — stable, rarely change
- **Preferences**: "Summarize in bullets" / "Skip the intro" — evolve over time
- **Episodes**: "On March 12 we debugged the auth timeout together" — historical, may expire

**Privacy and Retention**
- What should agents remember? What should they forget?
- GDPR/data residency: memory stored in Dataverse inherits the tenant's data policies
- User control: "Forget everything about me" as an explicit agent action

---

## Issue #013 — 🔧 Practical: Building Persistent Memory in Copilot Studio

### Build Components

**Component 1: Dataverse Memory Table**
- Table: `AgentMemory`
- Fields: `user_id`, `memory_type` (fact/preference/episode), `key`, `value`, `confidence`, `created_at`, `updated_at`, `expires_at`
- Index on `user_id` + `memory_type` for fast retrieval
- Row-level security: users can only see their own memories

**Component 2: "Remember This" Plugin Action**
- Power Automate flow exposed as a Copilot Studio plugin
- Triggered when the agent detects a preference or fact worth saving
- Input: extracted fact (key-value pair) from the conversation
- Action: upsert into Dataverse (update if key exists, insert if new)
- System prompt instruction: "When the user states a preference or shares a fact about their work, call the Remember action to save it for future conversations."

**Component 3: "Recall" Greeting Topic**
- On every conversation start: Power Automate queries Dataverse for user's stored memories
- Returns top 10 most recent/relevant facts as a JSON array
- Injected into the system prompt as context: "Known facts about this user: [list]"
- Agent greets with context: "Welcome back! Last time we were working on Project Falcon — want to pick up where we left off?"

**Component 4: Memory Hygiene**
- Scheduled Power Automate flow (weekly):
  - Delete memories past `expires_at`
  - Summarize episodes older than 30 days into single-sentence summaries
  - Flag memories with low confidence for review
- User action: "Forget everything about me" → deletes all rows for user_id

**Component 5: Memory-Aware Responses**
- Agent uses recalled memories to personalize: format preferences, project context, role-based content
- Key prompt engineering: "Use the known facts to tailor your response. Do not ask the user to repeat information you already know."

### Try This Now
- Title: "Give Your Agent a Memory in One Afternoon"
- Step 1: Create the Dataverse table (5 minutes with the template)
- Step 2: Build the "Remember" plugin action (Power Automate, 20 minutes)
- Step 3: Build the "Recall" greeting topic (15 minutes)
- Step 4: Test: tell the agent your name and project. Close the conversation. Reopen. See if it remembers.
- The line: "What if your agent remembered every user's preferences, project context, and past decisions — so no one ever had to repeat themselves?"

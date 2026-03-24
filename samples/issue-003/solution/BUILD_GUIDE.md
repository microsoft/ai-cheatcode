# Copilot Studio Build Guide — Triage Agent

Step-by-step instructions to build the triage agent in Copilot Studio.
Follow these in order — each step builds on the previous one.

**Total time**: ~20 minutes

---

## Step 1: Create the Agent (~2 min)

1. Go to [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)
2. Click **Create** → **New agent**
3. Name: `Triage Agent`
4. Description: `Classifies requests and routes them to the right team with specific recommendations`
5. Paste the system prompt from `prompts/system-prompt.md` into the **Instructions** field
6. Click **Create**

---

## Step 2: Add the Classification Plugin Action (~5 min)

This connects the `classify-request` Power Automate flow to your agent.

1. In your agent, go to **Actions** → **Add an action**
2. Choose **Power Automate** → **Create a new flow** (or import `flows/classify-request.json`)
3. If creating manually:
   - **Trigger**: When Copilot Studio calls a flow (manual trigger)
   - **Input**: `userRequest` (text)
   - **Action 1**: HTTP → POST to your Azure OpenAI endpoint
     - URL: `{your-endpoint}/openai/deployments/gpt-4o/chat/completions?api-version=2024-06-01`
     - Headers: `api-key: {your-key}`, `Content-Type: application/json`
     - Body: Use the system prompt from `prompts/classify-prompt.md` as the system message, and `userRequest` as the user message
     - Request JSON response format
   - **Action 2**: Parse JSON (parse the OpenAI response)
   - **Action 3**: Create row in Dataverse `Triage Log` table (for audit)
   - **Output**: Return the parsed classification (category, confidence, entities, reasoning)
4. Save and publish the flow
5. Back in Copilot Studio, the action should appear. Set it up:
   - **Input mapping**: Map `userRequest` to `Activity.Text` (the user's message)
   - **Output**: `category`, `confidence`, `entities`, `reasoning`

---

## Step 3: Add the Playbook Runner Plugin Action (~5 min)

1. In **Actions** → **Add an action** → **Power Automate**
2. Import `flows/run-playbook.json` or create manually:
   - **Input**: `userRequest` (text), `category` (text), `entities` (text)
   - **Action 1**: List rows from Dataverse `Triage Playbooks` where category matches
   - **Action 2**: If playbook found → call Azure OpenAI with playbook + request context
   - **Action 3**: If no playbook → return "route to general help"
   - **Output**: Recommendations JSON (summary, actions, escalation_needed)
3. Save and publish

---

## Step 4: Create the Triage Topic (~5 min)

1. Go to **Topics** → **Add a topic** → **From blank**
2. Name: `Triage Request`
3. **Trigger phrases** (add these):
   - "I need help with"
   - "Can you help me"
   - "I have a request"
   - "Something is broken"
   - "I need to"
4. **Topic flow**:

```
[Trigger] → [Message: "I'll classify your request and route it to the right team."]
         → [Call Action: classify-request]
            Input: userRequest = Activity.Text
         → [Condition: classification.confidence >= 0.75]
            YES → [Message: "I've classified this as {category} ({confidence}%). Here's why: {reasoning}"]
                → [Call Action: run-playbook]
                   Input: userRequest, category, entities
                → [Message: Display recommendations]
            NO  → [Message: "I'm not confident in my classification. Let me connect you with someone who can help."]
                → [Escalate to human agent]
```

5. Add an **Adaptive Card** for the recommendations display (optional but nice):

```json
{
  "type": "AdaptiveCard",
  "version": "1.5",
  "body": [
    { "type": "TextBlock", "text": "📋 Triage Result", "weight": "bolder", "size": "medium" },
    { "type": "TextBlock", "text": "${summary}", "wrap": true },
    { "type": "FactSet", "facts": [
      { "title": "Category", "value": "${category}" },
      { "title": "Confidence", "value": "${confidence}%" },
      { "title": "Est. Resolution", "value": "${estimated_resolution}" }
    ]},
    { "type": "TextBlock", "text": "Recommended Actions:", "weight": "bolder" },
    { "type": "TextBlock", "text": "${actions_formatted}", "wrap": true }
  ]
}
```

---

## Step 5: Test (~3 min)

1. Click **Test** in the Copilot Studio canvas
2. Try these queries from `data/test-queries.csv`:

| Query | Expected |
|-------|----------|
| "My laptop screen is flickering" | IT Support, high urgency |
| "How many PTO days do I have left?" | HR, low urgency |
| "We need an NDA reviewed for Contoso" | Legal, high urgency |
| "Coffee machine on floor 3 is broken" | Other, low confidence → escalate |

3. Verify the Triage Log table in Dataverse is being populated

---

## Step 6: Publish (~1 min)

1. Click **Publish** in Copilot Studio
2. Choose your channel (Teams recommended for demo)
3. Share the agent link with test users

---

## Alternate: No Azure OpenAI?

If Azure OpenAI isn't available, you can use Copilot Studio's built-in generative AI:

1. Skip the Power Automate flows
2. Create separate topics for each category with specific trigger phrases:
   - **IT Support topic**: "laptop", "password", "VPN", "printer", "access", "software"
   - **HR topic**: "PTO", "benefits", "onboarding", "leave", "policy", "payroll"
   - **Legal topic**: "contract", "NDA", "compliance", "regulatory", "legal"
3. Use Copilot Studio's **Generative Answers** for the recommendation step
4. This is simpler but less accurate — the Azure OpenAI path gives better classification

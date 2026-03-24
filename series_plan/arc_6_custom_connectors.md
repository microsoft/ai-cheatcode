# Arc 6: Custom Connector Patterns (#018–#019)

## Customer Pain
The agent needs to call an internal API — a legacy ERP, a custom CRM, a proprietary compliance system. No pre-built connector exists. Graph API doesn't cover it. The project stalls at "we can't reach our data."

## Why This Matters for CSAs
Custom connectors unlock the long tail of enterprise use cases. Pre-built connectors cover 80% of M365 scenarios. The other 20% — where the highest-value, most differentiated use cases live — require custom connectors. CSAs who can build these own the enterprise expansion conversation.

---

## Issue #018 — 🧠 Conceptual: Custom Connector Patterns

### Key Sections

**When Custom Connector vs. Plugin Action (Power Automate)**
- Use a custom connector when: the API will be reused across multiple agents/flows, it has a stable OpenAPI spec, it needs to be governed as a platform asset
- Use a plugin action (Power Automate HTTP) when: it's a one-off integration, the API is unstable or undocumented, you need complex pre/post-processing
- Rule of thumb: if a second team would benefit from the same integration, make it a connector

**The OpenAPI Specification**
- The connector is only as good as its OpenAPI spec
- Minimum viable spec: one GET (read), one POST (write), clear parameter descriptions
- Pro tip: LLMs in Copilot Studio use the operation descriptions to decide when to call the connector — make descriptions clear and scenario-specific, not just technical

**Authentication Patterns**
1. API Key — simplest, suitable for internal APIs with low security requirements
2. OAuth 2.0 (authorization code) — standard for user-delegated access to SaaS APIs
3. OAuth 2.0 (client credentials) — for service-to-service, no user context
4. Azure AD / Entra ID — for Microsoft-ecosystem APIs, uses managed identity where possible
- Design decision: per-user auth (sees only their data) vs. service account (sees everything, agent filters)

**Error Handling and Resilience**
- What happens when the API is slow? Down? Returns garbage?
- Three-tier response: retry (transient errors) → fallback (cached data or degraded response) → escalate (tell the user and offer alternatives)
- Timeout budget: the agent has ~10 seconds before the user thinks it's broken

**Cross-references**
- Issue #006: Pete's custom connector for Teams transcript access via Graph API — the canonical example
- Issue #004: In-Boundary Processing — custom connectors inherit the security boundary of the Power Platform environment

---

## Issue #019 — 🔧 Practical: Building Custom Connectors for Copilot Studio

### Build Components

**Component 1: Write the OpenAPI Spec**
- Start from an existing API: use Copilot Chat to generate the OpenAPI spec from API documentation or example curl commands
- Minimum: `info`, `servers`, `paths` with one GET and one POST, `components/schemas` for request/response
- Critical: `summary` and `description` on every operation — Copilot Studio's LLM reads these to decide when to invoke the connector
- Example descriptions: NOT "GET /api/employees/{id}" → YES "Look up an employee's profile, team, and current project assignments by their employee ID"

**Component 2: Create the Custom Connector in Power Platform**
- Maker Portal → Custom Connectors → Import from OpenAPI
- Configure authentication (match the API's auth model)
- Test each operation directly in the connector editor
- Key gotcha: response schema must match exactly — if the API returns extra fields, they're silently dropped unless declared

**Component 3: Expose as Copilot Studio Plugin Action**
- In Copilot Studio: Actions → Add a connector action
- Map input parameters to conversational entities (e.g., "employee name" → `employee_id` lookup)
- Map output fields to agent response template
- Add natural-language descriptions: "Use this action when the user asks about an employee's details, team, or current project"

**Component 4: Azure API Management Gateway (Production)**
- For production deployments: front the internal API with Azure APIM
- Adds: rate limiting (protect the backend), caching (reduce latency), retry policies (handle transient failures), request/response logging
- The connector points to APIM, not directly to the backend — enables monitoring and governance without changing the API

**Component 5: Error Handling Topic in Copilot Studio**
- When the connector returns an error (timeout, 500, auth failure):
  - Don't show raw error to user
  - Topic catches the failure and responds: "I wasn't able to reach the [system name] right now. Here's what I can tell you from cached data, or I can try again in a moment."
  - Power Automate logs the error for ops visibility
- Graceful degradation > cryptic failure

### Try This Now
- Title: "Wrap Any REST API and Expose It to Your Agent"
- Step 1: Find an internal REST API with documentation (even a Swagger page works)
- Step 2: Use Copilot Chat to generate an OpenAPI spec from the docs
- Step 3: Import into Power Platform as a custom connector, configure auth, test
- Step 4: Add as a plugin action in your Copilot Studio agent with clear operation descriptions
- The line: "Your customer's most valuable data lives behind APIs that Copilot can't reach today. One custom connector changes that — and you can build it in an afternoon."

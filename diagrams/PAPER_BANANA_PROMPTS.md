# Paper Banana Diagram Prompts
# The Cheat Code — Architecture Diagram Library
#
# HOW TO USE:
# 1. Go to https://paper-banana.org/
# 2. Select style: "Methodology Diagrams" (or "System Architecture" if available)
# 3. Aspect Ratio: 16:9 (landscape) for most; 3:4 (portrait) for #005
# 4. Resolution: High
# 5. Format: PNG
# 6. Paste each prompt below into the text field
# 7. Generate → download → save to The Cheat Code/diagrams/
#
# BRANDING NOTES FOR ALL DIAGRAMS:
# - Use Microsoft's Fluent Design color palette: Blue (#0078D4), Purple (#6B2FA0),
#   Green (#107C10), Orange (#D83B01), Teal (#008272)
# - Clean white background with subtle light gray (#F5F5F5) section fills
# - Rounded rectangle nodes with drop shadows for depth
# - Segoe UI-style sans-serif typography
# - Professional corporate aesthetic — NOT academic/research style
# - Include Azure service icons where applicable (Azure Functions, Azure OpenAI, etc.)
# - Dashed lines for optional/conditional flows, solid for primary data paths
# - Arrow labels in smaller italic text describing the data or action


================================================================
DIAGRAM 1: Code-First Agent Delivery Pipeline
Issue #001 — Pattern: Code-First Agent Delivery
Filename: issue_001_deployment.png
Aspect ratio: 16:9 (landscape)
================================================================

Generate a professional system architecture diagram showing a three-zone deployment pipeline for building and deploying AI agents to Microsoft 365 Copilot Chat.

The diagram flows left-to-right across three clearly labeled zones with rounded borders and subtle background fills:

ZONE 1 — "Developer Workstation" (left, light purple background #F5F0FA, purple border #6B2FA0):
Contains three stacked components:
- "VS Code + GitHub Copilot Chat" (main development tool, prominent)
- "Teams Toolkit Extension" (deployment tooling)
- "Bicep / Infrastructure-as-Code Templates" (infrastructure definitions)

ZONE 2 — "Azure Resource Group" (center, light blue background #EBF3FD, blue border #0078D4):
Contains four interconnected Azure services:
- "Azure Functions" (agent runtime) — connected bidirectionally to:
  - "Azure OpenAI (GPT-4o)" (language model)
  - "Azure AI Search" (document index)
- "Azure Blob Storage" (PDF/document store) — connected to Azure AI Search

ZONE 3 — "M365 Copilot Platform" (right, light purple background #F5F0FA, purple border #6B2FA0):
Contains three components:
- "Copilot Chat" (user-facing interface, prominent)
- "Declarative Agent" (Teams manifest configuration)
- "Copilot Studio" (optional ZIP import path, shown with dashed border)

Primary flow arrows (solid, dark gray):
1. VS Code → Teams Toolkit: "Copilot generates agent code"
2. Teams Toolkit → Azure Functions: "azd up — deploy infrastructure"
3. Bicep Templates → Azure Resource Group: "Provision resources"
4. Azure Functions ↔ Declarative Agent: "API Plugin (OpenAPI spec)"

Secondary flow arrow (dashed, lighter):
5. Teams Toolkit ⟶ Copilot Studio: "Export ZIP (optional path)"

Use Microsoft Azure service icons. Professional, clean, corporate style with depth and visual hierarchy. The Azure zone should feel like a cloud deployment. Include a small lifecycle indicator showing "azd up / azd down" near the deployment arrow.


================================================================
DIAGRAM 2: Scoped Multi-Source Search
Issue #002 — Pattern: Scoped Multi-Source Search
Filename: issue_002_query_routing.png
Aspect ratio: 16:9 (landscape)
================================================================

Generate a professional system architecture diagram showing an intelligent query routing pattern for a Microsoft Copilot Chat agent that searches across multiple enterprise data sources.

The diagram flows top-to-bottom with a fan-out/fan-in pattern:

TOP — Input Layer:
- "User Query via Copilot Chat" (purple node #6B2FA0, prominent, with chat bubble icon)

SECOND ROW — Intelligence Layer (light purple background):
- "Query Analyzer" — a single processing node that performs intent classification and source selection. Show it as a prominent rounded rectangle with a brain/AI icon. Label: "Intent Classification + Source Routing"

THIRD ROW — Fan-out to three parallel data source lanes (light blue background #EBF3FD):
Three columns, each representing a scoped search path:

Column 1 — Azure DevOps:
- "ADO REST API" node
- Scope label: "Project + Work Item Type filter"
- Returns: "Work Items, Repos, Pipelines"

Column 2 — Microsoft Graph:
- "Graph API" node
- Scope label: "User + Date Range filter"
- Returns: "Email, Calendar, People, Files"

Column 3 — SharePoint:
- "Search API" node
- Scope label: "Site + Library filter"
- Returns: "Documents, Lists, Sites"

FOURTH ROW — Convergence Layer (light green background #E2F0E2):
Three processing steps in sequence:
1. "Merge Results" — deduplicate and normalize across sources
2. "Relevance Ranking" — score and filter by query intent
3. "Synthesize Response" — Azure OpenAI generates grounded answer

BOTTOM — Output:
- "Grounded Response with Source Citations" (green node #107C10)

Key visual element: The fan-out arrows from Query Analyzer to the three sources should each be labeled with the specific scoping criteria. The fan-in arrows converging to Merge should show result counts. Use distinct icons for each data source (DevOps boards icon, Outlook/Graph icon, SharePoint document icon).

Style: Microsoft corporate, Fluent Design colors, clean white background, professional. Emphasize the scoping (narrowing) at each source — this is the key insight of the pattern.


================================================================
DIAGRAM 3A: Prompt-Chained Triage Sequence
Issue #003 — Pattern: Prompt-Chained Triage + Playbook Orchestration
Filename: issue_003_chain_sequence.png
Aspect ratio: 16:9 (landscape)
================================================================

Generate a professional sequence/flow diagram showing a three-step prompt chaining pattern for automated work item triage in Azure DevOps.

The diagram should show a horizontal left-to-right flow with three distinct processing stages, each in its own bounded zone:

INPUT (left): "New Work Item / Bug Report" — raw unstructured text arriving from Azure DevOps

STEP 1 — "EXTRACT" (purple zone #F5F0FA):
- Label: "Step 1: Structured Extraction"
- System prompt extracts structured fields from raw text
- Output fields shown in a structured data card:
  • Title
  • Description
  • Affected Component
  • Error Signatures
  • Reproduction Steps
- Arrow label: "Raw text → Structured JSON"

STEP 2 — "CLASSIFY" (blue zone #EBF3FD):
- Label: "Step 2: Classification"
- Takes structured fields as input
- Output fields in a classification card:
  • Severity (P0–P4)
  • Category (Bug / Feature / Task)
  • Team Assignment
  • SLA Tier
- Arrow label: "Structured fields → Classification"

PLAYBOOK LOOKUP (between Step 2 and Step 3):
- Show a side branch from the classification result to a "YAML Playbook Registry" (orange accent #D83B01)
- The registry contains multiple playbook files: database-errors.yaml, ui-bugs.yaml, security-incidents.yaml
- Arrow: "Lookup by category + severity → matching playbook"

STEP 3 — "RECOMMEND" (green zone #E2F0E2):
- Label: "Step 3: Action Recommendation"
- Takes classification + matched playbook as input
- Output:
  • Suggested Assignee
  • Required Fields to Complete
  • Escalation Path
  • Related Work Items
- Arrow label: "Classification + Playbook → Actions"

OUTPUT (right): "Updated Work Item in Azure DevOps" — fields populated, tags applied, assignee set

Key visual: Each step should have a visible "system prompt" indicator (like a small document icon or prompt icon) to emphasize that each step has its own independent prompt. The chain nature (output of one = input of next) should be visually obvious with bold connecting arrows.

Style: Professional Microsoft corporate. Clean, modern, with depth. Color progression from purple (input) through blue (processing) to green (output).


================================================================
DIAGRAM 3B: Playbook Architecture — Agent vs. Customer Ownership
Issue #003 — Pattern: Playbook-Driven Orchestration (Decoupling View)
Filename: issue_003_playbook_arch.png
Aspect ratio: 16:9 (landscape)
================================================================

Generate a professional component architecture diagram showing the separation between developer-owned agent code and customer-owned YAML playbooks.

The diagram has two main zones side by side with a clear decoupling boundary between them:

LEFT ZONE — "Agent Code (Developer-Owned)" (purple background #F5F0FA, purple border):
Contains three stacked components:
1. "Prompt Chain Engine" — the 3-step extraction/classification/recommendation pipeline
2. "Playbook Loader" — runtime YAML parser that loads playbooks dynamically
3. "Action Executor" — executes API calls based on playbook instructions
Connected vertically: Chain Engine → Playbook Loader → Action Executor
Key label: "Deployed once. Never changes per customer."

RIGHT ZONE — "Playbook Registry (Customer-Owned)" (blue background #EBF3FD, blue border):
Contains a vertical stack of YAML files, each shown as a document/file icon:
- database-errors.yaml — "Severity mapping, escalation paths, required fields"
- ui-bugs.yaml — "Browser info required, screenshot attachment"
- feature-requests.yaml — "Product area routing, priority scoring"
- security-incidents.yaml — "Immediate P0 escalation, compliance notification"
- custom-playbook.yaml — shown with a dashed green border (#107C10) and a "+" icon, labeled "Customer adds new playbooks without code changes"
Key label: "Customer edits freely. No redeployment needed."

CENTER — Decoupling Boundary:
A prominent vertical dashed line or interface boundary between the two zones
Label: "Runtime Interface — Load at execution time by classification match"
Arrows showing: Playbook Loader → (crosses boundary) → YAML files

BOTTOM — Key Insight callout box (amber/gold background #FFF8E1, amber border #CA5010):
"🔑 The decoupling point: Agent logic stays constant. Playbooks change per customer. No redeployment needed."

Style: Microsoft corporate, clean. The visual emphasis should be on the SEPARATION — the boundary between the two zones is the hero of this diagram. Make it feel like two independent systems that interface cleanly.


================================================================
DIAGRAM 4: Secure In-Boundary Processing
Issue #004 — Pattern: Secure In-Boundary Processing
Filename: issue_004_trust_boundary.png
Aspect ratio: 16:9 (landscape)
================================================================

Generate a professional security/trust boundary architecture diagram showing how a Microsoft Copilot Chat agent processes data entirely within a customer's tenant boundary with zero external data leakage.

The diagram has one large TRUST BOUNDARY encompassing all processing, with blocked external paths:

MAIN ZONE — "Customer Tenant Boundary" (large rounded rectangle with dashed green border #107C10, very prominent, light green tint):

Inside the boundary, top to bottom:

Layer 1 — "M365 Copilot Platform" (purple accent):
- "Copilot Chat" (user interface)
- "Declarative Agent" (tenant-scoped configuration)

Layer 2 — "MCP Connectors (Tenant-Scoped)" (blue accent):
Three parallel connector nodes:
- "ADO Connector" — scoped to customer's Azure DevOps org
- "Graph Connector" — scoped to customer's M365 tenant
- "SharePoint Connector" — scoped to customer's sites
Each with a small lock/shield icon indicating auth scoping

Layer 3 — "In-Memory Processing" (orange accent #CA5010):
- "In-Memory Aggregation Layer" — no persistent external store, data lives only in session
- Prominent label: "Data lives only in session memory"

Layer 4 — "Tenant-Scoped AI" (green accent):
- "Azure OpenAI (Customer's Own Instance)"
- Label: "Customer-provisioned. Data processed in their region."

OUTSIDE the boundary (right side), show THREE BLOCKED paths with red X marks (#D13438):
- ❌ "External APIs" — crossed out, no connection
- ❌ "Cross-Tenant Data" — crossed out, no connection
- ❌ "Public LLM Endpoints" — crossed out, no connection

Each blocked path should have a dashed red line that STOPS at the tenant boundary with a prominent X or shield icon.

Style: This diagram's hero element is the TRUST BOUNDARY. It should be visually dominant — a thick dashed green border that clearly contains everything. The blocked external paths should be visually striking in red. Microsoft corporate style, clean, conveys security and isolation.


================================================================
DIAGRAM 5: Human-in-the-Loop Approval Gates
Issue #005 — Pattern: Human-in-the-Loop Approval Gates
Filename: issue_005_approval_flow.png
Aspect ratio: 4:3 (slightly taller)
================================================================

Generate a professional state machine / process flow diagram showing the Human-in-the-Loop approval gate pattern for AI-generated content.

The diagram flows top-to-bottom through five stages with a rejection feedback loop:

STAGE 1 — "Generate" (purple #6B2FA0):
- "AI Agent Output" — the agent generates content (summary, report, email, etc.)
- Show as a prominent starting node with an AI/robot icon

STAGE 2 — "Stage" (blue #0078D4):
- "Staged Artifact" — versioned draft stored in a draft zone
- Connected to "Immutable Source Reference" with a dotted link — the original source data (meeting transcript, raw data, source documents) is preserved and linked
- Key label: "Versioned draft with source traceability"

STAGE 3 — "Review" (amber/orange #CA5010, most prominent):
- "Human Review Queue" — pending items with full context and source
- Large decision diamond: "Approve or Reject?"
- This is the HERO of the diagram — make it visually dominant
- Show a human icon/figure to emphasize the human judgment point

STAGE 4A — "Publish" (green #107C10, if approved):
- Three publication targets in parallel:
  - "SharePoint Knowledge Base"
  - "Email Distribution"
  - "Internal Wiki / Documentation"

STAGE 4B — "Revision Loop" (red/orange #D83B01, if rejected):
- "Feedback + Rejection Reason" flows back up to the Generate stage
- Arrow label: "Regenerate with corrections"
- This creates a visible loop in the diagram

SIDE ELEMENT — "Audit Trail" (purple accent, right side):
- "Every action logged" — who generated, who reviewed, who approved/rejected, timestamp, reason
- Connected to both the Generate and Review stages

Style: Clean state machine aesthetic. The approval gate (human review) should be the visual focal point — largest element, warmest color. The flow should feel like a quality control pipeline. Microsoft corporate colors, professional.


================================================================
DIAGRAM 6: Meeting-to-Knowledge Pipeline
Issue #006 — Pattern: Meeting-to-Knowledge Pipeline (Two-Agent Architecture)
Filename: issue_006_pipeline.png
Aspect ratio: 16:9 (landscape)
================================================================

Generate a professional two-agent pipeline architecture diagram showing how meeting recordings are transformed into searchable organizational knowledge through two specialized AI agents.

The diagram flows left-to-right through distinct processing stages:

INPUT (far left):
- "Teams Meeting" — with a video/meeting icon
- "Recording + Transcript via Graph API"

AGENT 1 ZONE — "Meeting Scribe Agent" (purple background #F5F0FA, prominent):
Three processing steps inside:
1. "Transcript Processing" — speaker identification, topic segmentation
2. "Structured Extraction" — extracts: key decisions, action items (who/when), open questions, follow-ups
3. "Meeting Summary" — formatted output with sections and metadata
Connected sequentially top-to-bottom or left-to-right
Label on zone: "Agent 1: Capture + Summarize"

APPROVAL GATE (center, amber/orange #CA5010):
- Human review decision point
- Diamond shape: "Verify accuracy before publishing"
- If rejected: arrow loops back to Structured Extraction with "Corrections needed"
- If approved: arrow continues to Agent 2

AGENT 2 ZONE — "Library Agent" (blue background #EBF3FD, prominent):
Three components:
1. "Knowledge Indexer" — tag, categorize, link to projects
2. "SharePoint Library" — structured knowledge base with metadata and search indexes
3. "Query Interface" — semantic search across all meeting knowledge
Connected sequentially
Label on zone: "Agent 2: Index + Serve"

OUTPUT (far right, green #107C10):
Two consumption channels:
- "Copilot Chat" — natural language queries: "What did we decide about X in last sprint?"
- "SharePoint Search" — direct document discovery

Key visual: The TWO-AGENT boundary should be very clear — these are separate, independently deployable agents that share data through the approval gate and SharePoint. The handoff between Agent 1 and Agent 2 (through the approval gate) is the architectural hero.

Style: Microsoft corporate, Fluent Design colors. Show the pipeline nature clearly — data transforms as it moves through each stage. Professional, clean, suitable for customer-facing presentations.


================================================================
END OF PROMPTS
================================================================

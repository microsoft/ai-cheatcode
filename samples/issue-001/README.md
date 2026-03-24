# Issue #001: Code-First Agent Delivery (PDF Agent) — Deployable Template

> **Tier**: Deployable Template · **Setup time**: ~15 minutes · **Environment**: Azure subscription + M365 tenant for Teams
> **Builder**: Cristiano Almeida Gonçalves · **Validator**: Cristiano Almeida Gonçalves

## What This Deploys

An Azure-hosted agent that ingests large PDFs from SharePoint, processes them through Azure AI infrastructure, and surfaces results inside M365 Copilot and Teams. Uses Azure Functions for compute, Bicep for infrastructure, and `azd` for one-command deployment.

## Prerequisites

- [ ] Azure subscription with ~$5–10/day credit available while running
- [ ] [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed
- [ ] [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) installed
- [ ] [VS Code](https://code.visualstudio.com/) with GitHub Copilot extension (Agent mode)
- [ ] M365 tenant with Teams access (CDX "My Environment" works)
- [ ] SharePoint site where you can upload sample PDFs (or use CDX's pre-existing sites)

## What's in This Folder

| File/Folder | What It Is |
|-------------|-----------|
| `README.md` | This file — setup and demo instructions |
| `azure.yaml` | azd project definition — connects infra and app code |
| `infra/main.bicep` | Root Bicep template (provisions all Azure resources) |
| `infra/modules/` | Bicep modules: storage, search, openai, functions |
| `src/function_app.py` | Azure Functions entry point (3 endpoints: upload, query, status) |
| `src/services/` | Service layer: pdf_processor, openai_client, search_client, blob_client |
| `src/requirements.txt` | Python dependencies |
| `data/sample-pdfs/` | Instructions for creating test PDFs |
| `teams-manifest/` | Teams app manifest for publishing to M365 |
| `prompts/` | System prompts and the Copilot agent-mode prompt |
| `smoke-test.sh` | Post-deployment verification script |
| `.env.sample` | Environment variables (auto-populated by `azd up`) |

## How This Was Built

This template was generated using GitHub Copilot in VS Code Agent mode, then debugged and hardened into a reliable `azd` template. The original prompt:

```
Create an agent that analyzes large PDF documents from SharePoint.
Deploy to Azure with Bicep and integrate with Teams.
```

You can re-run this prompt in Copilot Agent mode to see how the scaffolding works, or simply use the pre-built template below.

## Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  User/Teams  │────▶│  Azure Functions  │────▶│  Blob Storage   │
│              │◀────│  (3 endpoints)    │     │  (PDF originals)│
└─────────────┘     └────────┬─────────┘     └─────────────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
              ┌─────▼──────┐   ┌──────▼───────┐
              │ Azure AI   │   │ Azure OpenAI │
              │ Search     │   │ (GPT-4o +    │
              │ (index +   │   │  embeddings) │
              │  hybrid    │   └──────────────┘
              │  search)   │
              └────────────┘
```

**API Endpoints:**
- `POST /api/upload` — Upload a PDF, extract text, chunk, embed, and index
- `POST /api/query` — Ask a question (hybrid search + RAG answer with citations)
- `GET  /api/status` — Check index health and document count

## Deploy

```bash
# 1. Navigate to this folder
cd samples/issue-001

# 2. Configure environment
cp .env.sample .env
# Edit .env — set your Azure subscription, M365 tenant ID, SharePoint site URL

# 3. Log in to Azure
az login
azd auth login

# 4. Deploy everything
azd up
# Choose a region when prompted (e.g., eastus2)
# This provisions Azure Functions, AI Services, and deploys the agent code

# 5. Note the output — you'll see the agent endpoint URL
```

## Publish to Teams

1. Go to [dev.teams.microsoft.com](https://dev.teams.microsoft.com)
2. Upload the Teams manifest from `teams-manifest/`
3. Install the app in your Teams tenant
4. The agent will appear in Teams and M365 Copilot chat

## Demo Script

1. **Open Teams** → Find the PDF Agent in your apps
2. **Upload a sample PDF** from `data/sample-pdfs/` to your SharePoint site
3. **Ask the agent**: "Summarize the key findings in [document name]"
4. **Show cross-document querying**: "Compare the compliance requirements across all uploaded documents"
5. **Highlight speed**: The agent processes large PDFs that would exceed M365 Copilot's token limits

### Key Demo Talking Points
- "This agent was deployed with a single command — `azd up`"
- "The system prompt is the only thing that changes per customer — swap in their industry context"
- "Azure resources only cost money while they're running — `azd down` removes everything"

## Customize for a Customer

The fastest path to a customer-specific demo:

1. Edit `prompts/system-prompt.md` — replace the industry context and document types
2. Upload the customer's PDFs (or representative samples) to SharePoint
3. Re-deploy: `azd deploy` (no need for full `azd up` if infrastructure is already provisioned)

## Tear Down (Important!)

```bash
azd down
```

**⚠️ Always tear down after demos.** Azure Functions, AI Services, and storage incur costs while provisioned.

## Cost Estimate

| Resource | SKU | Estimated Cost |
|----------|-----|---------------|
| Azure Functions | Consumption plan | ~$0.50/day (minimal at demo scale) |
| Azure AI Services | S0 | ~$1–3/day depending on usage |
| Storage Account | Standard LRS | ~$0.10/day |
| **Total while running** | | **~$2–5/day** |

*Costs are zero after `azd down`.*

## Alternate Path: Copilot Studio Import

If the customer prefers a no-code approach:
1. VS Code can export the agent as a ZIP package
2. Import the ZIP into Copilot Studio via Solutions → Import
3. Schema mismatches may need manual fixing — check the import log

## Smoke Test

After deployment, verify everything works:

```bash
# Get your function URL and key from the azd output
./smoke-test.sh https://your-func-app.azurewebsites.net your-function-key
```

The smoke test checks:
1. `/api/status` returns healthy
2. `/api/query` handles empty index gracefully
3. `/api/upload` processes a PDF (if sample PDFs are present)

## Known Limitations

- PDF uploads require an authenticated M365 Copilot or Teams session (won't work unauthenticated)
- PDFs work reliably; Office document (docx, pptx) parity is still catching up
- Large PDFs (100+ pages) may take 30-60 seconds to process on first query
- The GitHub Copilot agent-mode prompt may generate slightly different code each time — this template is the hardened, tested version

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `azd up` fails with permission error | Ensure you have Contributor role on the Azure subscription |
| Agent doesn't appear in Teams | Check that the manifest was published and the app is approved in Teams Admin |
| PDF processing times out | Check Azure Function timeout settings in `infra/` — increase if needed |
| "Token limit exceeded" error | This usually means the PDF is extremely large — the agent should chunk it, but check `src/` for chunk size settings |

## Related

- 📰 [Newsletter Issue #001](../../issues/the_cheat_code_issue_001.html)
- 📊 [Architecture Diagram](../../diagrams/issue_001_deployment_rich.png)

## Validation

```
Validated by: [Pending — Cristiano Almeida Gonçalves]
Date: [Pending]
Environment: Azure subscription + CDX M365 tenant
All checks: [Pending]
```

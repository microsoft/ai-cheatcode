# Issue #008: Cross-Project Knowledge Agent — Deployable Template

> **Tier**: Deployable Template · **Setup time**: ~20 minutes (deploy) + ~30 minutes (data enrichment)
> **Environment**: Azure subscription (AI Search + OpenAI) + CDX tenant (Copilot Studio)
> **Builder**: Tyson Dowd · **Validator**: Tyson Dowd · **Status**: 🔲 Planned

## What This Deploys

A Copilot Studio agent backed by an enriched Azure AI Search index that performs cross-project synthesis. Implements the Holographic Memory pattern from Issue #007 with layer-aware retrieval.

## Prerequisites

- [ ] Azure subscription with Azure AI Search + Azure OpenAI access
- [ ] M365 tenant with Copilot Studio (CDX "My Environment" recommended)
- [ ] 2+ project SharePoint sites with 10-15 documents each
- [ ] Azure Developer CLI (azd) installed

## What Needs to Be Built

*To be developed — Tyson Dowd to provide:*
1. Azure AI Search index schema (fields: project_name, author, decisions[], related_artifacts[], summary_context)
2. Power Automate enrichment flow (trigger: file created/modified → extract → Azure OpenAI enrichment → index push)
3. Copilot Studio agent with generative answers + cross-project system prompt
4. "Index this conversation" plugin action
5. Sample documents across 2-3 mock projects
6. Enrichment prompts for adding holographic context to documents
7. Cross-project "impossible questions" for demo

## Cost Estimate

| Resource | SKU | Estimated Cost |
|----------|-----|---------------|
| Azure AI Search | Basic | ~$2.50/day |
| Azure OpenAI | Standard | ~$1-3/day (enrichment + queries) |
| **Total while running** | | **~$4-6/day** |

*Tear down Azure resources after demos to avoid ongoing costs.*

## Related

- 📰 [Newsletter Issue #008](../../issues/the_cheat_code_issue_008.html)
- 🧠 See also: [Issue #007 — Holographic Memory](../issue-007/) (the conceptual pattern)
- 📊 [Architecture Diagram](../../diagrams/issue_007_holographic_memory_rich.png)

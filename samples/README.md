# Code Samples for The Ch(e)at Code

Each newsletter issue has a companion code sample in `samples/issue-NNN/`. Samples come in three tiers based on what the pattern requires:

| Tier | What You Get | Setup Time | Environment |
|------|-------------|------------|-------------|
| **Prompt Pack** | Tested prompts + expected outputs | ~5 min | Any Copilot Chat or Azure OpenAI Playground |
| **Starter Kit** | Importable Copilot Studio solution + flows + data | ~30 min | CDX tenant or any M365 + Power Platform environment |
| **Deployable Template** | `azd up` from zero to working demo | ~15 min | Azure subscription (+ M365 for Teams integration) |

## External Reference: Copilot Studio and Azure Labs

The **[Azure/Copilot-Studio-and-Azure](https://github.com/Azure/Copilot-Studio-and-Azure)** repo (by Cristiano Almeida Gonçalves, builder of Issue #001) provides hands-on labs and solution accelerators for Copilot Studio + Azure AI. Several labs directly complement our newsletter patterns:

| Newsletter Issue | Related Lab / Accelerator | Link |
|------------------|--------------------------|------|
| #001 Code-First Agent Delivery | Lab 0.0: Create an Agent | [Lab 0.0](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/0.0-create-an-agent) |
| #002 Scoped Multi-Source Search | Lab 1.4: AI Search in Copilot Studio | [Lab 1.4](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/1.4-ai-search) |
| #003 Prompt-Chained Triage | Lab 1.1: Create Topics | [Lab 1.1](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/1.1-create-topics) |
| #007/#008 Holographic Memory | Lab 2.1: Advanced AI Search | [Lab 2.1](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/2.1-ai-search-advanced) |
| #007/#008 Holographic Memory | Lab 2.4: Foundry Agentic Retrieval | [Lab 2.4](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/2.4-microsoft-foundry-agentic-retrieval) |
| #017/#018 Evaluation & Analytics | Lab 1.7: Monitor with App Insights | [Lab 1.7](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/1.7-monitoring) |
| #019/#020 Custom Connectors | SharePoint Connector Accelerator | [Accelerator](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/accelerators/sharepoint-connector) |

Also includes: [MCP integration](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/1.3-MCP), [fine-tuned models](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/2.2-Fine-Tunned-Model), [ALM](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/labs/1.6-application-lifecycle-management), [Video RAG accelerator](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/accelerators/Video-RAG), and [project scoping templates](https://github.com/Azure/Copilot-Studio-and-Azure/tree/main/docs).

## Quick Start

1. Navigate to the issue folder: `samples/issue-NNN/`
2. Read the `README.md` — it tells you exactly what you need and how long it takes
3. Follow the steps. Every sample targets **under 30 minutes** from zero to working demo.

## Issue Map

| Issue | Pattern | Tier | Status |
|-------|---------|------|--------|
| [#001](issue-001/) | Code-First Agent Delivery | Deployable Template | 🔲 In Progress |
| [#002](issue-002/) | Scoped Multi-Source Search | Prompt Pack | 🔲 Planned |
| [#003](issue-003/) | Prompt-Chained Triage + Playbooks | Starter Kit | 🔲 In Progress |
| [#004](issue-004/) | Secure In-Boundary Processing | Prompt Pack | 🔲 Planned |
| [#005](issue-005/) | Human-in-the-Loop Approval Gates | Prompt Pack | 🔲 Planned |
| [#006](issue-006/) | Meeting-to-Knowledge Pipeline | Starter Kit | 🔲 Planned |
| [#007](issue-007/) | Holographic Memory | Prompt Pack | 🔲 Planned |
| [#008](issue-008/) | Cross-Project Knowledge Agent | Deployable Template | 🔲 Planned |

## Environment Guide

See [ENVIRONMENT_GUIDE.md](ENVIRONMENT_GUIDE.md) for details on CDX demo tenants, personal Azure subscriptions, and which environment to use for each pattern type.

## Provenance

Every issue is tracked back to its source: who built the pattern, what customer engagement it came from, and how the content was developed. See [PROVENANCE.md](PROVENANCE.md) for the full registry.

## Validation

Every code sample passes the [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) before it's considered ready. If you find an issue, file it in this repo.

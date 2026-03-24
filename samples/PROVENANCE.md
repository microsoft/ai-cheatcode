# Issue Provenance Registry

Tracks where each newsletter issue came from: who built the original pattern, what customer engagement sourced it, and how the content was developed.

---

## Published Issues

| # | Title | Type | Builder | Source Engagement | How It Was Sourced | Date |
|---|-------|------|---------|-------------------|--------------------|------|
| 001 | Code-First Agent Delivery | 🔧 | Cristiano Almeida Gonçalves | **Coca-Cola** — large regulatory/compliance PDFs in SharePoint | Customer engagement: agent built, deployed to Azure, integrated into Teams in a single session | Mar 23, 2026 |
| 002 | Scoped Multi-Source Search | 🧠 | Raghav BN | **Live ADO work items** — real Azure DevOps queries against M365 data | Extracted from a multi-source search agent demo; pattern disaggregated from a larger agent build | Mar 31, 2026 |
| 003 | Prompt-Chained Triage + Playbooks | 🔧 | Raghav BN | **Part 2 of #002 agent** — triage orchestration layer on top of scoped search | Same engagement as #002; the triage chain was a separate reusable pattern worth its own issue | Apr 7, 2026 |
| 004 | Secure In-Boundary Processing | 🧠 | Raghav BN | **Enterprise compliance** — data residency and tenant boundary requirements | Pattern extracted from compliance-sensitive customer conversations (financial services, healthcare) | Apr 14, 2026 |
| 005 | Human-in-the-Loop Approval Gates | 🧠 | Pete Puustinen | **General enterprise pattern** — trust checkpoints between AI generation and consumption | Conceptual pattern observed across multiple engagements; Eggis Pharma meeting scribe used as primary example | Apr 21, 2026 |
| 006 | Meeting-to-Knowledge Pipeline | 🔧 | Pete Puustinen | **Eggis Pharma** — Budapest Hackathon (2.5-day build with train-the-trainer Day 0) | Hackathon engagement: two-agent architecture (Scribe + Library) built end-to-end with customer team | Apr 28, 2026 |
| 007 | Holographic Memory | 🧠 | Tyson Dowd | **Internal 1:1 discussion** — cross-project knowledge synthesis problem | Pattern developed from internal conversations about how to handle multi-project knowledge with graceful degradation | May 5, 2026 |
| 008 | Cross-Project Knowledge Agent | 🔧 | Tyson Dowd | **Internal 1:1 discussion** — practical build of the Holographic Memory pattern | Implementation companion to #007; enriched Azure AI Search + Copilot Studio generative answers | May 12, 2026 |

## Planned Issues

| # | Title | Type | Builder | Source / Target Industries | Arc | Date |
|---|-------|------|---------|----------------------------|-----|------|
| 009 | Adaptive Guardrails | 🧠 | TBD | Financial, Healthcare, Government, HR | Arc 1 | May 19, 2026 |
| 010 | Building Adaptive Guardrails | 🔧 | TBD | HR agent guardrails (AI Builder classifier) | Arc 1 | May 26, 2026 |
| 011 | Multi-Agent Handoff | 🧠 | TBD | Enterprise multi-domain (HR+IT) | Arc 2 | Jun 2, 2026 |
| 012 | Building Multi-Agent Handoff | 🔧 | TBD | Two-agent handoff with session state | Arc 2 | Jun 9, 2026 |
| 013 | Persistent Agent Memory | 🧠 | TBD | Enterprise (all verticals) | Arc 3 | Jun 16, 2026 |
| 014 | Building Persistent Memory | 🔧 | TBD | User preferences & project context | Arc 3 | Jun 23, 2026 |
| 015 | Proactive Agent Triggers | 🧠 | TBD | Compliance, Finance, Project Management | Arc 4 | Jun 30, 2026 |
| 016 | Building Proactive Agents | 🔧 | TBD | Weekly project health checks | Arc 4 | Jul 7, 2026 |
| 017 | Agent Evaluation & Trust Signals | 🧠 | TBD | Enterprise (all verticals) | Arc 5 | Jul 14, 2026 |
| 018 | Building Agent Analytics | 🔧 | TBD | Agent adoption & quality dashboard | Arc 5 | Jul 21, 2026 |
| 019 | Custom Connector Patterns | 🧠 | TBD | Legacy systems, proprietary APIs | Arc 6 | Jul 28, 2026 |
| 020 | Building Custom Connectors | 🔧 | TBD | Internal REST API integration | Arc 6 | Aug 4, 2026 |

## Builder Directory

| Builder | Issues | Sourcing Method |
|---------|--------|-----------------|
| Cristiano Almeida Gonçalves | #001 | Customer engagement (Coca-Cola) |
| Raghav BN | #002, #003, #004 | Customer engagement + pattern disaggregation |
| Pete Puustinen | #005, #006 | Hackathon (Eggis Pharma) + cross-engagement pattern |
| Tyson Dowd | #007, #008 | Internal 1:1 discussions |
| TBD | #009–#020 | To be assigned from team meetings and 1:1s as demos surface |

## Customer Engagements Referenced

| Customer | Industry | Issues | Engagement Type |
|----------|----------|--------|-----------------|
| Coca-Cola | Consumer goods / Regulatory | #001 | Direct customer engagement |
| Eggis Pharma | Pharmaceutical | #005, #006 | Budapest Hackathon (2.5 days) |
| *(ADO internal)* | Internal tooling | #002, #003 | Live work item demos |
| *(Internal)* | Cross-functional | #007, #008 | 1:1 pattern discussions |

## Cross-Reference Chain

Issues are not standalone — patterns build on and reference each other:

```
#001 (PDF Agent) — standalone code-first reference
#002 (Scoped Search) → #003 (Triage + Playbooks) — same agent, disaggregated
#004 (Secure Boundary) — standalone, references #001 and #002 principles
#005 (Approval Gates) → #006 (Meeting Pipeline) — concept → implementation
#007 (Holographic Memory) → #008 (Cross-Project Agent) — concept → implementation
#009/#010 (Adaptive Guardrails) — references #005 (approval as human fallback)
#011/#012 (Multi-Agent Handoff) — references #005 (escalation patterns)
#013/#014 (Persistent Memory) — references #007 (holographic memory as knowledge-layer parallel)
#015/#016 (Proactive Triggers) — references #006 (event-driven pipeline)
#017/#018 (Agent Evaluation) — references #005 (approval as quality check)
#019/#020 (Custom Connectors) — references #006 (custom Teams connector as example)
```

## How to Update This Registry

When a new issue is sourced:
1. Add the builder, customer engagement, and sourcing method to the tables above
2. Update the builder directory
3. Add any new customer engagements to the customer table
4. Note cross-references to existing issues
5. For planned issues (#009+), update "TBD" entries as builders are assigned

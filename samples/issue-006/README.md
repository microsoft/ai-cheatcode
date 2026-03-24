# Issue #006: Meeting-to-Knowledge Pipeline — Starter Kit

> **Tier**: Starter Kit · **Setup time**: ~30 minutes (agent setup) + additional time for custom connector
> **Environment**: CDX tenant + Azure subscription
> **Builder**: Pete Puustinen · **Validator**: Pete Puustinen · **Status**: 🔲 Planned

## What This Builds

A two-agent architecture: (1) a Scribe Agent that fetches Teams transcripts, generates structured summaries, and routes for approval, and (2) a Library Agent that indexes approved docs in Azure AI Search and answers leadership questions via natural language.

## Prerequisites

- [ ] M365 tenant with Copilot Studio (CDX "My Environment" recommended)
- [ ] Power Automate premium license (included in CDX)
- [ ] Azure subscription with Azure AI Search + Azure Blob Storage
- [ ] Teams meetings with transcription enabled (need 2-3 sample transcripts)
- [ ] SharePoint site with two document libraries (archival + editable)

## What Needs to Be Built

*To be developed — Pete Puustinen to provide:*
1. Copilot Studio solutions for both agents (Scribe + Library)
2. Power Automate flows for transcript retrieval and processing
3. Custom connector for Graph API transcript access (base64 decoding, meeting ID resolution)
4. Azure AI Search index schema
5. SharePoint library configuration guide
6. Sample meeting transcripts for testing

## Known Complexity

This is the most complex Starter Kit — the original build took 2.5 days at a hackathon. Key challenges:
- Custom connector for Graph API (base64 meeting chat ID → join URL → meeting ID → transcript ID)
- Save-then-reference workaround (transcript too large for token limit; pass link instead of content)
- Two separate SharePoint libraries needed (immutable archives vs. editable summaries)
- Known bug: `.vtt` and `.txt` files can't be passed as attachments — must pass links

## Related

- 📰 [Newsletter Issue #006](../../issues/the_cheat_code_issue_006.html)
- 📊 [Architecture Diagram](../../diagrams/issue_006_pipeline_rich.png)
- 🧠 See also: [Issue #005 — Approval Gates](../issue-005/) (the conceptual pattern behind the approval step)

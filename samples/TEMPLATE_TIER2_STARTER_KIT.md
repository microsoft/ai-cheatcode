# README Template — Tier 2: Starter Kit

Use this template for practical Copilot Studio issues (even-numbered, 🔧 type).

---

# Issue #NNN: [Pattern Name] — Starter Kit

> **Tier**: Starter Kit · **Setup time**: ~30 minutes · **Environment**: CDX tenant or any M365 + Power Platform environment

## What This Builds

[1-2 sentences: what the CSA will have running at the end of setup]

## Prerequisites

- [ ] M365 tenant with Copilot Studio access (CDX "My Environment" recommended)
- [ ] Power Automate premium license (included in CDX)
- [ ] Dataverse environment provisioned
- [ ] [Any additional prerequisites — Azure OpenAI, specific connectors, etc.]

## What's in This Folder

| File | What It Is |
|------|-----------|
| `README.md` | This file — setup instructions |
| `solution.zip` | Copilot Studio solution — import into your environment |
| `flows/` | Power Automate flow templates (.json) |
| `data/` | Sample data files (Dataverse seed data, test queries) |
| `prompts/` | System prompts and topic configurations |

## Setup Steps

### Step 1: Import the Copilot Studio Solution
1. Go to [make.powerapps.com](https://make.powerapps.com) → Solutions → Import
2. Upload `solution.zip`
3. Follow the import wizard — resolve any connection references

### Step 2: Configure Connections
1. [Specific connection setup steps]
2. [Connection reference mapping]

### Step 3: Import Sample Data
1. [Dataverse table creation if not in solution]
2. [Data import steps]

### Step 4: Test It
Run these test queries to verify everything works:

| # | Test Query | Expected Behavior |
|---|-----------|-------------------|
| 1 | [query] | [expected response] |
| 2 | [query] | [expected response] |
| 3 | [query] | [expected response] |

## Known Limitations

- [Limitation 1]
- [Limitation 2]
- [CDX-specific quirks if any]

## Cost Notes

[What premium features are used, any Azure costs, etc.]

## Related

- 📰 [Newsletter Issue #NNN](../../issues/the_cheat_code_issue_NNN.html)
- 🧠 [Conceptual Pattern: Issue #NNN-1](../issue-NNN-1/) (if applicable)

## Validation

```
Validated by:
Date:
Environment:
All checks: PASS
```

# Issue #003: Prompt-Chained Triage + Playbook Orchestration — Starter Kit

> **Tier**: Starter Kit · **Setup time**: ~30 minutes · **Environment**: CDX tenant or any M365 + Power Platform environment
> **Builder**: Raghav BN · **Validator**: Raghav BN

## What This Builds

A Copilot Studio agent that decomposes triage tasks into discrete prompt chains (Extract → Classify → Recommend) and orchestrates them via YAML-defined playbooks. By the end of setup, you'll have an agent that takes incoming requests, classifies them, and runs the appropriate playbook — all inside Teams.

## Prerequisites

- [ ] M365 tenant with Copilot Studio access (CDX "My Environment" recommended)
- [ ] Power Automate premium license (included in CDX)
- [ ] Dataverse environment provisioned
- [ ] Azure OpenAI access (for classification and recommendation prompts) — or use Copilot Studio's built-in generative AI if Azure OpenAI isn't available

## What's in This Folder

| File/Folder | What It Is |
|-------------|-----------|
| `README.md` | This file — setup and demo instructions |
| `solution/triage-agent.zip` | Copilot Studio solution — import into your environment |
| `flows/classify-request.json` | Power Automate flow: classifies incoming requests |
| `flows/run-playbook.json` | Power Automate flow: executes the matched playbook |
| `data/playbooks/` | YAML playbook definitions (IT, HR, Legal examples) |
| `data/test-queries.csv` | 50 synthetic test queries for validation |
| `prompts/system-prompt.md` | The agent's system prompt |
| `prompts/classify-prompt.md` | The classification prompt used in the chain |
| `prompts/recommend-prompt.md` | The recommendation prompt used in the chain |

## The Prompt Chain

This agent uses a three-step prompt chain, each step feeding the next:

```
[User Request] → Step 1: EXTRACT → Step 2: CLASSIFY → Step 3: RECOMMEND
                 (entities,      (IT/HR/Legal/     (matched playbook
                  intent,         Other + confidence  steps + suggested
                  urgency)        score)              actions)
```

Each step is a separate prompt with a specific job. This is more reliable than asking one prompt to do everything.

## Setup Steps

### Step 1: Import the Copilot Studio Solution (~5 min)
1. Go to [make.powerapps.com](https://make.powerapps.com) → Solutions → Import
2. Upload `solution/triage-agent.zip`
3. Follow the import wizard
4. When prompted for connection references:
   - **Dataverse**: Select your default Dataverse connection
   - **Azure OpenAI** (if used): Enter your Azure OpenAI endpoint and key

### Step 2: Import Power Automate Flows (~5 min)
1. Go to [make.powerautomate.com](https://make.powerautomate.com) → My Flows → Import
2. Import `flows/classify-request.json` — configure the Azure OpenAI (or HTTP) connection
3. Import `flows/run-playbook.json` — configure the Dataverse connection
4. Turn on both flows

### Step 3: Load the Playbooks (~5 min)
1. In Dataverse, find the `Triage Playbooks` table (created by the solution import)
2. Import the YAML playbooks from `data/playbooks/`:
   - `it-support.yaml` — Device provisioning, access requests, software issues
   - `hr-requests.yaml` — PTO, benefits, onboarding questions
   - `legal-intake.yaml` — Contract review, compliance questions, NDA requests
3. Or create your own — the YAML format is documented below

### Step 4: Test It (~15 min)
Open the agent in Copilot Studio's test chat and run these queries:

| # | Test Query | Expected Classification | Expected Behavior |
|---|-----------|------------------------|-------------------|
| 1 | "My laptop screen is flickering and I can't present in meetings" | IT Support (high confidence) | Extracts: device=laptop, issue=display, urgency=high. Runs IT playbook → suggests hardware ticket + interim workaround |
| 2 | "How many PTO days do I have left this year?" | HR (high confidence) | Extracts: topic=PTO, type=balance inquiry. Runs HR playbook → directs to HR portal with instructions |
| 3 | "We need an NDA reviewed for the Contoso partnership" | Legal (high confidence) | Extracts: document=NDA, party=Contoso, action=review. Runs Legal playbook → creates intake item with priority |
| 4 | "The coffee machine on floor 3 is broken again" | Other / Low confidence | Falls through classification → polite redirect to facilities or general help |
| 5 | "I need to onboard a new contractor starting Monday who needs a laptop and building access" | HR + IT (multi-category) | Should detect both HR (onboarding) and IT (device provisioning) → chains both playbooks |

For full validation, use the 50 queries in `data/test-queries.csv`.

## YAML Playbook Format

Playbooks define the steps for each category. Here's the format:

```yaml
name: IT Support Triage
category: it-support
description: Handles device, access, and software issues

steps:
  - id: extract
    action: prompt
    prompt_ref: prompts/classify-prompt.md
    extracts: [device_type, issue_category, urgency]

  - id: classify
    action: route
    rules:
      - condition: "issue_category == 'hardware'"
        next: hardware_flow
      - condition: "issue_category == 'access'"
        next: access_flow
      - condition: "default"
        next: general_it

  - id: hardware_flow
    action: prompt
    prompt_ref: prompts/recommend-prompt.md
    context: "Hardware issue for {device_type}: {user_description}"
    output: recommendation

  - id: access_flow
    action: prompt
    prompt_ref: prompts/recommend-prompt.md
    context: "Access request: {user_description}"
    output: recommendation

  - id: general_it
    action: escalate
    target: "IT Help Desk"
    message: "Unclassified IT request — needs human review"
```

You can add new playbooks by creating a new YAML file and importing it into the Dataverse table.

## Customize for a Customer

1. **Replace the playbooks** — Swap IT/HR/Legal for the customer's actual intake categories
2. **Update the classification prompt** — Edit `prompts/classify-prompt.md` to match the customer's categories and terminology
3. **Add real data** — Replace synthetic test queries with the customer's actual intake examples (anonymized)
4. **Adjust confidence thresholds** — In the `classify-request` flow, tune the confidence score cutoff (default: 0.75)

## Known Limitations

- Classification accuracy improves with better prompts and more category examples — start with 10+ examples per category
- Multi-category requests (like query #5 above) are the hardest — the chain may only detect the primary category
- YAML playbooks are stored as text in Dataverse — there's no built-in YAML editor, so edit locally and re-import
- Azure OpenAI adds 1-2 seconds latency per prompt step (3 steps = 3-6 seconds total chain time)

## Cost Notes

- **Copilot Studio**: Included in CDX tenant or M365 Copilot license
- **Power Automate**: Premium connectors used (included in CDX)
- **Azure OpenAI** (if used): ~$0.01-0.05 per triage chain (3 prompt calls × ~500 tokens each)
- **Dataverse**: Storage included in CDX (minimal for playbook data)

## Related

- 📰 [Newsletter Issue #003](../../issues/the_cheat_code_issue_003.html)
- 📊 [Architecture Diagram](../../diagrams/issue_003_chain_sequence_rich.png)
- 🧠 See also: [Issue #002 — Scoped Multi-Source Search](../issue-002/) (the search scoping pattern that feeds into triage)

## Validation

```
Validated by: [Pending — Raghav BN]
Date: [Pending]
Environment: CDX My Environment tenant
All checks: [Pending]
```

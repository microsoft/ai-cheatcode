# README Template — Tier 3: Deployable Template

Use this template for code-first, Azure-heavy issues.

---

# Issue #NNN: [Pattern Name] — Deployable Template

> **Tier**: Deployable Template · **Setup time**: ~15 minutes · **Environment**: Azure subscription (+ M365 for Teams integration)

## What This Deploys

[1-2 sentences: what Azure resources are created and what the agent does]

## Prerequisites

- [ ] Azure subscription with sufficient credits (~$X/day while running)
- [ ] [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed
- [ ] [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) installed
- [ ] [Any additional tools — Node.js, Python, etc.]
- [ ] [M365 tenant if Teams integration is included]

## What's in This Folder

| File/Folder | What It Is |
|-------------|-----------|
| `README.md` | This file — setup instructions |
| `azure.yaml` | azd project definition |
| `infra/` | Bicep infrastructure templates |
| `src/` | Application code |
| `data/` | Sample data files (PDFs, documents, etc.) |
| `.env.sample` | Environment variables template |

## Deploy

```bash
# 1. Clone and navigate
cd samples/issue-NNN

# 2. Configure environment
cp .env.sample .env
# Edit .env with your values (see comments in file)

# 3. Deploy everything
azd up

# 4. Note the output URL — that's your agent endpoint
```

## Demo It

[Step-by-step demo walkthrough — what to show, what to say, expected results]

## Tear Down (Important!)

```bash
azd down
```

**⚠️ Always tear down after demos.** Azure resources incur costs while running. Running `azd down` removes everything cleanly.

## Cost Estimate

| Resource | SKU | Estimated Cost |
|----------|-----|---------------|
| [Resource 1] | [SKU] | ~$X/day |
| [Resource 2] | [SKU] | ~$X/day |
| **Total while running** | | **~$X/day** |

*Costs are zero after `azd down`.*

## Smoke Test

```bash
# Verify the deployment is working
[curl or test commands]
```

## Known Limitations

- [Limitation 1]
- [Limitation 2]

## Related

- 📰 [Newsletter Issue #NNN](../../issues/the_cheat_code_issue_NNN.html)

## Validation

```
Validated by:
Date:
Environment:
All checks: PASS
```

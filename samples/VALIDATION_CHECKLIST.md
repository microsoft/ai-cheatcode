# Code Sample Validation Checklist

Every code sample must pass these 10 checks before it's considered ready. The original builder validates their own samples.

---

## The Checklist

| # | Check | Pass? |
|---|-------|-------|
| 1 | **README is complete** — Prerequisites, setup steps, expected behavior, known limitations, and teardown (if applicable) are all documented. |  |
| 2 | **Prerequisites are explicit** — Every license, service, tool, and permission needed is listed. No hidden assumptions. |  |
| 3 | **Setup time is under 30 minutes** — A CSA who reads the README can go from zero to working demo in 30 minutes or less. |  |
| 4 | **Prompts produce expected output** — Every prompt in the sample has been run 3x and produces consistent, correct results. Expected outputs are documented. |  |
| 5 | **Imports cleanly** — Copilot Studio solutions import without errors. Power Automate flows import and can be configured. Dataverse tables create correctly. (Tier 2 only) |  |
| 6 | **Deploys cleanly** — `azd up` completes without errors on a fresh subscription. All resources provision correctly. (Tier 3 only) |  |
| 7 | **Teardown works** — `azd down` removes all resources. No orphaned resources or ongoing charges. (Tier 3 only) |  |
| 8 | **Cost is documented** — Azure resource costs are estimated. The importance of teardown after demos is called out. (Tier 2 & 3) |  |
| 9 | **No placeholder content** — No "TODO", "FIXME", "replace this", or sample tokens/keys left in the code. |  |
| 10 | **Works in target environment** — Tested in CDX tenant (Tier 2) or personal Azure subscription (Tier 3). Environment-specific quirks are documented. |  |

---

## How to Use

1. Copy this checklist into the issue's `samples/issue-NNN/` folder as you validate
2. Work through each item
3. If something fails, fix it before marking the sample as ready
4. Note any environment-specific quirks in the README's "Known Limitations" section

## Validation Sign-Off

```
Validated by: [Name]
Date: [YYYY-MM-DD]
Environment: [CDX tenant / Azure subscription / Both]
All 10 checks: [PASS / FAIL — list failures]
```

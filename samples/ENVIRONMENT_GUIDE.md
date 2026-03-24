# Environment Guide for Code Samples

This is a one-page reference for the environments CSAs can use to run these code samples.

---

## CDX Demo Tenants (cdx.transform.microsoft.com)

**What it is**: Pre-provisioned Microsoft 365 tenants for Microsoft employees and partners.

**What's included**:
- Office 365 E5 licenses (Exchange, SharePoint, Teams, OneDrive)
- Microsoft Copilot licenses (Copilot Chat, M365 Copilot)
- Power Platform (Copilot Studio, Power Automate, Power Apps, Dataverse)
- Sample organizational data (users, groups, SharePoint sites with Contoso-style content)
- Teams pre-configured with channels and sample conversations

**Tenant types**:
| Type | Lifetime | Best For |
|------|----------|----------|
| Quick-use | Hours to days | Quick demos, screenshot walkthroughs |
| My Environments | ~90 days | Building and iterating on agent demos |
| Custom demos | Varies | Pre-built guided experiences |

**Limitations**:
- Time-limited (environments reset/expire)
- Azure credits are limited and vary by tenant type
- Sample data is generic (Contoso-style)
- Not all Azure services may be provisioned
- Some admin operations may be restricted

**Best for these samples**: Copilot Studio agents, Power Automate flows, SharePoint-based patterns, Teams integration — most Tier 2 (Starter Kit) samples.

**To get started**: Go to [cdx.transform.microsoft.com](https://cdx.transform.microsoft.com), sign in with your Microsoft account, and create a "My Environments" tenant.

---

## Personal Microsoft Azure Subscriptions

**What it is**: Azure access through Visual Studio Enterprise subscription or internal AIRS subscriptions.

**What's included**:
- Full Azure service catalog
- $150/month credit (VS Enterprise) or allocated AIRS budget
- Azure OpenAI, Azure AI Search, Azure Functions, Cosmos DB, etc.

**Limitations**:
- Monthly credit limits (watch your spend!)
- No M365 integration (separate tenant from CDX)
- You manage your own costs — always `azd down` after demos
- Azure OpenAI may require separate access approval

**Best for these samples**: Azure Functions, Bicep/IaC deployments, Azure AI Search, Azure OpenAI — all Tier 3 (Deployable Template) samples.

---

## Which Environment for Which Pattern?

| Pattern Type | Use This | Notes |
|---|---|---|
| Copilot Studio agents | CDX (My Environment) | Copilot Studio included, 90-day lifetime |
| Power Automate flows | CDX | Premium connectors available |
| Azure Functions / Bicep / `azd` | Personal Azure sub | Use VS Enterprise credit |
| Azure AI Search / Azure OpenAI | Personal Azure sub | May need OpenAI access approval |
| Teams integration | CDX | Teams pre-configured |
| SharePoint data sources | CDX | Sample SharePoint sites available |
| Combined patterns (most practical issues) | CDX + Personal Azure | Custom connector or HTTP action bridges the two |

**Tip**: The combined approach (CDX for M365 + personal Azure for AI services) mirrors how real customer deployments work. Getting comfortable with this setup makes your customer demos more authentic.

---

## Free Trial Alternative (Non-Microsoft Employees)

If you don't have CDX or VS Enterprise access:
- **M365**: [Microsoft 365 Business Premium trial](https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-business-premium) (1 month)
- **Copilot Studio**: [Copilot Studio trial](https://copilotstudio.microsoft.com) (sign up with M365 account)
- **Azure**: [Azure free account](https://azure.microsoft.com/free/) ($200 credit for 30 days)
- **Power Apps Developer Plan**: [Free developer environment](https://powerapps.microsoft.com/developerplan/) (includes Dataverse)

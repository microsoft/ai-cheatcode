# Dataverse Schema — Issue #003: Prompt-Chained Triage

Create these two tables in your Dataverse environment before importing the flows.

---

## Table 1: Triage Playbooks (`cheatcode_playbooks`)

Stores the YAML playbook definitions for each triage category.

| Column | Display Name | Type | Required | Notes |
|--------|-------------|------|----------|-------|
| `cheatcode_playbookid` | Playbook ID | Unique Identifier (PK) | Auto | Primary key |
| `cheatcode_name` | Name | Text (200) | Yes | e.g., "IT Support Triage" |
| `cheatcode_category` | Category | Text (50) | Yes | Must match: `it-support`, `hr-requests`, `legal-intake` |
| `cheatcode_description` | Description | Text (500) | No | What this playbook handles |
| `cheatcode_yaml_content` | YAML Content | Multiline Text (10000) | Yes | The full YAML playbook definition |
| `cheatcode_version` | Version | Text (10) | No | e.g., "1.0" |
| `cheatcode_active` | Active | Yes/No | Yes | Default: Yes |

### Seed Data

After creating the table, add 3 rows using the YAML files from `data/playbooks/`:

| Name | Category | YAML Content |
|------|----------|-------------|
| IT Support Triage | `it-support` | Contents of `data/playbooks/it-support.yaml` |
| HR Requests Triage | `hr-requests` | Contents of `data/playbooks/hr-requests.yaml` |
| Legal Intake Triage | `legal-intake` | Contents of `data/playbooks/legal-intake.yaml` |

---

## Table 2: Triage Log (`cheatcode_triagelog`)

Audit trail of all classification results. Populated automatically by the classify-request flow.

| Column | Display Name | Type | Required | Notes |
|--------|-------------|------|----------|-------|
| `cheatcode_triagelogid` | Log ID | Unique Identifier (PK) | Auto | Primary key |
| `cheatcode_request_text` | Request Text | Multiline Text (4000) | Yes | Original user request |
| `cheatcode_category` | Category | Text (50) | Yes | Classification result |
| `cheatcode_confidence` | Confidence | Decimal | Yes | 0.0 to 1.0 |
| `cheatcode_entities` | Entities | Multiline Text (4000) | No | JSON string of extracted entities |
| `cheatcode_reasoning` | Reasoning | Text (500) | No | One-sentence explanation |
| `cheatcode_created_on` | Created On | Date/Time | Auto | Timestamp |

---

## Quick Setup in Dataverse

1. Go to [make.powerapps.com](https://make.powerapps.com) → Tables → New Table
2. Create `Triage Playbooks` with the columns above
3. Create `Triage Log` with the columns above
4. Add the 3 seed data rows to Triage Playbooks (copy from `data/playbooks/*.yaml`)
5. The Triage Log table will auto-populate as requests are classified

**Tip**: Use "Import data from Excel" if you prefer — export the playbook YAML files to a CSV first.

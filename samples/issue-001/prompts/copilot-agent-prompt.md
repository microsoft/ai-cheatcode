# GitHub Copilot Agent Mode Prompt — Issue #001

This is the prompt used to scaffold the PDF Agent in VS Code with GitHub Copilot Agent mode.

## The Prompt

```
Create an agent that analyzes large PDF documents from SharePoint.
The agent should:
1. Connect to a SharePoint site to access PDF files
2. Process and chunk large PDFs that exceed normal token limits
3. Answer natural language questions about the document contents
4. Support cross-document comparison queries
5. Deploy to Azure using Azure Functions and Bicep
6. Include a Teams manifest for publishing to M365 Copilot

Use Azure Developer CLI (azd) for deployment orchestration.
Include infrastructure as code with Bicep templates.
The system prompt should be easily customizable for different industries.
```

## What Copilot Generates

When you run this prompt in Agent mode, Copilot will typically scaffold:
- An Azure Functions project (Python or TypeScript)
- Bicep templates in an `infra/` folder
- An `azure.yaml` for azd
- A basic Teams manifest

## Notes

- The generated code may need debugging — this template contains the hardened version
- If Copilot generates TypeScript, the template uses [language TBD based on what works best]
- The Bicep templates may need region-specific adjustments

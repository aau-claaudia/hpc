# Responsible use of Mistral

This is a short how-to for everyday use of Vibe and AI Studio. The **binding rules** are in the [T&C](/mistral/terms-and-conditions/). 

## Choose the right workspace

[Apply for access](/mistral/how-to-access/) and classify your data under [AAU’s data classification](https://www.security.aau.dk/data-classification){target="_blank"} **before** you paste or upload anything.

- **Default workspace** — Level 1 data with **no** personal data
- **Dedicated workspace, no personal data** — API access
- **Dedicated workspace with personal data** — personal data, including Level 2 or 3 data that contains personal data (WorkZone number and a DPIA are required)

See [How to access Mistral](/mistral/how-to-access/) and [T&C §3](/mistral/terms-and-conditions/#3-data-classification-personal-data-and-dedicated-workspaces).

## Before you paste or upload

Send only what the task needs. Clean the data **outside** Mistral: anonymise, pseudonymise, or mask names and other direct identifiers.

Examples: names, emails, phone numbers, addresses, and other unique IDs that can identify a person on their own.

Do not process **CPR numbers** in Mistral as a rule. Use a project ID, case ID, or other code, and keep the mapping table **outside** Mistral.

If you cannot anonymise or pseudonymise, and you are working with **Level 3 data** or **sensitive personal data**, work only from an **AAU-managed device**.

Full rule: [T&C §4](/mistral/terms-and-conditions/#4-data-minimisation-and-identifiers).

## Prompt, then check the answer

You decide what goes into Mistral. You are responsible for what you do with the output.

- Say clearly what you want, and include only the data the task needs.
- Ask the model to point back to the source text when that helps you check.
- Check the output against the **underlying data**. Models can invent sources, skip information, or give wrong, biased, or incomplete answers.
- Do not follow a fluent answer uncritically. That is **automation bias**.

Mistral is an assisting research tool only. Output never stands alone. A person must check every answer before you use it in research.

See [T&C §2](/mistral/terms-and-conditions/#2-permitted-purpose) and [T&C §8](/mistral/terms-and-conditions/#8-output-review-and-automation-bias).

## Using the API

Keys are **personal**. Do not share them.

**How to rotate a key:** In AI Studio, select the correct workspace. Go to **API Keys** → **My API keys** and use **Rotate key**. Rotate at least every **30 days**.

A person must check API output before it leads to actions, classifications, or research conclusions.

When it is relevant for your methods, note which model and version you used (for example `mistral-medium-latest`).

Do not connect unapproved plugins, connectors, or MCP servers unless they meet the conditions in the T&C.

Binding rules: [T&C §5](/mistral/terms-and-conditions/#5-api-keys), [T&C §6](/mistral/terms-and-conditions/#6-integrations-and-third-party-tools), and [T&C §9](/mistral/terms-and-conditions/#9-traceability-and-documentation). Practical token guidance: [Tokens and seats](/mistral/guides/ai-studio/tokens-and-seats/).

## Chats last 90 days

Chat history is deleted after **90 days**. Do not use Vibe as a project archive. Store what you need in **AAU systems** before the 90 days end.

See [T&C §10](/mistral/terms-and-conditions/#10-chat-history-and-retention).

## Related pages

| Topic | Where to go |
|---|---|
| Binding rules | [T&C](/mistral/terms-and-conditions/) |
| Login and workspaces | [How to access Mistral](/mistral/how-to-access/) |
| Data classification | [AAU data classification](https://www.security.aau.dk/data-classification){target="_blank"} |
| Approved AI tools | [Generative AI and Security](https://www.security.aau.dk/gen-ai){target="_blank"} |
| Project registration | [Grants and Contracts registration forms](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx){target="_blank"} |

# Responsible use of Mistral

This page explains how to use Mistral Vibe and AI Studio in practice at AAU. The binding rules are in the [Terms and Conditions](/mistral/terms-and-conditions/).

Mistral is approved for use with **Level 1, 2, and 3 data** under [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank"}, provided you follow the guidelines below.


## 1. Choose the right workspace

<!-- 1 --><!-- 10 -->

| Workspace | What you may process | Api Keys
|---|---|---|
| **Default workspace** (Vibe and AI Studio after SSO login) | **Level 1 only** | No |
| **Dedicated workspace** (requested through the Serviceportal) | **Up to Level 3** | Yes |



## 2. Use Mistral only as an assisting research tool

<!-- 1 --><!-- 3 --><!-- 5 -->

Mistral is a **research-supporting tool**. It is not a decision-maker and not a production system.

- Do not use it to **make decisions about people** (data subjects).
- Do not let AI output **stand alone**. Check every important answer yourself before you use it in research or include it in research conclusions.
- Use it only for the **research purpose and processing activity** it was assessed for. Do not reuse it across projects or for a new purpose without a new assessment.
- Keep the work tied to the relevant **project, case, or dataset**.

## 3. Prepare data before you paste or upload

<!-- 2 --><!-- 5 --><!-- 6 --><!-- 7 --><!-- 8 --><!-- 14 -->
Where possible, **anonymise, pseudonymise, or mask direct identifiers before** the data is transferred to Mistral. Do this **outside** Mistral.

**Send only what the task needs.** If a short extract is enough, do not send the full dataset, extra variables, or extra identifiers.

**Remove or mask direct identifiers** wherever you can, for example:

- Names, email addresses, phone numbers, and physical addresses
- Other unique IDs that can identify a person on their own

**Do not process CPR numbers in Mistral as a rule.** If you exceptionally need a unique ID, use a **project ID, case ID, or other code**. Keep the table that maps those codes back to real identities **outside** Mistral.

When you process **Level 3 data**, or **sensitive personal data that has not been anonymised or pseudonymised**, you may only work from an **AAU-managed device**.


## 4. Prompt, then check the answer

<!-- 4 --><!-- 12 --><!-- 17 --><!-- 18 -->

You decide what goes into Mistral. You are responsible for what you do with the answer.

When you prompt:

- Say clearly what you want, and include only the data the task needs.
- Stay within the assessed research purpose. Do not ask the model to go beyond it.
- Ask the model to point back to the source text when that helps you check the answer.

Then check the output against the **underlying data**. Models can invent sources, skip relevant information, or give **wrong, biased, or incomplete** answers.

Knowing that AI can be wrong is not enough. **Automation bias** means you may still trust a fluent answer too quickly. Do not let the wording replace your own judgement.

Do not use:

- jailbreak-style or manipulative prompts
- input that contains more personal data than necessary
- output that goes beyond the intended purpose

You must be able to **explain** an answer by pointing to the source data, the prompt, the output, and the research context.


## 5. Using the API

<!-- 9 --><!-- 10 --><!-- 19 --><!-- 20 -->

**Keys are personal.** Do not share them. You are responsible for all activity under your key.

- Rotate the key every **30 days**.
- We will **close keys** that are not rotated in time, and when a project ends, you leave AAU, your role changes, or misuse is suspected.
- If a key may have leaked, revoke it in AI Studio and notify us as soon as possible.

**How to rotate a key:** In AI Studio, select the correct workspace. Go to **API Keys** → **My API keys** and use **Rotate key**.

**Human-in-the-loop:** API output must not automatically trigger actions, classifications, or research conclusions. A person must check the output first.

When it is relevant for method description, reproducibility, or later review of research results, **document which model and model version** were used for example `mistral medium 3.5`, the date, and how you used the output. Model names are listed on Mistral’s [Models](https://docs.mistral.ai/getting-started/models/models_overview/){target="_blank"} page.

!!! important "API keys with Level 2 or 3 sensitive personal data"
    When you use an API key with **Level 2 or Level 3 data** that contains **sensitive personal data**, you must ensure that the system or environment from which the key is used logs **who** accessed **which data** and **when**.


## 6. Connecting other tools

<!-- 21 -->

Integrations let you connect Mistral with other platforms, like plugins, connectors, or external tools. Only connect Mistral to third-party tools if they are approved and meet the required conditions.

- You may use an **MCP server** if it is managed by AAU, has the same (or higher) data classification approval, is covered by a proper data processing agreement and technical/organisation security.




## 7. Keep what you need — chats are deleted after 90 days

<!-- 13 --><!-- 14 --><!-- 20 -->

Chat history is deleted automatically after **90 days**. Do not use Vibe as a project archive.

If you need the prompt, the output, or a record of how you used Mistral, store it appropriately in **AAU systems before the 90 days end**.


## 8. If Mistral is unavailable, or someone exercises their rights

<!-- 15 --><!-- 16 -->

Do not design your research so that Mistral being down **in itself** has consequences for data subjects. Continue from the underlying data, with ordinary methods.

Requests from data subjects (for example access or erasure) follow **AAU’s ordinary procedures**. The research project handles them together with the relevant administrative functions, including Grants and Contracts.


## Related pages

| Topic | Where to go |
|---|---|
| Binding rules | [Terms and Conditions](/mistral/terms-and-conditions/) |
| Login and API access | [How to access Mistral](/mistral/how-to-access/) |
| Data classification | [AAU data classification](https://www.security.aau.dk/data-classification){target="_blank"} |
| Approved AI tools | [Generative AI and Security](https://www.security.aau.dk/gen-ai){target="_blank"} |
| Project registration | [Grants and Contracts registration forms](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx){target="_blank"} |
| Research data | [AAU data management recommendations](https://www.researcher.aau.dk/guides/research-data/data-management){target="_blank"} |

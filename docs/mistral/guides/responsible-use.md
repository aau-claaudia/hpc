# Responsible use of Mistral

This is our instruction to researchers on how Mistral Vibe and AI Studio may be used at Aalborg University. The binding rules are in the [Terms and Conditions](/mistral/terms-and-conditions/).

Mistral is approved for **Level 1, 2, and 3** under [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank"}.

---

## Use Mistral only as an assisting research tool
<!-- 1 -->

Mistral may only be used as a **research-supporting and assisting tool**.

- Do not use Mistral to **make decisions about data subjects**.
- AI output must **never stand alone**.
- All **significant output** must be reviewed professionally and checked by a person before it is used in research or included in research conclusions.

<!-- 1 -->
For projects working with level 3 data a **data protection impact assessment (DPIA)** must have been prepared for the research project, and it must include the project's use of AI. This is done as part of the project's registration with Grants and Contracts.


## Stay within the assessed purpose
<!-- 3 --><!-- 5 -->
Use Mistral only within the **specific research purpose** and the **specific processing activity** for which the use has been assessed.
<!-- 3 -->
Do not use the solution more broadly, **across projects**, or for **new purposes** without a separate assessment.

## Good data practice, minimisation, and data ethics
<!-- 2 --><!-- 5 --><!-- 7 --><!-- 14 -->

Process in Mistral **only the information that is necessary** for the specific research purpose.

- Prefer **bounded datasets or extracts** over larger volumes of data, if the purpose can be met with less. <!-- 7 -->
- Do not upload extra variables, full extracts, or identifiers that the task does not require. <!-- 2 --><!-- 5 -->
- The 90-day deletion of chat history reduces stored prompts and output. It does **not** replace data minimisation. Still avoid inserting more personal data than necessary. <!-- 14 -->

##  Before you transfer data to Mistral
<!-- 6 --><!-- 8 -->

Where possible, **anonymise, pseudonymise, or mask direct identifiers before** the data is transferred to Mistral. Do this outside the service, not in the prompt afterwards.

Remove or replace, for example, names, email addresses, phone numbers, physical addresses, and other unique IDs.

<!-- 8 -->
**Civil registration numbers (CPR) should as a rule not be processed in Mistral.** If unique identification is exceptionally necessary, use a **project ID, case ID, or other pseudonymous key**. Store the key table that maps those keys back to real identities **outside** Mistral.

## Sensitive data only in a dedicated workspace
<!-- 1 --><!-- 10 -->

**Level 2 or Level 3 data** may only be processed in a **dedicated workspace**. It is not allowed in Vibe or in the default workspace.

## Prompting, source checking, and critical review
<!-- 4 -->

You control what is sent to Mistral. Prompt correctly, check the sources, and review output critically.

When you prompt:

- State the task clearly and include only the data the task needs.
- Keep the prompt within the **assessed research purpose**. Do not ask the model to go beyond that purpose.
- Ask the model to point back to the source text where that helps you check the answer.
- Check claims, citations, classifications, and figures against the **underlying data sources**. Models may invent sources or skip relevant information.

Be aware of:

- **Manipulative or jailbreak-style prompts** that try to push the model outside its intended use
- **Inappropriate input**, including personal data or identifiers that are not necessary
- **Output that exceeds the intended purpose** — do not use such output

You remain responsible for the interpretation and use of the output.

---

## Erroneous output and automation bias
<!-- 17 --><!-- 18 -->

Mistral can give **erroneous, biased, or incomplete** answers. You are responsible for critical review, source checking, and professional validation of output.

<!-- 18 -->
Knowing that AI can be wrong is not enough. **Automation bias** means you may still follow output uncritically. Stay aware of this and do not let the model’s fluency replace your own professional judgement.

---

## Human-in-the-loop in API workflows
<!-- 19 -->

If you call Mistral through the API, build in **human-in-the-loop**. Model output must not automatically lead to actions, classifications, or research conclusions without a person checking the output.

---

## Traceability and documentation
<!-- 12 --><!-- 20 -->

You must be able to **explain and verify** output by referring to:

- the underlying data sources
- the prompt
- the output
- the specific research context

<!-- 20 -->
When it is relevant for method description, reproducibility, or later review of research results, document:

- the product (Vibe or AI Studio)
- the **model name and version** (or the API identifier, for example `mistral-large-latest`)
- the date, and a short description of how the output was used

In AI Studio, the model name and API identifier are shown on the [Models](https://docs.mistral.ai/models){target="_blank"} page.
---

## API keys
<!-- 9 -->
API keys are **personal**. Do not share them. You are responsible for all activity under your key.

- Rotate keys on a **30-day** cycle. Replace a key before it expires.
- CLAAUDIA will **close keys that have not been rotated in time**.
- Keys will also be closed when a project ends, when you leave AAU, when your **role changes**, or if incorrect or unauthorised use is suspected.
- If a key may have leaked, revoke it in AI Studio and notify us as soon as possile.

How to rotate a key: Click the rotate key button in then **My API keys** under API Keys in AI studio. Make sure to be in the correct workspace. 


## Do not combine Mistral with unapproved tools
<!-- 21 -->

Do not combine Mistral with **unapproved** third-party models, plugins, integrations, or tools unless they are **AAU-approved solutions** with at least the same approval of data classification as Mistral. 

---

## Chat history is deleted after 90 days
<!-- 13 --><!-- 14 -->

Automatic deletion of chat history is set to **90 days**.

<!-- 13 -->
If you need to keep prompts, output, or other records, save them in an **approved AAU system before the 90 days end**. After that, the chat data is deleted.

<!-- 14 -->
The 90-day period reduces historical prompts and output. You must still minimise data and avoid inserting more personal data than necessary. Do not use Vibe as a project archive.

---

## Do not make data subjects depend on Mistral
<!-- 16 -->

Do not organise research processes so that temporary unavailability of Mistral **in itself** can have consequences for data subjects.

If the service is down, continue from the underlying data, with ordinary research methods, or with manual procedures.

---

## Rights of data subjects
<!-- 15 -->

The rights of data subjects are handled according to **AAU’s ordinary procedures**. In research projects this is typically done by the **research project together with the relevant administrative functions, including Grants and Contracts**.

---

## Related pages

| Topic | Where to go |
|---|---|
| Binding rules | [Terms and Conditions](/mistral/terms-and-conditions/) |
| Login and API access | [How to access Mistral](/mistral/how-to-access/) |
| Data classification | [AAU data classification](https://www.security.aau.dk/data-classification){target="_blank"} |
| Approved AI tools | [Generative AI and Security](https://www.security.aau.dk/gen-ai){target="_blank"} |
| Project registration | [Grants and Contracts registration forms](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx){target="_blank"} |
| Research data | [AAU data management recommendations](https://www.researcher.aau.dk/guides/research-data/data-management){target="_blank"} |

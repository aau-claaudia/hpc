---
icon: lucide/scale
---

<!--
Security instruction coverage (1–21)
1  §1 Who may use; also §8. Guide: assisting tool
2  §4 Data minimisation. Guide: good data practice
3  §2 Permitted purpose. Guide: stay within assessed purpose
4  Guide: prompting, source checking, and critical review (instruction; not a terms clause)
5  §2 last paragraph; §4 first paragraph. Guide: assessed purpose + minimisation
6  §4 anonymise before transfer. Guide: anonymise before transfer
7  §4 bounded datasets. Guide: good data practice
8  §4 CPR. Guide: anonymise / CPR
9  §5 API keys. How to access §2. Guide: API keys
10 §5 first paragraph. How to access warning + §2. Guide: API keys
12 §9 Traceability. Guide: traceability and documentation
13 §10 Chat 90 days. Vibe page. Guide: chat history
14 §10 last paragraph. Vibe page. Guide: chat history + minimisation
15 §12 Rights of data subjects. Guide: rights
16 §11 Research must not depend on Mistral. Guide: do not make data subjects depend
17 §8 Output, review. Guide: erroneous output
18 §8 automation bias. Guide: automation bias
19 §8 API human-in-the-loop. AI Studio page. Guide: human-in-the-loop
20 §9 last paragraph. Guide: document model and version
21 §6 Integrations and approved solutions. Guide: unapproved tools
-->

##### Use of Mistral Vibe and AI Studio at Aalborg University (AAU)


## 1. Who may use Mistral at AAU

Mistral Vibe and AI Studio are provided by Aalborg University (AAU) for **academic research activities**. The services must not be used for any teaching, commercial or private purposes.


<!--
NOTE FOR REVISION:
Add reference or instructions on where and how to obtain or complete a suitable DPIA for Mistral/AI use at AAU. Clarify the process or link to AAU's DPIA documentation for researchers.
-->
## 2. Permitted purpose

<!-- 3 -->
Mistral may only be used within the **specific research purpose** and the **specific processing activity** for which the use has been assessed. It must not be used more broadly, across projects, or for new purposes without a separate assessment.

<!-- 5 -->
Use of Mistral should, as far as possible, be linkable to the relevant project, case, or underlying data.

<!-- 1 -->
Mistral may only be used as a **research-supporting and assisting tool**. It must not be used to make decisions about data subjects, and AI output must **never stand alone**. All outputs must be reviewed professionally and checked by a person before it is used in research or included in research conclusions.

## 3. Data classification, Personal data and dedicated workspaces

Mistral may be used with data classified as **Level 1, Level 2, or Level 3** under [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank"}. Users are personally responsible for classifying their data correctly before submitting any content to the service.

**Level 1 data without any personal data** may be used in the default workspace in both Vibe and AI Studio.

**Personal data** and **Level 2 or Level 3 data** may only be processed in a **dedicated workspace** created by us. This type of data must never be entered into the default workspace.

Projects involving **personal data** is required to register the project with the [Grants and Contracts](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx){target="_blank"} and make a **data protection impact assessment (DPIA)**  in collaboration with Grants and Contracts; it must include the project's use of AI.


## 4. Data minimisation and identifiers

<!-- 2 -->
<!-- 5 -->
<!-- 7 -->
Users must follow good data practice, data minimisation, and data ethics by ensuring that only information **necessary for the specific research purpose** is processed in Mistral; wherever possible, use **bounded datasets or extracts of datasets** instead of larger volumes of data if the purpose can be achieved with less.

<!-- 6 -->
Prior to transferring data to Mistral, users shall, to the extent practicable, anonymise, pseudonymise, or otherwise mask direct identifiers. In circumstances where anonymisation or pseudonymisation is not feasible and the data being processed qualifies as **Level 3 data** or **sensitive personal data**, processing is permitted solely on Mistral from an **AAU-managed device**.

<!-- 8 -->
**Civil registration numbers (CPR) should as a rule not be processed in Mistral.** If unique identification is exceptionally necessary, use a project ID, case ID, or other pseudonymous key instead. The key table must be stored **outside** Mistral.


## 5. API keys

<!-- 9 -->
API keys issued through AI Studio are **personal and must not be shared**. Users are responsible for all activity performed using their personal API key.

When you use an API key with **Level 2 or Level 3 data** that contains **sensitive personal data**, you must ensure that the system or environment from which the key is used logs **who** accessed **which data** and **when**. This logging is not required when the API is used with **Level 1 or Level 2 data** that only contains **ordinary personal data**.

<!-- 9 -->
All API keys must be rotated at intervals not exceeding **30 days**. API keys must also be deactivated upon project completion, termination of the user's affiliation with AAU, any change in the user's role, or if there is any suspected improper or unauthorised use. If you suspect that an API key has been compromised or misused, you must immediately revoke the key and notify us. Please note: AAU reserves the right to revoke any API key at any time.

## 6. Integrations and third-party tools

<!-- 21 -->
Integrations are used to exchange data to or from another platform. Connecting Mistral to unapproved third-party models, plugins, connectors, integrations, or tools is not permitted unless the conditions below are met.

- Mistral may be connected to an MCP server if the server is managed by AAU, approved for at least the same data classification, and governed by a valid data processing agreement.

- When you are working with **Level 2 or Level 3 data** that contains **sensitive personal data** and this data is transferred to or processed on the platform you integrate with, you must also ensure that the following are in place:

    - **Agreement basis:** typically a data processing agreement or a confidentiality agreement that covers the processing performed in the integration.
    - **Technical and organisational security** on the platform being integrated with, commensurate with the intended processing based on the data classification level and/or the type of personal data.


## 7. Shared libraries

Users who upload documents to a shared library are solely responsible for ensuring that all library members are authorised to access the uploaded material. Users must not invite individuals to a shared library unless those individuals are permitted to access all documents contained within it.


## 8. Output, review, and automation bias

<!-- 17 -->
<!-- 1 -->
Mistral can produce **erroneous, biased, or incomplete** answers. The user is responsible for critical review, source checking, and professional validation of output.

<!-- 1 -->
AI output must never stand alone. All outputs must be assessed professionally and checked by a person before it is used in research or included in research conclusions.

<!-- 18 -->
Users are hereby notified of the risk of **automation bias**, defined as the tendency to accept or act upon AI-generated output without sufficient critical assessment, despite awareness of potential inaccuracies or errors in AI responses. Users are obliged to exercise independent professional judgment and must not rely on AI output uncritically.

<!-- 19 -->
For **API workflows**, human-in-the-loop must be built in. Model output must not automatically lead to actions, classifications, or research conclusions without human control of the output.


## 9. Traceability and documentation

<!-- 12 -->
Output must be **explainable and verifiable** by reference to the underlying data sources, the prompt, the output, and the specific research context.

<!-- 20 -->
When it is relevant for method description, reproducibility, or later review of research results, you must **document which model and model version** were used.


## 10. Chat history and retention

<!-- 13 -->
Automatic deletion of chat history is set to **90 days**. 
Data that needs to be retained must be stored appropriately in **AAU systems before the end of the 90 days**, after which the chat data is deleted.
<!-- 14 -->
The 90-day deletion period reduces the amount of historical prompts and output. Users must still minimise data and **avoid inserting more personal data than necessary**.


## 11. Research must not depend on Mistral

<!-- 16 -->
Research processes must not be organised so that temporary unavailability of Mistral in itself can have consequences for data subjects.

The service is provided **"as is"** without guarantees of availability, performance, or uptime. We receive operational notices from the supplier. Where possible, users will be informed of major changes **6 weeks in advance**. Updates, upgrades, and scheduled maintenance are not considered major changes.

### Seat availability

Access to Mistral is subject to the availability of user seats. AAU makes no representations or warranties regarding the continuous availability of seats, and access for all researchers at all times cannot be assured. AAU reserves the right to revoke or reallocate seats due to user inactivity, in order to maintain equitable access to the service for all eligible AAU researchers.


## 12. Rights of data subjects

<!-- 15 -->
The rights of data subjects are handled according to **AAU’s ordinary procedures**. In research projects this is typically done by the research project together with the relevant administrative functions, including Grants and Contracts.


## 13. Compliance with Mistral terms

Use of the services must comply with the applicable [terms and conditions](https://chat.mistral.ai/legal/terms) of Mistral AI in addition to these AAU-specific terms.


## 14. Support and responsibilities

Claaudia are responsible for the institutional setup of Mistral at AAU. This includes managing access, workspaces, and token quotas. For all technical questions about the Mistral products themselves — including API behaviour, model output, interface issues, and bugs — users must contact **Mistral's support** directly.


## 15. Fair usage

AI Studio workspaces are assigned a standard monthly usage quota in order to promote fair usage and ensure access for AAU users. AAU may adjust the monthly quota at any time if needed.


## 16. Changes to Terms

AAU may update these Terms and Conditions periodically. Users will be informed of significant changes.


## 17. Suspension

Access may be suspended or removed if these terms, AAU policies, or Mistral AI's own terms are violated.

## 18. Additional workspace member 
The workspace applicant shall ensure that all **additional workspace members** are duly informed of, understand, and agree to comply with all terms and conditions set forth herein, and that such members are duly authorized to access and process any data contained within the workspace.

*Effective date: 01/09/2026 — Version 2.1*

---
icon: lucide/lock-keyhole-open
---


Access to Mistral is granted in two stages — the base login works for both Vibe and AI Studio interfaces, while a **dedicated workspace** is required for API keys and for all work with Level 2 and 3 data.

!!! warning "Sensitive data only in a dedicated workspace"
    **Level 2 or 3 data may only be processed in a dedicated workspace.** It must not be used in Vibe or in the default workspace.

    API access requires that the research project or processing activity has been assessed by Grants and Contracts.

    Register the project with [Grants and Contracts](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx){target="_blank"} and apply through the [Serviceportal](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=b3a364e5c3a336d4f0f3041ad001316e){target="_blank"}. See [Responsible use of Mistral](/mistral/guides/responsible-use/).


## Access steps

| Step | What you get | Who needs it |
|---|---|---|
| **Vibe & AI Studio (default workspace)** | Access to Vibe at [chat.mistral.ai](https://chat.mistral.ai) and the AI Studio console at [console.mistral.ai](https://console.mistral.ai), including the Playground, Document AI and Audio transcription. **Level 1 data only.** | Anyone who wants to use Mistral for writing, research assistance, summarisation, model testing, or prompt refinement with Level 1 data. |
| **Dedicated workspace** | A project workspace created by us. Required for API keys and for **Level 2 or 3 data**. Create API keys, call models from code, and work in the Playground inside that workspace only. | Researchers who need API access, or who will process Level 2 or 3 data. |

---

## Step 1 — Log in (Vibe and AI Studio without a dedicated workspace)

All AAU **academic staff** can log in immediately via SSO. No application needed. This access is for **Level 1 data only**.

??? info "Not employed as academic staff?"
    Access is granted based on the academic staff role at AAU. If you hold a different employment category — such as technical, administrative, or external staff — but need access to support ongoing academic research activities, you must request access manually.

    Contact us through the [AAU Serviceportal](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e) and include a short description of:

    - your role and department
    - which research project or activity you are supporting
    - why access to Mistral is needed for that work

    We will review the request and confirm whether access can be granted.

1. Go to the [Mistral login page](https://v2.auth.mistral.ai/login)
2. Enter your AAU email address and click **Continue**.

    ![Mistral login page](/assets/img/mistral/login/m_login_1.png)

3. Click **Continue with AAU – SSO**.

    ![Mistral login page](/assets/img/mistral/login/m_login_2.png)

4. Log in with your AAU credentials (e.g. `ab12cd@domain.aau.dk`).
5. Approve the login using multi-factor authentication (MFA). If you have not set up MFA, see the [AAU MFA guide](https://www.en.its.aau.dk/instructions/mfa).


After completing these steps, you have access to:

- **Vibe** at [chat.mistral.ai](https://chat.mistral.ai)
- **AI Studio Playground** at [console.mistral.ai](https://console.mistral.ai) (default workspace, without API keys)



---

## Step 2 — Request a dedicated workspace
A dedicated workspace is required if you need **API keys**, or if you will process **Level 2 or 3 data**.


### Prerequisites

Complete Step 1 and verify that you can log in to Mistral before applying.

If you are working with level 2 or 3 data then have the **WorkZone case number** ready from your project registration and the data protection impact assessment (DPIA) of the project. <!-- 1 --><!-- 10 -->

### How to apply

1. Apply through the [**Mistral workspace request form**](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=b3a364e5c3a336d4f0f3041ad001316e) in the AAU Serviceportal.
2. For project with level 2 and 3 data: Include the **WorkZone case number**.
3. We will review your request. If approved, a dedicated workspace will be created for your project.
4. You will receive a notification when the workspace is ready.


### Finding your workspace

Once a workspace is created for you:

1. Log in to AI Studio.
2. Click the **Default Workspace** selector in the bottom-left corner.
3. Select your named workspace from the dropdown.

![Mistral create workspace](/assets/img/mistral/login/m_create_workspcae.png)

---


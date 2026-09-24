---
icon: lucide/lock-keyhole-open
---

Access it granted though the [Mistral access form](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=b3a364e5c3a336d4f0f3041ad001316e) in the AAU Serviceportal. 

Different access options are available, each with their own specific requirements depending on your project needs:

| Option | What you get | Data allowed | What you must provide | API keys? |
|---|---|---|---|---|
| **Default workspace** | Access to Vibe at [chat.mistral.ai](https://chat.mistral.ai) and AI Studio at [console.mistral.ai](https://console.mistral.ai), including the Playground, Document AI and Audio transcription. | **Level 1 data with no personal data** | Consent, and select the default workspace | No |
| **Dedicated workspace, no personal data** | A closed project workspace. Full access to Vibe, AI Studio, and the API. | **No personal data.** | Request a dedicated workspace | Yes |
| **Dedicated workspace with personal data** | A closed project workspace. Full access to Vibe, AI Studio, and the API. | **Personal data**, including Level 2 or 3 data that contains personal data | **WorkZone case number**, and confirmation that you have prepared a **DPIA** together with [Grants and Contracts](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx){target="_blank"} | Yes |

<p style="font-size: 0.92em; margin-top: -1.5em; color: #555;">
  <em>
    Not sure which data type you have?  
    <a href="https://www.security.aau.dk/data-classification" target="_blank">
      Read more about the AAU data classification here
    </a>.
  </em>
</p>



When you have submitted the form, CLAAUDIA will review your application. When your project have been approved you can login by: 

## For the Default Workspace

1. Go to the [Mistral login page](https://v2.auth.mistral.ai/login)
2. Enter your AAU email address and click **Continue**.

    ![Mistral login page](/assets/img/mistral/login/m_login_1.png)

3. Click **Continue with AAU – SSO**.

    ![Mistral login page](/assets/img/mistral/login/m_login_2.png)

4. Log in with your AAU credentials (e.g. `ab12cd@domain.aau.dk`).
5. Approve the login using multi-factor authentication (MFA). If you have not set up MFA, see the [AAU MFA guide](https://www.en.its.aau.dk/instructions/mfa).

    (If you are already logged into your AAU account in your browser, you will not need to approve.)

After login:

- **Vibe** at [chat.mistral.ai](https://chat.mistral.ai)
- **AI Studio** at [console.mistral.ai](https://console.mistral.ai)

If you applied for the **default workspace**, use that workspace only.

## For the Dedicated Workspace

Dedicated workspaces can *only* include the users that have approved the Terms and Conditions, these include:

1. The **Dedicated Workspace** applicant, and
2. Any user with an approved *Default Workspace*.

### Steps:
1. Submit [an application](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=b3a364e5c3a336d4f0f3041ad001316e) for a **Dedicated Workspace**.
2. Each additional member must submit an application for a **Default Workspace**.
3. CLAAUDIA will grant each member access to Mistral.
4. All project members **must log into the Mistral platform** (See log in process above).
5. The project applicant should inform CLAAUDIA when all project members have logged into Mistral, in the ServicePortal case.
6. CLAAUDIA will add all project members to the **Dedicated Worskspace**.


### Finding your dedicated workspace

1. Click the **Default Workspace** selector in the bottom-left corner.
2. Click the **# workspace** settings.
3. Select your named workspace from the dropdown.
4. Confirm in the bottom-left corner that the correct workspace is selected.

![Mistral create workspace](/assets/img/mistral/Mistral-change-workspace.png)

### FAQ

??? question "Why can’t I log in with AAU SSO directly?"

    Direct SSO login is **disabled**. Everyone must apply first, including for the **Default Workspace**.

    That is so we can record consent, assign the right workspace, and — for **dedicated workspace with personal data** — check that a WorkZone number and DPIA are in place before anyone starts working.

    Apply through the [Mistral access form](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=b3a364e5c3a336d4f0f3041ad001316e). After we approve the request, log in with AAU SSO as usual.

??? question "I used to log in without applying. Do I need to apply now?"

    Yes. Previous walk-in access no longer works. Submit the form even if you have used Mistral before.

??? question "After I am approved, do I still use AAU SSO?"

    Yes. The form only grants access. You still log in with **Continue with AAU – SSO** and your AAU credentials.
# Logging in to AI Studio

AI Studio is accessed at [console.mistral.ai](https://console.mistral.ai){target="_blank"} using your AAU credentials. No separate account or password is needed.

!!! warning "Data classification depends on your workspace"
    The **default workspace** may only be used with **Level 1** data under [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank"}. **Level 2 or 3 data** may only be processed in a **dedicated workspace** and must never be entered in the default workspace. See [How to access Mistral](/mistral/how-to-access/) and [Responsible use of Mistral](/mistral/guides/responsible-use/).


## Step 1 — Go to the login page

Go to [console.mistral.ai](https://console.mistral.ai){target="_blank"}

## Step 2 — Enter your AAU email

Enter your AAU email address (e.g. `ab12cd@domain.aau.dk`) and click **Continue**.

![AI Studio email entry](/assets/img/mistral/login/m_login_1.png){style=max-height:600px;}


## Step 3 — Select AAU SSO

Click **Continue with AAU – SSO** to be redirected to the AAU login page.

![AI Studio SSO selection](/assets/img/mistral/login/m_login_2.png){style=max-height:600px;}


## Step 4 — Log in with AAU credentials

Log in with your AAU credentials (for example `ab12cd`) and approve the login using multi-factor authentication (MFA).

![AAU login page](/assets/img/mistral/vibe/login/login4.png){style=max-height:600px;}


## Step 5 — Select your workspace

After logging in you will land on the AI Studio home screen.

!!! warning "Select the dedicated workspace for Level 2 or 3 data"
    If you will process Level 2 or 3 data, you **must** select your dedicated project workspace before you enter any content. The default workspace is Level 1 only.

    If you do not yet have a dedicated workspace, apply through the [Serviceportal](/mistral/how-to-access/#step-2-request-a-dedicated-workspace). API keys are issued only after Grants and Contracts has assessed the project and a WorkZone case number has been provided.

Click the organisation and workspace name in the top-left corner and select your named workspace.

![AI Studio workspace selector](/assets/img/mistral/login/m_create_workspcae.png){style=max-height:600px;}


!!! info "MFA not set up?"
    If you have not set up multi-factor authentication, see the [AAU MFA guide](https://www.en.its.aau.dk/instructions/mfa){target="_blank"} before logging in.

!!! info "Need a dedicated workspace?"
    A dedicated workspace is required for API keys and for Level 2 or 3 data. To obtain one you must register the project with Grants and Contracts, obtain a WorkZone case number, and apply through the Serviceportal. A WorkZone case number is also required before an API key is issued. See [How to access Mistral](/mistral/how-to-access/).

!!! info "Access issues?"
    If you cannot log in, contact us via the [service portal](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328){target="_blank"}.

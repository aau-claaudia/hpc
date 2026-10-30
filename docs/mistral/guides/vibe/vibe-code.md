# Vibe Code

Vibe Code is Mistral’s coding assistant. It can run in your **terminal (CLI)**, in the **VS Code extension** or another coding inferece using the OpenAi API scheme. It can read and write files in your project, run commands, and help with coding tasks under your supervision.

For product details, see Mistral’s [Vibe Code documentation](https://docs.mistral.ai/vibe/code){target="_blank"}.

!!! warning "Do not sign in with Launch browser"
    Creating API keys **directly through Vibe Code** is disabled at AAU. If you choose **Launch browser**, authorisation will fail with *This workspace can't be used*.

    Create an API key in [AI Studio](https://console.mistral.ai/api-keys){target="_blank"} and paste it into the CLI or the VS Code extension instead.

API keys require a **dedicated workspace**. Apply via [How to access Mistral](/mistral/how-to-access/) if you do not have one yet. Keys are **personal** — do not share them, and rotate them at least every **30 days**. See [Responsible use](/mistral/guides/responsible-use/#using-the-api) and in the [terms and conditions](/mistral/terms-and-conditions/#5-api-keys).


## Create an API key in AI Studio

1. [Apply for a dedicated workspace](/mistral/how-to-access/) if you do not already have API access.
2. Log in to [AI Studio](/mistral/guides/ai-studio/getting-started/).
3. Select your **named project workspace** (not the default workspace).
4. Open [API Keys](https://console.mistral.ai/api-keys){target="_blank"} and create a key.
5. Copy the key and store it securely. You will only see the full key once.

Treat the key like a password. Do not commit it to Git, paste it into chats, or share it in notebooks.


## Why Launch browser does not work

The CLI and the VS Code extension offer **Launch browser** as the recommended sign-in. That flow tries to issue a Vibe Code key in the workspace. At AAU that option is turned off due to a malfunction of the Vibe API key, so the browser page looks like this:

![Vibe Code browser authorisation is not available in the AAU workspace](/assets/img/mistral/vibe_code/Mistral_API_Browser_auth.png){style=max-height:600px;}

Cancel that screen and use an API key from AI Studio instead.


## Add the key in the CLI

Install the CLI if you have not already. Mistral’s installer is documented in [Install and setup](https://docs.mistral.ai/vibe/code/cli/install-setup){target="_blank"}:

```bash
curl -LsSf https://mistral.ai/vibe/install.sh | bash
```

Then, in your project folder:

```bash
vibe --setup
```

On first run you get a sign-in menu. **Do not** choose **Launch browser**. Select **Use an API key** and paste the key from AI Studio.

![Vibe Code CLI: choose Use an API key](/assets/img/mistral/vibe_code/Mistral_API.png){style=max-height:600px;}

You can run the setup again at any time with `vibe --setup`.

You can also set the key in your environment:

```bash
export MISTRAL_API_KEY="your_mistral_api_key"
```

On Windows PowerShell:

```powershell
$env:MISTRAL_API_KEY="your_mistral_api_key"
```

## Related pages

| Topic | Where to go |
|---|---|
| Apply for API access | [How to access Mistral](/mistral/how-to-access/) |
| Log in to AI Studio | [Logging in to AI Studio](/mistral/guides/ai-studio/getting-started/) |
| Key rotation and quotas | [Tokens and seats](/mistral/guides/ai-studio/tokens-and-seats/) |
| Binding rules | [T&C](/mistral/terms-and-conditions/) |
| Vibe Code on UCloud | [Mistral Vibe and Continue on UCloud](/ucloud/guides/advanced-guides/mistral-vibe-and-continue/) |
| Mistral product docs | [Vibe Code](https://docs.mistral.ai/vibe/code){target="_blank"} |

# Vibe Code

Vibe Code is Mistral’s coding assistant. It can read and write files, run commands, and help with coding tasks under your supervision. It is available in four places:

- **Vibe Code Web** — the **Code** tab in the browser at [chat.mistral.ai](https://chat.mistral.ai){target="_blank"}
- **Vibe Desktop** — the Mistral desktop app for macOS and Windows
- **CLI** — your terminal
- **VS Code extension** — or another editor using the OpenAI-compatible API

For product details, see Mistral’s [Vibe Code documentation](https://docs.mistral.ai/vibe/code){target="_blank"}. Compare the surfaces in [Choose CLI, VS Code, web, or Desktop](https://docs.mistral.ai/vibe/code/choose-cli-vscode-web-sessions){target="_blank"}.

!!! warning "Not available in the default workspace"
    **Vibe Code is not available in the default project** — not in the Code tab, Desktop, CLI, or VS Code. You need a **dedicated workspace**.

    The CLI and VS Code extension also need an API key from [AI Studio](https://console.mistral.ai/api-keys){target="_blank"}. Do not sign in with **Launch browser**; that flow is disabled at AAU and will fail with *This workspace can't be used*.

    Apply via [How to access Mistral](/mistral/how-to-access/) if you do not have a dedicated workspace yet. Keys are **personal** — do not share them, and rotate them at least every **30 days**. See [Responsible use](/mistral/guides/responsible-use/#using-the-api) and the [terms and conditions](/mistral/terms-and-conditions/#5-api-keys).


## In the browser and on Desktop

Vibe Code Web and Vibe Desktop use your AAU login. They do **not** use an AI Studio API key.

1. [Apply for a dedicated workspace](/mistral/how-to-access/) if you do not already have one.
2. Log in to [Vibe](/mistral/guides/vibe/getting-started/) with AAU SSO, or open the [Vibe Desktop](https://docs.mistral.ai/vibe/code/desktop){target="_blank"} app.
3. Select your **named project workspace** (not the default workspace).
4. In the browser, open the **Code** tab. In Desktop, start a session from the app.

If the Code tab is missing, or Desktop cannot start a coding session, you are still in the default project.

Mistral’s setup guides: [Vibe Code Web](https://docs.mistral.ai/vibe/code/web){target="_blank"} and [Vibe Desktop](https://docs.mistral.ai/vibe/code/desktop){target="_blank"}.


## Create an API key in AI Studio (CLI and VS Code)

1. [Apply for a dedicated workspace](/mistral/how-to-access/) if you do not already have API access.
2. Log in to [AI Studio](/mistral/guides/ai-studio/getting-started/).
3. Select your **named project workspace** (not the default workspace).
4. Open [API Keys](https://console.mistral.ai/api-keys){target="_blank"} and create a key.
5. Copy the key and store it securely. You will only see the full key once.

Treat the key like a password. Do not commit it to Git, paste it into chats, or share it in notebooks.


## Why Launch browser does not work

The CLI and the VS Code extension offer **Launch browser** as the recommended sign-in. That flow tries to issue a Vibe Code key in the workspace you are signed into. It cannot be used with the **default project**, and at AAU the browser flow is turned off, so the page looks like this:

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
| Apply for a dedicated workspace | [How to access Mistral](/mistral/how-to-access/) |
| Log in to Vibe | [Logging in to Vibe](/mistral/guides/vibe/getting-started/) |
| Log in to AI Studio | [Logging in to AI Studio](/mistral/guides/ai-studio/getting-started/) |
| Key rotation and quotas | [Tokens and seats](/mistral/guides/ai-studio/tokens-and-seats/) |
| Binding rules | [T&C](/mistral/terms-and-conditions/) |
| Vibe Code on UCloud | [Mistral Vibe and Continue on UCloud](/ucloud/guides/advanced-guides/mistral-vibe-and-continue/) |
| Mistral product docs | [Vibe Code](https://docs.mistral.ai/vibe/code){target="_blank"} |

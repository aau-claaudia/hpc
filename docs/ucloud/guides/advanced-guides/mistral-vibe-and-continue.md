# Mistral Vibe and Continue on UCloud

This is a detailed guide for setting up Mistral Vibe and Continue in Coder on the UCloud platform.

---

## Important data classification restrictions

!!! warning "Data classification restrictions"

    **The use of Mistral Vibe and Codestral is only permitted with AAU data classification level 1 data.**

    Before using this guide, consult the [AAU data classification guidelines](https://www.security.aau.dk/data-classification).

    Personal data and data classified as Level 2 or Level 3 must never be exposed to Mistral AI Studio, Mistral Vibe, Continue, Codestral, or any associated API.

    When launching Coder, ensure that no folders containing data above Classification Level 1 are attached to the job.

---

## Overview

This guide describes how to:

* Obtain access to Mistral AI Studio
* Create a Mistral API key
* Launch a Coder environment in UCloud
* Install Mistral Vibe and Continue
* Configure AI-assisted coding and code completion

The setup uses:

* Mistral Vibe
* Continue
* Mistral AI Studio API access
* Coder with Python on UCloud

A machine with **1 CPU** is sufficient for installation and normal usage.

---

## Before you begin

Before proceeding, make sure that you:

* Have access to UCloud
* Have access to Mistral AI Studio
* Are only working with data classification level 1 data
* Have downloaded the installation script provided by AAU

---

## Installation guide

### Step 1: Request access to Mistral AI Studio

Before using Mistral Vibe in UCloud, you must have access to a Mistral AI Studio workspace with API key permissions.

Follow the official [AAU guide for obtaining access to Mistral AI Studio](/mistral/how-to-access/).

The guide explains:

* How to obtain access to Mistral
* How to request API key permissions
* How to gain access to an AI Studio workspace
* How to create API keys for programmatic access

!!! info "API key access is required"

    Access to Vibe and AI Studio alone is not sufficient.

    You must have access to an AI Studio workspace that allows API key creation before proceeding with this guide.

---

### Step 2: Create an API key

Once your AI Studio workspace has been approved:

1. Log in to AI Studio
2. Select your project workspace
3. Open **API Keys**
4. Create a new API key
5. Copy and securely store the key

You will need this key during installation.

!!! warning "Protect your API key"

    Treat your API key like a password.

    * Do not share it with others.
    * Do not commit it to Git repositories.
    * Do not include it in notebooks or scripts that are shared publicly.

---

### Step 3: Upload the installation script to UCloud

Create a folder in your UCloud workspace.

For example:

```text
mistral-setup
```

Upload:

```text
setup-mistral-vibe-with-continue.sh
```

to this folder.


Copy and pase the text of this script into a blank file and save it as: `setup-mistral-vibe-with-continue.sh`

??? info "Set up script"

    ```bash
    #!/usr/bin/env bash
    set -euo pipefail

    EXT_ID="mistralai.mistral-vibe-code"
    EXT_BASE="$HOME/.local/share/code-server/extensions"
    VSIX_DIR="$HOME/.cache/vsix"
    VSIX_PATH="$VSIX_DIR/mistral-vibe-code.vsix"
    SECRET_FILE="$HOME/.config/mistral/env"

    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

    echo "== UCloud code-server AI setup =="

    mkdir -p "$HOME/.vibe" "$HOME/.cache" "$HOME/.local/bin" "$HOME/.config/mistral" "$VSIX_DIR"
    chmod 700 "$HOME/.config/mistral"

    # API key
    if [ -f "$SECRET_FILE" ]; then
    source "$SECRET_FILE"
    fi

    if [ -z "${MISTRAL_API_KEY:-}" ]; then
    read -r -s -p "Enter your Mistral API key: " MISTRAL_API_KEY
    echo
    cat > "$SECRET_FILE" <<EOF
    export MISTRAL_API_KEY="$MISTRAL_API_KEY"
    EOF
    chmod 600 "$SECRET_FILE"
    export MISTRAL_API_KEY
    else
    echo "Mistral API key loaded."
    fi

    # Mistral Vibe CLI
    if ! command -v vibe >/dev/null 2>&1 || ! command -v vibe-acp >/dev/null 2>&1; then
    echo "Installing Mistral Vibe CLI..."
    curl -LsSf https://mistral.ai/vibe/install.sh | bash
    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    else
    echo "Mistral Vibe CLI already installed."
    fi

    echo "vibe: $(command -v vibe)"
    vibe --version || true
    echo "vibe-acp: $(command -v vibe-acp)"
    vibe-acp --version || true

    # Mistral Vibe code-server extension
    if code-server --list-extensions | grep -qx "$EXT_ID"; then
    echo "Mistral Vibe extension already installed."
    else
    echo "Installing Mistral Vibe extension..."

    rm -f "$VSIX_PATH" "$VSIX_PATH.gz"

    curl -fL --compressed \
        -H "Accept: application/octet-stream" \
        "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/mistralai/vsextensions/mistral-vibe-code/latest/vspackage" \
        -o "$VSIX_PATH"

    if file "$VSIX_PATH" | grep -qi "gzip compressed"; then
        mv "$VSIX_PATH" "$VSIX_PATH.gz"
        gunzip "$VSIX_PATH.gz"
    fi

    unzip -t "$VSIX_PATH" >/dev/null
    code-server --install-extension "$VSIX_PATH"
    fi

    # Patch broken bundled vibe-acp
    EXT_DIR="$(find "$EXT_BASE" -maxdepth 1 -type d -name 'mistralai.mistral-vibe-code-*' | sort -V | tail -1)"

    if [ -z "${EXT_DIR:-}" ] || [ ! -d "$EXT_DIR" ]; then
    echo "ERROR: Could not find installed Mistral Vibe extension directory."
    exit 1
    fi

    mkdir -p "$EXT_DIR/bin"

    if [ -f "$EXT_DIR/bin/vibe-acp" ] && [ ! -f "$EXT_DIR/bin/vibe-acp.original" ]; then
    cp "$EXT_DIR/bin/vibe-acp" "$EXT_DIR/bin/vibe-acp.original"
    fi

    cat > "$EXT_DIR/bin/vibe-acp" <<'EOF'
    #!/usr/bin/env bash
    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    [ -f "$HOME/.config/mistral/env" ] && source "$HOME/.config/mistral/env"
    exec "$HOME/.local/bin/vibe-acp" "$@"
    EOF

    chmod +x "$EXT_DIR/bin/vibe-acp"

    if [ -f "$EXT_DIR/bin/vibe" ]; then
    if [ ! -f "$EXT_DIR/bin/vibe.original" ]; then
        cp "$EXT_DIR/bin/vibe" "$EXT_DIR/bin/vibe.original"
    fi

    cat > "$EXT_DIR/bin/vibe" <<'EOF'
    #!/usr/bin/env bash
    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    [ -f "$HOME/.config/mistral/env" ] && source "$HOME/.config/mistral/env"
    exec "$HOME/.local/bin/vibe" "$@"
    EOF

    chmod +x "$EXT_DIR/bin/vibe"
    fi

    # Continue extension
    if code-server --list-extensions | grep -qi '^continue\.continue$'; then
    echo "Continue extension already installed."
    else
    echo "Installing Continue extension..."

    if ! code-server --install-extension Continue.continue; then
        echo "Primary install failed, trying lowercase publisher..."
        code-server --install-extension continue.continue
    fi
    fi

    # Continue config
    mkdir -p "$HOME/.continue"

    cat > "$HOME/.continue/config.yaml" <<EOF
    name: UCloud Mistral
    version: 1.0.0
    schema: v1

    models:
    - name: Mistral Large
        provider: mistral
        model: mistral-large-latest
        apiKey: ${MISTRAL_API_KEY}
        roles:
        - chat
        - edit
        - apply

    - name: Mistral codestral
        provider: mistral
        model: codestral-latest
        apiKey: ${MISTRAL_API_KEY}
        roles:
        - autocomplete

    EOF

    # Merge code-server settings safely
    python3 - <<'PY'
    import json
    from pathlib import Path

    settings = Path.home() / ".local/share/code-server/User/settings.json"
    settings.parent.mkdir(parents=True, exist_ok=True)

    data = {}
    if settings.exists():
        try:
            data = json.loads(settings.read_text())
        except Exception:
            data = {}

    data["editor.inlineSuggest.enabled"] = True
    data["editor.suggest.preview"] = True

    settings.write_text(json.dumps(data, indent=2) + "\n")
    PY

    echo
    echo "Installed AI extensions:"
    code-server --list-extensions | grep -Ei 'mistral|continue' || true

    echo
    echo "Setup complete."
    echo "Use Chrome, not Safari."
    echo "Reload code-server: Ctrl+Shift+P → Developer: Reload Window"
    echo "Open Mistral Vibe or Continue from the sidebar or Command Palette."
    ```

---

### Step 4: Launch Coder with Python

From UCloud:

1. Open **Applications**
2. Select **Coder with Python**
3. Launch a new job

A machine with:

| Resource | Recommended |
|----------|-------------|
| CPU | 1 |
| Memory | Default |
| GPU | Not required |

is more than adequate for installation and usage.

Attach the folder containing:

```text
setup-mistral-vibe.sh
```

to the job.

Wait for the application to start.

---

### Step 5: Run the installation script

Open the integrated terminal inside Coder.

Navigate to the folder where the installation script was uploaded.

For example:

```bash
cd /work/mistral-setup
```

Run the installer:

```bash
bash setup-mistral-vibe.sh
```

The installer will:

* Install Mistral Vibe
* Install Continue
* Configure code-server
* Configure the Mistral API integration
* Apply compatibility fixes required for UCloud and code-server

---

### Step 6: Enter your API key

During installation you will be prompted for your Mistral API key.

Paste the API key created earlier.

Allow the installation to finish completely.

Once completed, you may close the terminal.

---

### Step 7: Reload the Coder window

Open the Command Palette.

#### Windows and Linux

```text
Ctrl + Shift + P
```

#### macOS

```text
Cmd + Shift + P
```

Run:

```text
Developer: Reload Window
```

This ensures that the newly installed extensions are loaded correctly.

!!! info "Browser recommendation"

    We recommend using Google Chrome.

    Some users have experienced compatibility issues with Safari when using Mistral Vibe inside code-server.

---

### Step 8: Open Mistral Vibe

After the reload has completed:

* Click the Mistral icon in the left-hand sidebar

or

Open the Command Palette and run:

```text
Mistral Vibe: Open Mistral Vibe
```

The Mistral Vibe panel will appear.

You can now:

* Ask questions about your codebase
* Request code explanations
* Generate new code
* Refactor existing code
* Modify files directly through the agent

---

### Step 9: Use code completion

Open any source code file.

Place the cursor where you would like assistance.

The Continue extension will automatically provide suggestions when available.

Many users find that pressing:

```text
Tab
```

once helps trigger completion requests.

You can then:

* Accept suggestions
* Continue writing code
* Request modifications through Mistral Vibe

---

## Verifying the installation

### Verify Mistral Vibe

Open the Command Palette and run:

```text
Mistral Vibe: Open Mistral Vibe
```

Try asking:

```text
What files are available in this workspace?
```

If the workspace contents are returned successfully, the installation is functioning correctly.

---

### Verify Continue

Open the Continue panel from the sidebar.

Ask:

```text
Explain the current file.
```

If a response is returned, Continue is functioning correctly.

---

## Troubleshooting

### Mistral Vibe opens but remains loading

If the Mistral Vibe panel appears but never loads:

1. Reload the window
2. Verify that Chrome is being used
3. Verify that the installation script completed successfully

---

### Agent failed to initialize

This is often caused by:

* Missing installation files
* An interrupted installation
* A corrupted extension installation

Re-run:

```bash
bash setup-mistral-vibe.sh
```

and reload the window.

---

### Clipboard access errors

If you encounter:

```text
Unable to read from the browser's clipboard
```

verify that clipboard permissions are enabled for the UCloud website in your browser settings.

---

### Continue autocomplete errors

Some Mistral models do not support Fill-In-the-Middle (FIM) completion.

If you encounter errors related to autocomplete:

* Continue chat functionality will still work.
* Mistral Vibe functionality will still work.
* Code completion availability depends on the specific model and API access level associated with your Mistral AI Studio project.

---

## Summary

After completing this guide you should have:

* Access to Mistral AI Studio
* A working API key
* Mistral Vibe installed in Coder
* Continue installed in Coder
* AI-assisted coding functionality available directly in your UCloud development environment

Remember that these tools may only be used with **AAU data classification level 1 data**.

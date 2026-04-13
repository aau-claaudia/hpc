# AAU HPC Documentation (`hpc.aau.dk`)

Documentation for AAU HPC, built with **Zensical**.

The project contains:
- content pages in `docs/`
- theme overrides in `overrides/`
- configuration in `zensical.toml`

## Getting started (new contributors)

This section assumes you are starting from an empty machine and want to edit this documentation locally.

### 1. Install Visual Studio Code

1. Download **Visual Studio Code** from the official site: [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Run the installer and accept the defaults, or enable **“Add to PATH”** if the installer offers it (handy for launching from a terminal).
3. Start VS Code once so it can finish any first-run setup.

### 2. Install Git

Git is required to copy the repository from GitHub.

- **Windows:** Install [Git for Windows](https://git-scm.com/download/win). During setup, the default options are fine for most people. This also installs **Git Bash**, which you can use instead of PowerShell for Git commands.
- **macOS:** Install [Git](https://git-scm.com/download/mac) (Xcode Command Line Tools include `git`, or use the installer from the Git site).
- **Linux:** Install Git with your package manager, for example `sudo apt install git` on Debian/Ubuntu.

Check that Git is available:

```bash
git --version
```

### 3. Clone the repository from GitHub

The source lives in the **aau-claaudia/hpc** repository:

[https://github.com/aau-claaudia/hpc](https://github.com/aau-claaudia/hpc)

1. Open a terminal (on Windows: **PowerShell** or **Git Bash**).
2. Go to the folder where you keep projects, for example `Documents`:

   ```powershell
   cd $HOME\Documents
   ```

   On macOS or Linux you might use `cd ~/Documents` instead.

3. Clone the repo (this creates a folder named `hpc`):

   ```bash
   git clone https://github.com/aau-claaudia/hpc.git
   ```

4. If the repository is **private**, GitHub will ask you to sign in. Use a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) or [GitHub CLI](https://cli.github.com/) as described in GitHub’s documentation, or clone via SSH if your AAU GitHub account has SSH keys set up:

   ```bash
   git clone git@github.com:aau-claaudia/hpc.git
   ```

### 4. Open the project in VS Code

1. In VS Code, choose **File → Open Folder…** (or **Open…** on macOS).
2. Select the `hpc` folder you just cloned (the one that contains `README.md`, `docs/`, and `zensical.toml`).
3. Confirm; the project root should appear in the Explorer sidebar.

Optional: from a terminal, you can open the folder directly:

```bash
cd hpc
code .
```

(`code` works if VS Code’s shell command was installed; in VS Code, use **Command Palette → “Shell Command: Install ‘code’ command in PATH”** if needed.)

### 5. Run the documentation site locally

Follow **Requirements** and **Install** below to create a Python virtual environment and install dependencies, then use **Serve locally** to preview the site in your browser. That is the usual workflow when editing pages under `docs/`.

## Requirements

- Python 3.10+ (recommended)
- `pip`

## Install

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

### macOS/Linux (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Serve locally

### Recommended (Windows)

Use the project helper script:

```powershell
.\serve.ps1
```

`serve.ps1` will:
- create `.venv` if missing
- install/update dependencies from `requirements.txt`
- start `zensical serve`

### Manual (all platforms)

Windows:

```powershell
.\.venv\Scripts\python -m zensical serve
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m zensical serve
```

## Notes

- Main navigation is defined in `zensical.toml` under `nav`.
- Custom styles and scripts are in:
  - `docs/stylesheets/extra.css`
  - `docs/javascripts/extra.js`

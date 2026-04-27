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

Check that Git is available in a terminal (try closing and opening the terminal if it cant fint git):

```bash
git --version
```

### 2.1 Set up Git (first time only)

Open a terminal and configure your Git identity (replace with your own name/email):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Clone the repository from GitHub

The source lives in the **aau-claaudia/hpc** repository:

[https://github.com/aau-claaudia/hpc](https://github.com/aau-claaudia/hpc)

1. In VS Code, open the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
2. Run `Git: Clone`.
3. Paste the repository URL: `https://github.com/aau-claaudia/hpc.git`.
4. Choose where to save it locally.
5. When prompted, click **Open** to open the cloned folder in VS Code.
6. If the repository is private, sign in to GitHub when VS Code asks.

### 4. Open the project in VS Code

If you clicked **Open** after cloning, this is already done. Otherwise:

1. In VS Code, choose **File -> Open Folder...** (or **Open...** on macOS).
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

If Python is not installed yet, install it first:

- **Windows:** Install from [python.org](https://www.python.org/downloads/windows/). During setup, enable **Add Python to PATH**.
- **macOS:** Install from [python.org](https://www.python.org/downloads/macos/) or with Homebrew (`brew install python`).
- **Linux:** Install with your package manager (for example `sudo apt install python3 python3-venv python3-pip` on Debian/Ubuntu).

Verify installation:

```bash
python --version
```

If `python` is not recognized on macOS/Linux, use:

```bash
python3 --version
```

## Install

### Windows (PowerShell)

```powershell
.\serve.ps1
```

If that doesnt work, try  :

```powershell
Set-ExecutionPolicy RemoteSigned
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

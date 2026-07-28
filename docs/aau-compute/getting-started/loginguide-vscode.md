# Logging into AAU Compute via VS Code

This guide explains **step-by-step** how to:

1. Download and install Visual Studio Code (VS Code)
2. Install the Remote SSH extension
3. Connect to AAU Compute
4. Log in successfully for the first time

---

# Download and Install Visual Studio Code

## Step 1: Visit the official website

Go to: [download VS Code](https://code.visualstudio.com/download)


## Step 2: Download the correct version

Choose your operating system:

===+ "Windows"

    - Download for Windows

===+ "macOS"

    - Download for macOS

===+ "Linux"

    - `.deb` or `.rpm`

note til mig selv: Er der en bestemt version der skal vælges??

## Step 3: Install VS Code
===+ "Windows"

    - Open the installer
    - Click **Next**
    - Accept the terms
    - IMPORTANT: Enable **"Add to PATH"**
    - Click **Install**

===+ "macOS"

    - Drag VS Code into the Applications folder

===+ "Linux"

    - Install using package manager or software center.
---
# Install the Remote SSH Extension

To connect directly to AAU Compute from VS Code, you need Microsoft’s Remote SSH extension.

## Follow these steps:

### Step 1: Open VS Code.

### Step 2: Open Extensions:
![extensions](/assets/img/compute/Open_exentions_vscode.png)

**Shortcut:** Ctrl + Shift + X

### Step 3: Search for:
    Remote - ssh
### Step 4: Install the following extension
![remotessh](/assets/img/compute/remote_ssh_install.png)

#Login to AAU Compute
Understanding Access to AAU Compute

AAU Compute has two front-end nodes that act as entry points:

- **ailab-fe01.srv.aau.dk**
- **ailab-fe02.srv.aau.dk**

You can connect to either node - they provide the same functionality.

### Step 1: Open the terminal
Terminal → New Terminal 
![remotessh](/assets/img/compute/Open_terminal.png)
**Shortcut:** Ctrl + Shift + æ

### Step 2: Connect to AAU Compute
Run one of these commands (replace `user@student.aau.dk` with your actual AAU email address):

```bash
ssh -l user@student.aau.dk ailab-fe01.srv.aau.dk
```

or

```bash
ssh -l user@student.aau.dk ailab-fe02.srv.aau.dk
```

### Step 3: First-Time Connection
**Note:** The first time you connect, you will see a security message like this:
```bash 
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

**Type `yes` and press Enter** to proceed. This adds AI-LAB to your list of trusted hosts.

### Step 4: Enter Your Password

When prompted, enter your AAU password. **Important**: You won't see any characters (like `***`) as you type - this is normal for security reasons.

### Step 5: Success!

When you see a prompt like this, you're successfully logged in:

```bash
user@student.aau.dk@ailab-fe01:~$
```

This means you're now connected to AI-LAB and ready to start working!

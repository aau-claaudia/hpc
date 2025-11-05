# Logging into AI-LAB

This guide will help you connect to AI-LAB using SSH (Secure Shell). SSH is a secure way to access remote computers over a network.

## Understanding AI-LAB Access

AI-LAB has two front-end nodes that act as entry points:

- **ailab-fe01.srv.aau.dk**
- **ailab-fe02.srv.aau.dk**

You can connect to either node - they provide the same functionality.

## Basic SSH Connection

### Step 1: Open Your Terminal

===+ "Windows"

    - Open **PowerShell** (recommended)

===+ "macOS"

    - Open **Terminal** (found in Applications > Utilities)

===+ "Linux"

    - Open your preferred terminal application

### Step 2: Connect to AI-LAB

Run one of these commands (replace `user@student.aau.dk` with your actual AAU email address):

```bash
ssh -l user@student.aau.dk ailab-fe01.srv.aau.dk
```

or

```bash
ssh -l user@student.aau.dk ailab-fe02.srv.aau.dk
```

### Step 3: First-Time Connection

The first time you connect, you'll see a security message like this:

```
The authenticity of host 'ailab-fe01.srv.aau.dk (172.21.131.1300)' can't be established.
ED25519 key fingerprint is SHA256:xosJtOSfQyyW16c6RtpN8tAi/91XHCR3GxM9/KJEogg.
This key is not known by any other names.
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

## Setting Up SSH Shortcuts (Recommended)

Typing the full server addresses every time can be tedious. You can create shortcuts to make logging in much easier.

### Step 1: Create or update SSH Config File

===+ "Windows"

    - Navigate to `C:\Users\[YOUR_USERNAME]\.ssh\`
    - Create or update a file called `config` (no extension)

===+ "macOS/Linux"

    - Navigate to `~/.ssh/` in your terminal
    - Create or update a file called `config`: `touch config`

### Step 2: Add AI-LAB Shortcuts

Open the config file in a text editor and add these shortcuts (replace `user@student.aau.dk` with your actual email):

```bash title="~/.ssh/config"
# AI-LAB login nodes
Host ailab-1
    HostName ailab-fe01.srv.aau.dk
    User user@student.aau.dk

Host ailab-2
    HostName ailab-fe02.srv.aau.dk
    User user@student.aau.dk

# AI-LAB via SSH Gateway (for off-campus access)
# For this to work, you need to have set up AAU MFA (https://www.its.aau.dk/vejledninger/mfa)
Host ailab-vpn
    HostName ailab-fe01.srv.aau.dk
    User user@student.aau.dk
    ProxyJump user@student.aau.dk@sshgw.aau.dk
```

### Step 3: Test Your Shortcuts

Save the file and test your new shortcuts:

```bash
ssh ailab-1
ssh ailab-2
ssh ailab-vpn  # Connect via VPN (off-campus) # For this to work, you need to have set up AAU MFA (https://www.its.aau.dk/vejledninger/mfa)
```

Now you can log in with just `ssh ailab-1` instead of the full command!

## Troubleshooting

??? info "Connection refused" or "Host unreachable"
    - **Check your network**: Ensure you're connected to AAU Wi-Fi or VPN
    - **Try the other node**: Switch between `ailab-1` and `ailab-2`

??? info "Permission denied (publickey,password)"
    - **Check your email**: Make sure you're using your correct AAU email address
    - **Verify password**: Ensure you're entering your AAU password correctly

??? info "Windows-specific Issues"

    **If SSH command is not recognized:**

    - Install [OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui){target=_blank}
    - Or use [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/setup/environment){target=_blank}

    **If you can't create the .ssh folder:**

    - Open File Explorer and navigate to `C:\Users\[YOUR_USERNAME]\`
    - Create a new folder named `.ssh` (with the dot)
    - Create the `config` file inside this folder

??? info "Connection Timeouts"
    - **Check VPN**: If off-campus, ensure VPN is connected and working
    - **Antivirus**: Some Antivirus software block SSH - try disabling your Antivirus momentarily 



<hr>

You are now ready to proceed to learn about [**file handling :octicons-arrow-right-24:**](file-handling.md)
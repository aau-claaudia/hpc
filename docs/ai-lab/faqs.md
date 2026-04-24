---
icon: lucide/message-circle-question-mark
---

# FAQs

## Troubleshooting questions

??? question "Why do I get `Error generating job credential` or `unknown userid` when running a job?"

    This is a very frustrating error we get a lot, unfortunately. The error will disappear after some while, but it can sometimes take a few hours. So when the error happens, you cannot run your job on the affected node, but it will most likely work on the other compute nodes.

    So when it happens you can try to run your job on a different node. So in your command or sbatch script you can add e.g. --nodelist=ailab-l4-08 (or more nodes if needed). If that fails, then try some another nodes.

    Unfortunately there is not much else to do right now, as it is a general AAU network issue that happens from time to time.

??? question "Why do I get `\r` error when running my Python script?"

    If you encounter an error message like: `/usr/bin/env python3/r: bad interpreter: No such file or directory` while running a .py file, it might be because the file was edited on your local Windows computer before moving it to AI-LAB. Line endings often get converted when files are moved between Linux and Windows. This conversion is a frequent issue as Linux and Unix-like systems use `\n` for line breaks, whereas Windows uses `\r\n` (CRLF, Carriage Return + Line Feed). 

    **Solution:** In code editors such as VS Code or PyCharm, you can switch between LF (Linux endings) and CRLF (Windows endings) from the right-hand side of the status bar at the bottom of the window. Therefore, use LF endings if you wish to move a file to AI-LAB.

## Login known issues and fixes

??? question "If you get `Permission denied, please try again`, what should you check?"

    Most often this means the password or username format is incorrect.

    **Check this:**

    - Use your AAU username in the email format (for example `ab12cd@student.aau.dk`).
    - Make sure you did not misspell your username.
    - If you connect through `sshgw`, it is normal to enter credentials in multiple steps:
      1. Password for `sshgw`.
      2. Microsoft Authenticator approval.
      3. Password again for AI-LAB.

??? question "If SSH gets stuck in a password loop and MFA is not triggered on `sshgw.aau.dk`, what should you check?"

    This is usually an MFA setup issue for SSH gateway access.

    **Check this:**

    - Verify AAU MFA is configured according to AAU's official guide, especially the Microsoft Authenticator push/message method.
    - Make sure MFA is enabled for the account and device you are currently using.
    - Try again with verbose logging and include output when requesting support:
      - `ssh -vvv user@student.aau.dk@sshgw.aau.dk`

??? question "If login fails when you are off campus, what should you check?"

    Off-campus access requires either AAU VPN or SSH gateway.

    **Check this:**

    - If you use Cisco VPN, confirm you are actually connected to AAU VPN before running SSH.
    - If VPN is unstable, use SSH gateway instead:
      - `ssh -J user@student.aau.dk@sshgw.aau.dk -l user@student.aau.dk ailab-fe01.srv.aau.dk`
    - If you are already on AAU network (on campus), connect directly to AI-LAB and skip `sshgw`.

??? question "If `ailab-fe01` is unavailable or very slow, what should you check?"

    This can happen during frontend incidents or heavy load.

    **Check this:**
    
    - Try the secondary frontend:
      - `ssh user@student.aau.dk@ailab-fe02.srv.aau.dk`
    - Retry later if there is an ongoing frontend incident.
    - If both nodes are slow/unavailable, it is likely a platform-side issue and should be reported.

??? question "If VS Code Remote SSH says `Failed to parse remote port from server output`, what should you check?"

    This is commonly a VS Code remote environment issue, not a basic SSH account issue.

    **Check this:**

    - First test plain terminal SSH login to confirm credentials/network are working:
      - `ssh user@student.aau.dk@ailab-fe01.srv.aau.dk`
    - If terminal login works but VS Code fails, clean VS Code server files on AI-LAB and reconnect:
      - `rm -rf ~/.vscode-server`
      - `rm -rf ~/.vscode-remote`
    - Temporarily reduce enabled VS Code extensions if reconnect is still unstable.

??? question "If your login suddenly stops working after it worked before, what should you check first?"

    In many cases this is a temporary node/load incident, not your account.

    **Check this:**

    - Retry on `ailab-fe02`.
    - Retry after some time.
    - Run a verbose SSH test and include it in support tickets:
      - `ssh -vvv user@student.aau.dk@ailab-fe01.srv.aau.dk`
    - Include whether you are on campus, on VPN, or using `sshgw`.

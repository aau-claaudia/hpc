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

??? question "Why can't I connect to AI-LAB?"

    If you encounter an error like `ssh: Could not resolve hostname ailab-fe01.srv.aau.dk: No such host is known.`, you may need to connect through AAU's jump host (SSH gateway).

    **Solution:** Use the jump host option with the `-J` flag:

    ```bash
    ssh -J user@student.aau.dk@sshgw.aau.dk -l user@student.aau.dk ailab-fe01.srv.aau.dk
    ```

    Replace `user@student.aau.dk` with your actual AAU email address. You will need to enter your password twice and use Microsoft Authenticator in between.

    If you still encounter issues, try using [PuTTY terminal](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) software as an alternative.


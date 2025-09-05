## SSH Configuration Setup (Recommended)

For a more convenient login experience, we recommend setting up SSH configuration and key-based authentication. This allows you to connect with simple commands like `ssh ailab-1` instead of typing the full connection details each time.

### Prerequisites

Before setting up SSH configuration, you need to:

1. **Generate an SSH key pair** (if you don't have one already):
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your.email@student.aau.dk"
   ```
   - Press Enter to accept the default file location (`~/.ssh/id_rsa`)
   - Optionally set a passphrase for additional security

2. **Copy your public key to the server**:
   ```bash
   ssh-copy-id your.email@student.aau.dk@ailab-fe01.srv.aau.dk
   ```
   - Replace `your.email@student.aau.dk` with your AAU email address
   - Enter your password when prompted

### SSH Configuration

Create or edit the SSH configuration file at `~/.ssh/config` and add the following entries:

```bash
Host sshgw
    HostName sshgw.aau.dk
    User your.email@student.aau.dk
    IdentityFile ~/.ssh/id_rsa

Host ailab-1
    HostName ailab-fe01.srv.aau.dk
    User your.email@student.aau.dk
    IdentityFile ~/.ssh/id_rsa

Host ailab-2
    HostName ailab-fe02.srv.aau.dk
    User your.email@student.aau.dk
    IdentityFile ~/.ssh/id_rsa

Host ailab-vpn
    HostName ailab-fe01.srv.aau.dk
    User your.email@student.aau.dk
    IdentityFile ~/.ssh/id_rsa
    ProxyJump sshgw
```

!!! info "Replace Email Address"
    Replace `your.email@student.aau.dk` with your actual AAU email address in all the configuration entries above.

### Using the Configuration

Once configured, you can connect using these simple commands:

- `ssh ailab-1` - Connect to the first front-end node
- `ssh ailab-2` - Connect to the second front-end node  
- `ssh ailab-vpn` - Connect through the VPN gateway (useful when off-campus)

---

## Manual Login (Alternative Method)

To login you need to [SSH connect](https://www.cloudflare.com/learning/access-management/what-is-ssh/) to either of the two front-end nodes, `ailab-fe01` or `ailab-fe02`. 

Run the following command on a command-line interface on your local Windows (*Windows PowerShell*), macOS, or Linux computer:

!!! info "Troubleshooting Windows Login Issues"
    If you cannot log in using Windows PowerShell, try installing [OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) or a [Linux subsystem](https://learn.microsoft.com/en-us/windows/wsl/setup/environment).

```
ssh -l user@student.aau.dk ailab-fe01.srv.aau.dk
```
or
```
ssh -l user@student.aau.dk ailab-fe02.srv.aau.dk
```

Replace `user@student.aau.dk` with your AAU email address.

!!! info "The first time you connect, you will get a message like:"
    
    ```
    The authenticity of host 'ailab-fe01.srv.aau.dk (172.21.131.1300)' can't be established.
    ED25519 key fingerprint is SHA256:xosJtOSfQyyW16c6RtpN8tAi/91XHCR3GxM9/KJEogg.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

    Please confirm by typing `yes` to proceed with the connection.

Enter your AAU password when prompted. 

When you can see `user@student.aau.dk@ailab-fe01:~$` you are succesfully logged in.

<hr>

You are now ready to proceed to learn about [**file management :octicons-arrow-right-24:**](file-management.md)
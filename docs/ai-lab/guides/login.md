To login you need to [SSH connect](https://www.cloudflare.com/learning/access-management/what-is-ssh/){target=_blank} to either of the two front-end nodes, `ailab-fe01` or `ailab-fe02`. 

Run the following command on a command-line interface on your local Windows (*Windows PowerShell*), macOS, or Linux computer:

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

When prompted, enter your AAU password. Please note that you will not see any characters, like ***, on the screen as you type.

When you can see `user@student.aau.dk@ailab-fe01:~$` you are succesfully logged in.

!!! info "Troubleshooting Windows Login Issues"
    If you cannot log in using Windows PowerShell, try installing [OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui){target=_blank} or a [Linux subsystem](https://learn.microsoft.com/en-us/windows/wsl/setup/environment){target=_blank}.

!!! info "No access to VPN or AAUs network?"
    If you do not have access to VPN, it is also possible to connect to your instance by using AAU's SSH gateway as a jump host. This way your connection gets established through the gateway without redirecting the rest of your network traffic. Note that this will ask you for [multifactor authentication](https://www.en.its.aau.dk/instructions/mfa).

    ```
    ssh -J user@student.aau.dk@sshgw.aau.dk -l user@student.aau.dk ailab-fe01.srv.aau.dk
    ```
    
    Replace `user@student.aau.dk` with your AAU email address.

    
<hr>

You are now ready to proceed to learn about [**file handling :octicons-arrow-right-24:**](file-handling.md)
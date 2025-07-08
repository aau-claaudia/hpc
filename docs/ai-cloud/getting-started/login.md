To login you need to [SSH connect](https://www.cloudflare.com/learning/access-management/what-is-ssh/) to the front-end node, `ai-fe02.srv.aau.dk`. 

Run the following command on a command-line interface on your local Windows (*Windows PowerShell*), macOS, or Linux computer:

```
ssh -l user@domain.aau.dk ai-fe02.srv.aau.dk
```


Replace `user@domain.aau.dk` with your AAU email address.

Enter your AAU password when prompted. 

When you can see `user@domain.aau.dk@ai-fe02:~$` you are succesfully logged in.

!!! info "First time you log in"
    The first time you connect, you will get a message like:

    ```
    The authenticity of host 'ai-fe02.srv.aau.dk (172.21.131.1300)' can't be established.
    ED25519 key fingerprint is SHA256:xosJtOSfQyyW16c6RtpN8tAi/91XHCR3GxM9/KJEogg.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```
    Please confirm by typing 'yes' to proceed with the connection.

!!! info "Having trouble with logging in?"
    - In most cases where users have trouble logging in, they are not connected to the AAU network. See the section: [Before you begin](/ai-cloud/getting-started/).

    - If it's still not working, add an extra `-v` to your command, like so:
    ```
    ssh -vvv -l user@domain.aau.dk ai-fe02.srv.aau.dk
    ```
    This increases the verbosity of the command. If have difficulties with making sense of the output, create a case with us on [serviceportal.aau.dk](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e) and make sure to share the it with us.

<hr>

You are now ready to proceed to learn about [**file management :octicons-arrow-right-24:**](file-management.md)

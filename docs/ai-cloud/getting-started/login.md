
Logging in to the platform is done with an SSH connection to the [front end node](/ai-cloud/system-overview/#front-end-node).

Find [an SSH-capable terminal application](/ai-cloud/getting-started/#find-a-terminal-application) and run the command:
```
ssh -l user@domain.aau.dk ai-fe02.srv.aau.dk
```
Replace `user@domain.aau.dk` with your AAU email address.

Enter your AAU password when prompted.

!!! warning "Accept the fingerprint?"
    The first time you connect, you will get the following message:
    ```
    The authenticity of host 'ai-fe02.srv.aau.dk (172.21.131.1300)' can't be established.
    ED25519 key fingerprint is SHA256:xosJtOSfQyyW16c6RtpN8tAi/91XHCR3GxM9/KJEogg.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

    Confirm by typing `yes` to proceed with the connection.


### Success!
When your prompt changes to: `user@domain.aau.dk@ai-fe02:~$` - you are successfully logged in.

<hr>


#### Troubleshooting

!!! failure "Having trouble with logging in?"
    - In most cases where users have trouble logging in, they are not connected to the AAU network. See the section: [Before you begin](/ai-cloud/getting-started/).

    - If it's still not working, create a case with us on [serviceportal.aau.dk](https://aau.service-now.com/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e). Please share the command output with us in the case, as this gives us a better oppurtunity to understand what is going on. Add the flag `-vv` to the command, like so:
    ```
    ssh -vv -l user@domain.aau.dk ai-fe02.srv.aau.dk
    ```
#### Bonus tips

!!! tip "The ssh-gateway"

    AAU provides an ssh-gateway service, that can be used as an alternative to the VPN service. This requires only a small change to your command:

    ```
    ssh -J user@domain.aau.dk@sshgw.aau.dk -l user@domain.aau.dk ai-fe02.srv.aau.dk
    ```

!!! tip "Easy access with ~/.ssh/config"

    It's possible to store your credentials in a file in your `~/.ssh` directory, called `config`. Open this file and add the following:
    ```
    Host sshgw
      HostName sshgw.aau.dk
      User user@domain.aau.dk

    Host aicloud
      HostName ai-fe02.srv.aau.dk
      User user@domain.aau.dk
      Proxyjump sshgw
    ```

    Now we can log in to AI Cloud, simply by typing:

    ```
    ssh aicloud
    ```
<hr>

You are now ready to proceed to [**look around :octicons-arrow-right-24:**](file-management.md)

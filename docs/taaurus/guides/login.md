# Logging into TAAURUS

This guide will help you connect to TAAURUS using Remote Desktop Protocol (RDP).

## Prerequisites
- [Access to TAAURUS platform](/taaurus/guides/applying-for-a-taaurus-project/)
- Remote Desktop Protocol (RDP) client installed (see the guides below)
- AAU email
- Microsoft Authenticator app for 2FA authentication
    - **Default sign-in method**: Must be set to **App based authentication** (can be changed at [https://aka.ms/mfasetup](https://aka.ms/mfasetup))
    - **Notification type**: You must have Microsoft Authenticator **push notifications** set up — **NOT SMS**
    - Make sure to follow the complete setup guide: [https://www.en.its.aau.dk/instructions/mfa](https://www.en.its.aau.dk/instructions/mfa)
- AAU network connection
    - If off campus please follow [these instructions](https://www.en.its.aau.dk/instructions/vpn) to set up VPN at AAU

===+ "Windows"

    ### Step 1: Connecting from Windows

    On your local Windows PC:

    1. Open the Start menu and search for **Remote Desktop Connection**
    2. Select **Remote Desktop Connection** from the results
        - *Danish users: Look for "Forbindelse til Fjernskrivebord"*

    ### Step 2: Enter Server Details

    3. In the Remote Desktop Connection window, enter the server address:
    ```
    sp-test05.srv.aau.dk
    ```
    4. Click **Show Options** to access **Advanced** settings in the tab

    ![Screenshot of RDP](/assets/img/taaurus/windows-rdp-1.png){style=max-height:600px;}

    ### Step 3: Configure Gateway Settings

    5. Go to the **Advanced** tab
    6. Click **Settings...** under "Connect from anywhere"
    7. In the Connection settings dialog:
        - Enter `rdgw.taaurus.aau.dk` in the Server name field
        - Select **Ask for password** from the Logon method dropdown
        - **Uncheck** "Use these RD Gateway server settings"
    8. Click **OK** to save settings
    9. Click **Connect** to initiate the connection

    ![Screenshot of RDP](/assets/img/taaurus/windows-rdp-2.png){style=max-height:600px;}

    ### Step 4: Authentication Process

    You will go through a multi-step authentication process:

    ### First Authentication
    - A Windows Security popup will appear
    - Click **More choices** and then **Use a different account**
    - Enter your **AAU email address** and **password**
    - Click **OK**

    ![Screenshot of RDP](/assets/img/taaurus/rdp-windows-security-1.png){style=max-height:600px;}

    ### Second Authentication (2FA)
    - You will be prompted to authenticate using your **Microsoft Authenticator app**
        - If you need help setting up AAU MFA please follow these [instructions](https://www.en.its.aau.dk/instructions/mfa)
    - Open the app and approve the login request

    ### Final Authentication
    - You may need to authenticate once more with your **AAU email and password**

    ![Screenshot of RDP](/assets/img/taaurus/general-rdp-3.png){style=max-height:600px;}

    ### Step 5: Success!

    Once authenticated, you will be connected to the TAAURUS remote desktop environment. You should see the desktop interface of the TAAURUS server.

    ![Screenshot of RDP](/assets/img/taaurus/taaurus-server.png){style=max-height:600px;}

    ### Troubleshooting

    If you encounter any issues during the login process:

    1. **Connection fails**: Check that you are connected to AAU network and try again
    2. **Authentication errors**: Verify your AAU credentials and MFA setup
    3. **Gateway issues**: Ensure you've correctly configured the RD Gateway settings
    4. **Still having problems**: Contact CLAAUDIA support at [serviceportal.aau.dk](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad00131d0)

===+ "macOS"

    ### Step 1: Connecting from macOS

    TAAURUS provides access through a **Windows Remote Desktop environment**, which means all operating systems must connect using the **Remote Desktop Protocol (RDP)**.

    Because only Windows includes an RDP client by default, **macOS users must install one** before connecting.

    ### Install Microsoft Remote Desktop

    1. Open the **Software Center**
    2. Search for **Windows App**
    3. Install the application

    ![Screenshot of Software Center](/assets/img/taaurus/mac-software-center-1.png){style=max-height:600px;}

    ### Step 2: Configure the connection

    1. Open **Microsoft Remote Desktop**
    ![Screenshot of Software Center](/assets/img/taaurus/mac-rdp-0.png){style=max-height:600px;}

    2. Open Settings in top menu (⌘ ,)
    3. Add Gateway in "Gateways", use gateway name:     ```rdgw.taaurus.aau.dk```
      ![Screenshot of remote desktop add pc](/assets/img/taaurus/mac-rdp-1.png){style=max-height:600px;}
    4. Click **Connections** -> **Add PC** (⌘ N) use server address: ```sp-test05.srv.aau.dk```
      ![Screenshot of remote desktop add pc](/assets/img/taaurus/mac-rdp-2.png){style=max-height:600px;}


    Save the connection and double-click it to connect.
      ![Screenshot of remote desktop add pc](/assets/img/taaurus/mac-rdp-3.png){style=max-height:600px;}

    ### Step 3: Authentication Process

    You will be prompted to log in with your **AAU email and password**, followed by approval in **Microsoft Authenticator**.
      ![Screenshot of remote desktop add pc](/assets/img/taaurus/mac-rdp-4.png){style=max-height:600px;}

    ### Step 4: Final Authentication
    - You may need to authenticate once more with your **AAU email and password**

    ![Screenshot of RDP](/assets/img/taaurus/general-rdp-3.png){style=max-height:600px;}

    ### Step 5: Success!

    Once authenticated, you will be connected to the TAAURUS remote desktop environment. You should see the desktop interface of the TAAURUS server.

    ![Screenshot of RDP](/assets/img/taaurus/taaurus-server.png){style=max-height:600px;}

    ### Troubleshooting

    If you encounter any issues during the login process:

    1. **Connection fails**: Check that you are connected to AAU network and try again
    2. **Authentication errors**: Verify your AAU credentials and MFA setup
    3. **Gateway issues**: Ensure you've correctly configured the RD Gateway settings
    4. **Still having problems**: Contact CLAAUDIA support at [serviceportal.aau.dk](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad00131d0)

===+ "Linux"

    ### Connecting from Linux 

    TAAURUS provides access through a **Windows Remote Desktop environment**, which means all operating systems must connect using the **Remote Desktop Protocol (RDP)**.

    Because only Windows includes an RDP client by default, **Linux users must install one** before connecting.

    Linux desktop environments use a **display server** to handle windows, input, and graphics.  
    The two most common ones are:

    - **X11 (X.Org)** – Older, very widely supported
    - **Wayland** – Newer, more secure, and default on many modern distributions

    To check which one you are running, open a terminal and run:

    ```bash
    echo $XDG_SESSION_TYPE
    ```

    - Output `x11` → follow **X11 instructions**
    - Output `wayland` → follow **Wayland instructions**

    ---

    ### Step 1: Install FreeRDP

    FreeRDP is an open-source Remote Desktop (RDP) client for Linux.

    #### For X11
    ```bash
    sudo apt install freerdp2-x11
    ```

    This installs the `xfreerdp` command.

    #### For Wayland
    ```bash
    sudo apt install freerdp2-wayland
    ```

    This installs the `wlfreerdp` command  
    *(note: **not** `wfreerdp` — this is a common mistake)*

    ---

    ### Step 2: Connect to TAAURUS

    Use the command that matches your display server.

    #### Wayland
    ```bash
    wlfreerdp /v:SERVER-NAME /f /u:AAU-EMAIL /g:rdgw.taaurus.aau.dk
    ```

    #### X11
    ```bash
    xfreerdp /v:SERVER-NAME /f /u:AAU-EMAIL /g:rdgw.taaurus.aau.dk
    ```

    Replace `SERVER-NAME` with your TAAURUS projects server name. 

    Replace `AAU-EMAIL` with your AAU Email.

    **Parameter explanation:**
    - `/v:` – Target TAAURUS server
    - `/f` – Fullscreen mode
    - `/u:` – Your AAU username (email format)
    - `/g:` – RD Gateway used for secure access

    When prompted:
    1. Enter your **AAU password**
    2. Approve the login in **Microsoft Authenticator**

    You may be asked to authenticate more than once — this is expected.

    ---

    ### Known Notes & Limitations

    - MFA **must** be set up with Microsoft Authenticator push notifications
    - VPN may be required if you are off campus
    - Clipboard and drive redirection may behave differently than on Windows/macOS
    - This setup is **not guaranteed** to work on all Linux distributions

    ---

    ### Need Help?

    If this does not work for you, please submit a support ticket and include:
    - Your Linux distribution
    - Whether you use X11 or Wayland
    - The full command you tried
    - Any error output from the terminal

    👉 Submit a ticket via the AAU Service Portal:  
    https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad00131d0



## Next Steps

Now that you're logged in, you're ready to explore the TAAURUS platform. Continue to learn about [navigating TAAURUS](/taaurus/guides/navigating-taaurus), available applications, and the file system.
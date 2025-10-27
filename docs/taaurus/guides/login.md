# Logging into TAAURUS

This guide will help you connect to TAAURUS using Remote Desktop Protocol (RDP).

## Prerequisites

- Windows computer with Remote Desktop Connection installed
- AAU email address and password
- Microsoft Authenticator app for 2FA authentication
- Access to TAAURUS platform

## Step 1: Open Remote Desktop Connection

On your local Windows PC:

1. Open the Start menu and search for **Remote Desktop Connection**
2. Select **Remote Desktop Connection** from the results
      - *Danish users: Look for "Forbindelse til Fjernskrivebord"*

## Step 2: Enter Server Details

1. In the Remote Desktop Connection window, enter the server address:
   ```
   sp-test05.srv.aau.dk
   ```
2. Click **Show Options** to access advanced settings

![Screenshot of RDP](/assets/img/taaurus/rdp-1.png)

## Step 3: Configure Gateway Settings

1. Go to the **Advanced** tab
2. Click **Settings...** under "Connect from anywhere"
3. In the Connection settings dialog:
   - **Uncheck** "Use these RD Gateway server settings"
   - Enter **rdgw.taaurus.aau.dk** in the Server name field
   - Select **Ask for password** from the Logon method dropdown
4. Click **OK** to save settings
5. Click **Connect** to initiate the connection

![Screenshot of RDP](/assets/img/taaurus/rdp-2.png)

## Step 4: Authentication Process

You will go through a multi-step authentication process:

### First Authentication
- A Windows Security popup will appear
- Enter your **AAU email address** and **password**
- Click **OK**

### Second Authentication (2FA)
- You will be prompted to authenticate using your **Microsoft Authenticator app**
- Open the app and approve the login request

### Final Authentication
- You may need to authenticate once more with your **AAU email and password**

![Screenshot of RDP](/assets/img/taaurus/rdp-3.png)

## Step 5: Success!

Once authenticated, you will be connected to the TAAURUS remote desktop environment. You should see the desktop interface of the TAAURUS server.

![Screenshot of RDP](/assets/img/taaurus/taaurus-server.png)

## Troubleshooting

If you encounter any issues during the login process:

1. **Connection fails**: Check your internet connection and try again
2. **Authentication errors**: Verify your AAU credentials and 2FA setup
3. **Gateway issues**: Ensure you've correctly configured the RD Gateway settings
4. **Still having problems**: Contact CLAAUDIA support at [serviceportal.aau.dk](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad00131d0)

## Next Steps

Now that you're logged in, you're ready to explore the TAAURUS platform. Continue to learn about [navigating TAAURUS](/taaurus/guides/navigating-taaurus), available applications, and the file system.
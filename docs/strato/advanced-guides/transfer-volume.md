# Guide: Transferring volumes using the Strato interface

This guide explains how to transfer a volume to another user using the Strato web interface. You can also use this method to change the ownership of a volume within a project by transferring it to another person or yourself within the same project.

### 1. Log in to [Strato](https://strato-new.claaudia.aau.dk/)

1. Open your web browser and navigate to your Strato interface.
2. Log in with your WAYF credentials.

### 2. Select the right project

1. Select the project where the volume is owned in the top ribbon.

### 3. Navigate to volumes

1. In the left sidebar, navigate to **Volumes** > **Volumes** and you will now see a list of all the volumes in the project.

### 4. Select the volume

1. Locate the volume you want to transfer.
2. Ensure the volume is **available** (not attached to any instance).
3. Click the **Create Transfer** button in the **Actions** column for that volume.

![Create Transfer button in Strato interface](../../assets/img/openstack/transfer-volumes_create%20transfer.png)

### 5. Create the transfer

1. Enter a **Name** for the transfer (optional).
2. Click **Create Volume Transfer**.

A **Transfer ID** and **Authorization Key** will be displayed. **Copy these details** and share them securely with the recipient.

### 6. Accept the transfer (Recipient)

1. The recipient logs in to the Strato interface.
2. Go to **Volumes** > **Volumes**.
3. Click **Accept Transfer**.
4. Enter the **Transfer ID** and **Authorization Key** provided.
5. Click **Accept Volume Transfer**.

The volume will now appear in the recipient's project.

### Notes

- The volume must be detached from the server before transfer.
- After transfer, all access to the volume is moved to the recipient.


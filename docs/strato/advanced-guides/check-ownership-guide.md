
# How to Check Ownership of a Volume or Server on Strato

This guide walks you through verifying whether you are the owner of a **volume** or **instance (server)** on **Strato**.

### Finding your User ID and Project ID
- You can use the **Identity > Projects** section to confirm your current *project ID*.
- You can use the **Identity > Users** section to confirm your *user ID*.
- You need to check that you select the correct project from the project dropdown menu in the top-left corner of the Strato landing page.

## Checking Server (Instance) Ownership

### 1. **Log in** to the Strato web interface.
1. Navigate to the [Strato web interface](https://strato-new.claaudia.aau.dk/)
2. Log in with your AAU (WAYF) credentials.

### 2. Navigate to your list of instances (servers)

1. Go to **Project > Compute > Instances**.

### 3. Find the instance

1. Find the instance you want to check in the list.

### 4. Open the instance details page

1. Click the instance name to open its **details page**.

### 5. Under the **"Overview"** tab, check:

   1. **Project ID**
   2. **User ID**
   3. **Launched by**

If your **User** and **Project ID** matches the metadata, you are the owner.


## Checking Volume Ownership

### 1. **Log in** to the Strato web interface.
1. Navigate to the [Strato web interface](https://strato-new.claaudia.aau.dk/)
2. Log in with your AAU (WAYF) credentials.

### 2. Open the volumes list

1. Navigate to **Project > Volumes > Volumes**.

> Note: It is a good idea to name your volumes appropriately before deleting any compute instances that they are attached to. Click the **Edit Volume** button to edit the volume name.

### 3. Find the volume you want to transfer

1. In the volume list, locate the volume in question.

> If you have not named the volume appropriately, you can check the **Attached To** column to get the name of the instance it is attached to.

### 4. Click the volume name to view **detailed metadata**, which includes:
   1. **User ID**
   2. **Project ID**
   3. **Created at**
   4. **Attachments**, to identify any server attachments that are registered for the volume.

If your **User** and **Project ID** matches the metadata, you are the owner.
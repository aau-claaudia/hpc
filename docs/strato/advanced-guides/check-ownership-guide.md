
# How to Check Ownership of a Volume or Server on Strato

This guide walks you through verifying whether you are the owner of a **volume** or **instance (server)** on **Strato**.

## Prerequisites

- Access to the [Strato dashboard](https://strato-new.claaudia.aau.dk/).
- Valid Strato credentials for the project in question

## Tips

- You can use the **Identity > Projects** section to confirm your current *project ID*.
- You can use the **Identity > Users** section to confirm your *user ID*.
- You need to check that you select the correct project from the project dropdown menu in the top-left corner of the Strato landing page.


## Checking Volume Ownership

1. **Log in** to the Strato web interface.
2. Navigate to **Project > Volumes > Volumes**.
3. In the volume list, locate the volume in question.
4. Click the volume name to view **detailed metadata**, which includes:
   a. **User ID**
   b. **Project ID**
   c. **Created at**

> If your user or **Project ID** matches the metadata, you are the owner.

## Checking Server (Instance) Ownership

1. Go to **Project > Compute > Instances**.
2. Find the instance in the list.
3. Click the instance name to open its **details page**.
4. Under the **"Overview"** tab, check:
   a. **Project ID**
   b. **User ID**
   c. **Launched by**

> These fields confirm who launched the instance and under which project.
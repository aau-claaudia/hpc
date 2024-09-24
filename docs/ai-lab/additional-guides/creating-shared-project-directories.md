##### In AI-LAB, semester groups can collaborate by creating shared project directories in `/ceph/project`. Follow this guide to set up a project directory and ensure that only group members can access it.

!!! info "Note: This guide only works between users in a semester group"
    You can check if your part of the same group, by using this command:
    
    ```
    groups
    ```
    
    A semester group could be something like `xx-43-xx-9-01@student.aau.dk`.


### Step 1: Create a Project Directory
Navigate to the `/ceph/project` directory:

```
cd /ceph/project
```

Create your project directory (replace [project_name] with the name of your project):

```
mkdir [project_name]
```

### Step 2: Set Directory Permissions
Next, set the directory permissions so that only users in your group can access and collaborate in the project directory.

Check your group (you can confirm the group with this command):

```
groups
```

A semester group could be something like `xx-43-xx-9-01@student.aau.dk`.

Assign the group ownership to your project directory (replace [your_group] with your group’s name):

```
chgrp [your_group] [project_name]
```

Set the directory permissions to allow full access for the group:

```
chmod 770 [project_name]
```

!!! info "What does `770` mean?"

    `770` means:

    * rwx (read, write, execute) for the owner and the group.
    * No permissions for others.

### Step 3: Ensure New Files Inherit Group Permissions
To make collaboration easier, you can set the setgid (set group ID) bit on the directory. This ensures that all files and subdirectories created inside will inherit the same group.

Set the setgid bit on your project directory:

```
chmod g+s [project_name]
```

This ensures that any new files or directories created inside the project will automatically belong to the group.

### Step 4: Verify Permissions
You can verify that the permissions are correctly set by listing the directory details:

```
ls -ld [project_name]
```

You should see something like:

```
drwxrws--- 2 [your_username] [your_group] 4096 Sep 17 12:34 [project_name]
```

`s` under the group permissions indicates the setgid bit is enabled.

The directory is now only accessible by the owner and the group members.

### Step 5: Collaboration
Now that the project directory is set up:

* Any group member can access, read, write, and create files within the directory.
* Users who are not in the group cannot access the directory.

!!! info "Notes:"
    * No other users outside the group will be able to access this directory.
    *  If you need to change the group or add more users, you’ll need administrative assistance.
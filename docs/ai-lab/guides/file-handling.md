You are now logged into AI-LAB and are in your user directory, which is located at `/ceph/home/domain/user`. You can confirm this by typing `pwd`. 

This directory is your private storage space where you can keep all your files. It is stored on a network file system, so you can access your files from any compute node within the platform.

Here is the general file structure on AI-LAB:

<div class="tree">
	<ul>
	<li><i class="fa fa-folder-open"></i> /ceph <span>AI-LAB's file system</span>
		<ul>
		<li><i class="fa fa-folder-open"></i> home <span>user home directories</span>
			<ul>
			<li><i class="fa fa-folder-open"></i> [domain] <span>e.g student.aau.dk</span>
				<ul>
				<li><i class="fa fa-folder"></i> [user] <span>your user directory </span>
				</li>
				</ul>
			</li>
			</ul>
		</li>
		<li><i class="fa fa-folder-open"></i> project <span>shared project directories</span>
		</li>
		<li><i class="fa fa-folder-open"></i> course <span>directory with course specific material</span>
		</li>
		<li><i class="fa fa-folder-open"></i> container <span>directory with ready-to-use applications</span>
		</li>
		</ul>
	</li>
	</ul>
</div>

For a detailed overview of the AI-LAB storage system, click [here](/ai-lab/system-overview/#storage){target=_blank}.

<hr>

## Essential Linux commands you should know

As you've properly noticed, working on AI-LAB involves navigating a **Linux** environment. Whether you're managing files or editing scripts, familiarity with a few core Linux commands can make your workflow smoother. If you’re completely new to Linux or just need a quick refresher, explore the commands below.

??? info "Basic Linux commands to know"

    Below are some basic commands that will help you navigate and manage files on AI-LAB:

    ### 1. Navigation
    - `pwd`: Prints the current working directory.  
    - `cd`: Changes the current directory. E.g. `cd /ceph/home/student.aau.dk/user/folder`
    - `ls`: Lists files and directories.  

    ### 2. Working with directories and files
    - `mkdir`: Creates a new directory. E.g `mkdir my_new_folder`
    - `rm`: Removes files or directories.  
      ```bash
      rm myfile.txt  # remove a file
      rm -r myfolder  # remove a directory and its contents
      ```
    - `cp` Copies files or directories.  
      ```bash
      cp target_folder/file1.txt destination_folder/file2.txt # copy a file
      cp -r target_folder/folder1 destination_folder/folder2  # copy a directory
      ```
    - `mv`: Moves or renames files/directories.  
      ```bash
      mv file1.txt file2.txt # rename
      mv target_folder/file.txt destination_folder/ # move to a new location
      ```
	- `cat`: Displays file content. E.g. `cat file.txt`    

	### 3: A simple text editor
	Nano is a beginner-friendly text editor. It is easy to use, making it a good choice for new users.
	
	- `nano myfile.txt`: Create a new file or edit an existing file.

	Once inside Nano, use the following commands:

	* Move the cursor: Use the arrow keys.
	* Save the file: Press `Ctrl + O`, then hit `Enter`.
	* Exit Nano: Press `Ctrl + X`.
	* Cut and Paste:
		* To cut: `Ctrl + K` cuts the current line.
		* To paste: `Ctrl + U` pastes the cut text.
	* Search within the file: Press `Ctrl + W`, type the search term, and hit `Enter`.

	!!! info "Tips for Nano"
		* The commands at the bottom of the Nano screen start with the `^` symbol, which stands for the `Ctrl` key.
		* For more advanced editing, Nano has flags like syntax highlighting and can open files as read-only using the `-v` flag:
		```
		nano -v myfile.txt
		```
    ---
    **Tip:** Use `man <command>` (e.g., `man ls`) or `--help` (e.g., `ls --help`) to learn more about a specific command and its options.

<hr>

## Transfer files between your local computer and AI-LAB

===+ "Windows"
	You can transfer files between your local computer and AI-LAB using [WinSCP](https://winscp.net/eng/download.php){target=_blank}. Other popular solutions are [PuTTY](https://www.putty.org/){target=_blank} and [FileZilla](https://filezilla-project.org/){target=_blank}. Alternatively, you can use the `scp` command, as shown for [Linux/MacOS](#__tabbed_1_2) users.

	When you open WinSCP, you will be greeted by a *Login* modal. Follow the instructions in the image above to establish a connection to the server.
	![Screenshot of WinSCP setup](/assets/img/ai-lab/winscp-setup.png)
		
	You can now drag and drop files between your local computer and the AI-LAB platform.

	!!! info
		You might want to display hidden files in WinSCP (such as files starting with a dot on Linux systems). Go to Options → Preferences... → Panels and turn on "Show hidden files".

===+ "Linux/MacOS"

	You can transfer files between your local computer and AI-LAB using the command line utility `scp` from your local computer (**note:** You have to be logged out from AI-LAB to use `scp`).

	```console
	scp -r some-file user@student.aau.dk@ailab-fe01.srv.aau.dk:~/some-dir
	```

	Replace `user@student.aau.dk` with your AAU email address.
	
	Here, `~` represents your user directory on AI-LAB and `/some-dir` a folder in your directory. 

	<hr>

	To copy files from AI-LAB to your local computer, use:


	```console
	scp -r user@student.aau.dk@ailab-fe01.srv.aau.dk:~/some-folder/some-subfolder/some-file .
	```

	Replace `user@student.aau.dk` with your AAU email address.

	Here, `.` represents the current directory on your local computer.

<hr>

## Creating shared project directories

On AI-LAB, semester groups can collaborate by creating shared project directories in `/ceph/project`. Follow the guide below to set up a project directory and ensure that only group members can access it.

??? info "Guide on how to create shared project directories"

	!!! info "Note: This guide only works between users in a semester group"
		Unfortunately you cannot create a private shared directory for specific users that are not part of a semester group. Therefore, you can only create a public available project directory.

		Navigate to the `/ceph/project` directory:

		```
		cd /ceph/project
		```

		Create your project directory (replace [project_name] with the name of your project):

		```
		mkdir [project_name]
		```

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

	!!! info "Important: Fix Permission Issues for Uploaded Files:"
		When uploading existing files from your own computer, they may **not** automatically get the correct permissions, preventing other group members from editing them.

		To **automatically fix permissions**, follow these steps:

		#### **1. Create an Automatic Fix Script**
		Create a script that will regularly correct the permissions of uploaded files.

		1. Open a terminal and create a new script file, e.g. inside the project directory:
	
			```
			nano /ceph/project/[project_name]/fix_permissions.sh
			```

		2. Add the following content to the file:
		
			```
			#!/bin/bash
			chmod -R g+rwX /ceph/project/[project_name]
			```

		3. Save the file (`CTRL + X`, then `Y`, then `ENTER`).

		4. Make the script executable:

			```
			chmod +x /ceph/project/fix_permissions.sh
			```

		#### **2. Set Up a Cron Job to Run the Script Automatically**
		A cron job will run the script **every 5 minutes**, ensuring tht all uploaded files get the correct permissions.

		1. Open the cron job editor:

			```
			crontab -e
			```

		2. Add this line at the bottom:

			```
			*/5 * * * * /ceph/project/[project_name]/fix_permissions.sh
			```

		**Remember to replace [project_name] with the name of your project folder throughout the guide**
		
		3. Save the file (`CTRL + X`, then `Y`, then `ENTER`).

		Now, every **5 minutes**, the script will automatically fix permissions for any uploaded files.


Now that you know the basics of file handling, lets proceed to learn how to [**run jobs on AI-LAB :octicons-arrow-right-24:**](running-jobs.md)


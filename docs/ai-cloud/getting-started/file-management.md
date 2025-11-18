
### Transfer files between a server and a local computer

On this page you will learn how to transfer files from your local computer to AI Cloud.

===+ "Linux/MacOS"

	You can transfer files between your local computer and AI Cloud using the command line utility `scp`. This will only work if you call the command from your local computer and not the server.

	```console
	scp some-file user@domain.aau.dk@ai-fe02.srv.aau.dk:~/some-dir
	```

	Replace `user@domain.aau.dk` with your AAU email address.
	
	Here, `~` represents your user directory on AI Cloud and `/some-dir` a folder in your directory. 

	<hr>

	To copy files from AI Cloud to your local computer, use:

	```console
	scp user@domain.aau.dk@ai-fe02.srv.aau.dk:~/some-folder/some-subfolder/some-file .
	```

	Replace `user@domain.aau.dk` with your AAU email address.

	Here, `.` represents the current directory on your local computer.

    !!! error
        Please keep in mind that this a network operation, where files are transferred over the SSH protocol. Before attempting to reach the server with WinSCP, please ensure that you are conencted to the AAU network - either by being physically on campus grounds or using the [VPN service](https://www.en.its.aau.dk/instructions/vpn)


===+ "Windows"

    From a Windows PC you can transfer files to AI Cloud using [WinSCP](https://winscp.net/eng/download.php) - or in the command line using `scp`.

	1. Start by downloading and installing [WinSCP](https://winscp.net/eng/download.php).

    2. Open WinSCp - this will greet you with a *login interface*.

	   ![Screenshot of WinSCP setup](/assets/img/ai-cloud/winscp-setup.png)

    Configure the connection as follows:

	- **Host name**: `ai-fe02.srv.aau.dk`
	- **User name**: Your AAU email address
	- **Password**: Your AAU password

    3. Click **Login** and a new window should open.

    ### Success! 
	You should now be able to drag and drop files between your local computer and AI Cloud.

    <hr>

	!!! tip
		Yay want to display hidden files in WinSCP (such as files starting with a dot on Linux systems). Go to Options → Preferences... → Panels and turn on "Show hidden files".

    !!! failure "Can't login?"
        Please keep in mind that this a network operation, where files are transferred over the SSH protocol. Before attempting to reach the server with WinSCP, please ensure that you are conencted to the AAU network - either by being physically on campus grounds or using the [VPN service](https://www.en.its.aau.dk/instructions/vpn)


<hr>

Now that you know the basics of file transfer, lets proceed to learn how to obtain [**container images :octicons-arrow-right-24:**](/ai-cloud/getting-started/container-images/)


### Transfer files between a server and a local computer

===+ "Windows"
	You can transfer files between your local computer and AI Cloud using [WinSCP](https://winscp.net/eng/download.php). Other popular solutions are [PuTTY](https://www.putty.org/) and [FileZilla](https://filezilla-project.org/). Alternatively, you can install [OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) to use the `scp` command, as shown for [Linux/MacOS](#__tabbed_1_2) users.

	When you open WinSCP, you will be greeted by a *Login* modal. Follow the instructions in the image above to establish a connection to the server.
	![Screenshot of WinSCP setup](/assets/img/ai-cloud/winscp-setup.png)
		
	You can now drag and drop files between your local computer and the AI Cloud platform.

	!!! info
		You might want to display hidden files in WinSCP (such as files starting with a dot on Linux systems). Go to Options → Preferences... → Panels and turn on "Show hidden files".

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


<hr>

Now that you know the basics of file transfer, lets proceed to learn how to obtain [**container images :octicons-arrow-right-24:**](/ai-cloud/getting-started/container-images/)

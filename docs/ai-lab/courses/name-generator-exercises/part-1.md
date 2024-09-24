1. Log in to AI-LAB

2. Copy the project `/ceph/course/claaudia/generating-names-with-pytorch` to your user directory

3. Open `name_generator.py` from the copied `/generating-names-with-pytorch` with [vim](https://www.geeksforgeeks.org/how-to-edit-text-files-in-linux/#2-vim) or [nano](https://www.geeksforgeeks.org/how-to-edit-text-files-in-linux/#1-nano) text editors.

4. Add `samples('German', 'GER')` at the bottom of the code, to generate some German names, save it and exit the file.


!!! info "References"
     * [https://hpc.aau.dk/ai-lab/getting-started/login/](https://hpc.aau.dk/ai-lab/getting-started/login/)
     * [https://hpc.aau.dk/ai-lab/getting-started/file-management/](https://hpc.aau.dk/ai-lab/getting-started/file-management/)


??? info "Solution"
     1. Run the following command on a command-line interface on your local Windows (Windows PowerShell), macOS, or Linux computer `ssh -l user@student.aau.dk ailab-fe01.srv.aau.dk`. Replace user@student.aau.dk with your AAU email address.

          The first time you connect, you will get a message like:

          ```
          The authenticity of host 'ailab-fe01.srv.aau.dk (172.21.131.1300)' can't be established.
          ED25519 key fingerprint is SHA256:xosJtOSfQyyW16c6RtpN8tAi/91XHCR3GxM9/KJEogg.
          This key is not known by any other names.
          Are you sure you want to continue connecting (yes/no/[fingerprint])?
          Please confirm by typing 'yes' to proceed with the connection.
          ```

          Please confirm by typing `yes` to proceed with the connection.

     2. Enter `cp -r /ceph/course/claaudia/generating-names-with-pytorch .` to copy the directory to your user directory
     3. Enter `cd generating-names-with-pytorch` to go into the directory
     4. Use `nano name_generator.py` to open the python file with nano text editor
           * Go down to the bottom of the script and enter `samples('German', 'GER')`.
           * Press `CTRL+O` followed by `ENTER` to save the file, then press `CTRL+X` to exit the file.
     5. Use `cat name_generator.py` and check that `samples('German', 'GER')` is now at the bottom of the code.
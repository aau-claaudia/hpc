##### In this exercise series, you'll work with a Recurrent Neural Network (RNN) to generate 3 fictional German names based on a dataset of ~700 german names. The script you'll interact with is based on PyTorch and demonstrates how AI-LAB can be used for sequence prediction tasks.

1. Log in to AI-LAB ([Login guide](https://hpc.aau.dk/ai-lab/getting-started/login/))

2. Copy the folder `/ceph/course/claaudia/generating-names-with-pytorch` to your user directory ([Guide on how to copy a folder](https://hpc.aau.dk/ai-lab/getting-started/file-management/#transfer-files-within-ai-lab))

3. Go into the copied directory `generating-names-with-pytorch` and open `name_generator.py` with nano ([Nano guide](https://hpc.aau.dk/ai-lab/applications/linux-text-editors/#nano-a-simple-text-editor)) or vim ([Vim guide](https://hpc.aau.dk/ai-lab/applications/linux-text-editors/#vim-a-powerful-text-editor)) text editor.

4. Add this line: `samples('German', 'GER')` at the bottom of the code, save it, and exit the file.

5. (Optional) run `cat name_generator.py` to print out the code, and verify that `samples('German', 'GER')` is at the bottom.


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

     2. Enter `cp -r /ceph/course/claaudia/generating-names-with-pytorch ~/` to copy the directory to your user directory
     3. Enter `cd generating-names-with-pytorch` to go into the directory
     4. Use `nano name_generator.py` to open the python file with nano text editor
           * Go down to the bottom of the script and enter `samples('German', 'GER')`.
           * Press `CTRL+O` followed by `ENTER` to save the file, then press `CTRL+X` to exit the file.
     5. Use `cat name_generator.py` and check that `samples('German', 'GER')` is now at the bottom of the code.



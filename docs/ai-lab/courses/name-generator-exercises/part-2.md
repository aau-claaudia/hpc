1. Use `ls /ceph/container/pytorch` command to find an appropriate PyTorch container. Copy the path to the container. 

2. Edit `run.sh` with nano ([Nano guide](https://hpc.aau.dk/ai-lab/applications/linux-text-editors/#nano-a-simple-text-editor)) or vim ([Vim guide](https://hpc.aau.dk/ai-lab/applications/linux-text-editors/#vim-a-powerful-text-editor)) text editor.

3. Set the following parameters in the script ([Guide to run a bash script](https://hpc.aau.dk/ai-lab/additional-guides/run-a-bash-script/))
      * Set `#SBATCH --cpus-per-task=` to 15
      * Set `#SBATCH --mem=` to 24G
      * Set `#SBATCH --gres=gpu:1`
      * Add the container path you copied to `PATHTOCONTAINER=`
      * Add `name_generator.py` to `SCRIPT=`

4. Save and exit the file.

5. Start `run.sh` using `sbatch` command

6. Use `watch -n 1 squeue --me` to check your job process (approx. 3 minutes to processs)

7. When the job done, press `CTRL+C` to exit `watch`-mode and check the content of `result_x.out` using  `cat` command. The `x` is the job id.


??? info "Solution"
     1. Use `ls /ceph/container` to locate a PyTorch container image in the `/ceph/container` directory. Copy the path, e.g. `/ceph/container/pytorch/pytorch_24.07.sif`.
     2. Make sure your current directory is `user@student.aau.dk@ailab-fe01:~/generating-names-with-pytorch$`.
        * If not, go into the directory by using `cd generating-names-with-pytorch`.
     3. Use `nano run.sh` to open the bash script with nano text editor
        * Set `#SBATCH --cpus-per-task=` to 15
        * Set `#SBATCH --mem=` to 24G
        * Set `#SBATCH --gres=gpu:1`
        * Add the container path you copied to `PATHTOCONTAINER=`
        * Add `name_generator.py` to `SCRIPT=`
     4. Press `CTRL+O` followed by `ENTER` to save the file, then press `CTRL+X` to exit the file.
     5. Use `sbatch run.sh` to start the job.
     6. Use `watch -n 1 squeue --me` to check your job process
     7. When the job done, press `CTRL+C` to exit `watch`-mode and check the content of `result_x.out` using  `cat` command 
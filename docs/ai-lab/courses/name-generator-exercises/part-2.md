1. Find and copy the path to a PyTorch container in the `/ceph/container` directory.

2. Edit `run.sh`.
      * Replace `PATHTOCONTAINER` with the path to the container you copied.
      * Edit the script to use the following allocation:
           * 1 GPU
           * 15 CPUs
           * 24GB memory

3. Start `run.sh` using `sbatch` command 

4. Use `watch -n 1 squeue --me` to check your job process (approx. 3 minutes to processs)

5. When the job done, press `CTRL+C` to exit `watch`-mode and check the content of `result_x.out` using  `cat` command 

!!! info "References"
     * [https://hpc.aau.dk/ai-lab/additional-guides/run-a-bash-script/](https://hpc.aau.dk/ai-lab/additional-guides/run-a-bash-script/)
     * [https://hpc.aau.dk/ai-lab/additional-guides/cpu-gpu-and-memory-allocation/](https://hpc.aau.dk/ai-lab/additional-guides/cpu-gpu-and-memory-allocation/)

??? info "Solution"
     1. Use `ls /ceph/container` to locate a PyTorch container image in the `/ceph/container` directory. Copy the path, e.g. `/ceph/container/pytorch/pytorch_24.07.sif`.
     2. Make sure your current directory is `user@student.aau.dk@ailab-fe01:~/generating-names-with-pytorch$`.
        * If not, go into the directory by using `cd generating-names-with-pytorch`.
     3. Use `nano run.sh` to open the bash script with nano text editor
           * Replace `PATHTOCONTAINER` with `/ceph/container/pytorch/pytorch_24.07.sif`.
           * Edit the script to use `#SBATCH --cpus-per-task=15`, `#SBATCH --mem=24G`, `#SBATCH --gres=gpu:1`
           * Press `CTRL+O` followed by `ENTER` to save the file, then press `CTRL+X` to exit the file.
     4. Use `sbatch run.sh` to start the job.
     5. Use `watch -n 1 squeue --me` to check your job process
     6. When the job done, press `CTRL+C` to exit `watch`-mode and check the content of `result_x.out` using  `cat` command 

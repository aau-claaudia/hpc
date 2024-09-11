## Part 1: 

1. Log in to AI-LAB

2. Copy the project `/ceph/course/claaudia/generating-names-with-pytorch` to your user directory

3. Open `name_generator.py` from the copied `/generating-names-with-pytorch` with [vim](https://www.geeksforgeeks.org/how-to-edit-text-files-in-linux/#2-vim) or [nano](https://www.geeksforgeeks.org/how-to-edit-text-files-in-linux/#1-nano) text editors.

4. Add `samples('German', 'GER')` at the bottom of the code, to generate some German names, save it and exit the file.

!!! info "References"
  * [https://hpc.aau.dk/ai-lab/getting-started/login/](https://hpc.aau.dk/ai-lab/getting-started/login/)
  * [https://hpc.aau.dk/ai-lab/getting-started/file-management/](https://hpc.aau.dk/ai-lab/getting-started/file-management/)


## Part 2:

1. Edit the bash script `run.sh` to run `name_generator.py` using a PyTorch container from the `/ceph/container` directory.

    * **Use the following allocation:**
        * 1 GPU
        * 15 CPUs
        * 60GB memory

2. Start `run.sh` using `sbatch` command 

3. Use `squeue --me` to check your job process

4. When the job done, check the content of `result_x.out` using  `cat` command 

!!! info "References"
  * [https://hpc.aau.dk/ai-lab/additional-guides/run-a-bash-script/](https://hpc.aau.dk/ai-lab/additional-guides/run-a-bash-script/)
  * [https://hpc.aau.dk/ai-lab/additional-guides/cpu-gpu-and-memory-allocation/](https://hpc.aau.dk/ai-lab/additional-guides/cpu-gpu-and-memory-allocation/)

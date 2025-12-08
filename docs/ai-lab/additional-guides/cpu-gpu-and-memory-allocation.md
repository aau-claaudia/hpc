To effectively run jobs, it's important to understand the hardware configuration and set appropriate parameters for resource allocation. Here’s a detailed guide on setting Slurm parameters based on the specified hardware on the platform:

### Memory per job
`--mem` specifies the memory allocated to the job. Maximum value is 24 GB per GPU. Example:

```
srun --mem=24G singularity exec --nv /ceph/container/pytorch/pytorch_24.09.sif python3 /ceph/course/claaudia/docs/torch_bm.py
```


### CPUs per task

`--cpus-per-task` specifies the number of CPUs allocated to each task. Maximum value is 15 CPUs per GPU. Example:

```
srun --cpus-per-task=15 singularity exec --nv /ceph/container/pytorch/pytorch_24.09.sif python3 /ceph/course/claaudia/docs/torch_bm.py
```

<p>There is actually 16 CPUs per GPU available, but using a maximum of 15 CPUs per GPU, leaves 1 CPU free per GPU for system overhead and non-GPU tasks, which helps in maintaining overall system stability and performance.</p>


### GPUs per job

`--gres=gpu` specifies the number of GPUs required for the jobs. **Maximum value is 4 GPUs per job.** Example:

```
srun --gres=gpu:4 singularity exec --nv /ceph/container/pytorch/pytorch_24.09.sif python3 /ceph/course/claaudia/docs/torch_bm.py
```

!!! info "GPU Resource Limits"
    To ensure fair access for all users, AI-LAB enforces two important limits:
    
    - **Maximum 4 GPUs per job**: A single job can request no more than 4 GPUs (e.g., `--gres=gpu:4` or `-G 4`)
    - **Maximum 8 GPUs per user**: Each user can run jobs using a total of up to 8 GPUs simultaneously across all their running jobs
    
    We strongly encourage inexperienced users to allocate only 1 GPU, as most workloads do not speed up automatically with more GPUs. For advanced users who know how to configure multi-GPU training correctly, up to 4 GPUs per job remain available.

Request only the number of GPUs your job can effectively utilize. Over-requesting can lead to resource underutilization and longer queue times. Some applications may need adjustments to scale effectively across multiple GPUs. [Here](multiple-gpus-with-pytorch.md) is an example of a PyTorch script that can handle multiple GPUs. 

!!! info "Monitor GPU usage"

    You can use the NVIDIA GPU monitoring command `nvidia-smi` to output GPU usage information. Learn how to use it in [this guide](checking-gpu-usage.md).

### Number of tasks to be run

`--ntasks` specifies the number of tasks to be run. Each task typically corresponds to an independent execution of your program or script. If your job can be parallelized across multiple tasks, set the number of tasks to e.g. `--ntasks=4` for running 4 parallel tasks. Each task gets its allocation of resources (CPU, memory, etc.) based on other parameters like `--cpus-per-task`, `--mem`, and `--gres=gpu`.
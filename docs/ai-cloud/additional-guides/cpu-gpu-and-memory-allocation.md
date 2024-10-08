To effectively run jobs, it's important to understand the hardware configuration and set appropriate parameters for resource allocation. Here’s a detailed guide on setting Slurm parameters based on the specified hardware on the platform:

### Memory per job

`--mem` specifies the memory allocated to the job. Example:

```
srun --mem=60G singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
```

### CPUs per task


`--cpus-per-task` specifies the number of CPUs allocated to each task. Example:

```
srun --cpus-per-task=15 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
```

### GPUs per job


`--gres=gpu` specifies the number of GPUs required for the jobs. Example:

```
srun --gres=gpu:4 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
```

Request only the number of GPUs your job can effectively utilize. Over-requesting can lead to resource underutilization and longer queue times. Some applications may need adjustments to scale effectively across multiple GPUs. [Here](multiple-gpus-with-pytorch.md) is an example of a PyTorch script that can handle multiple GPUs. 

!!! info "Monitor GPU usage"

    You can use the NVIDIA GPU monitoring command `nvidia-smi` to output GPU usage information. Learn how to use it in [this guide](checking-gpu-usage.md).

### Number of tasks to be run

`--ntasks` specifies the number of tasks to be run. Each task typically corresponds to an independent execution of your program or script. If your job can be parallelized across multiple tasks, set the number of tasks to e.g. `--ntasks=4` for running 4 parallel tasks. Each task gets its allocation of resources (CPU, memory, etc.) based on other parameters like `--cpus-per-task`, `--mem`, and `--gres=gpu`.
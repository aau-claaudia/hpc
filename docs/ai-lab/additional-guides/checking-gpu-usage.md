Monitoring GPU usage is a good practice for optimizing the performance of your jobs running, particularly if you intend to utilize multiple GPUs and verify their usage. This guide will provide step-by-step instructions on how to monitor GPU usage using a Python script.

### Start a job with GPU allocation

First, submit a job using `srun` or `sbatch` with one GPU or more allocated and execute some code inside a Singularity container. In this example we will use the `pytorch_24.09.sif` container image from `/ceph/container/pytorch` directory and a PyTorch benchmark script `torch_bm.py` from `/ceph/course/claaudia/docs` directory:

```
srun --gres=gpu:1 singularity exec --nv /ceph/container/pytorch/pytorch_24.09.sif python3 torch_bm.py
```

### Check job id

Open another AI-LAB terminal session, and check the status of your jobs using `squeue --me` to find the job ID of the job you just submitted.

```
squeue --me
```

### Connect to running job interactively

Once you have identified the job ID (let's assume it's `1978` in this example), connect to the running job interactively using the following command to start a new shell.

```
srun --jobid 1978 --interactive --pty /bin/bash
```

### Monitor GPU usage

Inside the interactive session of your job, start monitoring GPU usage using the following command:

```
python3 /ceph/course/claaudia/docs/gpu_util.py
```

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 555.42.02              Driver Version: 555.42.02      CUDA Version: 12.5     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA L4                      Off |   00000000:01:00.0 Off |                    0 |
| N/A   44C    P0             36W /   72W |     245MiB /  23034MiB |     90%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA L4                      Off |   00000000:02:00.0 Off |                    0 |
| N/A   38C    P8             16W /   72W |       4MiB /  23034MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA L4                      Off |   00000000:41:00.0 Off |                    0 |
| N/A   41C    P8             16W /   72W |       1MiB /  23034MiB |      0%      Default |
|                                         |                        |                  N/A |
...

+------------------------------------------------------------------------------+
|  GPU    PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND               |
|    0 232843   user@+     236MiB   100   0.1  01:00:20  /usr/bin/python3 tor  |
+------------------------------------------------------------------------------+

```

The most important parameter to notice here is the `GPU-Util` metric. Here, you can see that the first GPU is operating at 90% GPU utilization. This indicates excellent utilization of the GPU.

!!! info "High Utilization (70-100%)"
    For many GPU-accelerated applications like deep learning training or scientific simulations, a high GPU utilization (often around 70-100%) during compute-intensive tasks is considered good. It indicates that the GPU is efficiently processing tasks without significant idle time.

!!! info "Low to Moderate Utilization (10-40%)"
    In some cases, especially when the workload is less intensive or the application is idle waiting for data or other resources, the GPU utilization might be lower (e.g., 10-40%). This doesn't necessarily mean the GPU is underutilized or performing poorly; it could indicate a natural variation in workload or efficient scheduling of tasks.

You can locate which GPU(s) that belongs to your job, by finding your username below `USER` and the GPU number under `GPU`. In this case `user@+` are utilizing GPU number `0` in the NVIDIA-SMI list.

``` 
+------------------------------------------------------------------------------+
|  GPU    PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND               |
|    0 232843   user@+     236MiB   100   0.1  01:00:20  /usr/bin/python3 tor  |
+------------------------------------------------------------------------------+
```


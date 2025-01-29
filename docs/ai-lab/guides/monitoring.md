## Checking the queue

When using the cluster, you typically wish to see an overview of what is currently in the queue. For example to see how many jobs might be waiting ahead of you or to get an overview of your own jobs.

The command `squeue` can be used to get a general overview:

```
squeue

JOBID   PARTITION       NAME      USER    ST      TIME    NODES   NODELIST(REASON)
42            gpu   interact  xxxxxxxx     R   6:45:14        1        ailab-l4-01
```

1.  `JOBID` shows the `ID` number of each job in queue.
2.  `PARTITION` shows which partition each job is running in.
3.  `NAME` is the name of the job which can be specified by the user creating it.
4.  `USER` is the username of the user who created the job.
5.  `ST` is the current state of each job; for example `R` means a job is running and `PD` means pending. There are other states as well - see `man squeue` for more details (under `JOB STATE CODES`).
6.  `TIME` shows how long each job has been running.
7.  `NODES` shows how many nodes are involved in each job allocation.
8.  `NODELIST` shows which node(s) each job is running on, or alternatively, why it is not running yet.

 
Showing your own jobs only:

```
squeue --me
```

`squeue` can show many other details about jobs as well. Run `man squeue` to see detailed documentation on how to do this.


## Checking the status of compute nodes

It is often desirable to monitor the resource status of the compute nodes when you wish to run a job. 

The `sinfo` command shows basic information about partitions in the queue system and what the states of nodes in these partitions are.

```
sinfo
    
PARTITION       AVAIL      TIMELIMIT      NODES      STATE             NODELIST
l4*                up       12:00:00         11       idle     ailab-l4-[01-11]
vmware             up          10:00          4       idle        vmware[01-04]
```


1.  `PARTITION` can be understood as distinct categories or groups of compute nodes, essentially serving as separate queues for jobs.
2.  `AVAIL` shows the availability of the partition where `up` is normal, working state where you can submit jobs to it.
3.  `TIMELIMIT` shows the time limit imposed by each partition in `HH:MM:SS` format.
4.  `NODES` shows how many nodes are in the shown state in the specific partition.
5.  `STATE` shows which state the listed nodes are in: `mix` means that the nodes are partially full - some jobs are running on them and they still have available resources; `idle` means that they are completely vacant and have all resources available; `allocated` means that they are completely occupied. Many other states are possible, most of which mean that something is wrong.
6.  `NODELIST` shows the specific compute nodes that is affected by the job.

You can also use the command `scontrol show node` or `scontrol show node <node name>` to show details about all nodes or a specific node, respectively.

```
scontrol show node ailab-l4-04

NodeName=ailab-l4-04 Arch=x86_64 CoresPerSocket=32
CPUAlloc=0 CPUTot=128 CPULoad=2.00
AvailableFeatures=(null)
ActiveFeatures=(null)
Gres=gpu:l4:8(S:0-1)
...
```


The two commands `sinfo` and `scontrol show node` provide information which is either too little or way too much detail in most situations. As an alternative, we provide the tool `nodesummary` to show a hopefully more intuitive overview of the used/available resources.

```
nodesummary
```

![Screenshot of `nodesummary` in use.](/assets/img/ai-lab/nodesummary.png)

## Checking GPU utilization
Monitoring GPU utilization is a good practice for optimizing the performance of your jobs running, particularly if you intend to utilize multiple GPUs and verify their utilization. The guide below will provide step-by-step instructions on how to monitor GPU utilization using a Python script.

??? news "Guide on how to check GPU utilization"

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

    ### Monitor GPU utilization

    Inside the interactive session of your job, start monitoring GPU utilization using the following command:

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

    You can locate which GPU(s) that belongs to your job, by finding your username below `USER` and the GPU number under `GPU`. In this case `user@+` are utilizing GPU number `0` in the NVIDIA-SMI list.

    ``` 
    +------------------------------------------------------------------------------+
    |  GPU    PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND               |
    |    0 232843   user@+     236MiB   100   0.1  01:00:20  /usr/bin/python3 tor  |
    +------------------------------------------------------------------------------+
    ```

    !!! info "High Utilization (70-100%)"
        For many GPU-accelerated applications like deep learning training or scientific simulations, a high GPU utilization (often around 70-100%) during compute-intensive tasks is considered good. It indicates that the GPU is efficiently processing tasks without significant idle time.

    !!! info "Low to Moderate Utilization (10-40%)"
        In some cases, especially when the workload is less intensive or the application is idle waiting for data or other resources, the GPU utilization might be lower (e.g., 10-40%). This doesn't necessarily mean the GPU is underutilized or performing poorly; it could indicate a natural variation in workload or efficient scheduling of tasks.


**:material-party-popper: Congratulations! :material-party-popper:**

You've mastered the fundamentals of AI-LAB. If you have experience any errors or if you have feedback, [please let us know!](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e).

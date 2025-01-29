Before you start running jobs, it is important to be aware of the queueing system [Slurm](https://slurm.schedmd.com/quickstart.html).

## Slurm queue system
Slurm is a job scheduling system and is used to allocate resources and manage user jobs on AI-LAB. Jobs on AI-LAB can only be run through Slurm. 

The primary method to run a job via Slurm is by utilizing the command `srun`. Let's try launching a job on a compute node:

```
srun hostname
```

!!! info "Waiting in queue"

    Upon execution, you might receive a notification indicating your job has been queued, awaiting resource availability:

    ```
    srun: job X queued and waiting for resources
    ```

    Once a compute node becomes available, you'll receive confirmation:

    ```
    srun: job X has been allocated resources
    ```

Once a compute node becomes available the `hostname` command executes on the allocated compute node, revealing its identifier (e.g. `ailab-l4-01`).

!!! info "More Slurm commands"
    You can find [additional Slurm commands](../additional-guides/checking-the-queue.md) available to customize your job submissions, such as setting the time limit for a job, specifying the number of CPUs or GPUs, and more.

<hr>

## Adding job arguments



## Executing a containerized job with Singularity
To run a task within a container using Singularity, we need to add specific parameters to the Slurm command. 

As an example, let's try running `print('hello world')` using `Python3` within the `tensorflow_24.03.sif` container image from `/ceph/container/tensorflow` directory.

```
srun singularity exec /ceph/container/tensorflow/tensorflow_24.03.sif python3 -c "print('hello world')"
```

- `srun` is the Slurm command used to submit a job.
- `singularity` is the command-line interface for interacting with Singularity.
- `exec` is a sub-command that tells Singularity to execute a command inside the specified container.
- `/ceph/container/tensorflow/tensorflow_24.03.sif` is the path to the container image.
- `python3 -c "print('hello world')"` is the task that singularity executes.

While this execution proceeds smoothly, it's important to note that the command exclusively utilizes CPUs. The primary role of AI-LAB is to run software that utilises GPUs for computations. In order to run applications with a GPU you need to allocate a GPU to a job using Slurm. 

<hr>

## Allocating a GPU to your job
You can allocate a GPU to a job using the `--gres=gpu` option for Slurm. Additionally, you need to add the `--nv` option to Singularity to enable NVIDIA drivers in the container.

Let's try running a small Python script that performs a simple matrix multiplication of random data to benchmark TensorFlow computing speed with 1 GPU allocated:

First copy `benchmark_tensorflow.py` from `/ceph/course/claaudia/docs` to your user directory (`~/`):

```
cp /ceph/course/claaudia/docs/benchmark_tensorflow.py ~/
```

Then lets try allocating 1 GPU to the job by adding `--gres=gpu:1`:

```
srun --gres=gpu:1 singularity exec --nv /ceph/container/tensorflow/tensorflow_24.03.sif python3 benchmark_tensorflow.py
```

Note that the above example allocate 1 GPU to the job. It is possible to allocate more, for example `--gres=gpu:2` for two GPUs. Software for computing on GPU is not necessarily able to utilise more than one GPU at a time. It is your responsibility to ensure that the software you run can indeed utilise as many GPUs as you allocate. It is not allowed to allocate more GPUs than your job can utilise. [Here](../additional-guides/multiple-gpus-with-pytorch.md) is an example of a PyTorch script that can handle multiple GPUs. 

<hr>



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

`--gres=gpu` specifies the number of GPUs required for the jobs. Maximum value is 8 GPUs per job. Example:

```
run --gres=gpu:4 singularity exec --nv /ceph/container/pytorch/pytorch_24.09.sif python3 /ceph/course/claaudia/docs/torch_bm.py
```



Request only the number of GPUs your job can effectively utilize. Over-requesting can lead to resource underutilization and longer queue times. Some applications may need adjustments to scale effectively across multiple GPUs. [Here](multiple-gpus-with-pytorch.md) is an example of a PyTorch script that can handle multiple GPUs. 

!!! info "Monitor GPU usage"

    You can use the NVIDIA GPU monitoring command `nvidia-smi` to output GPU usage information. Learn how to use it in [this guide](checking-gpu-usage.md).

### Number of tasks to be run

`--ntasks` specifies the number of tasks to be run. Each task typically corresponds to an independent execution of your program or script. If your job can be parallelized across multiple tasks, set the number of tasks to e.g. `--ntasks=4` for running 4 parallel tasks. Each task gets its allocation of resources (CPU, memory, etc.) based on other parameters like `--cpus-per-task`, `--mem`, and `--gres=gpu`.



**:material-party-popper: Congratulations! :material-party-popper:**

You've mastered the fundamentals of AI-LAB. Ready to take the [**next steps? :octicons-arrow-right-24:**](next-steps.md)
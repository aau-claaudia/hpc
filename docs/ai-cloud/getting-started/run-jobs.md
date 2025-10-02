In this section, you will learn how to launch on a compute node (see section [System overview](/ai-cloud/system-overview/)). We do this by submitting a job to our queuing system, Slurm. We will be exploring two commands for doing this.

## The srun command
One way of running a job via Slurm is by utilizing the `srun` command. Let's try to launch a job on a compute node:
```
srun hostname
```
We might have to wait a little bit, but once a compute node becomes available the `hostname` command is executed on the compute node that was allocated to our job. The output could be something like:
```
a256-t4-01.srv.aau.dk
```
This also serves as proof that the command was indeed executed on a compute node `a256-t4-01.srv.aau.dk`.
Running `hostname` again - this time on the front end node (without `srun`):
```
hostname
```
Will return the name of the front end node:
```
ai-fe02.srv.aau.dk
```
## The sbatch command

Another way of launching a job is with the `sbatch` command. This command can be launched with *a batch-script* or *on-the-fly* with the `--wrap` argument.

### sbatch - *on the fly*

Let's this approach by entering the follwing command:
```
sbatch --wrap="hostname"
```

Notice how the command output is not printed directly to the console, but instead we get a message from Slurm, telling us that our job was submitted to the queue:
```
Submitted batch job 737186
```
We can check the state of our job by [checking the queue](/ai-cloud/additional-guides/checking-the-queue/).

Once the job is finished, we will be able to find a file in the directory we launched our job in (`slurm-737186.out`). Let's print this file:
```
cat slurm-737186.out
a256-t4-02.srv.aau.dk
```
### sbatch - with a batch-script
For better reproducibility it can be a very good idea to launch your job with a batch-script. Let's try this with a minimal example. Assuming that we have the file `hostname.sh` with the following content:
```
#!/usr/bin/env bash

#SBATCH --job-name=hostname
#SBATCH --partition=prioritized
#SBATCH --nodelist=a768-l40s-02

srun hostname
```

Here we will be launching the hostname command on the compute node `a768-l40s-02`. 

We launch a job from these instructions, with:
```
sbatch hostname.sh
```
This prints:
```
Submitted batch job 737223
```
Once the job is finished, we can use the `cat` command to print the content of the output file:
```
cat slurm-737223.out
a768-l40s-02.srv.aau.dk
```
Proving that our job did indeed run on the node we asked for.

## Which one to use: srun vs sbatch

The most important difference between these two commands is:

* `srun` returns command output directly to the console - `sbatch` writes it to a file.

A job launched with `srun` is therefore dependent on the console session the front end node, and will only run as long as the output can be printed directly to the console. If the console session is interrupted, the job is terminated. A job launched with `sbatch` does not depend on an external process, and will run until it is explicitly cancelled by the user.

!!! info "Don't launch jobs from within interactive sessions"
    It is not very good practice to start your jobs from within interactive shell sessions (using `srun --pty`), as this will start that runs until it reaches the time limit in the (6 days in the prioritized partition) - not when the actual job is finished. As a consequence the resources allocated to the job will be occupied for longer than needed.

    As stated in our [Fair usage](/ai-cloud/fair-usage/)-section, we want to encourage our users to be mindful of their resource consumption for the sake of their fellow researchers, and not occupy ressources that others could have put to use.


!!! info "Persistent terminal sessions"
    If used correctly terminal multiplexers like Tmux/Screen are great tools! However if they are used to start an interactive job on a compute node, this counts as monopolising resources (which is not allowed).

### Conclusion:

  * `srun` is best suited for development - where you want the command output to be printed directly in the console.
  * `sbatch` is best suited for long-running unmaintained jobs.

  Try to use `sbatch` as much as possible.

!!! info "More Slurm commands"
    You can find [additional Slurm commands](../additional-guides/checking-the-queue.md) available to customize your job submissions, such as setting the time limit for a job, specifying the number of CPUs or GPUs, and more.


## Executing a containerized job with Singularity
To run a task within a container using Singularity, we need to add specific parameters to the Slurm command. 

As an example, let's try running `print('hello world')` using `Python3` within a `tensorflow_24.03-tf2-py3.sif` container image.
```
srun singularity exec tensorflow_24.03-tf2-py3.sif python3 -c "print('hello world')"
```

- `srun` is the Slurm command used to submit a job.
- `singularity` is the command-line interface for interacting with Singularity.
- `exec` is a sub-command that tells Singularity to execute a command inside the specified container.
- `tensorflow_24.03-tf2-py3.sif` is the path to the container image.
- `python3 -c "print('hello world')"` is the task that singularity executes.

While this execution proceeds smoothly, it's important to note that the command exclusively utilizes CPUs. The primary role of AI Cloud is to run software that utilises GPUs for computations. In order to run applications with a GPU you need to allocate a GPU to a job using Slurm. 

<hr>

## Resource specifications

The default resource specification
You can always

`--mem`: Allocate more host memory to your job (this **not** GPU memory)

There's also
Per task?

`scontrol show node`

## Allocating a GPU to your job

Allocating a GPU to your job can be done in the following manner.

`srun --gres=gpu:1 nvidia-smi`


Please see this section for more in depth guide for resource specification.

You can allocate a GPU to a job using the `--gres=gpu` option for Slurm. Additionally, you need to add the `--nv` option to Singularity to enable NVIDIA drivers in the container.

Let's try running a small Python script that performs a simple matrix multiplication of random data to benchmark TensorFlow computing speed with a GPU allocated.

Type `nano` and press `ENTER` (or use the editor of your choice), and enter the following code:

```py
import tensorflow as tf
import time

def benchmark_tensorflow():
    # Create some random data
    input_data = tf.random.normal((10000, 10000))

    # Define a simple TensorFlow computation (for example, matrix multiplication)
    @tf.function
    def some_computation(x):
        return tf.matmul(x, x)

    # Warm-up to ensure graph optimizations are done
    _ = some_computation(input_data)

    # Run the computation and measure the time
    start_time = time.time()
    result = some_computation(input_data)
    end_time = time.time()

    # Print the elapsed time
    print("Time taken: {:.4f} seconds".format(end_time - start_time))

if __name__ == "__main__":
    benchmark_tensorflow()
```

Save by pressing `CTRL + O` enter a file name, e.g. `benchmark_tensorflow.py` and exit by pressing `CTRL + X`. Now you should have `benchmark_tensorflow.py` in your directory. 


Lets try allocating 1 arbitrary available GPU to the job by adding `--gres=gpu:1`:

```console
srun --gres=gpu:1 singularity exec --nv tensorflow_24.03-tf2-py3.sif python3 benchmark_tensorflow.py
```

Note that the above example allocate 1 GPU to the job. It is possible to allocate more, for example `--gres=gpu:2` for two GPUs. Software for computing on GPU is not necessarily able to utilise more than one GPU at a time. It is your responsibility to ensure that the software you run can indeed utilise as many GPUs as you allocate. It is not allowed to allocate more GPUs than your job can utilise. [Here](../additional-guides/multiple-gpus-with-pytorch.md) is an example of a PyTorch script that can handle multiple GPUs. 


<hr>

**:material-party-popper: Congratulations! :material-party-popper:**

You've mastered the fundamentals of AI Cloud. Ready to take the [**next steps? :octicons-arrow-right-24:**](next-steps.md)

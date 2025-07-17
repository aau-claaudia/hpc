Before you start running jobs, it is important to be aware of the queueing system [Slurm](https://slurm.schedmd.com/quickstart.html).

## Slurm queue system
Slurm is a job scheduling system and is used to allocate resources and manage user jobs on AI Cloud. All computationally demanding jobs should take place on the compute nodes, and they are only accessible via Slurm.

### The srun command
One way of running a job via Slurm is by utilizing the `srun` command. Let's try to launch a job on a compute node:
```
srun hostname
```
We might have to wait a little bit, but once a compute node becomes available the `hostname` command is executed on the compute node that was allocated to our job. The output could be something like:
```
a256-t4-01.srv.aau.dk
```
This also serves as proof that the command was executed on the node `a256-t4-01.srv.aau.dk`, which is indeed a compute node. 

Running the `hostname` again (this witout `srun`) will execute the command on the front end node:
```
hostname
```
Which will output the hostname of the front end node:
```
ai-fe02.srv.aau.dk
```
!!! warning "Don't run jobs on the frontend"
    Please remember to not launch computationally heavy jobs on the front end node. Always delegate them to a compute node.

### The sbatch command

Another way of launching a job is with the `sbatch` command. This command can be launched with [a batch-script](/ai-cloud/additional-guides/run-a-batch-script/) or *on-the-fly* with the `--wrap` argument.

Let's try this:
```
sbatch --wrap="hostname"
```

Notice how the command output is not printed directly to the console. Instead what we get is a message from Slurm, telling us that our job was submitted to the queue:
```
Submitted batch job 737186
```
We can check the state of our job by [checking the queue](/ai-cloud/additional-guides/checking-the-queue/).

Once the job is finished, we will be able to find a file in the directory we launched our job in (`slurm-737186.out`). Let's print this file:
```
cat slurm-737186.out
a256-t4-02.srv.aau.dk
```

!!! info "How are they different: srun vs sbatch"
    * Where `srun` prints the command output directly to the console, `sbatch` writes it to a file.
    * A job launched with the `srun` command will run only as long as its output can be printed to the console (ie. it depends on a process on the host node). Some users find a workaround for this, and launch long-running jobs within from Tmux sessions, but these jobs will be stopped if something happens to the host. 
    * A job launched with `sbatch` is managed entirely by Slurm and does not rely on external processes. It is more robust, and can withstand the host node being rebooted.
    
    **Put short:** Use `srun` for short experiments. Always use `sbatch` for long-running jobs.

!!! info "More Slurm commands"
    You can find [additional Slurm commands](../additional-guides/checking-the-queue.md) available to customize your job submissions, such as setting the time limit for a job, specifying the number of CPUs or GPUs, and more.

<hr>

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

## Allocating a GPU to your job
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

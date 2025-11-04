
Jobs can be delegated to compute nodes, by submitting them to the queueing mechanism *Slurm*. There are two different commands for doing this, which can be useful in different situations.

* `srun`: the output is printed directly to the console.
* `sbatch`: the output is written to a file.

## Run attended jobs with srun

First we will be exploring how we can launch attended jobs with the srun command

### Execute a command on a compute node

Assuming that we have logged in to the front end node, we can execute the following command to return the name of the node it ran on.

```bash
❯ hostname
ai-fe02.srv.aau.dk
```

If we instead wanted to execute the same command on a compute node, we could use the `srun` command:

```bash
❯ srun hostname
srun: job 767369 queued and waiting for resources
srun: job 767369 has been allocated resources
a256-t4-02.srv.aau.dk
```

We see here that the output is different from before, proving that we did indeed reach a compute node before executing the command.

!!! warning "Don't compute on front-end"

    It is important to note that the front-end node is not intended for heavy computations, as it is a virtual server with a very modest amount of resources. Crashing the node, will affect all users on the system.

### Execute a command in a Singularity container

The preferred way to assemble different software environments on AI Cloud is with Singularity containers.

Let's use on of the pre-built containers in the directory `/home/container`.

```bash
❯ srun singularity exec /home/container/pytorch/pytorch_25.04.sif python3 -c "print('hello world')"
srun: job 767229 queued and waiting for resources
srun: job 767229 has been allocated resources
hello world
```

Here you should especially note that the command has three components:

  1. **The Slurm component**: in this case we are simply calling `srun` and thereby making a request for the default ressource configuration.
  
  2. **The Singularity component**: we call `singularity` and ask it to execute a `.sif` file
   
  3. **The actual command, we want to execute.**: `python3 -c "print('hello worl')"`


### Execute a command on a GPU

If we want to execute a command on a GPU, we need to use software that is able to interact with the GPU. The preferred way to do this on AI Cloud, is to use Singularity containers.

```bash
❯ srun --gres=gpu:1 singularity exec --nv /home/container/pytorch/pytorch_25.04.sif python3 -c "import torch; print(torch.cuda.is_available())"
srun: job 767221 queued and waiting for resources
srun: job 767221 has been allocated resources
True
```

## Run unattended jobs with sbatch

In most cases we do not want to print the output directly to the console, but to write it to a file. We can do this with an batch script, which we can launch with the `sbatch` command.

Let's assume we have the following file:

```python title="is-available.py"
import torch
print(torch.cuda.is_available())
```

In order to launch this job, we can reference it in our batch script:

``` bash title="sbatch-test.sh"
#!/usr/bin/env bash

#SBATCH --job-name=hostname
#SBATCH --partition=prioritized
#SBATCH --output=result_%j.out
#SBATCH --error=error_%j.err
#SBATCH --gres=gpu:1
#SBATCH --time=00:01:00

# The container image we want to launch:
container_image="/home/container/pytorch/pytorch_25.04.sif"

# The file we want to process on the compute node:
file="is-available.py"

singularity exec --nv $container_image python3 $file
```

We can now launch the job with:

```bash
sbatch sbatch-test.sh
```

And the following message will confirm, that it was indeed submitted to the queue:
```
Submitted batch job 737223
```

We can double check that our job was indeed submitted to the queue with:

```bash
squeue --me
```

Once the job is finished, we can use the `cat` command to print the content of the output file:
```bash
cat slurm-737223.out
True
```

Proving that we did indeed manage to launch the job on a GPU node.

!!! tip "Bonus tip: Launch unattended jobs *on-the-fly*"
    It's also possible to launch unattended jobs without a batch script. To do this, we can simply enter the `sbatch` command (optionally with a resource specification), and then wrapping the command we want to execute:
    
    ```
    sbatch --gres=gpu:1 --wrap="singularity exec --nv /home/container/pytorch/pytorch_25.04.sif python3 -c 'import torch; print(torch.cuda.is_available())'"
    ```


## Which one to use: srun vs sbatch

The most important difference between these two commands is that `srun` returns command output directly to the console - `sbatch` writes it to a file.

Another important difference has to do with the robustness of your job. If it's launched with `srun`, it will be dependent on the console session the front end node, and will only run as long as the output can be printed directly to the console. If anything happens to the front-end node or the console session is interrupted, the job is terminated. A job launched with `sbatch` does not depend on an external process, and will run until it is explicitly cancelled by the user.

### Conclusion:

  * `srun` is best suited for when you are testing and you want the command output to be printed directly in the console.
  * `sbatch` is best suited for long-running unmaintained jobs.

Our recommendation: Try to use `sbatch` as much as possible.

!!! info "Don't launch jobs from within interactive sessions"
    It is not very good practice to start your jobs from within interactive shell sessions (using `srun --pty`), as this will start that runs until it reaches the time limit in the (6 days in the prioritized partition) - not when the actual job is finished. As a consequence the resources allocated to the job will be occupied for longer than needed.

    As stated in our [Fair usage](/ai-cloud/fair-usage/)-section, we want to encourage our users to be mindful of their resource consumption for the sake of their fellow researchers, and not occupy ressources that others could have put to use.


!!! info "Persistent terminal sessions"
    If used correctly terminal multiplexers like Tmux/Screen are great tools! However if they are used to start an interactive job on a compute node, this counts as monopolising resources (which is not allowed).

!!! info "More Slurm commands"
    You can find [additional Slurm commands](../additional-guides/checking-the-queue.md) available to customize your job submissions, such as setting the time limit for a job, specifying the number of CPUs or GPUs, and more.


<hr>

**:material-party-popper: Congratulations! :material-party-popper:**

You've mastered the fundamentals of AI Cloud! Do check our additional guides for more, or reach out to us at [serviceportal.aau.dk](serviceportal.aau.dk) if you are having any issues.

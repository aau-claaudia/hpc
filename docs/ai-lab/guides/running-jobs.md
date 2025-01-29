Before you start running jobs, it is important to be aware of the queueing system [Slurm](https://slurm.schedmd.com/quickstart.html){target=_blank}. Slurm is a job scheduling system and is used to allocate resources and manage user jobs on AI-LAB.

There are two ways to run jobs using Slurm:

1. [srun](/ai-lab/guides/running-jobs/#using-srun) – Primarily for interactive or short, immediate tasks.
2. [sbatch](/ai-lab/guides/running-jobs/#using-sbatch) – For non-interactive, batch jobs where you submit a script and let Slurm handle the rest.

<hr>

## Using `srun`
`srun` launches a job and connects your current terminal session directly to the compute node. This is ideal for testing, debugging, or running short commands that require on-the-fly interaction. For example, if you just want to see the hostname of the machine allocated to you:

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

**Why use `srun`?**

* You can quickly test commands and code.
* You get an interactive session on the compute node (helpful for debugging).

**Drawbacks of `srun`**

* Ties up your terminal session until the job finishes.
* Not ideal for long-running jobs where you might lose connection or want to log out.

<hr>

## Using `sbatch`
For longer-running jobs, `sbatch` is preferred. You create a job script containing all the commands you want to run. Then you submit the job to the queue. Slurm schedules it, runs it, and writes output to a file. 


1. First [create a file](/ai-lab/guides/file-handling/#essential-linux-commands-you-should-know), say `my_job.sh`, Slurm directives at the top (these configure your job settings), and then lets print the hostname of the machine allocated to you:

    ```bash title="my_job.sh"
    #!/bin/bash

    #SBATCH --job-name=my_test_job  # Name of your job
    #SBATCH --output=my_job.out     # Name of the output file
    #SBATCH --error=file-my_job.err # Name of the error file

    hostname # Print the hostname of the node
    ```
    
2. Submit the job using `sbatch`:

    ```
    sbatch my_job.sh
    ```


    !!! info "What happens now?"

        * Slurm will display a job ID, for example:

            ```
            Submitted batch job 12345
            ```
        
        * You can log out or close your terminal — Slurm will run your job when resources are available.
        * You can monitor the job’s status with `squeue --me`.

3. Once it completes, check the output file using the `cat` commando.

    ```
    cat my_job.out
    ``` 

**Why use `sbatch`?**

* Does not require you to remain logged in — ideal for long or resource-intensive jobs.
* Easy to repeat or modify by adjusting the job script.

<hr>

## Specifying job options
In addition to simply running commands with Slurm, you can (and often must) specify options to clearly define the resources and constraints your job requires. These options ensure that Slurm can efficiently schedule and allocate the appropriate compute nodes to handle your job. You can set options either as command-line flags or within a job script. Some commonly used options include:

* `--mem`: The total memory requested for your job (e.g. `--mem=24G`). Maximum value is 24 GB per GPU.
* `--cpus-per-task`: The number of CPU cores required per task (e.g. `--cpus-per-task=15`). Maximum value is 15 CPUs per GPU.
* `--gres`: The generic resources required, such as GPUs (e.g. `--gres=gpu:1` for a single GPU). 
* `--time`: The maximum runtime for your job (e.g. `--time=01:00:00` for 1 hour).

!!! info "Multi GPU allocation"
    It is possible to allocate more than 1 GPU per job, for example `--gres=gpu:2` for two GPUs. **However**, your software and scripts are not necessarily able to utilise more than one GPU at a time. It is your responsibility to ensure that the software you run can indeed utilise as many GPUs as you allocate. It is not allowed to allocate more GPUs than your job can utilise (according to our [Fair Usage Policy](https://hpc.aau.dk/ai-lab/fair-usage/){target=_blank}).

### Setting options for `srun` jobs
When using `srun`, you can specify job options directly in the command to request resources for your job, like:

```
srun --mem=24G --cpus-per-task=15 --gres=gpu:1 --time=01:00:00 hostname
```

### Setting options for `sbatch` jobs
For `sbatch`, you specify job options at the top of your batch script using `#SBATCH` directives, like:

```bash title="my_job.sh"
#!/bin/bash

#SBATCH --job-name=my_test_job  # Name of your job
#SBATCH --output=my_job.out     # Name of the output file
#SBATCH --error=file-my_job.err # Name of the error file
#SBATCH --mem=24G               # Memory
#SBATCH --cpus-per-task=15      # CPUs per task
#SBATCH --gres=gpu:1            # Allocated GPUs
#SBATCH --time=01:00:00         # Maximum run time

hostname # Print the hostname of the node
```

<hr>

Now that you know how to run jobs on AI-LAB, let's delve into [**how to get applications/containers :octicons-arrow-right-24:**](getting-containers.md)
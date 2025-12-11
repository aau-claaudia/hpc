
# Using Containers to Run Jobs

Now that you know how to get containers, let's learn how to use them to run your computational tasks on TAAURUS.

## Basic Container Usage

To run commands inside a container, you use `singularity exec` with either `srun` or `sbatch`.

### Running a Simple Command

Let's start with a basic example using a Python container:

```bash
srun --mem=24G --cpus-per-task=6 --gres=gpu:1 --time=01:00:00 singularity exec --nv /media/project/work/pytorch_25.05.sif python3 -c "print('Hello from TAAURUS!')"
```

**Command breakdown:**

- `srun`: Run on a compute node with specified resources
- `singularity exec`: Execute a command inside a container
- `--nv`: Enable NVIDIA GPU drivers (required for GPU jobs)
- `/media/project/work/pytorch_25.05.sif`: Path to the container (replace `project` with your projects name)
- `python3 -c "print('Hello from TAAURUS!')"`: Command to run

### Using Containers with sbatch

For longer jobs, create a batch script:

```bash title="my_job.sh"
#!/bin/bash

#SBATCH --job-name=my_python_job
#SBATCH --output=my_job.out
#SBATCH --error=my_job.err
#SBATCH --mem=24G
#SBATCH --cpus-per-task=15
#SBATCH --gres=gpu:1
#SBATCH --time=01:00:00

# Run Python script in container
singularity exec --nv /media/project/work/pytorch_25.05.sif python3 my_script.py
```

Submit the job:

```bash
sbatch my_job.sh
```

Check the results:

```bash
cat my_job.out  # View output
cat my_job.err  # View errors (if any)
```

---

## Cancelling Jobs

Sometimes you need to cancel jobs that are running too long, stuck, or have incorrect parameters.

### Check Your Jobs First

Before cancelling, see what jobs you have running:

```bash
squeue --me
```

This shows all your jobs with their IDs and status.

### Cancel a Specific Job

To cancel a single job, use its job ID:

```bash
scancel 12345  # Replace 12345 with your actual job ID
```

### Cancel All Your Jobs

To cancel all your jobs at once:

```bash
scancel --user=$USER
```

Now that you know how to run jobs using containers, let's delve into the last part about [**monitoring on TAAURUS :octicons-arrow-right-24:**](monitoring.md)





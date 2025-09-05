
# Using Containers to Run Jobs

Now that you know how to get containers, let's learn how to use them to run your computational tasks on AI-LAB.

## Basic Container Usage

To run commands inside a container, you use `singularity exec` with either `srun` or `sbatch`.

### Running a Simple Command

Let's start with a basic example using a Python container:

```bash
srun --mem=24G --cpus-per-task=15 --gres=gpu:1 --time=01:00:00 singularity exec --nv /ceph/container/python/python_3.10.sif python3 -c "print('Hello from AI-LAB!')"
```

**Command breakdown:**

- `srun`: Run on a compute node with specified resources
- `singularity exec`: Execute a command inside a container
- `--nv`: Enable NVIDIA GPU drivers (required for GPU jobs)
- `/ceph/container/python/python_3.10.sif`: Path to the container
- `python3 -c "print('Hello from AI-LAB!')"`: Command to run

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
singularity exec --nv /ceph/container/python/python_3.10.sif python3 my_script.py
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


<hr>

## Adding Python Packages

Sometimes you need additional Python packages that aren't included in the container. The best way to handle this is by creating a virtual environment.

### Quick Setup Guide

Here's the simplest way to add packages to your container:


#### Step 1: Create Virtual Environment

Create a virtual environment in your current directory:

```bash
# Create virtual environment
srun singularity exec /ceph/container/pytorch/pytorch_24.09.sif python -m venv --system-site-packages my_venv
```

#### Step 2: Install Additional Packages

Install packages in your virtual environment:

```bash
# Install packages (example: openpyxl)
srun singularity exec --nv \
     -B ~/my_venv:/scratch/my_venv \
     -B $HOME/.singularity:/scratch/singularity \
     /ceph/container/pytorch/pytorch_24.09.sif \
     /bin/bash -c "export TMPDIR=/scratch/singularity/tmp && \
                   source /scratch/my_venv/bin/activate && \
                   pip install --no-cache-dir openpyxl"
```

#### Step 3: Use Your Virtual Environment

Run scripts with your additional packages:

```bash
# Run script with virtual environment
srun singularity exec --nv \
     -B ~/my_venv:/scratch/my_venv \
     /ceph/container/pytorch/pytorch_24.09.sif \
     /bin/bash -c "source /scratch/my_venv/bin/activate && python my_script.py"
```

### Virtual Environment Tips

- **Use absolute paths** when working in shared project directories
- **Always activate** the environment before running Python scripts
- **Use `--no-cache-dir`** to save disk space
- **Mount directories** with `-B` to access your virtual environment inside the container


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

### Common Scenarios

**Job is stuck or running too long:**
```bash
squeue --me  # Find the job ID
scancel 12345  # Cancel it
```

**Wrong parameters in batch script:**
```bash
scancel 12345  # Cancel the job
nano my_job.sh  # Edit the script
sbatch my_job.sh  # Resubmit with correct parameters
```

**Emergency - cancel everything:**
```bash
scancel --user=$USER  # Cancel all your jobs
```


Now that you know how to run jobs using containers, let's delve into the last part about [**monitoring on AI-LAB :octicons-arrow-right-24:**](monitoring.md)





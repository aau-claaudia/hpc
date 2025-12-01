# Running jobs on TAAURUS

This guide will teach you how to run computational tasks on TAAURUS using the Slurm job scheduler. Slurm manages all the computing resources and ensures fair access for all users.

## Understanding Slurm

[Slurm](https://slurm.schedmd.com/quickstart.html){target=_blank} is a job scheduling system that:

- **Manages resources**: Allocates CPUs, GPUs, and memory to your jobs
- **Queues jobs**: Organizes jobs when resources are busy
- **Ensures fairness**: Prevents any single user from monopolizing resources

## Two Ways to Run Jobs

Slurm offers two methods for running jobs:

1. **[srun](#using-srun)** - Interactive jobs for testing and debugging
2. **[sbatch](#using-sbatch)** - Batch jobs for longer computations

### When to Use Each Method

| Method | Best For | Duration | Interaction |
|--------|----------|----------|-------------|
| `srun` | Testing, debugging, quick tasks | Short (< 1 hour) | Interactive |
| `sbatch` | Training models, long computations | Long (> 1 hours) | Non-interactive |

<hr>

## Using srun (Interactive Jobs)

`srun` runs commands interactively on a compute node. Your terminal connects directly to the compute node, making it perfect for testing and debugging.

### Basic srun Example

Let's start with a simple test:

```
srun hostname
```

This command will:

1. Request a compute node
2. Run the `hostname` command on that node
3. Display the result
4. Return you to the front-end node

### What You'll See

When you run an srun command, you might see:

```
sp-l40s-01
```

This shows the hostname of one of the compute nodes (in this case `sp-l40s-01`)

### When to Use srun

✅ **Good for:**

- Testing commands and scripts
- Debugging code
- Quick computations
- Interactive exploration

❌ **Not ideal for:**

- Long-running jobs (hours/days)
- Jobs that need to run without you being connected
- Production model training

<hr>

## Using sbatch (Batch Jobs)

`sbatch` is perfect for longer-running jobs. You create a script with your commands, submit it to the queue, and Slurm runs it when resources are available.

### Creating a Job Script

Let's create a simple job script:

```
nano my_job.sh
```

Add this content:

```bash title="my_job.sh"
#!/bin/bash

#SBATCH --job-name=my_test_job  # Name of your job
#SBATCH --output=my_job.out     # Output file
#SBATCH --error=my_job.err      # Error file

# Your commands go here
hostname
echo "Hello from TAAURUS!"
date
```

### Understanding the Script

- **`#!/bin/bash`**: Tells the system to use bash shell
- **`#SBATCH` lines**: Slurm directives that configure your job
- **Commands below**: What you want to run

### Submitting the Job

```
sbatch my_job.sh
```

You'll see:
```
Submitted batch job 12345
```

### What Happens Next

1. **Job is queued**: Slurm adds your job to the queue
2. **Resources allocated**: When available, Slurm assigns compute resources
3. **Job runs**: Your script executes on the compute node
4. **Output saved**: Results are written to your specified output file

### Checking Results

Once the job completes, check the output:

```
cat my_job.out    # View the output
cat my_job.err    # View any errors (if empty, no errors occurred)
```

### When to Use sbatch

✅ **Perfect for most jobs:**

- Training machine learning models
- Long data processing tasks
- Jobs that take hours or days
- Running jobs overnight or while you're away

<hr>

## Specifying Job Resources

Most jobs need specific resources like GPUs, memory, or time limits. You specify these using Slurm options.

### Common Resource Options

| Option | Description | Example | Notes |
|--------|-------------|---------|-------|
| `--mem` | Memory allocation | `--mem=32G` | Per‑job request; node total 768 GB |
| `--cpus-per-task` | CPU cores | `--cpus-per-task=6` | Per‑task; node total 64 cores |
| `--gres` | GPUs | `--gres=gpu:1` | 8 GPUs per node (L40S, 48 GB) |
| `--time` | Time limit | `--time=01:00:00` | HH:MM:SS |

### Not sure what to request?

- Start with `--gres=gpu:1`, `--cpus-per-task=4–8`, `--mem=16–48G`
- Increase CPUs if data loading or preprocessing is a bottleneck
- Increase memory for larger batches or models
- Only request multiple GPUs if your code supports it

### Using Options with srun

Add options directly to your srun command:

```
srun --mem=32G --cpus-per-task=6 --gres=gpu:1 --time=01:00:00 hostname
```

### Using Options with sbatch

Add options as `#SBATCH` directives in your script:

```bash title="my_job.sh"
#!/bin/bash

#SBATCH --job-name=my_training_job
#SBATCH --output=training.out
#SBATCH --error=training.err
#SBATCH --mem=32G
#SBATCH --cpus-per-task=6
#SBATCH --gres=gpu:1
#SBATCH --time=04:00:00

# Your training commands here
python train_model.py
```

<hr>

Now that you know how to run jobs on TAAURUS, let's delve into [**how to get applications/containers :octicons-arrow-right-24:**](getting-containers.md)
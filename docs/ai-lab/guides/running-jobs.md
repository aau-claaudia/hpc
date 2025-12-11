# Running Jobs on AI-LAB

This guide will teach you how to run computational tasks on AI-LAB using the Slurm job scheduler. Slurm manages all the computing resources and ensures fair access for all users.

## Understanding Slurm

[Slurm](https://slurm.schedmd.com/quickstart.html){target=_blank} is a job scheduling system that:

- **Manages resources**: Allocates CPUs, GPUs, and memory to your jobs
- **Queues jobs**: Organizes jobs when resources are busy
- **Ensures fairness**: Prevents any single user from monopolizing resources

## Two Ways to Run Jobs

AI-LAB offers two methods for running jobs:

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

```bash
srun hostname
```

This command will:

1. Request a compute node
2. Run the `hostname` command on that node
3. Display the result
4. Return you to the front-end node

### What You'll See

When you run an srun command, you might see:

```bash
srun: job 12345 queued and waiting for resources
srun: job 12345 has been allocated resources
ailab-l4-01
```

This shows:

- Your job ID (12345)
- The job was queued (waiting for resources)
- Resources were allocated
- The hostname of the compute node (ailab-l4-01)

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

```bash
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
echo "Hello from AI-LAB!"
date
```

### Understanding the Script

- **`#!/bin/bash`**: Tells the system to use bash shell
- **`#SBATCH` lines**: Slurm directives that configure your job
- **Commands below**: What you want to run

### Submitting the Job

```bash
sbatch my_job.sh
```

You'll see:
```bash
Submitted batch job 12345
```

### What Happens Next

1. **Job is queued**: Slurm adds your job to the queue
2. **Resources allocated**: When available, Slurm assigns compute resources
3. **Job runs**: Your script executes on the compute node
4. **Output saved**: Results are written to your specified output file

### Checking Results

Once the job completes, check the output:

```bash
cat my_job.out    # View the output
cat my_job.err    # View any errors (if empty, no errors occurred)
```

### When to Use sbatch

✅ **Perfect for:**

- Training machine learning models
- Long data processing tasks
- Jobs that take hours or days
- Running jobs overnight or while you're away

❌ **Not needed for:**

- Quick tests or debugging
- Interactive exploration
- Commands that finish in minutes

<hr>

## Specifying Job Resources

Most jobs need specific resources like GPUs, memory, or time limits. You specify these using Slurm options.

### Common Resource Options

| Option | Description | Example | Notes |
|--------|-------------|---------|-------|
| `--mem` | Memory allocation | `--mem=24G` | Max 24GB per GPU |
| `--cpus-per-task` | CPU cores | `--cpus-per-task=15` | Max 15 CPUs per GPU |
| `--gres` | GPUs | `--gres=gpu:1` | Max 4 GPUs per job, max 8 GPUs per user |
| `--time` | Time limit | `--time=01:00:00` | 1 hour (HH:MM:SS) |

### Resource Guidelines

**Memory**: Request enough memory for your data and model

- Small models: `--mem=8G`
- Large models: `--mem=24G`

**CPUs**: More CPUs can speed up data loading and preprocessing

- Basic: `--cpus-per-task=4`
- Intensive: `--cpus-per-task=15`

**GPUs**: Essential for deep learning

- Single GPU: `--gres=gpu:1` (recommended for most users)
- Multiple GPUs: `--gres=gpu:2` to `--gres=gpu:4` (only if your code supports it)

!!! info "GPU Resource Limits"
    To ensure fair access for all users, AI-LAB enforces two important limits:
    
    - **Maximum 4 GPUs per job**: A single job can request no more than 4 GPUs (e.g., `--gres=gpu:4` or `-G 4`)
    - **Maximum 8 GPUs per user**: Each user can run jobs using a total of up to 8 GPUs simultaneously across all their running jobs
    
    We strongly encourage inexperienced users to allocate only 1 GPU, as most workloads do not speed up automatically with more GPUs. For advanced users who know how to configure multi-GPU training correctly, up to 4 GPUs per job remain available.

**Time**: Set realistic time limits

- Quick tests: `--time=00:30:00` (30 minutes)
- Training: `--time=04:00:00` (4 hours)
- Default: 1 hour (if not specified)
- Maximum: 12 hours

!!! info "Multi-GPU Usage"
    You can request multiple GPUs with `--gres=gpu:2` (up to 4), but **only if your code actually uses them**. Allocating unused GPUs violates our [Fair Usage Policy](https://hpc.aau.dk/ai-lab/fair-usage/){target=_blank}.

### Using Options with srun

Add options directly to your srun command:

```bash
srun --mem=24G --cpus-per-task=15 --gres=gpu:1 --time=01:00:00 hostname
```

### Using Options with sbatch

Add options as `#SBATCH` directives in your script:

```bash title="my_job.sh"
#!/bin/bash

#SBATCH --job-name=my_training_job
#SBATCH --output=training.out
#SBATCH --error=training.err
#SBATCH --mem=24G
#SBATCH --cpus-per-task=15
#SBATCH --gres=gpu:1
#SBATCH --time=04:00:00

# Your training commands here
python train_model.py
```

<hr>

Now that you know how to run jobs on AI-LAB, let's delve into [**how to get applications/containers :octicons-arrow-right-24:**](getting-containers.md)
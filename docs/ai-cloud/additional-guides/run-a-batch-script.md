In this guide, we will demonstrate how to submit a job to Slurm using a batch script. 

!!! info "What is a batch script?"
    A batch script is a text file that contains all the arguments you would otherwise give to Slurm via `srun`. The advantage of using batch scripts, is that they are a convenient way for us to document our workflow.

Let's create a bash script to submit a simple job that runs a Singularity container. This job will run a Python script inside the container.

#### Step 1: Prepare the Singularity Container

Ensure you have a Singularity image (.sif file) ready. For this example, we will use `tensorflow_24.03-tf2-py3.sif` container image.

#### Step 2: Create the Python Script
Create a simple Python script named hello.py:

```
print("Hello from within the Singularity container!")
```

#### Step 3: Create the Bash Script
Create a bash script named run_job.sh:

```
#!/bin/bash
#SBATCH --job-name=singularity_test
#SBATCH --output=result_%j.out
#SBATCH --error=error_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

singularity exec tensorflow_24.03-tf2-py3.sif python hello.py
```

Explanation of SBATCH Options:

- `--job-name`: Name of the job (<span style="font-weight: 700;">Optional</span>).
- `--output`: File where standard output will be written, with %j replaced by the job ID (<span style="font-weight: 700;">Required</span>).
- `--error`: File where standard error will be written, with %j replaced by the job ID (<span style="font-weight: 700;">Optional</span>).
- `--time`: Maximum run time (hh:mm) (<span style="font-weight: 700;">Optional</span>).
- `--ntasks`: Number of tasks (<span style="font-weight: 700;">Optional</span>).
- `--cpus-per-task`: Number of CPUs per task (<span style="font-weight: 700;">Optional</span>).
- `--mem`: Memory per node (<span style="font-weight: 700;">Optional</span>).

#### Step 4: Submit the Job
To submit the job, use the sbatch command:

```
sbatch run_job.sh
```

After the job gets submitted, you should be able to find a file called something like `result_x.out` with `Hello from within the Singularity container!` in it.

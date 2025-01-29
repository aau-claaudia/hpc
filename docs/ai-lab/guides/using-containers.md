
To run a task within a container, we need to add specific parameters to the `srun` or `sbatch` command.

As an example, let's try running `print('hello world')` using `Python3` within the `python_3.10.sif` container from `/ceph/container/python` directory.

### Using `srun`

```
srun --mem=24G --cpus-per-task=15 --gres=gpu:1 --time=01:00:00 singularity exec --nv /ceph/container/python/python_3.10.sif python3 -c "print('hello world')"
```

- `singularity` is the command for interacting with Singularity.
- `exec` is a sub-command that tells Singularity to execute a command inside the specified container.
- `--nv` is a sub-command that enables NVIDIA drivers in the container (**Important when using GPUs**).
- `/ceph/container/python/python_3.10.sif` is the path to the container.
- `python3 -c "print('hello world')"` is the task that singularity executes.

### Using `sbatch`

```bash title="my_job.sh"
#!/bin/bash

#SBATCH --job-name=my_test_job  # Name of your job
#SBATCH --output=my_job.out     # Name of the output file
#SBATCH --error=file-my_job.err # Name of the error file
#SBATCH --mem=24G               # Memory
#SBATCH --cpus-per-task=15      # CPUs per task
#SBATCH --gres=gpu:1            # Allocated GPUs
#SBATCH --time=01:00:00         # Maximum run time

singularity exec --nv /ceph/container/python/python_3.10.sif python3 -c "print('hello world')"
```

Then submit the job using `sbatch`:

```
sbatch my_job.sh
```

After the job gets submitted, you should be able to find a file called `my_job.out` with `hello world` in it. You can print the content using:

```
cat my_job.out
```

<hr>

## Adding Python packages via virtual environment
In many cases, you will need to add additional Python packages to an existing container. The easiest way to do this, is using a virtual environment. The guide below outlines the steps to create and utilize a virtual environment within your directory on AI-LAB.

??? news "Guide on adding Python packages via virtual environment"
    To enhance the functionality of a containerized environment, you can add additional Python packages using a virtual environment. This guide outlines the steps to create and utilize a virtual environment within your directory on AI-LAB.

    ### Step 1: Create a virtual environment

    Begin by creating a virtual environment in your home directory. This allows you to install packages locally, making them accessible from within your container.

    ```
    python3 -m venv my-virtual-env
    ```

    ### Step 2: Activate the virtual environment

    Activate your virtual environment:

    ```
    source my-virtual-env/bin/activate
    ```

    !!! info "Remember to always activate the virtual environment when you want to use it"
        Remember that you must always activate the virtual environment (`source my-virtual-env/bin/activate`) to ensure that Python knows where to find the installed packages.

    ### Step 3: Install Python packages

    With the virtual environment activated, install the Python packages you need. For example, to install `numpy`, `pandas`, and `matplotlib`:

    ```
    srun --mem=24G --cpus-per-task=15 bash -c "export TMPDIR=/scratch; pip install numpy pandas matplotlib --no-cache-dir"
    ```

    This command will download and install the specified packages into your virtual environment.

    ### Step 4: Verify the installation

    To confirm that the packages were installed correctly, you can check their versions or run a basic script. For instance, to check the installed version of `matplotlib`:

    ```
    srun python3 -c "import matplotlib; print(matplotlib.__version__)"
    ```

    ### Step 5: Use the virtual environment with containers

    You can now expand containers with the virtual environment, such as a standard Python container.

    To do this, you will need to use the Singularity `--bind` option to bind your virtual environment directory to a location inside the container, and point Python to the path where it can find the installed packages.

    ```
    srun singularity exec --bind ~/my-virtual-env:/my-virtual-env /ceph/container/python/python_3.10.sif /my-virtual-env/bin/python3 -c "import matplotlib; print(matplotlib.__version__)"
    ```

    Here, `~/my-virtual-env:/my-virtual-env` binds your virtual environment to a new directory inside the container. `/my-virtual-env/bin/python3` tells Singularity to use the Python interpreter inside your virtual environment.


## Cancelling jobs
There are several scenarios where you might need to cancel jobs, such as when a job is stuck, running longer than expected, or you realize that the job parameters were set incorrectly. Here’s a guide on how to cancel jobs with Slurm.

??? news "Guide on cancelling jobs"

    ### Checking Job Status
    Before cancelling a job, it’s often useful to check its current status or job ID. You can list your currently running or queued jobs using the squeue command:

    ```
    squeue --me
    ```

    ### Cancelling a Single Job
    To cancel a specific job, use the `scancel` command followed by the job ID. For example, if your job ID is `12345`, you can cancel it by running:

    ```
    scancel 12345
    ```

    ### Cancelling Multiple Jobs
    If you need to cancel all your jobs, you can cancel all jobs belonging to your user by using:

    ```
    scancel --user=$USER
    ```

    This command is particularly useful if you have submitted a batch of jobs and need to cancel them all simultaneously.


Now that you know how to run jobs using containers, let's delve into the last part about [**monitoring on AI-LAB :octicons-arrow-right-24:**](monitoring.md)





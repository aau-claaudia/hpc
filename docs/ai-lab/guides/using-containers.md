
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
Sometimes, you’ll need additional Python packages that aren’t included in the container you’re using. The simplest and cleanest way to manage these is by creating a virtual environment within your own directory.

This guide walks you through creating a **virtual environment** inside a Singularity container and installing additional packages for use in your Python scripts.

!!! warning "This guide is recently updated and under testing" 
    This guide has just been updated to reflect new container paths and best practices. If you encounter any issues, please report them by submitting a ticket through our [service portal](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328).


??? info "Guide on adding Python packages via virtual environment"

    ### Step 1: Create a virtual environment inside the container.

    Run the following command to create a virtual environment in your current directory.
    
    ** Replace the container**, with the one you want to use. You need to do this thoughout the guide.

    ```
    srun singularity exec /ceph/container/python/pytorch/pytorch_25.01.sif python -m venv --system-site-packages my_venv
    ```

    !!! info "Using a shared project directory?" 
        If you're working in a shared project directory, first `cd` into that directory and then run the command.
    
    ### Step 2: Install Additional Packages

    Activate the environment inside the container and install the Python packages you need. In this case we will install `openpyxl`:

    ```
    srun singularity exec --nv -B ~/my_venv /ceph/container/pytorch/pytorch_25.01.sif /bin/bash -c "source my_venv/bin/activate && pip install openpyxl"
    ```

    !!! info "Using a shared project directory?" 
        Replace `~/my_venv` with the absolute path, e.g. `/ceph/project/my_project/my_venv`.

    * `--nv` enables GPU support.
    * `-B ~/my_venv` binds your virtual environment directory into the container.
    * `source my_venv/bin/activate` activates the environment.
    * `pip install openpyxl` installs your chosen package(s).
  

    ### Step 3: Test with a simple Python script
    Now you can test with a script that uses the packages you've installed. For example:


    ```python title="my_script.py"
    import torch
    import openpyxl

    print("Torch version:", torch.__version__)
    print("Openpyxl version:", openpyxl.__version__)
    ```

    Save this as my_script.py in your working directory.


    ### Step 4: Run Your Script Using the Virtual Environment
    To run the script inside the container using your virtual environment:

    ```
    srun singularity exec --nv -B ~/my_venv /ceph/container/pytorch/pytorch_25.01.sif /bin/bash -c "source my_venv/bin/activate && python my_script.py"
    ```

    !!! info "Using a shared project directory?" 
        Again, make sure to use the full path to `my_venv` if it’s not in your home directory.

     You’ve now added custom packages to your own isolated Python environment without modifying the base container.

    !!! info "Reminder" 
        Always activate your virtual environment inside the container before running Python scripts to ensure your packages are available.


??? info "(OLD) Guide on adding Python packages via virtual environment"
    To enhance the functionality of a containerized environment, you can add additional Python packages using a virtual environment. This guide outlines the steps to create and utilize a virtual environment within a Singularity container to ensure compatibility between different Python versions.

    ### Step 1: Create a virtual environment inside a Singularity container.

    Create the virtual environment using the installed `virtualenv` tool. Remember to replace `/ceph/container/python/python_3.10.sif` with your container path.

    ```
    srun singularity exec /ceph/container/python/python_3.10.sif virtualenv ~/my-virtual-env
    ```

    This ensures that the virtual environment is set up using the correct Python version from the container.

    !!! info "Missing `virtualenv` package?"
        If the command fails due to missing `virtualenv` dependency, try installing the package in the container:

        ```
        srun singularity exec /ceph/container/python/python_3.10.sif pip install --user virtualenv
        ```

        Then run:

        ```
        srun singularity exec /ceph/container/python/python_3.10.sif ~/.local/bin/virtualenv ~/my-virtual-env
        ```

        In case you are trying to set up the virtual environment inside a [shared project directory](../../system-overview/#shared-project-directories), you will first need to navigate to the project directory and execute the command from there.

    ### Step 2: Install Python packages inside the virtual environment

    With the virtual environment created, you can now install the necessary Python packages within it.

    ```
    srun singularity exec --bind ~/my-virtual-env:/my-virtual-env /ceph/container/python/python_3.10.sif /bin/bash -c "source /my-virtual-env/bin/activate && python3 -m pip install numpy pandas matplotlib"
    ```

    Here’s what happens in this command:
    - The `--bind` option mounts the virtual environment directory inside the container.
    - The virtual environment is activated using `source`.
    - The required Python packages (`numpy`, `pandas`, `matplotlib`) are installed using `pip`.

    ### Step 3: Verify the installation

    After installing the packages, you can verify that they are correctly installed inside the virtual environment.

    ```
    srun singularity exec --bind ~/my-virtual-env:/my-virtual-env /ceph/container/python/python_3.10.sif /bin/bash -c "source /my-virtual-env/bin/activate && python -c 'import matplotlib; print(matplotlib.__version__)'"
    ```

    This command runs a short Python script inside the virtual environment to check if `matplotlib` is properly installed.

    ### Step 4: Use the virtual environment for running scripts

    Now that the virtual environment is set up and populated with the necessary packages, you can use it to run your Python scripts inside the Singularity container.

    ```
    srun singularity exec --bind ~/my-virtual-env:/my-virtual-env /ceph/container/python/python_3.10.sif /bin/bash -c "source /my-virtual-env/bin/activate && python my_script.py"
    ```

    This ensures that `my_script.py` runs with the correct Python version and installed dependencies.

    !!! info "Remember to always use the virtual environment when running Python scripts"
        Always make sure to activate the virtual environment (`source /my-virtual-env/bin/activate`) inside the Singularity container before running any Python scripts to ensure they use the correct dependencies.



## Cancelling jobs
There are several scenarios where you might need to cancel jobs, such as when a job is stuck, running longer than expected, or you realize that the job parameters were set incorrectly. Here’s a guide on how to cancel jobs with Slurm.

??? info "Guide on cancelling jobs"

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





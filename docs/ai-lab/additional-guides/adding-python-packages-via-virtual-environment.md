To enhance the functionality of a containerized environment, you can add additional Python packages using a virtual environment. This guide outlines the steps to create and utilize a virtual environment within your directory on AI-LAB.

## Step 1: Create a Virtual Environment

Begin by creating a virtual environment in your home directory. This allows you to install packages locally, making them accessible from within your container.

```
python3 -m venv my-virtual-env
```

## Step 2: Activate the Virtual Environment

Activate your virtual environment:

```
source my-virtual-env/bin/activate
```

!!! info "Remember to always activate the virtual environment when you want to use it"
    Remember that you must always activate the virtual environment (`source my-virtual-env/bin/activate`) to ensure that Python knows where to find the installed packages.

## Step 3: Install Python Packages

With the virtual environment activated, install the Python packages you need. For example, to install `numpy`, `pandas`, and `matplotlib`:

```
srun --mem=24G --cpus-per-task=15 bash -c "export TMPDIR=/scratch; pip install numpy pandas matplotlib --no-cache-dir"
```

This command will download and install the specified packages into your virtual environment.

## Step 4: Verify the Installation

To confirm that the packages were installed correctly, you can check their versions or run a basic script. For instance, to check the installed version of `matplotlib`:

```
srun python3 -c "import matplotlib; print(matplotlib.__version__)"
```

## Step 5: Use the Virtual Environment with Containers

You can also use this method to expand containers, such as a PyTorch container.

To do this, you will need to use the Singularity `--bind` option to bind your virtual environment directory to a location inside the container, and point Python to the path where it can find the installed packages.

```
srun singularity exec --bind ~/my-virtual-env:/my-virtual-env /ceph/container/pytorch/pytorch_24.09.sif /my-virtual-env/bin/python3 -c "import matplotlib; print(matplotlib.__version__)"
```

Here, `~/my-virtual-env:/my-virtual-env` binds your virtual environment to a new directory inside the container. `/my-virtual-env/bin/python3` tells Singularity to use the Python interpreter inside your virtual environment.




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

## Step 3: Install Python Packages

With the virtual environment activated, install the Python packages you need. For example, to install `numpy`, `pandas`, and `matplotlib`:

```
srun --mem=24G --cpus-per-task=15 pip install numpy pandas matplotlib
```

This command will download and install the specified packages into your virtual environment.

## Step 4: Verify the Installation

To confirm that the packages were installed correctly, you can check their versions or run a basic script. For instance, to check the installed version of `matplotlib`:

```
srun python3 -c "import matplotlib; print(matplotlib.__version__)"
```

## Step 5: Use the Virtual Environment with Containers

You can also use this method to expand other containers, such as a PyTorch container:

```
srun singularity exec /ceph/container/pytorch/pytorch_24.09.sif python3 -c "import matplotlib; print(matplotlib.__version__)"
```

!!! info "Remember to activate the virtual environment"
    Remember that you must always activate the virtual environment (`source my-virtual-env/bin/activate`) to ensure that Python knows where to find the installed packages.

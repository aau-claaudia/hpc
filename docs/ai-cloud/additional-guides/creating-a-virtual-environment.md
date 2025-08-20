To enhance the functionality of a containerized environment, you can add additional Python packages using a virtual environment. This guide outlines the steps to create and utilize a virtual environment within a Singularity container to ensure compatibility between different Python versions.

### Step 1: Create a virtual environment inside a Singularity container.

Create the virtual environment using the installed `virtualenv` tool. Remember to replace `python_3.10.sif` with your container path.

```
srun singularity exec python_3.10.sif virtualenv ~/my-virtual-env
```

This ensures that the virtual environment is set up using the correct Python version from the container.

!!! info "Missing `virtualenv` package?"
    If the command fails due to missing `virtualenv` dependency, try installing the package in the container:

    ```
    srun singularity exec python_3.10.sif pip install --user virtualenv
    ```

    Then run:

    ```
    srun singularity exec python_3.10.sif ~/.local/bin/virtualenv ~/my-virtual-env
    ```

### Step 2: Install Python packages inside the virtual environment

With the virtual environment created, you can now install the necessary Python packages within it.

```
srun singularity exec --bind ~/my-virtual-env:/my-virtual-env python_3.10.sif /bin/bash -c "source /my-virtual-env/bin/activate && pip install numpy pandas matplotlib"
```

Here’s what happens in this command:
- The `--bind` option mounts the virtual environment directory inside the container.
- The virtual environment is activated using `source`.
- The required Python packages (`numpy`, `pandas`, `matplotlib`) are installed using `pip`.

### Step 3: Verify the installation

After installing the packages, you can verify that they are correctly installed inside the virtual environment.

```
srun singularity exec --bind ~/my-virtual-env:/my-virtual-env python_3.10.sif /bin/bash -c "source /my-virtual-env/bin/activate && python -c 'import matplotlib; print(matplotlib.__version__)'"
```

This command runs a short Python script inside the virtual environment to check if `matplotlib` is properly installed.

### Step 4: Use the virtual environment for running scripts

Now that the virtual environment is set up and populated with the necessary packages, you can use it to run your Python scripts inside the Singularity container.

```
srun singularity exec --bind ~/my-virtual-env:/my-virtual-env python_3.10.sif /bin/bash -c "source /my-virtual-env/bin/activate && python my_script.py"
```

This ensures that `my_script.py` runs with the correct Python version and installed dependencies.

!!! info "Remember to always use the virtual environment when running Python scripts"
    Always make sure to activate the virtual environment (`source /my-virtual-env/bin/activate`) inside the Singularity container before running any Python scripts to ensure they use the correct dependencies.

Cotainr is a tool that allows for easily extending Singularity container images with [conda environments](https://www.anaconda.com/docs/tools/working-with-conda/environments).

Cotainr is relatively straight forward provided that either:

  1) The package you want to use can be found on either [anaconda.org](https://anaconda.org/) or [PyPI](https://pypi.org/).

  2) Your are able to provide a conda environment YAML-file (eg. by calling `conda export > environment.yml` from within your environment) .


## Where to find it

We have made Cotainr available in `/home/container/cotainr`.

## Preparing the conda environment to build from

#### Option 1: Export an existing environment
If you already have a working conda environment on another platform, simply call `conda env export > environment.yml` from within the Conda environment.

#### Option 2: Gather the environment manually

If you do not have a working conda environment, you can create the yaml-file manually. In this case it will be preferable to only specify a minimal number of packages, and rely on Anacondas ability to gather the necessary dependencies in the most stable way.

It is preferable to start by by verifying that the package can be found on [anaconda.org](https://anaconda.org/). If the package can not be found here, check if it can be installed from [PyPI](https://pypi.org/) (using `pip`).

!!! tip "Create/edit the YAML-file with nano"
    Open a text editor like `nano` to start creating the file. When you are finished, press `CTRL + O` enter a file name, e.g. `environment.yml` and exit by pressing `CTRL + X`. Now you should have `environment.yml` in your directory. 

If the package can be found on anaconda.org, we would specify it like so:

```yml
name: cupy
channels:
  - conda-forge
dependencies:
  - cupy
```
In case we want to install modules with pip, we could say:

```yml
name: cupy
channels:
  - conda-forge
dependencies:
  - pip
  pip:
    - cupy
```

## Build the container image

Let's create the following batch script for our build:


```bash
#!/bin/bash

#SBATCH --job-name=build_cupy
#SBATCH --cpus-per-task=32
#SBATCH --time=04:00:00
#SBATCH --output=out.%x
#SBATCH --error=err.%x

export SINGULARITY_TMPDIR=$HOME/.singularity/tmp
export SINGULARITY_CACHEDIR=$HOME/.singularity/cache
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR

# The location of the cotainr executable
cotainr_path="/home/container/cotainr"

# The base image which build on top of
base_image="docker://ubuntu:24.04"

# The conda environment file from which we build
requirements="environment.yml"

# The resulting container
output_sif="cupy.sif"

# Call the build instructions
$cotainr_path build $output_sif --base-image=$base_image --conda-env=$requirements --accept-licenses
```

Choose an appropriate name for the file, like `build_cupy.sh`.

To initiate the build, call:

```bash
sbatch build_cupy.sh
```

A few minutes later you should have `cupy.sif` container image in your directory.

!!! failure "Out of memory"

    In case you get an "out of memory" error (sometimes refered to as the *OOM-killer*), we can pass the `--mem` parameter to Slurm to ask for more host memory. Try out with 50 gb: `sbatch --mem=50G --wrap...`

## Use the container image

You can access the conda image and run code using the dependencies you set up. Lets try to see if it works by printing the numpy version:
```
srun singularity exec cupy.sif python3 -c 'import cupy; print(cupy.__version__)'
```

This should print the package version out to the console.

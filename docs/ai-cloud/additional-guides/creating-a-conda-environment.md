
Cotainr is a tool that allows for easily extending Singularity container images with [conda environments](https://www.anaconda.com/docs/tools/working-with-conda/environments).

Cotainr is relatively straight forward provided that either:

  1) The package you want to use can be found on either [anaconda.org](https://anaconda.org/) or [PyPI](https://pypi.org/).

  2) Your are able to provide a conda environment YAML-file (eg. by calling `conda export > env.yml` from within your environment) .


## Where to find it

We have made Cotainr available in `/home/container/cotainr`.

## Preparing the conda environment to build from

#### Option 1: Export an existing environment
If you already have a working conda environment on another platform, simply call `conda env export > conda_env.yml` from within the Conda environment.

#### Option 2: Gather the environment manually

If you do not have a working conda environment, you can create the yaml-file manually. In this case it will be preferable to only specify a minimal number of packages, and rely on Anacondas ability to gather the necessary dependencies in the most stable way.

It is preferable to start by by verifying that the package can be found on [anaconda.org](https://anaconda.org/). If the package can not be found here, check if it can be installed from [PyPI](https://pypi.org/) (using `pip`).

!!! tip "Create the yaml-file with nano"
    Open a text editor like `nano` to start creating the file. When you are finished, press `CTRL + O` enter a file name, e.g. `conda_env.yml` and exit by pressing `CTRL + X`. Now you should have `conda_env.yml` in your directory. 

If the package can be found on anaconda.org, we would specify it like so:

```yml
channels:
  - conda-forge
dependencies:
  - cupy
```
If we want to install modules from Pip, we could say:

```yml
channels:
  - conda-forge
dependencies:
  - pip
  pip:
    - pillow=11.3.0
```



## Build the container image

We can now build a container containing the conda environment specified in `conda_env.yml` with the following command:
```
sbatch --wrap="/home/container/cotainr build cupy.sif --base-image=docker://ubuntu:24.04 --conda-env=conda_env.yml --accept-licenses"
```
After some time you should have `conda_container.sif` container image in your directory. 

!!! failure "Out of memory"

    In case you get an "out of memory" error (sometimes refered to as oom), we can pass the `--mem` parameter to Slurm to ask for more host memory. Try out with 50 gb: `sbatch --mem=50G --wrap...`

## Use the container image

You can access the conda image and run code using the dependencies you set up. Lets try to see if it works by printing the numpy version:
```
srun singularity exec cupy.sif python3 -c 'import cupy; print(cupy.__version__)'
```
This should print the package version out to the console.

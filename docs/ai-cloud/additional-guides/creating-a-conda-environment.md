[Cotainr](https://github.com/DeiC-HPC/cotainr) is a tool that allows for easily extending Singularity container images with conda environments.

## Requirements

Cotainr is relatively straight forward provided that either:

  1) The package you want to use can be found on either [anaconda.org](https://anaconda.org/) or [PyPI](https://pypi.org/).

  2) Your are able to provide a conda environment YAML-file (eg. by calling `conda export > environment.yml` from within your environment) .


!!! note "Where to find Cotainr"

    We have made Cotainr available in `/home/container/cotainr`.

    Cotainr can also be found on [their official Github](https://github.com/DeiC-HPC/cotainr) - note that on AI Cloud the newest supported version is 2024.10.0.

## Prepare the Conda environment

#### Option 1: Export an existing environment
If you already have a working conda environment on another platform, simply call `conda env export > environment.yml` from within the Conda environment.

#### Option 2: Gather the environment manually

If you do not have a working conda environment, you can create the yaml-file manually. In this case it will be preferable to only specify a minimal number of packages, and rely on Anacondas ability to gather the necessary dependencies in the most stable way.

It is preferable to start by by verifying that the package can be found on [anaconda.org](https://anaconda.org/). If the package can not be found here, check if it can be installed from [PyPI](https://pypi.org/) (using `pip`).

!!! tip "Create/edit the YAML-file with nano"
    Open a text editor like `nano` to start creating the file. When you are finished, press `CTRL + O` enter a file name, e.g. `environment.yml` and exit by pressing `CTRL + X`. Now you should have `environment.yml` in your directory. 

If the package can be found on anaconda.org, we would specify it like so:

```yml title="environment.yml"
name: cupy
channels:
  - conda-forge
dependencies:
  - cupy
```
In case we want to install modules with pip, we could say:

```yml title="environment.yml"
name: cupy
channels:
  - conda-forge
dependencies:
  - pip
  - pip:
    - cupy
```

## Build the container image

Let's create the following batch script for our build:


```bash title="build_cupy.sif"
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

Initiate the build proces with:

```bash
sbatch build_cupy.sh
```

A few minutes later you should have `cupy.sif` container image in your directory.

## Test out the container image

You can access the conda image and run code using the dependencies you set up. Lets try to see if it works by printing the numpy version:
```
srun singularity exec cupy.sif python3 -c 'import cupy; print(cupy.__version__)'
```

This should print the Cupy version out to the console, verifying that was indeed installed to our Container image.

<hr>

## Troubleshooting
!!! failure "Out of memory?"

    In case your build did not complete, and exited with an "out of memory" error (the *OOM-killer*), we can attempt to allocate more memory to our job. Remember we don't want to be overly greedy, so let's try bumping up from the default 40G to 60G. Adjust this incrementally as you need.

!!! failure "Ensure the character encoding is correct"

    If you are trying to build from an environment export from a Windows system, you should ensure that the [character encoding](https://en.wikipedia.org/wiki/Character_encoding) is correct.
    After having uploaded the file to the server, inspect the file with:
    ```
    file environment.yml
    ``` 

    If this command outputs: `ASCII text, with CRLF line terminators` you need to convert the file to a Linux supported character encoding:
    ```
    iconv -ct ascii environment.yml | sed 's/\r$//' > converted_environment.yml`
    ```

!!! failure "Create a YAML-file with only *installed on request*"

    If you encounter difficulties building the container image, it may be helpful to export only the modules that were explicitly installed (ie. excluding dependencies installed automatically by Conda).

    ```
    conda env export --from-history > environment.yml
    ```

    This should result in a shorter list without pinned version numbers.


<hr>

### Are you still experiencing issues?
Reach out to CLAAUDIA at [serviceportal.aau.dk](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e)

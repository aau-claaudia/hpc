It is possible to define and build your own container with Singularity. Lets try creating a simple Singularity container with Python and pip installed. 

!!! info "Another way to build containers using Cotainr"
    You also have the option to use a software called [cotainr](creating-a-conda-environment.md) to build containers. We have a guide on how to install a Conda environment with Cotainr [here](creating-a-conda-environment.md).

First we need to create a [Singularity definition file](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank} (`.def`). This definition file is a blueprint for how Singularity should build the container. It includes information about the base OS to build, which software to install and several other options.

Lets create an empty text file by using the `nano` command:

```
nano
```

Now we can enter the blueprint needed to install our application:

```
Bootstrap: docker
From: ubuntu:20.04

%post
    # This section is where you install additional packages or software
    # Update package list and install the latest Python and pip version
    apt-get update
    apt-get install -y python3 python3-pip
    pip install numpy pandas scikit-learn matplotlib

%test
    # Define tests to run after the container is built
    python3 --version
```

In this example we will use `docker` to pull `ubuntu:20.04` as the base OS of our container. 

In the next section,`%post`, we can define commands that will be executed after the base OS has been installed. In this example, we will update the container and install `python3` and `pip` along with `numpy pandas scikit-learn matplotlib` packages. 

After that we can define commands to run after the container is built in the `%test` section. Lets try with `python3 --version`.

You can find more options to use in definition file in the [Singularity definition file documentation](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank}.

To save the file press `CTRL + O` and enter a filename ending with `.def` and hit `ENTER`. In this example, lets call it `python3.def`.

#### Setting environment variables
Before building the container, we need to set the `SINGULARITY_TMPDIR` and `SINGULARITY_CACHEDIR` environment variables, to speed up repeated operations. We will use these variables to a temporary directory (`$HOME/.singularity/tmp/` and `$HOME/.singularity/cache/`) inside your home directory. Singularity will use this directory for storing temporary files and cached data during container operations.

```
export SINGULARITY_TMPDIR="$HOME/.singularity/tmp/"
export SINGULARITY_CACHEDIR="$HOME/.singularity/cache/"
```

Then we need to create the directories defined by `SINGULARITY_CACHEDIR` and `SINGULARITY_TMPDIR`, if they don’t already exist. The -p flag ensures that the command does not return an error if the directories are already in place.

```
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR
```

### Building the container

You can now build container from the `python3.def` file:

```
srun singularity build --fakeroot python3.sif python3.def
```

After some time you should see the `Python X.X.X` version be printed in the terminal, and you should now have a `python3.sif` container image ready to run.

Lets for example print the matplotlib version:

```
srun singularity exec python3.sif python3 -c "import matplotlib; print('Matplotlib version:', matplotlib.__version__)"
```

You can find more information about building containers from Singularity definition files [here](https://docs.sylabs.io/guides/3.0/user-guide/definition_files.html){target=_blank}.